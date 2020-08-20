Inner workings
===============


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
The SIM class contains the sections of the CP2K input file as objects. There are individual classes for all subsections and varibales can be changed by accessing the object in that class.
For example, if the RUN_TYPE has to be set to MD, it can be changed as : SIM.


