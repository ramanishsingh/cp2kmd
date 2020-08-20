#!/usr/bin/env python
# coding: utf-8

# # CP2K MD workflow

# In[1]:


# Deleting files that we do not need, files generated from a previous run
import os
import glob

extension_list=["*inp*","*out","*ener","*rest*","*Hess*","*REST*","*.xyz","*.pdb"]
for name in extension_list:
    
    filelist=glob.glob(name)
    for file in filelist:
        os.remove(file)


# ### Loading modules

# In[2]:



import mbuild as mb 

import numpy as np
from cp2kmd import runners
import unyt as u

from cp2kmd.cp2kmd import Cp2kmd
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
        
        fluorine1= mb.Particle(pos=[0.0, 0.0, 0.0], name='F')
        chlorine2= mb.Particle(pos=[0.2, 0.0, 0.0], name='Cl')
        self.add([fluorine1,chlorine2])
        self.add_bond((fluorine1,chlorine2))


# In[4]:


md=Cp2kmd(molecule=[Cl2(),FCl()])


# ### Forcefield and ensemble

# In[5]:



md.basis_set={'F':'DZVP-MOLOPT-SR-GTH','Cl':'DZVP-MOLOPT-SR-GTH'}
md.functional='PBE'
md.dire='/home/siepmann/singh891/cp2k-6.1.0/data/'
md.CUTOFF=400

md.ensemble='NPT_I'
md.number_of_molecules=[10,10]
md.box_length=1.1*u.nm;
md.temperature=273.15*u.K
md.pressure=1*u.bar

md.simulation_time=0.02*u.ps #ps

md.project_name='chlorine'
md.timestep=1*u.fs;


# ### Generating opt input file

# In[6]:


md.optimize_files()


# In[ ]:





# ### Running molecule optimization

# In[7]:



runners.run_optimize(md)
print('opt completed')


# ### Generating pre run files

# In[ ]:


md.run_pre_files()


# ### pre run

# In[ ]:



runners.run_md_pre(md)


# ### Generating main run files

# In[ ]:


md.run_main_files()


# ### Running main MD

# In[ ]:


runners.run_md_main(md)


# #### chlorine-1.ener and chlorine-pos-1.xyz (energy and trajectory files generated)
