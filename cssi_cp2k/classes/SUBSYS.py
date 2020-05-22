import datetime
import cssi_cp2k.utilities as utilities
from cssi_cp2k.classes import CELL
from cssi_cp2k.classes import KINDs
from cssi_cp2k.classes import COORD
from cssi_cp2k.utilities1 import oneDimArray as oda
from cssi_cp2k.utilities1 import objectArray as oba






BOOL_VALS   = [".TRUE.",".FALSE"]

def _validate_SEED(val,errorLog=[]):
  if utilities.is_integer(val) or (val is None):
    return val
  else:
    errorMessage = "SEED must be an integer."
    errorLog.append({'Date': datetime.datetime.now(), 'Type': 'init', 'Module': 'FORCE_EVAL.SUBSYS',
                     'Variable': 'SEED', 'ErrorMessage': errorMessage})
    raise TypeError

    


class SUBSYS:

  def __init__(self,SEED=None, errorLog=[],changeLog=[],location=""):
    self.__errorLog = errorLog
    self.__changeLog = changeLog
    self.__location  = "{}/SUBSYS".format(location)
    self.__KIND=None
    self.__SEED=_validate_SEED(SEED, errorLog=self.__errorLog)

    self.__CELL = CELL.CELL(errorLog=self.__errorLog, changeLog=self.__changeLog,
                         location=self.__location)
    self.__COORD = COORD.COORD(errorLog=self.__errorLog, changeLog=self.__changeLog,
                         location=self.__location)
    #self.__KIND       = KIND.KIND(errorLog=self.__errorLog,changeLog=self.__changeLog,
                           #location=self.__location)

    
    #ENERGY subsections
    #self.__EACH      = EACH.EACH(errorLog=self.__errorLog,changeLog=self.__changeLog,
                 #        location=self.__location)

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
  def SEED(self):
    return self.__SEED

  @property
  def CELL(self):
      return self.__CELL
    
  @property
  def COORD(self):
      return self.__COORD


  @property
  def KIND(self):
    return self.__KIND
    
  def init_atoms(self,natomty):
    KIND = []
    for i in range(natomty):
      KIND.append(KINDs.KINDs(number=i+1,errorLog=self.__errorLog,changeLog=self.__changeLog,
                                location=self.__location))
    self.__KIND = oba.objectArray.listToOBA(KIND,errorLog=self.__errorLog,changeLog=self.__changeLog,
                                                location=self.__location)
    
    
  @SEED.setter
  def SEED(self, val):
    if utilities.is_integer(val):
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'FORCE_EVAL.SUBSYS', 'Variable': 'SEED',
                               'Success': True, 'Previous': self.__SEED, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__SEED = val
    else:
      errorMessage = "SEED must be an  integer."
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'FORCE_EVAL.SUBSYS', 'Variable': 'SEED',
                               'Success': False, 'Previous': self.__SEED, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'DFT',
                              'Variable': 'SEED', 'ErrorMessage': errorMessage,
                              'Location': self.__location})    
    
 