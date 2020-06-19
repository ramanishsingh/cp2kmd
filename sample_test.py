#!/usr/bin/env python
# coding: utf-8

# # CP2K MD workflow

# In[ ]:


# Deleting files that we do not need, files generated from a previous run
import os
import glob

extension_list=["*inp*","*out","*ener","*rest*","*Hess*","*REST*","*.xyz","*.pdb"]
for name in extension_list:
    
    filelist=glob.glob(name)
    for file in filelist:
        os.remove(file)


# ### Loading modules

# In[1]:



import mbuild as mb 

import signac
import flow
from shutil import copyfile

import numpy as np
from cp2kmd import Cp2kmd
import runners
import unyt as u


# In[ ]:





# ### Defining the molecule

# In[3]:


class Cl2(mb.Compound): # this class builds a chlorine molecule with a bond-length given in the chlorine2 x coor (nm)
    def __init__(self):
        super(Cl2, self).__init__()
        
        chlorine1= mb.Particle(pos=[0.0, 0.0, 0.0], name='Cl')
        chlorine2= mb.Particle(pos=[0.2, 0.0, 0.0], name='Cl')
        self.add([chlorine2,chlorine1])
        self.add_bond((chlorine2,chlorine1))
        
class FCl(mb.Compound): # this class builds a chlorine molecule with a bond-length given in the chlorine2 x coor (nm)
    def __init__(self):
        super(FCl, self).__init__()
        
        chlorine1= mb.Particle(pos=[0.0, 0.0, 0.0], name='F')
        chlorine2= mb.Particle(pos=[0.2, 0.0, 0.0], name='Cl')
        self.add([chlorine2,chlorine1])
        self.add_bond((chlorine2,chlorine1))


# In[4]:



md=Cp2kmd(molecule=[Cl2(),FCl()])


# In[5]:


dir(md)


# ### Forcefield and ensemble

# In[6]:



md.basis_set={'F':'DZVP-MOLOPT-SR-GTH','Cl':'DZVP-MOLOPT-SR-GTH'}
md.box_length=1.1*u.nm;
md.dire='/home/siepmann/singh891/cp2k-6.1.0/data/'
md.ensemble='NVT'
md.number_of_molecules=[10,10]
md.temperature=273.15*u.K
md.simulation_time=0.010*u.ps #ps
md.CUTOFF=400
md.functional='PBE'
md.project_name='chlorine'
md.timestep=1*u.fs;


# In[ ]:





# ### Generating opt input file

# In[7]:


md.optimize_files()


# ### Running molecule optimization

# In[9]:



runners.run_optimize(md)
print('opt completed')


# ### Generating pre run files

# In[11]:


md.run_pre_files()


# ### pre run

# In[12]:



runners.run_md_pre(md)


# ### Generating main run files

# In[15]:


md.run_main_files()


# ### Running main MD

# In[16]:


runners.run_md_main(md)


# In[ ]:




