Inner workings
===============
cp2kmd requires the input molecules to be defined as an mBuild molecule. The conditions of the simulation also need to be defined (See Cp2kmd class below).
After the structure(s) of the molecule(s) is defined, an instance of Cp2kmd class shall be generated and all the information about the simulation can be specified in it (see examples).

cp2kmd workflow executes the MD simulations in three steps

#. Optimize the structure of each molecule type.
#. Launch a short MD trajectory with very small time step to prevent any blow-ups during the main run.
#. Launch the main simulation with desired number of steps.



The Cp2kmd class
-----------------
An instance of the Cp2kmd class contains the following objects:

#. molecule: List of molecule(s), each element must be a mBuild `Compound <https://mbuild.mosdef.org/en/stable/data_structures.html>`_
#. functional:  `XC functional <https://manual.cp2k.org/trunk/CP2K_INPUT/ATOM/METHOD/XC/XC_FUNCTIONAL.html>`_, must be string
#. project_name: Name of the project, must be a string
#. dire: The directory where the functional data is stored, must be a string
#. temperature: Simulation temperature, not needed for *NVE* simulations, float
#. box_length: List containing the box lengths
#. number_of_molecules: List of number of molecules of different types
#. simulation_time: Length of simulations
#. CUTOFF: Plane-wave cutoff in Ry
#. SCF_tolerence: Tolerance for SCF convergence
#. basis_set: Dictionary of basis sets with atomic symbols (string) as the keys
#. ensemble: Ensemble for the simulation
#. timestep: Timestep for MD simulation
#. thermostat: Type of thermostat, not required if ensemble is NVE
#. pressure: Pressure, only required if ensemble is *NpT*


Input file writer
------------------

The input files are written using the cssi_cp2k module. It can be found in the cp2kmd/writer directory.
The SIM class contains the sections of the CP2K input file as objects. There are individual classes for all subsections and variables can be changed by accessing the object in that class.
For example, if the RUN_TYPE has to be set to MD, it can be changed as : SIM().GLOBAL.RUN_TYPE=MD.

The input file writer (cssi_cp2k) is used in cp2kmd/novice_functions to generate the optimization, pre-md, and main-md input files (.inp).


Changing the default parameters
----------------------------------
In case the objects other than the objects in the Cp2kmd class need to be changed, they can be changed in the novice_functions.py file.
Parameters for molecule optimization can be changed in optimize_molecule function.
Similarly for pre-md run and main-md run, change the run_md_pre and run_md_main function respectively.

test
----------------------------------