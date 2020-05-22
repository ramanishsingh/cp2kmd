#quick test that works on my laptop
from cssi_cp2k.classes import SIM as sim

mySim = sim.SIM()
mySim.GLOBAL.RUN_TYPE = "MC"
mySim.write_changeLog()
mySim.GLOBAL.RUN_TYPE = "ARb"
mySim.write_errorLog()
mySim.write_changeLog()
