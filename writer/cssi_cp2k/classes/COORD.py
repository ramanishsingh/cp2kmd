import datetime
import cssi_cp2k.utilities as utilities





BOOL_VALS   = [".TRUE.",".FALSE."]



def _validate_DEFAULT_KEYWORD(val,errorLog=[]):

  return val

def _validate_SCALED(val,errorLog=[]):
  if val is not None:
    val = str(val).upper()
  
  if val in BOOL_VALS or (val is None):
        return val
  else:
    errorMessage = ("Invalid option for SCALED: {}. Valid options are: {}".format(
                     val,BOOL_VALS))
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'FORCE_EVAL.SUBSYS.COORD',
                            'Variable':'SCALED','ErrorMessage':errorMessage})
    raise TypeError   

def _validate_UNIT(val,errorLog=[]):

  return val   
    

    


class COORD:

  def __init__(self,DEFAULT_KEYWORD=None,SCALED=None,UNIT=None,errorLog=[],changeLog=[],location=""):
    self.__errorLog = errorLog
    self.__changeLog = changeLog
    self.__location  = "{}/DFT".format(location)
    self.__DEFAULT_KEYWORD=_validate_DEFAULT_KEYWORD(DEFAULT_KEYWORD, errorLog=self.__errorLog)
    self.__SCALED=_validate_SCALED(SCALED, errorLog=self.__errorLog)
    self.__UNIT=_validate_UNIT(UNIT, errorLog=self.__errorLog)
    
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
  def DEFAULT_KEYWORD(self):
    return self.__DEFAULT_KEYWORD

  @property
  def SCALED(self):
    return self.__SCALED

  @property
  def UNIT(self):
    return self.__UNIT

 

  @DEFAULT_KEYWORD.setter
  def DEFAULT_KEYWORD(self, val):
    
    
    self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'FORCE_EVAL.SUBSYS.COORD', 'Variable': 'DEFAULT_KEYWORD',
                               'Success': True, 'Previous': self.__DEFAULT_KEYWORD, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
    self.__DEFAULT_KEYWORD= val
    
  @SCALED.setter
  def SCALED(self, val):
    val = str(val).upper()
    if val in BOOL_VALS:
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'FORCE_EVAL.SUBSYS.COORD', 'Variable': 'SCALED',
                               'Success': True, 'Previous': self.__SCALED, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__SCALED = val
    else:
      errorMessage = ("Invalid option for SCALED: {}. Valid options are: {}".format(val, BOOL_VALS))
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'FORCE_EVAL.SUBSYS.COORD', 'Variable': 'SCALED',
                               'Success': False, 'Previous': self.__SCALED, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'DFT',
                              'Variable': ' SCALED', 'ErrorMessage': errorMessage,
                              'Location': self.__location})
    
    
    

  @UNIT.setter
  def UNIT(self, val):
    
    
    self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'FORCE_EVAL.SUBSYS.COORD', 'Variable': 'UNIT',
                               'Success': True, 'Previous': self.__UNIT, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
    self.__UNIT= val
    
    
  