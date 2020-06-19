from subprocess import call
import mbuild as mb
def run_optimize(system):
    for i in range(len(system.molecule)):
        
        inp_file, out_file,struc_file=system.opt_inp_file[i],system.molecule[i].name+'_opt.out',system.mol_unopt_coord[i];
        print(inp_file)
        call("~/test-cp2k/cp2k/exe/Linux-x86-64-intel/cp2k.popt -i {} -o {}".format(inp_file,out_file),shell=True)
        string="tail -{} {}_opt-pos-1.xyz > opt_coor.xyz".format(system.number_atom_per_molecule[i]+2,system.molecule[i].name)
        
        call(string,shell=True)
        system.molecule[i]=mb.load('opt_coor.xyz')
       
        system.molecule[i].xyz=system.molecule[i].xyz
    
def run_md_pre(system):
    inp_file,out_file='md-pre.inp','md-pre.out'
    call("~/test-cp2k/cp2k/exe/Linux-x86-64-intel/cp2k.popt -i {} -o {}".format(inp_file,out_file),shell=True) 

def run_md_main(system):
    inp_file,out_file='md-main.inp','md-main.out'
    call("~/test-cp2k/cp2k/exe/Linux-x86-64-intel/cp2k.popt -i {} -o {}".format(inp_file,out_file),shell=True)


