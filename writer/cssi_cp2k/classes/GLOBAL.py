import os
import datetime
from cssi_cp2k.classes import DBCSR
from cssi_cp2k.classes import FM
from cssi_cp2k.classes import FM_DIAG_SETTINGS
from cssi_cp2k.classes import PRINT
from cssi_cp2k.classes import PRINT_ELPA
from cssi_cp2k.classes import PROGRAM_RUN_INFO
from cssi_cp2k.classes import REFERENCES
from cssi_cp2k.classes import TIMINGS
import cssi_cp2k.utilities as utilities

BLACS_GRID_VALS     = ["COLUMN","ROW","SQUARE"]
CALLGRAPH_VALS      = ["ALL","MASTER","NONE"]
ELPA_KERNEL_VALS    = ["AUTO","AVX2_BLOCK2","AVX2_BLOCK4","AVX2_BLOCK6","AVX512_BLOCK2",
                       "AVX512_BLOCK4","AVX512_BLOCK6","AVX_BLOCK2","AVX_BLOCK4","AVX_BLOCK6","BGP",
                       "BGQ","GENERIC","GENERIC_SIMPLE","GPU","SSE","SSE_BLOCK2","SSE_BLOCK4",
                       "SSE_BLOCK6"]
FFTW_PLAN_TYPE_VALS = ["ESTIMATE","EXHAUSTIVE","MEASURE","PATIENT"]
PREFERRED_DIAG_LIBRARY_VALS = ["ELPA","SL","SL2"]
PREFERRED_FFT_LIBRARY_VALS  = ["FFTSG","FFTW","FFTW3"]
PRINT_LEVEL_VALS            = ["DEBUG","HIGH","LOW","MEDIUM","SILENT"]
PROGRAM_NAME_VALS           = ["ATOM","CP2K","FARMING","MC_ANALYSIS","OPTIMIZE_BASIS","OPTIMIZE_INPUT",
                               "SWARM","TEST","TMC"]
RUN_TYPE_VALS               = ["BAND","BSSE","CELL_OPT","DEBUG","DRIVER","EHRENFEST_DYN",
                               "ELECTRONIC_SPECTRA","ENERGY","ENERGY_FORCE","GEOMETRY_OPTIMIZATION",
                               "GEO_OPT","LINEAR_RESPONSE","LR","MC","MOLECULAR_DYNAMICS","MD","MONTECARLO",
                               "NEGF","NONE","NORMAL_MODES","PINT","RT_PROPAGATION","SPECTRA","TAMC",
                               "TMC","VIBRATIONAL_ANALYSIS","WAVEFUNCTION_OPTIMIZATION","WFN_OPT"]

class GLOBAL:

  def __init__(self,ALLTOALL_SGL=None,BLACS_GRID=None,BLACS_REPEATABLE=None,CALLGRAPH=None,
               CALLGRAPH_FILE_NAME=None,ECHO_ALL_HOSTS=None,ECHO_INPUT=None,ELPA_KERNEL=None,
               ELPA_QR=None,ELPA_QR_UNSAFE=None,EXTENDED_FFT_LENGTHS=None,FFTW_PLAN_TYPE=None,
               FFTW_WISDOM_FILE_NAME=None,FFT_POOL_SCRATCH_LIMIT=None,
               FLUSH_SHOULD_FLUSH=None,OUTPUT_FILE_NAME=None,PREFERRED_DIAG_LIBRARY=None,
               PREFERRED_FFT_LIBRARY=None,PRINT_LEVEL=None,PROGRAM_NAME=None,
               PROJECT_NAME=None,RUN_TYPE=None,SAVE_MEM=None,SEED=None,TRACE=None,
               TRACE_MASTER=None,TRACE_MAX=None,TRACE_ROUTINES=None,WALLTIME=None,errorLog=[],
               changeLog=[],location=""):

    self.__ALLTOALL_SGL           = ALLTOALL_SGL
    self.__BLACS_GRID             = BLACS_GRID
    self.__BLACS_REPEATABLE       = BLACS_REPEATABLE
    self.__CALLGRAPH              = CALLGRAPH
    self.__CALLGRAPH_FILE_NAME    = CALLGRAPH_FILE_NAME
    self.__ECHO_ALL_HOSTS         = ECHO_ALL_HOSTS
    self.__ECHO_INPUT             = ECHO_INPUT
    self.__ELPA_KERNEL            = ELPA_KERNEL
    self.__ELPA_QR                = ELPA_QR
    self.__ELPA_QR_UNSAFE         = ELPA_QR_UNSAFE
    self.__EXTENDED_FFT_LENGTHS   = EXTENDED_FFT_LENGTHS
    self.__FFTW_PLAN_TYPE         = FFTW_PLAN_TYPE
    self.__FFTW_WISDOM_FILE_NAME  = FFTW_WISDOM_FILE_NAME
    self.__FFT_POOL_SCRATCH_LIMIT = FFT_POOL_SCRATCH_LIMIT
    self.__FLUSH_SHOULD_FLUSH     = FLUSH_SHOULD_FLUSH
    self.__OUTPUT_FILE_NAME       = OUTPUT_FILE_NAME
    self.__PREFERRED_DIAG_LIBRARY = PREFERRED_DIAG_LIBRARY
    self.__PREFERRED_FFT_LIBRARY  = PREFERRED_FFT_LIBRARY
    self.__PRINT_LEVEL            = PRINT_LEVEL
    self.__PROGRAM_NAME           = PROGRAM_NAME
    self.__PROJECT_NAME           = PROJECT_NAME
    self.__RUN_TYPE               = RUN_TYPE
    self.__SAVE_MEM               = SAVE_MEM
    self.__SEED                   = SEED
    self.__TRACE                  = TRACE
    self.__TRACE_MASTER           = TRACE_MASTER
    self.__TRACE_MAX              = TRACE_MAX
    self.__TRACE_ROUTINES         = TRACE_ROUTINES
    self.__WALLTIME               = WALLTIME
    self.__errorLog               = errorLog
    self.__changeLog              = changeLog
    self.__location               = "{}/GLOBAL".format(location)
    # Consider adding subsec_args options to init
    self.__DBCSR                  = DBCSR.DBCSR(errorLog=self.__errorLog,changeLog=self.__changeLog,
                                      location=self.__location)
    self.__FM                     = FM.FM(errorLog=self.__errorLog,changeLog=self.__changeLog,
                                      location=self.__location)
    self.__FM_DIAG_SETTINGS       = FM_DIAG_SETTINGS.FM_DIAG_SETTINGS(errorLog=self.__errorLog,changeLog=self.__changeLog,
                                      location=self.__location)
    self.__PRINT                  = PRINT.PRINT(errorLog=self.__errorLog,changeLog=self.__changeLog,
                                      location=self.__location)
    self.__PRINT_ELPA             = PRINT_ELPA.PRINT_ELPA(errorLog=self.__errorLog,changeLog=self.__changeLog,
                                      location=self.__location)
    self.__PROGRAM_RUN_INFO       = PROGRAM_RUN_INFO.PROGRAM_RUN_INFO(errorLog=self.__errorLog,changeLog=self.__changeLog,
                                      location=self.__location)
    self.__REFERENCES             = REFERENCES.REFERENCES(errorLog=self.__errorLog,changeLog=self.__changeLog,
                                      location=self.__location)
    self.__TIMINGS                = TIMINGS.TIMINGS(errorLog=self.__errorLog,changeLog=self.__changeLog,
                                      location=self.__location)

  @property
  def ALLTOALL_SGL(self):
    return self.__ALLTOALL_SGL

  @property
  def BLACS_GRID(self):
    return self.__BLACS_GRID

  @property
  def BLACS_REPEATABLE(self):
    return self.__BLACS_REPEATABLE

  @property
  def CALLGRAPH(self):
    return self.__CALLGRAPH

  @property
  def CALLGRAPH_FILE_NAME(self):
    return self.__CALLGRAPH_FILE_NAME

  @property
  def ECHO_ALL_HOSTS(self):
    return self.__ECHO_ALL_HOSTS

  @property
  def ECHO_INPUT(self):
    return self.__ECHO_INPUT

  @property
  def ELPA_KERNEL(self):
    return self.__ELPA_KERNEL

  @property
  def ELPA_QR(self):
    return self.__ELPA_KERNEL

  @property
  def ELPA_QR_UNSAFE(self):
    return self.__ELPA_QR_UNSAFE

  @property
  def EXTENDED_FFT_LENGTHS(self):
    return self.__EXTENDED_FFT_LENGTHS

  @property
  def FFTW_PLAN_TYPE(self):
    return self.__FFTW_PLAN_TYPE

  @property
  def FFTW_WISDOM_FILE_NAME(self):
    return self.__FFTW_WISDOM_FILE_NAME

  @property
  def FFT_POOL_SCRATCH_LIMIT(self):
    return self.__FFT_POOL_SCRATCH_LIMIT

  @property
  def FLUSH_SHOULD_FLUSH(self):
    return self.__FLUSH_SHOULD_FLUSH

  @property
  def OUTPUT_FILE_NAME(self):
    return self.__OUTPUT_FILE_NAME

  @property
  def PREFERRED_DIAG_LIBRARY(self):
    return self.__PREFERRED_DIAG_LIBRARY

  @property
  def PREFERRED_FFT_LIBRARY(self):
    return self.__PREFERRED_FFT_LIBRARY

  @property
  def PRINT_LEVEL(self):
    return self.__PRINT_LEVEL

  @property
  def PROGRAM_NAME(self):
    return self.__PROGRAM_NAME

  @property
  def PROJECT_NAME(self):
    return self.__PROJECT_NAME

  @property
  def RUN_TYPE(self):
    return self.__RUN_TYPE

  @property
  def SAVE_MEM(self):
    return self.__SAVE_MEM

  @property
  def SEED(self):
    return self.__SEED

  @property
  def TRACE(self):
    return self.__TRACE

  @property
  def TRACE_MASTER(self):
    return self.__TRACE_MASTER

  @property
  def TRACE_MAX(self):
    return self.__TRACE_MAX

  @property
  def TRACE_ROUTINES(self):
    return self.__TRACE_ROUTINES

  @property
  def WALLTIME(self):
    return self.__WALLTIME

  @property
  def DBCSR(self):
    return self.__DBCSR

  @property
  def FM(self):
    return self.__FM

  @property
  def FM_DIAG_SETTINGS(self):
    return self.__FM_DIAG_SETTINGS

  @property
  def PRINT(self):
    return self.__PRINT

  @property
  def PRINT_ELPA(self):
    return self.__PRINT_ELPA

  @property
  def PROGRAM_RUN_INFO(self):
    return self.__PROGRAM_RUN_INFO

  @property
  def REFERENCES(self):
    return self.__REFERENCES

  @property
  def TIMINGS(self):
    return self.__TIMINGS

  @property
  def errorLog(self):
    return self.__errorLog

  @property
  def changeLog(self):
    return self.__changeLog

  @property
  def location(self):
    return self.__location

  @ALLTOALL_SGL.setter
  def ALLTOALL_SGL(self,val):
    if isinstance(val,bool):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'GLOBAL',
                               'Variable':'ALLTOALL_SGL','Success':True,
                               'Previous':self.__ALLTOALL_SGL,'New':val,'ErrorMessage':None,
                               'Location':self.__location})
      self.__ALLTOALL_SGL = val
    else:
      errorMessage = "ALLTOALL_SGL must be a boolean. You passed {}.".format(val)
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'GLOBAL',
                               'Variable':'ALLTOALL_SGL','Success':False,
                               'Previous':self.__ALLTOALL_SGL,'New':val,'ErrorMessage':errorMessage,
                               'Location':self.__location})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Module':'GLOBAL',
                              'Variable':'ALLTOALL_SGL','ErrorMessage':errorMessage,
                              'Location':self.__location})

  @BLACS_GRID.setter
  def BLACS_GRID(self,val):
    val = str(val).upper()
    if val in BLACS_GRID_VALS:
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'GLOBAL',
                               'Variable':'BLACS_GRID','Success':True,
                               'Previous':self.__BLACS_GRID,'New':val,'ErrorMessage':None,
                               'Location':self.__location})
      self.__BLACS_GRID = val
    else:
      errorMessage = ("BLACS_GRID value not understood. You passed {}. Possible values are: "
                     "{}.".format(val,BLACS_GRID_VALS))
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'GLOBAL',
                               'Variable':'BLACS_GRID','Success':False,
                               'Previous':self.__BLACS_GRID,'New':val,'ErrorMessage':errorMessage,
                               'Location':self.__location})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Module':'GLOBAL',
                              'Variable':'BLACS_GRID','ErrorMessage':errorMessage,
                              'Location':self.__location})
  
  @BLACS_REPEATABLE.setter
  def BLACS_REPEATABLE(self,val):
    if isinstance(val,bool):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'GLOBAL',
                               'Variable':'BLACS_REPEATABLE','Success':True,
                               'Previous':self.__BLACS_REPEATABLE,'New':val,'ErrorMessage':None,
                               'Location':self.__location})
      self.__BLACS_REPEATABLE = val
    else:
      errorMessage = "BLACS_REPEATABLE must be a boolean. You passed {}".format(val)
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'GLOBAL',
                               'Variable':'BLACS_REPEATABLE','Success':False,
                               'Previous':self.__BLACS_REPEATABLE,'New':val,'ErrorMessage':errorMessage,
                               'Location':self.__location})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Module':'GLOBAL',
                              'Variable':'BLACS_REPEATABLE','ErrorMessage':errorMessage,
                              'Location':self.__location})

  @CALLGRAPH.setter
  def CALLGRAPH(self,val):
    val = str(val).upper()
    if val in CALLGRAPH_VALS:
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'GLOBAL',
                               'Variable':'CALLGRAPH','Success':True,
                               'Previous':self.__CALLGRAPH,'New':val,'ErrorMessage':None,
                               'Location':self.__location})
      self.__CALLGRAPH = val
    else:
      errorMessage = ("CALLGRAPH value not understood. You passed {}. Possible values are: "
                     "{}.".format(val,CALLGRAPH_VALS))
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'GLOBAL',
                               'Variable':'CALLGRAPH','Success':False,
                               'Previous':self.__CALLGRAPH,'New':val,'ErrorMessage':errorMessage,
                               'Location':self.__location})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Module':'GLOBAL',
                              'Variable':'CALLGRAPH','ErrorMessage':errorMessage,
                              'Location':self.__location})

  @CALLGRAPH_FILE_NAME.setter
  def CALLGRAPH_FILE_NAME(self,val):
    self.__CALLGRAPH_FILE_NAME = str(val)

  @ECHO_ALL_HOSTS.setter
  def ECHO_ALL_HOSTS(self,val):
    if isinstance(val,bool):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'GLOBAL',
                               'Variable':'ECHO_ALL_HOSTS','Success':True,
                               'Previous':self.__ECHO_ALL_HOSTS,'New':val,'ErrorMessage':None,
                               'Location':self.__location})
      self.__ECHO_ALL_HOSTS = val
    else:
      errorMessage = "ECHO_ALL_HOSTS must be a boolean. You passed {}.".format(val)
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'GLOBAL',
                               'Variable':'ECHO_ALL_HOSTS','Success':False,
                               'Previous':self.__ECHO_ALL_HOSTS,'New':val,'ErrorMessage':errorMessage,
                               'Location':self.__location})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Module':'GLOBAL',
                              'Variable':'ECHO_ALL_HOSTS','ErrorMessage':errorMessage,
                              'Location':self.__location})

  @ECHO_INPUT.setter
  def ECHO_INPUT(self,val):
    if isinstance(val,bool):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'GLOBAL',
                               'Variable':'ECHO_INPUT','Success':True,
                               'Previous':self.__ECHO_INPUT,'New':val,'ErrorMessage':None,
                               'Location':self.__location})
      self.__ECHO_INPUT = val
    else:
      errorMessage = "ECHO_INPUT must be a boolean. You passed {}.".format(val)
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'GLOBAL',
                               'Variable':'ECHO_INPUT','Success':False,
                               'Previous':self.__ECHO_INPUT,'New':val,'ErrorMessage':errorMessage,
                               'Location':self.__location})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Module':'GLOBAL',
                              'Variable':'ECHO_INPUT','ErrorMessage':errorMessage,
                              'Location':self.__location})

  @ELPA_KERNEL.setter
  def ELPA_KERNEL(self,val):
    val = str(val).upper()
    if val in ELPA_KERNEL_VALS:
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'GLOBAL',
                               'Variable':'ELPA_KERNEL','Success':True,
                               'Previous':self.__ELPA_KERNEL,'New':val,'ErrorMessage':None,
                               'Location':self.__location})
      self.__ELPA_KERNEL = val
    else:
      errorMessage = ("ELPA_KERNEL value not understood. You passed {}. Possible values are: "
                     "{}.".format(val,ELPA_KERNEL_VALS))
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'GLOBAL',
                               'Variable':'ELPA_KERNEL','Success':False,
                               'Previous':self.__ELPA_KERNEL,'New':val,'ErrorMessage':errorMessage,
                               'Location':self.__location})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Module':'GLOBAL',
                              'Variable':'ELPA_KERNEL','ErrorMessage':errorMessage,
                              'Location':self.__location})

  @ELPA_QR.setter
  def ELPA_QR(self,val):
    if isinstance(val,bool):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'GLOBAL',
                               'Variable':'ELPA_QR','Success':True,
                               'Previous':self.__ELPA_QR,'New':val,'ErrorMessage':None,
                               'Location':self.__location})
      self.__ELPA_QR = val
    else:
      errorMessage = "ELPA_QR must be a boolean. You passed {}.".format(val)
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'GLOBAL',
                               'Variable':'ELPA_QR','Success':False,
                               'Previous':self.__ELPA_QR,'New':val,'ErrorMessage':errorMessage,
                               'Location':self.__location})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Module':'GLOBAL',
                              'Variable':'ELPA_QR','ErrorMessage':errorMessage,
                              'Location':self.__location})

  @ELPA_QR_UNSAFE.setter
  def ELPA_QR_UNSAFE(self,val):
    if isinstance(val,bool):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'GLOBAL',
                               'Variable':'ELPA_QR_UNSAFE','Success':True,
                               'Previous':self.__ELPA_QR_UNSAFE,'New':val,'ErrorMessage':None,
                               'Location':self.__location})
      self.__ELPA_QR_UNSAFE = val
    else:
      errorMessage = "ELPA_QR_UNSAFE must be a boolean. You passed {}.".format(val)
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'GLOBAL',
                               'Variable':'ELPA_QR_UNSAFE','Success':False,
                               'Previous':self.__ELPA_QR_UNSAFE,'New':val,'ErrorMessage':errorMessage,
                               'Location':self.__location})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Module':'GLOBAL',
                              'Variable':'ELPA_QR_UNSAFE','ErrorMessage':errorMessage,
                              'Location':self.__location})

  @EXTENDED_FFT_LENGTHS.setter
  def EXTENDED_FFT_LENGTHS(self,val):
    if isinstance(val,bool):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'GLOBAL',
                               'Variable':'EXTENDED_FFT_LENGTHS','Success':True,
                               'Previous':self.__EXTENDED_FFT_LENGTHS,'New':val,'ErrorMessage':None,
                               'Location':self.__location})
      self.__EXTENDED_FFT_LENGTHS = val
    else:
      errorMessage = "EXTENDED_FFT_LENGTHS must be a boolean. You passed {}.".format(val)
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'GLOBAL',
                               'Variable':'EXTENDED_FFT_LENGTHS','Success':False,
                               'Previous':self.__EXTENDED_FFT_LENGTHS,'New':val,'ErrorMessage':errorMessage,
                               'Location':self.__location})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Module':'GLOBAL',
                              'Variable':'EXTENDED_FFT_LENGTHS','ErrorMessage':errorMessage,
                              'Location':self.__location})

  @FFTW_PLAN_TYPE.setter
  def FFTW_PLAN_TYPE(self,val):
    val = str(val).upper()
    if val in FFTW_PLAN_TYPE_VALS:
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'GLOBAL',
                               'Variable':'FFTW_PLAN_TYPE','Success':True,
                               'Previous':self.__FFTW_PLAN_TYPE,'New':val,'ErrorMessage':None,
                               'Location':self.__location})
      self.__FFTW_PLAN_TYPE = val
    else:
      errorMessage = ("FFTW_PLAN_TYPE value not understood. You passed {}. Possible values are: "
                     "{}.".format(val,FFTW_PLAN_TYPE_VALS))
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'GLOBAL',
                               'Variable':'FFTW_PLAN_TYPE','Success':False,
                               'Previous':self.__FFTW_PLAN_TYPE,'New':val,'ErrorMessage':errorMessage,
                               'Location':self.__location})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Module':'GLOBAL',
                              'Variable':'FFTW_PLAN_TYPE','ErrorMessage':errorMessage,
                              'Location':self.__location})

  @FFTW_WISDOM_FILE_NAME.setter
  def FFTW_WISDOM_FILE_NAME(self,val):
    if os.path.isfile(val):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'GLOBAL',
                               'Variable':'FFT_WISDOM_FILE_NAME','Success':True,
                               'Previous':self.__FFT_WISDOM_FILE_NAME,'New':val,'ErrorMessage':None,
                               'Location':self.__location})
      self.__FFT_WISDOM_FILE_NAME = val
    else:
      errorMessage = "FFT_WISDOM_FILE_NAME can't be set: file {} doesn't exist.".format(val)
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'GLOBAL',
                               'Variable':'FFTW_WISDOM_FILE_NAME','Success':False,
                               'Previous':self.__FFTW_WISDOM_FILE_NAME,'New':val,'ErrorMessage':errorMessage,
                               'Location':self.__location})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Module':'GLOBAL',
                              'Variable':'EXTENDED_FFT_LENGTHS','ErrorMessage':errorMessage,
                              'Location':self.__location})

  @FFT_POOL_SCRATCH_LIMIT.setter
  def FFT_POOL_SCRATCH_LIMIT(self,val):
    if utilities.is_number(val):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'GLOBAL',
                               'Variable':'FFT_POOL_SCRATCH_LIMIT','Success':True,
                               'Previous':self.__FFT_POOL_SCRATCH_LIMIT,'New':val,'ErrorMessage':None,
                               'Location':self.__location})
      self.__FFT_POOL_SCRATCH_LIMIT = val
    else:
      errorMessage = "FFT_POOL_SCRATCH_LIMIT must be a number. You passed {}".format(val)
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'GLOBAL',
                               'Variable':'FFTW_POOL_SCRATCH_LIMIT','Success':False,
                               'Previous':self.__FFTW_POOL_SCRATCH_LIMIT,'New':val,'ErrorMessage':errorMessage,
                               'Location':self.__location})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Module':'GLOBAL',
                              'Variable':'EXTENDED_FFTW_POOL_SCRATCH_LIMIT','ErrorMessage':errorMessage,
                              'Location':self.__location})

  @FLUSH_SHOULD_FLUSH.setter
  def FLUSH_SHOULD_FLUSH(self,val):
    if isinstance(val,bool):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'GLOBAL',
                               'Variable':'FLUSH_SHOULD_FLUSH','Success':True,
                               'Previous':self.__FLUSH_SHOULD_FLUSH,'New':val,'ErrorMessage':None,
                               'Location':self.__location})
      self.__FLUSH_SHOULD_FLUSH = val
    else:
      errorMessage = "FLUSH_SHOULD_FLUSH must be a boolean. You passed {}".format(val)
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'GLOBAL',
                               'Variable':'FLUSH_SHOULD_FLUSH','Success':False,
                               'Previous':self.__FLUSH_SHOULD_FLUSH,'New':val,'ErrorMessage':errorMessage,
                               'Location':self.__location})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Module':'GLOBAL',
                              'Variable':'FLUSH_SHOULD_FLUSH','ErrorMessage':errorMessage,
                              'Location':self.__location})

  @OUTPUT_FILE_NAME.setter
  def OUTPUT_FILE_NAME(self,val):
    self.__OUTPUT_FILE_NAME = val

  @PREFERRED_DIAG_LIBRARY.setter
  def PREFERRED_DIAG_LIBRARY(self,val):
    val = str(val).upper()
    if val in PREFERRED_DIAG_LIBRARY_VALS:
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'GLOBAL',
                               'Variable':'PREFERRED_DIAG_LIBRARY','Success':True,
                               'Previous':self.__PREFERRED_DIAG_LIBRARY,'New':val,'ErrorMessage':None,
                               'Location':self.__location})
      self.__PREFERRED_DIAG_LIBRARY = val
    else:
      errorMessage = ("PREFERRED_DIAG_LIBRARY value not understood. You passed {}. Possible values are: "
                     "{}.".format(val,PREFERRED_DIAG_LIBRARY_VALS))
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'GLOBAL',
                               'Variable':'PREFERRED_DIAG_LIBRARY','Success':False,
                               'Previous':self.__PREFERRED_DIAG_LIBRARY,'New':val,'ErrorMessage':errorMessage,
                               'Location':self.__location})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Module':'GLOBAL',
                              'Variable':'PREFERRED_DIAG_LIBRARY','ErrorMessage':errorMessage,
                              'Location':self.__location})

  @PREFERRED_FFT_LIBRARY.setter
  def PREFERRED_FFT_LIBRARY(self,val):
    val = str(val).upper()
    if val in PREFERRED_FFT_LIBRARY_VALS:
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'GLOBAL',
                               'Variable':'PREFERRED_FFT_LIBRARY','Success':True,
                               'Previous':self.__PREFERRED_FFT_LIBRARY,'New':val,'ErrorMessage':None,
                               'Location':self.__location})
      self.__PREFERRED_FFT_LIBRARY = val
    else:
      errorMessage = ("PREFERRED_FFT_LIBRARY value not understood. You passed {}. Possible values are: "
                     "{}.".format(val,PREFERRED_FFT_LIBRARY_VALS))
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'GLOBAL',
                               'Variable':'PREFERRED_FFT_LIBRARY','Success':False,
                               'Previous':self.__PREFERRED_FFT_LIBRARY,'New':val,'ErrorMessage':errorMessage,
                               'Location':self.__location})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Module':'GLOBAL',
                              'Variable':'PREFERRED_FFT_LIBRARY','ErrorMessage':errorMessage,
                              'Location':self.__location})
 
  @PRINT_LEVEL.setter
  def PRINT_LEVEL(self,val):
    val = str(val).upper()
    if val in PRINT_LEVEL_VALS:
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'GLOBAL',
                               'Variable':'PRINT_LEVEL','Success':True,
                               'Previous':self.__PRINT_LEVEL,'New':val,'ErrorMessage':None,
                               'Location':self.__location})
      self.__PRINT_LEVEL = val
    else:
      errorMessage = ("PRINT_LEVEL value not understood. You passed {}. Possible values are: "
                     "{}.".format(val,PRINT_LEVEL_VALS))
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'GLOBAL',
                               'Variable':'PRINT_LEVEL','Success':False,
                               'Previous':self.__PRINT_LEVEL,'New':val,'ErrorMessage':errorMessage,
                               'Location':self.__location})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Module':'GLOBAL',
                              'Variable':'PRINT_LEVEL','ErrorMessage':errorMessage,
                              'Location':self.__location})

  @PROGRAM_NAME.setter
  def PROGRAM_NAME(self,val):
    val = str(val).upper()
    if val in PROGRAM_NAME_VALS:
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'GLOBAL',
                               'Variable':'PROGRAM_NAME','Success':True,
                               'Previous':self.__PROGRAM_NAME,'New':val,'ErrorMessage':None,
                               'Location':self.__location})
      self.__PRINT_LEVEL = val
    else:
      errorMessage = ("PRINT_LEVEL value not understood. You passed {}. Possible values are: "
                     "{}.".format(val,PRINT_LEVEL_VALS))
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'GLOBAL',
                               'Variable':'PRINT_LEVEL','Success':False,
                               'Previous':self.__PRINT_LEVEL,'New':val,'ErrorMessage':errorMessage,
                               'Location':self.__location})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Module':'GLOBAL',
                              'Variable':'PRINT_LEVEL','ErrorMessage':errorMessage,
                              'Location':self.__location})

  @PROJECT_NAME.setter
  def PROJECT_NAME(self,val):
    self.__PROJECT_NAME = val

  @RUN_TYPE.setter
  def RUN_TYPE(self,val):
    val = str(val).upper()
    if val in RUN_TYPE_VALS:
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'GLOBAL',
                               'Variable':'RUN_TYPE','Success':True,
                               'Previous':self.__RUN_TYPE,'New':val,'ErrorMessage':None,
                               'Location':self.__location})
      self.__RUN_TYPE = val
    else:
      errorMessage = ("RUN_TYPE {} not allowed. Check for typo. Allowed values " 
        "are: {}".format(val,GLOBAL.RUN_TYPE_VALS))
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'GLOBAL',
                               'Variable':'RUN_TYPE','Success':False,
                               'Previous':self.__RUN_TYPE,'New':val,'ErrorMessage':errorMessage,
                               'Location':self.__location})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Module':'GLOBAL',
                              'Variable':'RUN_TYPE','ErrorMessage':errorMessage,
                              'Location':self.__location})

  @SAVE_MEM.setter
  def SAVE_MEM(self,val):
    if isinstance(val,bool):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'GLOBAL',
                               'Variable':'SAVE_MEM','Success':True,
                               'Previous':self.__SAVE_MEM,'New':val,'ErrorMessage':None,
                               'Location':self.__location})
      self.__SAVE_MEM = val
    else:
      errorMessage = "SAVE_MEM must be a boolean."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'GLOBAL',
                               'Variable':'SAVE_MEM','Success':False,
                               'Previous':self.__SAVE_MEM,'New':val,'ErrorMessage':errorMessage,
                               'Location':self.__location})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Module':'GLOBAL',
                              'Variable':'SAVE_MEM','ErrorMessage':errorMessage,
                              'Location':self.__location})

  @SEED.setter
  def SEED(self,val):
    if utilities.is_integer(val):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'GLOBAL',
                               'Variable':'SEED','Success':True,
                               'Previous':self.__SEED,'New':val,'ErrorMessage':None,
                               'Location':self.__location})
      self.__SEED = val
    else:
      errorMessage = "SEED must be an integer."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'GLOBAL',
                               'Variable':'SEED','Success':False,
                               'Previous':self.__SEED,'New':val,'ErrorMessage':errorMessage,
                               'Location':self.__location})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Module':'GLOBAL',
                              'Variable':'SEED','ErrorMessage':errorMessage,
                              'Location':self.__location})

  @TRACE.setter
  def TRACE(self,val):
    if isinstance(val,bool):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'GLOBAL',
                               'Variable':'TRACE','Success':True,
                               'Previous':self.__TRACE,'New':val,'ErrorMessage':None,
                               'Location':self.__location})
      self.__TRACE = val
    else:
      errorMessage = "TRACE must be a boolean."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'GLOBAL',
                               'Variable':'TRACE','Success':False,
                               'Previous':self.__TRACE,'New':val,'ErrorMessage':errorMessage,
                               'Location':self.__location})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Module':'GLOBAL',
                              'Variable':'TRACE','ErrorMessage':errorMessage,
                              'Location':self.__location})

  @TRACE_MASTER.setter
  def TRACE_MASTER(self,val):
    if isinstance(val,bool):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'GLOBAL',
                               'Variable':'TRACE_MASTER','Success':True,
                               'Previous':self.__TRACE_MASTER,'New':val,'ErrorMessage':None,
                               'Location':self.__location})
      self.__TRACE_MASTER = val
    else:
      errorMessage = "TRACE_MASTER must be a boolean."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'GLOBAL',
                               'Variable':'TRACE_MASTER','Success':False,
                               'Previous':self.__TRACE_MASTER,'New':val,'ErrorMessage':errorMessage,
                               'Location':self.__location})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Module':'GLOBAL',
                              'Variable':'TRACE_MASTER','ErrorMessage':errorMessage,
                              'Location':self.__location})

  @TRACE_MAX.setter
  def TRACE_MAX(self,val):
    if utilities.is_integer(val):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'GLOBAL',
                               'Variable':'TRACE_MAX','Success':True,
                               'Previous':self.__TRACE_MAX,'New':val,'ErrorMessage':None,
                               'Location':self.__location})
      self.__TRACE_MAX = val
    else:
      errorMessage = "TRACE_MAX must be an integer"
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'GLOBAL',
                               'Variable':'TRACE_MAX','Success':False,
                               'Previous':self.__TRACE_MAX,'New':val,'ErrorMessage':errorMessage,
                               'Location':self.__location})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Module':'GLOBAL',
                              'Variable':'TRACE_MAX','ErrorMessage':errorMessage,
                              'Location':self.__location})

  @TRACE_ROUTINES.setter
  def TRACE_ROUTINES(self,val):
    self.__TRACE_ROUTINES = val

  @WALLTIME.setter
  def WALLTIME(self,val):
    hhmmss = str(val).split(":")
    # If given in seconds, not HH:MM:SS
    if len(hhmmss) == 1 and utilities.is_number(val):
      self.__WALLTIME = int(float(val)//1)
    elif len(hhmmss) == 3:
      isn = True
      for v in hhmmss:
        if not(utilities.is_number(v)):
          isn = False
      if isn:
        self.__WALLTIME = val
      else:
        errorMessage = ("Wrong format for walltime: {}. Must be in seconds"
          "or HH:MM:SS.".format(val))
        self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Module':'GLOBAL',
                                'Variable':'WALLTIME','ErrorMessage':errorMessage,
                                'Location':self.__location})
    else:
      errorMessage = ("Wrong format for walltime: {}. Must be in seconds"
        "or HH:MM:SS.".format(val))
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Module':'GLOBAL',
                              'Variable':'WALLTIME','ErrorMessage':errorMessage,
                              'Location':self.__location})
