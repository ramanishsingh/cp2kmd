import datetime
import cssi_cp2k.utilities as utilities
#from cssi_cp2k.classes import EACH


BOOL_VALS   = [".TRUE.",".FALSE"]
SECTION_PARAMETERS_VALS=['B3LYP','BEEFVDW','BLYP','BP','HCTH120','LDA','NONE','NO_SHORTCUT','OLYP','PADE','PBE','PBE0','TPSS']




def _validate_SECTION_PARAMETERS(val,errorLog=[]):
  if val is not None:
    val = str(val).upper()

  if val in SECTION_PARAMETERS_VALS or (val is None):
    return val
  else:
    errorMessage = ("Invalid option for SECTION_PARAMETERS: {}. Valid options are: {}".format(
                     val,SECTION_PARAMETERS_VALS))
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'DFT.XC',
                            'Variable':'SECTION_PARAMETERS','ErrorMessage':errorMessage})
    raise TypeError

    





    
    
    
class XC_FUNCTIONAL:

  def __init__(self,SECTION_PARAMETERS=None, errorLog=[],changeLog=[],location=""):
    self.__errorLog = errorLog
    self.__changeLog = changeLog
    self.__SECTION_PARAMETERS=_validate_SECTION_PARAMETERS(SECTION_PARAMETERS, errorLog=self.__errorLog)




    

    self.__location  = "{}/XC_FUNCTIONAL".format(location)

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
  def SECTION_PARAMETERS(self):
    return self.__SECTION_PARAMETERS

 
  #@property
#  def OT(self):
#    return self.__OT
#  @property
#  def PRINT(self):
 #   return self.__PRINT
#



  @SECTION_PARAMETERS.setter
  def SECTION_PARAMETERS(self, val):
    val = str(val).upper()
    if val in SECTION_PARAMETERS_VALS:
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT.XC.XC_FUNCTIONAL', 'Variable': 'SECTION_PARAMETERS',
                               'Success': True, 'Previous': self.__SECTION_PARAMETERS, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__SECTION_PARAMETERS= val
    else:
      errorMessage = ("Invalid option for SECTION_PARAMETERS: {}. Valid options are: {}".format(val,SECTION_PARAMETERS_VALS))
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT.XC.XC_FUNCTIONAL', 'Variable': 'SECTION_PARAMETERS',
                               'Success': False, 'Previous': self.__SECTION_PARAMETERS, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'DFT.XC.XC_FUNCTIONAL',
                              'Variable': 'SECTION_PARAMETERS', 'ErrorMessage': errorMessage, 'Location': self.__location})
    
    
    

 
  