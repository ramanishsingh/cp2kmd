import datetime
import cssi_cp2k.utilities as utilities
SECTION_PARAMETERS_VALS  = [".TRUE.",".FALSE."]
OPTIMIZER_VALS=['BISECT','BROYDEN','DIIS','NEWTON','NEWTON_LS','NONE','SD','SECANT']
TYPE_VALS=['BASIS_CENTER_OPT','CDFT_CONSTRAINT','DDAPC_CONSTRAINT','NONE','S2_CONSTRAINT']





def _validate_SECTION_PARAMETERS(val,errorLog=[]):
  if val is not None:
    val = str(val).upper()

  if val in SECTION_PARAMETERS_VALS or (val is None):
    return val
  else:
    errorMessage = ("Invalid option for SECTION_PARAMETERS: {}. Valid options are: {}".format(
                     val,SECTION_PARAMETERS_VALS))
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'SCF.OUTER_SCF',
                            'Variable':'SECTION_PARAMETERS','ErrorMessage':errorMessage})
    raise TypeError

    
def _validate_BISECT_TRUST_COUNT(val,errorLog=[]):
  if utilities.is_integer(val) or (val is None):
    return val
  else:
    errorMessage = "BISECT_TRUST_COUNT  must be AN integer."
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'SCF OUTER_SCF',
                            'Variable':'BISECT_TRUST_COUNT','ErrorMessage':errorMessage})
    raise TypeError
        
        
def _validate_DIIS_BUFFER_LENGTH(val,errorLog=[]):
  if utilities.is_integer(val) or (val is None):
    return val
  else:
    errorMessage = "DIIS_BUFFER_LENGTH  must be AN integer."
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'SCF OUTER_SCF',
                            'Variable':'DIIS_BUFFER_LENGTH','ErrorMessage':errorMessage})
    raise TypeError
    
def _validate_EPS_SCF(val,errorLog=[]):
    return val    


def _validate_EXTRAPOLATION_ORDER(val,errorLog=[]):
  if utilities.is_integer(val) or (val is None):
    return val
  else:
    errorMessage = "EXTRAPOLATION_ORDER  must be AN integer."
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'SCF OUTER_SCF',
                            'Variable':'EXTRAPOLATION_ORDER','ErrorMessage':errorMessage})
    raise TypeError    
    
def _validate_MAX_SCF(val,errorLog=[]):
  if utilities.is_integer(val) or (val is None):
    return val
  else:
    errorMessage = "MAX_SCF  must be AN integer."
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'SCF OUTER_SCF',
                            'Variable':'MAX_SCF','ErrorMessage':errorMessage})
    raise TypeError 
    
def _validate_OPTIMIZER(val,errorLog=[]):
  if val is not None:
    val = str(val).upper()

  if val in OPTIMIZER_VALS or (val is None):
    return val
  else:
    errorMessage = ("Invalid option for OPTIMIZER: {}. Valid options are: {}".format(
                     val,OPTIMIZER_VALS))
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'SCF.OUTER_SCF',
                            'Variable':'OPTIMIZER','ErrorMessage':errorMessage})
    raise TypeError
    
def _validate_STEP_SIZE(val,errorLog=[]):
    return val

def _validate_TYPE(val,errorLog=[]):
  if val is not None:
    val = str(val).upper()

  if val in TYPE_VALS or (val is None):
    return val
  else:
    errorMessage = ("Invalid option for TYPE: {}. Valid options are: {}".format(
                     val,TYPE_VALS))
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'SCF.OUTER_SCF',
                            'Variable':'TYPE','ErrorMessage':errorMessage})
    raise TypeError
    
    
    
