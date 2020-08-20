# cp2kmd

This is workflow is intended for beginners to help them start running MD simulations in CP2K. It uses MoSDeF (https://github.com/mosdef-hub/mbuild) tools to set up input structure. Input files are generated using the codes in the cssi_cp2k folder. 

The input structures needs to be defined as an mbuild molecule. Other properties such as the box length, the simulation temperature, the functional etc. need to be defined before starting the simulation. Sample inputs for the workflow can be seen in sample_test.ipynb file. 

The worflow first optimizes the strucure of a single molecule. After that it runs a short MD trajectory with a very small timestep to make sure that the simulation does not blow up. After that, main MD simulation is submitted to the cluster.
If only the input files and input structures are wanted, the user can omit the run commands. 

You also need to install unyt package in your environment.


Make a `mosdef36` conda environment:

```bash
conda create -n mosdef36 -c mosdef -c conda-forge -c omnia python=3.6 mbuild foyer signac signac-flow pandas
conda activate mosdef36
conda install -c conda-forge openbabel  
pip install unyt
```
