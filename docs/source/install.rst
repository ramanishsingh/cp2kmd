Installation
============
Conda installation is recommended. The package can be downloaded from `here <https://github.com/ramanishsingh/cp2kmd>`_.


Conda environment
-----------------
cp2kmd has been built and tested on python 3.6.
You can use the following commands to create a virtual conda environment with all the cp2kmd dependencies.


>>> conda create -n mosdef36 -c mosdef -c conda-forge -c omnia python=3.6 mbuild foyer signac signac-flow pandas
>>> conda activate mosdef36
>>> conda install -c conda-forge openbabel
>>> cd cp2kmd/cp2kmd
>>> pip install -e .
>>> cd ../writer
>>> pip install -e .



