import novice_functions
from subprocess import call
import numpy as np
import mbuild as mb
class Cp2kmd():
    def __init__(self,molecule=None, functional=None, project_name=None,dire= '/home/siepmann/singh891/cp2k-6.1.0/data/',
                 temperature= None,box_length=None,number_of_molecules=None,simulation_time=None,CUTOFF=None, SCF_tolerence=None,
                 basis_set=[None], ensemble=None, timestep=None, thermostat=None):
        self.molecule=molecule;
        self.molecule.save('molecule.pdb',overwrite='True')
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
        
        molecule=molecule.to_parmed();
        
        self.number_atom_per_molecule=len(molecule.atoms)
    def optimize_files(self):
        molecule=self.molecule;
        functional=self.functional;
        project_name=self.project_name;
        dire=self.dire;
        temperature=self.temperature;
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
        
        novice_functions.optimize_molecule(molecule,functional,project_name,dire,temperature,box_length,number_of_molecules,
                                           simulation_time,CUTOFF,SCF_tolerence,basis_set, ensemble, timestep, thermostat)
        
        
        
    
        
        self.opt_inp_file='mol_opt.inp'
        self.mol_unopt_coord='mol_unopt_coord.xyz'
    def run_pre_files(self):
        molecule=self.molecule;
        functional=self.functional;
        project_name=self.project_name;
        dire=self.dire;
        temperature=self.temperature;
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
        string="tail -{} molecule_opt-pos-1.xyz > opt_coor.xyz".format(number_atom_per_molecule)
        call(string,shell=True)
        table=0*np.empty([1, 3])#dummy array to start with;
        scaling=0*np.empty([1,3])# scaling for nm to A
        with open('opt_coor.xyz') as input_data:
            for line in input_data:
                n, x, y,z = line.strip().split()
                table=np.concatenate((table, np.array([[float(x),float(y),float(z)]])), axis=0);
        table=np.delete(table,0,0)
        table=table*0.1;
        molecule=mb.load('molecule.pdb');
        novice_functions.run_md_pre(molecule,functional,project_name,dire,temperature,box_length,number_of_molecules,
                                    simulation_time,CUTOFF,SCF_tolerence,basis_set, ensemble, timestep, thermostat,table)
    def run_main_files(self):
        molecule=self.molecule;
        functional=self.functional;
        project_name=self.project_name;
        
        dire=self.dire;
        
        temperature=self.temperature;
        box_length=self.box_length;
        
        number_of_molecules=self.number_of_molecules;
        
        simulation_time=self.simulation_time;
        
        CUTOFF=self.CUTOFF
        SCF_tolerence=self.SCF_tolerence
        basis_set=self.basis_set
        ensemble=self.ensemble
        timestep=self.timestep
        thermostat=self.thermostat
        
        novice_functions.run_md_main(molecule,functional,project_name,dire,temperature,box_length,number_of_molecules,
                                    simulation_time,CUTOFF,SCF_tolerence,basis_set, ensemble, timestep, thermostat)
        