class OUTER_SCF:

  def __init__(self,SECTION_PARAMETERS=None, BISECT_TRUST_COUNT=None,DIIS_BUFFER_LENGTH=None,EPS_SCF=None,EXTRAPOLATION_ORDER=None,MAX_SCF=None,OPTIMIZER=None,STEP_SIZE=None,TYPE=None,errorLog=[],changeLog=[],location=""):
    self.__errorLog = errorLog
    self.__changeLog = changeLog
    self.__SECTION_PARAMETERS=_validate_SECTION_PARAMETERS(SECTION_PARAMETERS, errorLog=self.__errorLog)
    self.__BISECT_TRUST_COUNT=_validate_BISECT_TRUST_COUNT(BISECT_TRUST_COUNT, errorLog=self.__errorLog)
    self.__DIIS_BUFFER_LENGTH=_validate_DIIS_BUFFER_LENGTH(DIIS_BUFFER_LENGTH, errorLog=self.__errorLog)
    self.__EPS_SCF=_validate_EPS_SCF(EPS_SCF,errorLog=self.__errorLog)
    self.__EXTRAPOLATION_ORDER=_validate_EXTRAPOLATION_ORDER(EXTRAPOLATION_ORDER,errorLog=self.__errorLog)
    self.__MAX_SCF=_validate_MAX_SCF(MAX_SCF,errorLog=self.__errorLog)
    self.__OPTIMIZER=_validate_OPTIMIZER(OPTIMIZER,errorLog=self.__errorLog)
    self.__STEP_SIZE=_validate_STEP_SIZE(STEP_SIZE,errorLog=self.__errorLog)
    self.__TYPE=_validate_TYPE(TYPE,errorLog=self.__errorLog)
    
    

    

    

    self.__location  = "{}/OUTER_SCF".format(location)
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

  @property
  def BISECT_TRUST_COUNT(self):
    return self.__BISECT_TRUST_COUNT

  @property
  def DIIS_BUFFER_LENGTH(self):
    return self.__DIIS_BUFFER_LENGTH


  @property
  def EPS_SCF(self):
    return self.__EPS_SCF

  @property
  def EXTRAPOLATION_ORDER(self):
    return self.__EXTRAPOLATION_ORDER

  @property
  def MAX_SCF(self):
    return self.__MAX_SCF

  @property
  def OPTIMIZER(self):
    return self.__OPTIMIZER

  @property
  def STEP_SIZE(self):
    return self.__STEP_SIZE


  @property
  def TYPE(self):
    return self.__TYPE
 


  @SECTION_PARAMETERS.setter
  def SECTION_PARAMETERS(self, val):
    val = str(val).upper()
    if val in SECTION_PARAMETERS_VALS:
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SCF.OUTER_SCF', 'Variable': 'SECTION_PARAMETERS',
                               'Success': True, 'Previous': self.__SECTION_PARAMETERS, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__SECTION_PARAMETERS= val
    else:
      errorMessage = ("Invalid option for Section parameter OUTER_SCF: {}. Valid options are: {}".format(val,SECTION_PARAMETERS_VALS))
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SCF.OUTER_SCF', 'Variable': 'SECTION_PARAMETERS',
                               'Success': False, 'Previous': self.__SECTION_PARAMETERS, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'SCF.OUTER_SCF',
                              'Variable': 'SECTION_PARAMETERS', 'ErrorMessage': errorMessage, 'Location': self.__location})
    
      
  @BISECT_TRUST_COUNT.setter
  def BISECT_TRUST_COUNT(self, val):
    if utilities.is_integer(val):
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SCF.OUTER_SCF', 'Variable': 'BISECT_TRUST_COUNT',
                               'Success': True, 'Previous': self.__BISECT_TRUST_COUNT, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__BISECT_TRUST_COUNT = val
    else:
      errorMessage = "BISECT_TRUST_COUNT must be a positive integer."
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SCF.OUTER_SCF', 'Variable': 'BISECT_TRUST_COUNT',
                               'Success': False, 'Previous': self.__BISECT_TRUST_COUNT, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'SCF.OUTER_SCF',
                              'Variable': 'BISECT_TRUST_COUNT', 'ErrorMessage': errorMessage,
                              'Location': self.__location}) 
  @DIIS_BUFFER_LENGTH.setter
  def DIIS_BUFFER_LENGTH(self, val):
    if utilities.is_integer(val):
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SCF.OUTER_SCF', 'Variable': 'DIIS_BUFFER_LENGTH',
                               'Success': True, 'Previous': self.__DIIS_BUFFER_LENGTH, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__DIIS_BUFFER_LENGTH = val
    else:
      errorMessage = "DIIS_BUFFER_LENGTH must be a positive integer."
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SCF.OUTER_SCF', 'Variable': 'DIIS_BUFFER_LENGTH',
                               'Success': False, 'Previous': self.__DIIS_BUFFER_LENGTH, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'SCF.OUTER_SCF',
                              'Variable': 'DIIS_BUFFER_LENGTH', 'ErrorMessage': errorMessage,
                              'Location': self.__location}) 
      
  @EPS_SCF.setter
  def EPS_SCF(self,val):
    self.__EPS_SCF=val
    self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SCF.OUTER_SCF', 'Variable': 'EPS_SCF',
                               'Success': True, 'Previous': self.__EPS_SCF, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})  
   

  @EXTRAPOLATION_ORDER.setter
  def EXTRAPOLATION_ORDER(self, val):
    if utilities.is_integer(val):
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SCF.OUTER_SCF', 'Variable': 'EXTRAPOLATION_ORDER',
                               'Success': True, 'Previous': self.__EXTRAPOLATION_ORDER, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__EXTRAPOLATION_ORDER = val
    else:
      errorMessage = "EXTRAPOLATION_ORDER must be a positive integer."
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SCF.OUTER_SCF', 'Variable': 'EXTRAPOLATION_ORDER',
                               'Success': False, 'Previous': self.__EXTRAPOLATION_ORDER, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'SCF.OUTER_SCF',
                              'Variable': 'EXTRAPOLATION_ORDER', 'ErrorMessage': errorMessage,
                              'Location': self.__location}) 
    
  @MAX_SCF.setter
  def MAX_SCF(self, val):
    if utilities.is_integer(val):
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SCF.OUTER_SCF', 'Variable': 'MAX_SCF',
                               'Success': True, 'Previous': self.__MAX_SCF, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__MAX_SCF = val
    else:
      errorMessage = "MAX_SCF must be a positive integer."
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SCF.OUTER_SCF', 'Variable': 'MAX_SCF',
                               'Success': False, 'Previous': self.__MAX_SCF, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'SCF.OUTER_SCF',
                              'Variable': 'MAX_SCF', 'ErrorMessage': errorMessage,
                              'Location': self.__location}) 
  @OPTIMIZER.setter
  def OPTIMIZER(self, val):
    val = str(val).upper()
    if val in OPTIMIZER_VALS:
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SCF.OUTER_SCF', 'Variable': 'OPTIMIZER',
                               'Success': True, 'Previous': self.__OPTIMIZER, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__OPTIMIZER= val
    else:
      errorMessage = ("Invalid option for OPTIMIZER OUTER_SCF: {}. Valid options are: {}".format(val,OPTIMIZER_VALS))
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SCF.OUTER_SCF', 'Variable': 'OPTIMIZER',
                               'Success': False, 'Previous': self.__OPTIMIZER, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'SCF.OUTER_SCF',
                              'Variable': 'OPTIMIZER', 'ErrorMessage': errorMessage, 'Location': self.__location})

  @STEP_SIZE.setter
  def STEP_SIZE(self,val):
    self.__STEP_SIZE=val
    self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SCF.OUTER_SCF', 'Variable': 'STEP_SIZE',
                               'Success': True, 'Previous': self.__STEP_SIZE, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location}) 
    
    
  @TYPE.setter
  def TYPE(self, val):
    val = str(val).upper()
    if val in TYPE_VALS:
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SCF.OUTER_SCF', 'Variable': 'TYPE',
                               'Success': True, 'Previous': self.__TYPE, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__TYPE= val
    else:
      errorMessage = ("Invalid option for TYPE: {}. Valid options are: {}".format(val,TYPE_VALS))
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SCF.OUTER_SCF', 'Variable': 'TYPE',
                               'Success': False, 'Previous': self.__TYPE, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'SCF.OUTER_SCF',
                              'Variable': 'TYPE', 'ErrorMessage': errorMessage, 'Location': self.__location})  
  