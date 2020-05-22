from subprocess import call
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


