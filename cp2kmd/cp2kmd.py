from cp2kmd import novice_functions
from subprocess import call
import numpy as np
import mbuild as mb
class Cp2kmd():
    def __init__(self,molecule=None, functional=None, project_name=None,dire= '/home/siepmann/singh891/cp2k-6.1.0/data/',
                 temperature= None,box_length=None,number_of_molecules=None,simulation_time=None,CUTOFF=None, SCF_tolerence=None,
                 basis_set=[None], ensemble=None, timestep=None, thermostat=None,pressure=None):
        self.molecule=molecule;
        
        #self.molecule.save('molecule.pdb',overwrite='True')
        self.functional=functional;
        self.dire=dire;
        self.temperature=temperature;
        self.box_length=box_length;
        self.number_of_molecules=number_of_molecules;
        self.simulation_time=simulation_time;
        self.project_name=project_name
        self.CUTOFF=CUTOFF;
        self.SCF_tolerence=SCF_tolerence;
        self.basis_set=basis_set;
        self.ensemble=ensemble;
        self.timestep=timestep;
        self.thermostat=thermostat;
        self.pressure=pressure;
        
        molecule=[i.to_parmed() for i in molecule]
        self.number_atom_per_molecule=[len(i.atoms) for i in molecule]
    def optimize_files(self):
        
        
        molecule=self.molecule;
        
        functional=self.functional;
        project_name=self.project_name;
        dire=self.dire;
        temperature=self.temperature;
        pressure=self.pressure;
        number_of_molecules=self.number_of_molecules;
        box_length=self.box_length;
        number_of_molecules=self.number_of_molecules;
        simulation_time=self.simulation_time
        CUTOFF=self.CUTOFF
        SCF_tolerence=self.SCF_tolerence
        basis_set=self.basis_set
        ensemble=self.ensemble
        
        timestep=self.timestep
        thermostat=self.thermostat
        if temperature is not None:
            
            temperature=(temperature.to('K')).value
        if pressure is not None:
            pressure=(pressure.to('bar')).value
        box_length=(box_length.to('nm')).value
        simulation_time=(simulation_time.to('ps')).value
        timestep=(timestep.to('fs')).value
        names=[i.name for i in molecule]
        self.opt_inp_file=[str(i)+'_opt.inp' for i in names]
        self.mol_unopt_coord=[str(i)+'_unopt_coord.xyz' for i in names]
        
        opt_inp_file=self.opt_inp_file
        mol_unopt_coord=self.mol_unopt_coord
        for i in range(len(names)):
            
            novice_functions.optimize_molecule(molecule[i],functional,project_name,dire,temperature,box_length,number_of_molecules,
                                           simulation_time,CUTOFF,SCF_tolerence,basis_set, ensemble, timestep, thermostat,opt_inp_file[i],mol_unopt_coord[i])
            
        
        
        
    
        
        
    def run_pre_files(self):
        molecule=self.molecule;
        functional=self.functional;
        project_name=self.project_name;
        dire=self.dire;
        temperature=self.temperature;
        pressure=self.pressure;
        
        number_of_molecules=self.number_of_molecules;
        box_length=self.box_length;
        simulation_time=self.simulation_time
        CUTOFF=self.CUTOFF
        SCF_tolerence=self.SCF_tolerence
        basis_set=self.basis_set
        ensemble=self.ensemble
        timestep=self.timestep
        thermostat=self.thermostat
        number_atom_per_molecule=self.number_atom_per_molecule
        if temperature is not None:
            
            temperature=(temperature.to('K')).value
        if pressure is not None:
            pressure=(pressure.to('bar')).value
            
        box_length=(box_length.to('nm')).value
        simulation_time=(simulation_time.to('ps')).value
        timestep=(timestep.to('fs')).value
        novice_functions.run_md_pre(molecule,functional,project_name,dire,temperature,pressure, box_length,number_of_molecules,
                                    simulation_time,CUTOFF,SCF_tolerence,basis_set, ensemble, timestep, thermostat)
    def run_main_files(self):
        molecule=self.molecule;
        functional=self.functional;
        project_name=self.project_name;
        
        dire=self.dire;
        
        temperature=self.temperature;
        box_length=self.box_length;
        pressure=self.pressure;
        number_of_molecules=self.number_of_molecules;
        
        simulation_time=self.simulation_time;
        
        CUTOFF=self.CUTOFF
        SCF_tolerence=self.SCF_tolerence
        basis_set=self.basis_set
        ensemble=self.ensemble
        timestep=self.timestep
        thermostat=self.thermostat
        if temperature is not None:
            
            temperature=(temperature.to('K')).value
        if pressure is not None:
            pressure=(pressure.to('bar')).value
        box_length=(box_length.to('nm')).value
        simulation_time=(simulation_time.to('ps')).value
        timestep=(timestep.to('fs')).value
        
        novice_functions.run_md_main(molecule,functional,project_name,dire,temperature,pressure,box_length,number_of_molecules,
                                    simulation_time,CUTOFF,SCF_tolerence,basis_set, ensemble, timestep, thermostat)
        

