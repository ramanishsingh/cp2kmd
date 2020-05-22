import datetime
import cssi_cp2k.utilities as utilities
#from cssi_cp2k.classes import EACH
from cssi_cp2k.classes import PAIR_POTENTIAL


BOOL_VALS   = [".TRUE.",".FALSE"]
POTENTIAL_TYPE_VALS=['NONE','NON_LOCAL','PAIR_POTENTIAL']




def _validate_POTENTIAL_TYPE(val,errorLog=[]):
  if val is not None:
    val = str(val).upper()

  if val in  POTENTIAL_TYPE_VALS or (val is None):
    return val
  else:
    errorMessage = ("Invalid option for  POTENTIAL_TYPE: {}. Valid options are: {}".format(
                     val, POTENTIAL_TYPE_VALS))
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'DFT.XC.vdw_potential',
                            'Variable':' POTENTIAL_TYPE','ErrorMessage':errorMessage})
    raise TypeError

    





    
    
    
class VDW_POTENTIAL:

  def __init__(self,POTENTIAL_TYPE=None, errorLog=[],changeLog=[],location=""):
    self.__errorLog = errorLog
    self.__changeLog = changeLog
    self.__location  = "{}/VDW_POTENTIAL".format(location)
    self.__POTENTIAL_TYPE=_validate_POTENTIAL_TYPE(POTENTIAL_TYPE, errorLog=self.__errorLog)
    self.__PAIR_POTENTIAL      = PAIR_POTENTIAL.PAIR_POTENTIAL(errorLog=self.__errorLog,changeLog=self.__changeLog,location=self.__location)



    

    

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
  def POTENTIAL_TYPE(self):
    return self.__POTENTIAL_TYPE

  @property
  def PAIR_POTENTIAL(self):
    return self.__PAIR_POTENTIAL

 
  #@property
#  def OT(self):
#    return self.__OT
#  @property
#  def PRINT(self):
 #   return self.__PRINT
#



  @POTENTIAL_TYPE.setter
  def POTENTIAL_TYPE(self, val):
    val = str(val).upper()
    if val in POTENTIAL_TYPE_VALS:
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT.XC.POTENTIAL_TYPE', 'Variable': 'POTENTIAL_TYPE',
                               'Success': True, 'Previous': self.__POTENTIAL_TYPE, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__POTENTIAL_TYPE= val
    else:
      errorMessage = ("Invalid option for POTENTIAL_TYPE: {}. Valid options are: {}".format(val,POTENTIAL_TYPE_VALS))
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT.XC.POTENTIAL_TYPE', 'Variable': 'POTENTIAL_TYPE',
                               'Success': False, 'Previous': self.__POTENTIAL_TYPE, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'DFT.XC.POTENTIAL_TYPEL',
                              'Variable': 'POTENTIAL_TYPE', 'ErrorMessage': errorMessage, 'Location': self.__location})
    
    
    

 
  