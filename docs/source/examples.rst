Examples
========

- *NVT* ensemble molecular dynamics simulation of liquid dioxygen (O\ :sub:`2`) in CP2K

.. *pretend showing how to use* :code:`os` *module*



.. code-block:: python

    # Deleting files that we do not need, files generated from a previous run
    import os
    import glob

    extension_list=["*inp*","*out","*ener","*rest*","*Hess*","*REST*","*.xyz","*.pdb"]
    for name in extension_list:

        filelist=glob.glob(name)
        for file in filelist:
            os.remove(file)


    # ### Loading modules

    import mbuild as mb # mBuild is required for input structure generation
    import numpy as np
    from cp2kmd import runners
    import unyt as u

    from cp2kmd.cp2kmd import Cp2kmd



    #defining the molecule
    class O2(mb.Compound): # this class builds a chlorine molecule with a bond-length given in the chlorine2 x coor (nm)
    def __init__(self):
        super(O2, self).__init__()

        oxygen1= mb.Particle(pos=[0.0, 0.0, 0.0], name='O')
        oxygen2= mb.Particle(pos=[0.16, 0.0, 0.0], name='O')
        self.add([oxygen2,oxygen1])
        self.add_bond((oxygen2,oxygen1))

    md=Cp2kmd(molecule=[O2()]) # creating an instance of the Cp2kmd class
    md.basis_set={'O':'DZVP-MOLOPT-SR-GTH'} # defining the basis set we want to use for oxygen element
    md.functional='PBE'
    md.dire='/home/siepmann/singh891/cp2k-6.1.0/data/' # directory where the data is stored
    md.ensemble='NVT'
    md.number_of_molecules=[10]
    md.box_length=1.1*u.nm;
    md.temperature=173.15*u.K

    md.simulation_time=0.010*u.ps
    md.project_name='oxygen-md'
    md.timestep=1*u.fs;
    md.CUTOFF=400

    # ### Generating opt input file
    md.optimize_files()


    # ### Running molecule optimization

    runners.run_optimize(md)
    print('opt completed')

    ## running pre-md run
    md.run_pre_files()
    runners.run_md_pre(md)

    ### ### Generating main run files
    md.run_main_files()

    # ### Running main MD
    runners.run_md_main(md)

*NpT* ensemble molecular dynamics simulation of liquid dioxygen (O\ :sub:`2`)  and liquid dichlorine mixture (Cl\ :sub:`2`)in CP2K





.. code-block:: python

    # Deleting files that we do not need, files generated from a previous run
    import os
    import glob

    extension_list=["*inp*","*out","*ener","*rest*","*Hess*","*REST*","*.xyz","*.pdb"]
    for name in extension_list:

        filelist=glob.glob(name)
        for file in filelist:
            os.remove(file)


    # ### Loading modules

    import mbuild as mb # mBuild is required for input structure generation
    import numpy as np
    from cp2kmd import runners
    import unyt as u

    from cp2kmd.cp2kmd import Cp2kmd

    #defining the molecules
    class O2(mb.Compound): # this class builds a chlorine molecule with a bond-length given in the chlorine2 x coor (nm)
    def __init__(self):
        super(O2, self).__init__()

        oxygen1= mb.Particle(pos=[0.0, 0.0, 0.0], name='O')
        oxygen2= mb.Particle(pos=[0.16, 0.0, 0.0], name='O')
        self.add([oxygen2,oxygen1])
        self.add_bond((oxygen2,oxygen1))

    class Cl2(mb.Compound): # this class builds a chlorine molecule with a bond-length given in the chlorine2 x coor (nm)
        def __init__(self):
            super(Cl2, self).__init__()

            chlorine1= mb.Particle(pos=[0.0, 0.0, 0.0], name='Cl')
            chlorine2= mb.Particle(pos=[0.2, 0.0, 0.0], name='Cl')
            self.add([chlorine2,chlorine1])
            self.add_bond((chlorine2,chlorine1))

    md=Cp2kmd(molecule=[O2(),Cl2()]) # creating an instance of the Cp2kmd class
    md.basis_set={'O':'DZVP-MOLOPT-SR-GTH','Cl':'DZVP-MOLOPT-SR-GTH'} # defining the basis set we want to use for oxygen element
    md.functional='PBE'
    md.dire='/home/siepmann/singh891/cp2k-6.1.0/data/' # directory where the data is stored
    md.ensemble='NPT_I'
    md.number_of_molecules=[10,10]
    md.box_length=1.5*u.nm;
    md.temperature=173.15*u.K
    md.pressure=173.15*u.K

    md.simulation_time=0.010*u.ps
    md.project_name='O2Cl2-mix-nptmd'
    md.timestep=1*u.fs;
    md.CUTOFF=400

    # ### Generating opt input file
    md.optimize_files()


    # ### Running molecule optimization

    runners.run_optimize(md)
    print('opt completed')

    ## running pre-md run
    md.run_pre_files()
    runners.run_md_pre(md)

    ### ### Generating main run files
    md.run_main_files()

    # ### Running main MD
    runners.run_md_main(md)