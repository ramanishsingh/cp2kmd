#!/usr/bin/env python
# coding: utf-8

# # CP2K MD workflow

# In[1]:


# Deleting files that we do not need
import os
import glob

extension_list=["*inp*","*out","*ener","*rest*","*Hess*","*REST*","*.xyz","*.pdb"]
for name in extension_list:
    
    filelist=glob.glob(name)
    for file in filelist:
        os.remove(file)
    


# In[1]:




# In[5]:


import mbuild as mb 
import novice_functions
import signac
import flow
from shutil import copyfile
from subprocess import call
import numpy as np


# In[6]:


class cp2kmd():
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
        


# In[7]:


def run_optimize(system):
    inp_file, out_file,struc_file=system.opt_inp_file,'mol_opt.out',system.mol_unopt_coord;
    print(inp_file)
    call("~/test-cp2k/cp2k/exe/Linux-x86-64-intel/cp2k.popt -i {} -o {}".format(inp_file,out_file),shell=True)
    
def run_md_pre(system):
    inp_file,out_file='md-pre.inp','md-pre.out'
    call("~/test-cp2k/cp2k/exe/Linux-x86-64-intel/cp2k.popt -i {} -o {}".format(inp_file,out_file),shell=True) 

def run_md_main(system):
    inp_file,out_file='md-main.inp','md-main.out'
    call("~/test-cp2k/cp2k/exe/Linux-x86-64-intel/cp2k.popt -i {} -o {}".format(inp_file,out_file),shell=True)


# In[8]:


class Cl2(mb.Compound): # this class builds a chlorine molecule with a bond-length given in the chlorine2 x coor (nm)
    def __init__(self):
        super(Cl2, self).__init__()
        
        chlorine1= mb.Particle(pos=[0.0, 0.0, 0.0], name='Cl')
        chlorine2= mb.Particle(pos=[0.2, 0.0, 0.0], name='Cl')
        self.add([chlorine2,chlorine1])
        self.add_bond((chlorine2,chlorine1))


# In[9]:



molecule=Cl2();
md=cp2kmd(molecule=Cl2(), functional='PBE', project_name='chlorine')


# In[10]:


dir(md)


# In[17]:


md.box_length=1.1;
md.basis_set=['DZVP-MOLOPT-SR-GTH']
md.box_length=1.1;
md.dire='/home/siepmann/singh891/cp2k-6.1.0/data/'
md.ensemble='NVT'
md.number_of_molecules=10
md.temperature=200
md.simulation_time=0.002
md.CUTOFF=400;

# In[18]:


md.optimize_files()


# In[ ]:


run_optimize(md)
print('opt completed')


# In[19]:


md.run_pre_files()


# In[20]:


run_md_pre(md)


# In[21]:


md.run_main_files()


# In[23]:


run_md_main(md)


# In[ ]:




