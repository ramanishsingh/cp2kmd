import datetime
import cssi_cp2k.utilities as utilities
#from cssi_cp2k.classes import EACH
from cssi_cp2k.classes import XC_FUNCTIONAL

from cssi_cp2k.classes import VDW_POTENTIAL

BOOL_VALS   = [".TRUE.",".FALSE"]
FUNCTIONAL_ROUTINE_VALS=['DEBUG','NEW','OLD','TEST_LSD']



def _validate_DENSITY_CUTOFF(val,errorLog=[]):
    return val
def _validate_DENSITY_SMOOTH_CUTOFF_RANGE(val,errorLog=[]):
    return val

def _validate_FUNCTIONAL_ROUTINE(val,errorLog=[]):
  if val is not None:
    val = str(val).upper()

  if val in FUNCTIONAL_ROUTINE_VALS or (val is None):
    return val
  else:
    errorMessage = ("Invalid option for FUNCTIONAL_ROUTINE: {}. Valid options are: {}".format(
                     val,FUNCTIONAL_ROUTINE_VALS))
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'DFT.XC',
                            'Variable':'FUNCTIONAL_ROUTINE','ErrorMessage':errorMessage})
    raise TypeError

    

def _validate_GRADIENT_CUTOFF(val,errorLog=[]):
    return val
def _validate_TAU_CUTOFF(val,errorLog=[]):
    return val




    
    
    
class XC:

  def __init__(self,DENSITY_CUTOFF=None, DENSITY_SMOOTH_CUTOFF_RANGE=None,FUNCTIONAL_ROUTINE=None,GRADIENT_CUTOFF=None,TAU_CUTOFF=None, errorLog=[],changeLog=[],location=""):
    self.__errorLog = errorLog
    self.__changeLog = changeLog
    self.__DENSITY_CUTOFF=_validate_DENSITY_CUTOFF(DENSITY_CUTOFF, errorLog=self.__errorLog)
    self.__DENSITY_SMOOTH_CUTOFF_RANGE=_validate_DENSITY_SMOOTH_CUTOFF_RANGE(DENSITY_SMOOTH_CUTOFF_RANGE, errorLog=self.__errorLog)
    self.__FUNCTIONAL_ROUTINE=_validate_FUNCTIONAL_ROUTINE(FUNCTIONAL_ROUTINE, errorLog=self.__errorLog)
    self.__GRADIENT_CUTOFF=_validate_GRADIENT_CUTOFF(GRADIENT_CUTOFF,errorLog=self.__errorLog)
    self.__TAU_CUTOFF=_validate_TAU_CUTOFF(TAU_CUTOFF,errorLog=self.__errorLog)



    

    self.__location  = "{}/XC".format(location)
    self.__XC_FUNCTIONAL      = XC_FUNCTIONAL.XC_FUNCTIONAL(errorLog=self.__errorLog,changeLog=self.__changeLog,location=self.__location)
    self.__VDW_POTENTIAL      = VDW_POTENTIAL.VDW_POTENTIAL(errorLog=self.__errorLog,changeLog=self.__changeLog,location=self.__location)
    #ENERGY subsections
    #self.__EACH      = EACH.EACH(errorLog=self.__errorLog,changeLog=self.__changeLog,
                      #   location=self.__location)

  @property
  def errorLog(self):
    return self.__errorLog

  @property
  def changeLog(self):
    return self.__changeLog

  @property
  def location(self):
    return self.__location

  @property
  def DENSITY_CUTOFF(self):
    return self.__DENSITY_CUTOFF

  @property
  def DENSITY_SMOOTH_CUTOFF_RANGE(self):
    return self.__DENSITY_SMOOTH_CUTOFF_RANGE

  @property
  def FUNCTIONAL_ROUTINE(self):
    return self.__FUNCTIONAL_ROUTINE


  @property
  def GRADIENT_CUTOFF(self):
    return self.__GRADIENT_CUTOFF

  @property
  def TAU_CUTOFF(self):
    return self.__TAU_CUTOFF

  @property
  def EPS_SCF(self):
    return self.__EPS_SCF

  @property
  def EPS_SCF_HISTORY(self):
    return self.__EPS_SCF_HISTORY

  @property
  def LEVEL_SHIFT(self):
    return self.__LEVEL_SHIFT


  @property
  def MAX_DIIS(self):
    return self.__MAX_DIIS
  @property
  def MAX_ITER_LUMO(self):
    return self.__MAX_ITER_LUMO

  @property
  def MAX_SCF(self):
    return self.__MAX_SCF

  @property
  def XC_FUNCTIONAL(self):
    return self.__XC_FUNCTIONAL
  @property
  def VDW_POTENTIAL(self):
    return self.__VDW_POTENTIAL
#  @property
#  def PRINT(self):
 #   return self.__PRINT
#





  @DENSITY_CUTOFF.setter
  def DENSITY_CUTOFF(self, val):
 
    self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT.XC', 'Variable': 'DENSITY_CUTOFF',
                               'Success': True, 'Previous': self.__DENSITY_CUTOFF, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
    self.__DENSITY_CUTOFF = val


    
  @DENSITY_SMOOTH_CUTOFF_RANGE.setter
  def DENSITY_SMOOTH_CUTOFF_RANGE(self, val):
 
    self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT.XC', 'Variable': 'DENSITY_SMOOTH_CUTOFF_RANGE',
                               'Success': True, 'Previous': self.__DENSITY_SMOOTH_CUTOFF_RANGE, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
    self.__DENSITY_SMOOTH_CUTOFF_RANGE = val 
    
    

  @FUNCTIONAL_ROUTINE.setter
  def FUNCTIONAL_ROUTINE(self, val):
    val = str(val).upper()
    if val in FUNCTIONAL_ROUTINE_VALS:
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT.XC', 'Variable': 'FUNCTIONAL_ROUTINE',
                               'Success': True, 'Previous': self.__FUNCTIONAL_ROUTINE, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__FUNCTIONAL_ROUTINE= val
    else:
      errorMessage = ("Invalid option for FUNCTIONAL_ROUTINE: {}. Valid options are: {}".format(val,CHOLESKY_VALS))
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT.XC', 'Variable': 'FUNCTIONAL_ROUTINE',
                               'Success': False, 'Previous': self.__FUNCTIONAL_ROUTINE, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'DFT.XC',
                              'Variable': 'FUNCTIONAL_ROUTINE', 'ErrorMessage': errorMessage, 'Location': self.__location})
    
    
    

 
  @GRADIENT_CUTOFF.setter
  def GRADIENT_CUTOFF(self, val):
 
    self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT.XC', 'Variable': 'GRADIENT_CUTOFF',
                               'Success': True, 'Previous': self.__GRADIENT_CUTOFF, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
    self.__GRADIENT_CUTOFF = val


    
  @TAU_CUTOFF.setter
  def TAU_CUTOFF(self, val):
 
    self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT.XC', 'Variable': 'TAU_CUTOFF',
                               'Success': True, 'Previous': self.__TAU_CUTOFF, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
    self.__TAU_CUTOFF = val 




