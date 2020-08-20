#!/usr/bin/env python
# coding: utf-8

# In[1]:


import mbuild as mb
import subprocess
from cp2kmd.cssi_cp2k.classes import SIM as sim
# read this: https://www.cp2k.org/_media/events:2015_cecam_tutorial:watkins_optimization.pdf for more knowledge


# In[2]:


def info_molecule(molecule):
    num_atoms=len(molecule.atoms)
    name_atoms=[];
    mass_atoms=[];
    for i in range(num_atoms):
        name_atoms.append(molecule.atoms[i].element_name)
        mass_atoms.append(molecule.atoms[i].mass)
    
    return name_atoms,mass_atoms


# In[ ]:


def remove_duplicate(x):
    return list(dict.fromkeys(x))


# In[ ]:


def basis_set_setter(element_symbol):
    #HERE I should define all the elements and all the basis set
    if element_symbol=='H':
        return "TZV2PX-MOLOPT-GTH"
    elif element_symbol=='F':
        return "TZV2PX-MOLOPT-GTH"
    elif element_symbol=='Cl':
        return "TZV2PX-MOLOPT-GTH"
    elif element_symbol=='I':
        return "DZVP-MOLOPT-SR-GTH"
        


# In[ ]:


def potential(element_symbol,functional):
    return "GTH-"+functional
        


# In[ ]:


def optimize_molecule(molecule,functional,project_name,dire,temperature,box_length,number_of_molecules,simulation_time,
                      CUTOFF,SCF_tolerence,basis_set, ensemble, timestep, thermostat,opt_inp_file,mol_unopt_coord):
    molecule_in_A=mb.clone(molecule)
    molecule_in_A.save(mol_unopt_coord,overwrite='True')
    name=molecule.name
    with open(mol_unopt_coord, 'r') as fin:
        data = fin.read().splitlines(True)
    with open(mol_unopt_coord, 'w') as fout:
        fout.writelines(data[2:])
    molecule=molecule.to_parmed()
    atom_list,mass_list=info_molecule(molecule)
    unique_atom_list=remove_duplicate(atom_list)
    unique_atom_list.sort()
    num_atoms=len(atom_list)
    num_unique_atoms=len(unique_atom_list)

    mySim = sim.SIM()
    #setting defaults
    
    
    if thermostat==None:
        
        thermostat='NOSE';
    if CUTOFF==None:
        CUTOFF=900;
    if SCF_tolerence==None:
        SCF_tolerence=1e-6
    if ensemble==None:
        ensemble='NVT'
    
    mySim.GLOBAL.RUN_TYPE = "GEO_OPT"
    mySim.GLOBAL.PROJECT_NAME  = name+"_opt"
    mySim.GLOBAL.PRINT_LEVEL = "LOW"
    #FORCE EVAL SECTION
    mySim.FORCE_EVAL.METHOD='QUICKSTEP'
    mySim.FORCE_EVAL.SUBSYS.CELL.ABC='{L} {L} {L}'.format(L=2*10*box_length)
    mySim.FORCE_EVAL.SUBSYS.COORD.DEFAULT_KEYWORD=mol_unopt_coord
    mySim.FORCE_EVAL.SUBSYS.init_atoms(num_atoms);
    
    for i in range(num_unique_atoms):
        mySim.FORCE_EVAL.SUBSYS.KIND[i+1].SECTION_PARAMETERS=unique_atom_list[i]
        
        if basis_set==[None]:
            
            mySim.FORCE_EVAL.SUBSYS.KIND[i+1].BASIS_SET=basis_set_setter(unique_atom_list[i])
        else:
            mySim.FORCE_EVAL.SUBSYS.KIND[i+1].BASIS_SET=basis_set[unique_atom_list[i]]
        mySim.FORCE_EVAL.SUBSYS.KIND[i+1].POTENTIAL=potential(unique_atom_list[i],functional)

    mySim.FORCE_EVAL.DFT.BASIS_SET_FILE_NAME=dire+'BASIS_MOLOPT'
    mySim.FORCE_EVAL.DFT.POTENTIAL_FILE_NAME=dire+'GTH_POTENTIALS'
    mySim.FORCE_EVAL.DFT.QS.EPS_DEFAULT=1E-10
    
    mySim.FORCE_EVAL.DFT.MGRID.CUTOFF=CUTOFF
    mySim.FORCE_EVAL.DFT.MGRID.REL_CUTOFF=50
    mySim.FORCE_EVAL.DFT.MGRID.NGRIDS=5

    mySim.FORCE_EVAL.DFT.XC.XC_FUNCTIONAL.SECTION_PARAMETERS=functional
    mySim.FORCE_EVAL.DFT.XC.VDW_POTENTIAL.POTENTIAL_TYPE='PAIR_POTENTIAL'
    mySim.FORCE_EVAL.DFT.XC.VDW_POTENTIAL.PAIR_POTENTIAL.TYPE='DFTD3'
    mySim.FORCE_EVAL.DFT.XC.VDW_POTENTIAL.PAIR_POTENTIAL.PARAMETER_FILE_NAME='dftd3.dat'
    mySim.FORCE_EVAL.DFT.XC.VDW_POTENTIAL.PAIR_POTENTIAL.REFERENCE_FUNCTIONAL=functional
    mySim.FORCE_EVAL.DFT.XC.VDW_POTENTIAL.PAIR_POTENTIAL.R_CUTOFF=11

    mySim.FORCE_EVAL.DFT.SCF.SCF_GUESS='ATOMIC'
    mySim.FORCE_EVAL.DFT.SCF.MAX_SCF=20
    mySim.FORCE_EVAL.DFT.SCF.EPS_SCF=SCF_tolerence

    mySim.MOTION.GEO_OPT.TYPE='MINIMIZATION'
    mySim.MOTION.GEO_OPT.OPTIMIZER='BFGS'
    mySim.MOTION.GEO_OPT.MAX_ITER=2
    mySim.MOTION.GEO_OPT.MAX_DR=1e-3

    mySim.MOTION.CONSTRAINT.FIXED_ATOMS.LIST ='1'
    mySim.write_changeLog(fn="mol_opt-changeLog.out")
    mySim.write_errorLog()
    mySim.write_inputFile(fn=opt_inp_file)


# In[7]:


def run_md_pre(molecule,functional,project_name,dire,temperature,pressure,box_length,number_of_molecules,simulation_time,
                      CUTOFF,SCF_tolerence,basis_set, ensemble, timestep, thermostat):
    
    atom_list=[];
    mass_list=[];
    for i in range(len(molecule)):
        current_molecule=mb.clone(molecule[i])
        current_molecule_pmd=current_molecule.to_parmed()    
        x,y=info_molecule(current_molecule_pmd);
        atom_list.extend(x)
        mass_list.extend(y)
    
    
    unique_atom_list=remove_duplicate(atom_list)
    num_atoms=len(atom_list)
    num_unique_atoms=len(unique_atom_list)
    unique_atom_list.sort()
    box = mb.Box(lengths=[box_length,box_length,box_length])
    
    box_of_molecule= mb.fill_box(compound=molecule, n_compounds=number_of_molecules, box=box)
    box_of_molecule.xyz=box_of_molecule.xyz
    filename=project_name+".xyz"
    box_of_molecule.save(filename,overwrite=True)
    with open(project_name+".xyz", 'r') as fin:
        data = fin.read().splitlines(True)
    with open(project_name+".xyz", 'w') as fout:
        fout.writelines(data[2:])
        
    
    if thermostat==None:
        
        thermostat='NOSE';
    if CUTOFF==None:
        CUTOFF=900;
    if SCF_tolerence==None:
        SCF_tolerence=1e-6
    if ensemble==None:
        ensemble='NVT'
               
               
    mySim = sim.SIM()

    mySim.GLOBAL.RUN_TYPE = "MD"
    mySim.GLOBAL.PROJECT_NAME  = project_name+"pre"
    mySim.GLOBAL.PRINT_LEVEL = "LOW"


    #FORCE EVAL SECTION
    mySim.FORCE_EVAL.METHOD='QUICKSTEP'
    mySim.FORCE_EVAL.STRESS_TENSOR='ANALYTICAL';

    mySim.FORCE_EVAL.DFT.BASIS_SET_FILE_NAME=dire+'BASIS_MOLOPT'
    mySim.FORCE_EVAL.DFT.POTENTIAL_FILE_NAME=dire+'GTH_POTENTIALS'
    mySim.FORCE_EVAL.DFT.CHARGE=0
    mySim.FORCE_EVAL.DFT.MULTIPLICITY=1
    mySim.FORCE_EVAL.DFT.MGRID.CUTOFF=CUTOFF
    mySim.FORCE_EVAL.DFT.MGRID.REL_CUTOFF=50
    mySim.FORCE_EVAL.DFT.MGRID.NGRIDS=4
    mySim.FORCE_EVAL.DFT.QS.METHOD='GPW'
    mySim.FORCE_EVAL.DFT.QS.EPS_DEFAULT=1E-8
    mySim.FORCE_EVAL.DFT.QS.EXTRAPOLATION='ASPC'
    mySim.FORCE_EVAL.DFT.POISSON.PERIODIC="XYZ"
    mySim.FORCE_EVAL.DFT.PRINT.E_DENSITY_CUBE.SECTION_PARAMETERS="OFF"
    mySim.FORCE_EVAL.DFT.SCF.SCF_GUESS='ATOMIC'
    mySim.FORCE_EVAL.DFT.SCF.MAX_SCF=2
    mySim.FORCE_EVAL.DFT.SCF.EPS_SCF=SCF_tolerence

    mySim.FORCE_EVAL.DFT.SCF.OT.SECTION_PARAMETERS=".TRUE."
    mySim.FORCE_EVAL.DFT.SCF.OT.PRECONDITIONER="FULL_SINGLE_INVERSE"
    mySim.FORCE_EVAL.DFT.SCF.OT.MINIMIZER="DIIS"
    mySim.FORCE_EVAL.DFT.SCF.OUTER_SCF.SECTION_PARAMETERS='.TRUE.'

    mySim.FORCE_EVAL.DFT.SCF.OUTER_SCF.MAX_SCF=10
    mySim.FORCE_EVAL.DFT.SCF.OUTER_SCF.EPS_SCF=1e-6
    mySim.FORCE_EVAL.DFT.SCF.PRINT.RESTART.SECTION_PARAMETERS='OFF'
    mySim.FORCE_EVAL.DFT.SCF.PRINT.DM_RESTART_WRITE='.TRUE.'

    mySim.FORCE_EVAL.DFT.XC.XC_FUNCTIONAL.SECTION_PARAMETERS=functional
    mySim.FORCE_EVAL.DFT.XC.VDW_POTENTIAL.POTENTIAL_TYPE='PAIR_POTENTIAL'
    mySim.FORCE_EVAL.DFT.XC.VDW_POTENTIAL.PAIR_POTENTIAL.TYPE='DFTD3'
    mySim.FORCE_EVAL.DFT.XC.VDW_POTENTIAL.PAIR_POTENTIAL.PARAMETER_FILE_NAME='dftd3.dat'
    mySim.FORCE_EVAL.DFT.XC.VDW_POTENTIAL.PAIR_POTENTIAL.REFERENCE_FUNCTIONAL=functional
    mySim.FORCE_EVAL.DFT.XC.VDW_POTENTIAL.PAIR_POTENTIAL.R_CUTOFF=11
    
    mySim.FORCE_EVAL.SUBSYS.COORD.DEFAULT_KEYWORD=project_name+".xyz";
    mySim.FORCE_EVAL.SUBSYS.init_atoms(num_atoms);
    
    for i in range(num_unique_atoms):
        mySim.FORCE_EVAL.SUBSYS.KIND[i+1].SECTION_PARAMETERS=unique_atom_list[i]
        if basis_set==[None]:
            
            mySim.FORCE_EVAL.SUBSYS.KIND[i+1].BASIS_SET=basis_set_setter(unique_atom_list[i])
        else:
            mySim.FORCE_EVAL.SUBSYS.KIND[i+1].BASIS_SET=basis_set[unique_atom_list[i]]
        mySim.FORCE_EVAL.SUBSYS.KIND[i+1].POTENTIAL=potential(unique_atom_list[i],functional)
    mySim.FORCE_EVAL.SUBSYS.CELL.ABC='{L} {L} {L}'.format(L=10*box_length)

    #MOTION SECTION
    mySim.MOTION.GEO_OPT.OPTIMIZER='BFGS'
    mySim.MOTION.GEO_OPT.MAX_ITER=100
    mySim.MOTION.GEO_OPT.MAX_DR=0.003


    mySim.MOTION.MD.ENSEMBLE = ensemble
    mySim.MOTION.MD.STEPS  = 1
    mySim.MOTION.MD.TIMESTEP = 0.2
    
    mySim.MOTION.MD.TEMPERATURE = temperature
    mySim.MOTION.MD.THERMOSTAT.TYPE = thermostat
    mySim.MOTION.MD.THERMOSTAT.REGION = "MASSIVE"
    mySim.MOTION.MD.THERMOSTAT.NOSE.LENGTH = 3
    mySim.MOTION.MD.THERMOSTAT.NOSE.YOSHIDA = 3
    mySim.MOTION.MD.THERMOSTAT.NOSE.TIMECON = 1000.0
    mySim.MOTION.MD.THERMOSTAT.NOSE.MTS = 2

    mySim.MOTION.MD.BAROSTAT.PRESSURE = pressure
    #mySim.MOTION.MD.PRINT.ENERGY.EACH.MD = 20
    #mySim.MOTION.MD.PRINT.PROGRAM_RUN_INFO.EACH.MD = 20
    #mySim.MOTION.MD.AVERAGES.SECTION_PARAMETERS= ".falbmbjse."


    mySim.MOTION.PRINT.STRESS.SECTION_PARAMETERS='OFF'
    mySim.MOTION.PRINT.TRAJECTORY.EACH.MD=1
    mySim.MOTION.PRINT.VELOCITIES.SECTION_PARAMETERS='OFF'
    mySim.MOTION.PRINT.FORCES.SECTION_PARAMETERS="OFF"
    mySim.MOTION.PRINT.RESTART_HISTORY.SECTION_PARAMETERS="ON"
    mySim.MOTION.PRINT.RESTART_HISTORY.EACH.MD=500
    mySim.MOTION.PRINT.RESTART.SECTION_PARAMETERS="ON"
    mySim.MOTION.PRINT.RESTART.BACKUP_COPIES=3

    mySim.MOTION.PRINT.RESTART.EACH.MD=1

    
    mySim.write_changeLog(fn="md-pre-changeLog.out")
    mySim.write_errorLog()
    mySim.write_inputFile(fn='md-pre.inp')


# In[8]:


def run_md_main(molecule,functional,project_name,dire,temperature,pressure, box_length,number_of_molecules,
                simulation_time,CUTOFF,SCF_tolerence,basis_set, ensemble, timestep, thermostat):
    
    
    atom_list=[];
    mass_list=[];
    num_atom_per_molecule_list=[];
    for i in range(len(molecule)):
        current_molecule=mb.clone(molecule[i])
        current_molecule_pmd=current_molecule.to_parmed()    
        x,y=info_molecule(current_molecule_pmd);
        num_atom_per_molecule_list.append(len(x))
        atom_list.extend(x)
        mass_list.extend(y)
    
    
    unique_atom_list=remove_duplicate(atom_list)
    num_atoms=len(atom_list)
    num_unique_atoms=len(unique_atom_list)
    unique_atom_list.sort()
    
    
    
    total_atoms=sum([a*b for a,b in zip(num_atom_per_molecule_list,number_of_molecules)])
    
    string="tail -{} {}-pos-1.xyz > {}.xyz".format(total_atoms,project_name+"pre",project_name)
    subprocess.call(string,shell=True)
    
    
    if thermostat==None:
        
        thermostat='NOSE';
    if CUTOFF==None:
        CUTOFF=900;
    if SCF_tolerence==None:
        SCF_tolerence=1e-6
    if ensemble==None:
        ensemble='NVT'
        
    #we need to decide time_step
    if timestep==None:
        lightest=min(mass_list);
    
        if lightest <1.5:
            timestep=0.5
        elif (lightest>=1.5) and (lightest<40):
            timestep=1
        if lightest>=40:
            timestep=1.5
    steps= int(simulation_time*1000/timestep)
    
    mySim = sim.SIM()

    mySim.GLOBAL.RUN_TYPE = "MD"
    mySim.GLOBAL.PROJECT_NAME  = project_name
    mySim.GLOBAL.PRINT_LEVEL = "LOW"


    #FORCE EVAL SECTION
    mySim.FORCE_EVAL.METHOD='QUICKSTEP'
    mySim.FORCE_EVAL.STRESS_TENSOR='ANALYTICAL';

    mySim.FORCE_EVAL.DFT.BASIS_SET_FILE_NAME=dire+'BASIS_MOLOPT'
    mySim.FORCE_EVAL.DFT.POTENTIAL_FILE_NAME=dire+'GTH_POTENTIALS'
    mySim.FORCE_EVAL.DFT.CHARGE=0
    mySim.FORCE_EVAL.DFT.MULTIPLICITY=1
    mySim.FORCE_EVAL.DFT.MGRID.CUTOFF=CUTOFF
    mySim.FORCE_EVAL.DFT.MGRID.REL_CUTOFF=50
    mySim.FORCE_EVAL.DFT.MGRID.NGRIDS=4
    mySim.FORCE_EVAL.DFT.QS.METHOD='GPW'
    mySim.FORCE_EVAL.DFT.QS.EPS_DEFAULT=1E-8
    mySim.FORCE_EVAL.DFT.QS.EXTRAPOLATION='ASPC'
    mySim.FORCE_EVAL.DFT.POISSON.PERIODIC="XYZ"
    mySim.FORCE_EVAL.DFT.PRINT.E_DENSITY_CUBE.SECTION_PARAMETERS="OFF"
    mySim.FORCE_EVAL.DFT.SCF.SCF_GUESS='ATOMIC'
    mySim.FORCE_EVAL.DFT.SCF.MAX_SCF=2
    mySim.FORCE_EVAL.DFT.SCF.EPS_SCF=SCF_tolerence

    mySim.FORCE_EVAL.DFT.SCF.OT.SECTION_PARAMETERS=".TRUE."
    mySim.FORCE_EVAL.DFT.SCF.OT.PRECONDITIONER="FULL_SINGLE_INVERSE"
    mySim.FORCE_EVAL.DFT.SCF.OT.MINIMIZER="DIIS"
    mySim.FORCE_EVAL.DFT.SCF.OUTER_SCF.SECTION_PARAMETERS='.TRUE.'

    mySim.FORCE_EVAL.DFT.SCF.OUTER_SCF.MAX_SCF=2
    mySim.FORCE_EVAL.DFT.SCF.OUTER_SCF.EPS_SCF=1e-6
    mySim.FORCE_EVAL.DFT.SCF.PRINT.RESTART.SECTION_PARAMETERS='OFF'
    mySim.FORCE_EVAL.DFT.SCF.PRINT.DM_RESTART_WRITE='.TRUE.'

    mySim.FORCE_EVAL.DFT.XC.XC_FUNCTIONAL.SECTION_PARAMETERS=functional
    mySim.FORCE_EVAL.DFT.XC.VDW_POTENTIAL.POTENTIAL_TYPE='PAIR_POTENTIAL'
    mySim.FORCE_EVAL.DFT.XC.VDW_POTENTIAL.PAIR_POTENTIAL.TYPE='DFTD3'
    mySim.FORCE_EVAL.DFT.XC.VDW_POTENTIAL.PAIR_POTENTIAL.PARAMETER_FILE_NAME='dftd3.dat'
    mySim.FORCE_EVAL.DFT.XC.VDW_POTENTIAL.PAIR_POTENTIAL.REFERENCE_FUNCTIONAL=functional
    mySim.FORCE_EVAL.DFT.XC.VDW_POTENTIAL.PAIR_POTENTIAL.R_CUTOFF=11
    mySim.FORCE_EVAL.SUBSYS.COORD.DEFAULT_KEYWORD=project_name+".xyz";
    mySim.FORCE_EVAL.SUBSYS.init_atoms(num_atoms);
    
    for i in range(num_unique_atoms):
        mySim.FORCE_EVAL.SUBSYS.KIND[i+1].SECTION_PARAMETERS=unique_atom_list[i]
        if basis_set==[None]:
            
            mySim.FORCE_EVAL.SUBSYS.KIND[i+1].BASIS_SET=basis_set_setter(unique_atom_list[i])
        else:
            mySim.FORCE_EVAL.SUBSYS.KIND[i+1].BASIS_SET=basis_set[unique_atom_list[i]]
        mySim.FORCE_EVAL.SUBSYS.KIND[i+1].POTENTIAL=potential(unique_atom_list[i],functional)
    mySim.FORCE_EVAL.SUBSYS.CELL.ABC='{L} {L} {L}'.format(L=10*box_length)

    #MOTION SECTION
    mySim.MOTION.GEO_OPT.OPTIMIZER='BFGS'
    mySim.MOTION.GEO_OPT.MAX_ITER=100
    mySim.MOTION.GEO_OPT.MAX_DR=0.003


    mySim.MOTION.MD.ENSEMBLE = ensemble
    mySim.MOTION.MD.STEPS  = steps
    mySim.MOTION.MD.TIMESTEP = timestep
    mySim.MOTION.MD.TEMPERATURE = temperature
    mySim.MOTION.MD.THERMOSTAT.TYPE = thermostat
    mySim.MOTION.MD.THERMOSTAT.REGION = "MASSIVE"
    mySim.MOTION.MD.THERMOSTAT.NOSE.LENGTH = 3
    mySim.MOTION.MD.THERMOSTAT.NOSE.YOSHIDA = 3
    mySim.MOTION.MD.THERMOSTAT.NOSE.TIMECON = 1000.0
    mySim.MOTION.MD.THERMOSTAT.NOSE.MTS = 2

    mySim.MOTION.MD.BAROSTAT.PRESSURE = pressure
    #mySim.MOTION.MD.PRINT.ENERGY.EACH.MD = 20
    #mySim.MOTION.MD.PRINT.PROGRAM_RUN_INFO.EACH.MD = 20
    #mySim.MOTION.MD.AVERAGES.SECTION_PARAMETERS= ".falbmbjse."


    mySim.MOTION.PRINT.STRESS.SECTION_PARAMETERS='OFF'
    mySim.MOTION.PRINT.TRAJECTORY.EACH.MD=1
    mySim.MOTION.PRINT.VELOCITIES.SECTION_PARAMETERS='OFF'
    mySim.MOTION.PRINT.FORCES.SECTION_PARAMETERS="OFF"
    mySim.MOTION.PRINT.RESTART_HISTORY.SECTION_PARAMETERS="ON"
    mySim.MOTION.PRINT.RESTART_HISTORY.EACH.MD=500
    mySim.MOTION.PRINT.RESTART.SECTION_PARAMETERS="ON"
    mySim.MOTION.PRINT.RESTART.BACKUP_COPIES=3

    mySim.MOTION.PRINT.RESTART.EACH.MD=1

    
    mySim.write_changeLog(fn="md-main-changeLog.out")
    mySim.write_errorLog()
    mySim.write_inputFile(fn='md-main.inp')






