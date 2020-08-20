import datetime
import cssi_cp2k.utilities as utilities
from cssi_cp2k.classes import EACH
BOOL_VALS   = [".TRUE.",".FALSE"]
SECTION_PARAMETERS_VALS=["DEBUG","HIGH","LOW","MEDIUM","OFF","ON","SILENT"]
FORMAT_VALS=["ATOMIC","DCD","XMOL","XYZ"]

def _validate_SECTION_PARAMETERS(val,errorLog=[]):
  if val is not None:
    val = str(val).upper()

  if val in SECTION_PARAMETERS_VALS or (val is None):
    return val
  else:
    errorMessage = ("Invalid option for SECTION_PARAMETERS: {}. Valid options are: {}".format(
                     val,SECTION_PARAMETERS_VALS))
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'PRINT/TRAJECTORY',
                            'Variable':'SECTION_PARAMETERS','ErrorMessage':errorMessage})
    raise TypeError


def _validate_ADD_LAST(val,errorLog=[]):
    return val


def _validate_CHARGE_BETA(val,errorLog=[]):
  if val is not None:
    val = str(val).upper()

  if val in BOOL_VALS or (val is None):
    return val
  else:
    errorMessage = ("Invalid option for CHARGE_BETA: {}. Valid options are: {}".format(
                     val,BOOL_VALS))
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'PRINT/TRAJECTORY',
                            'Variable':'CHARGE_BETA','ErrorMessage':errorMessage})
    raise TypeError
    
    
    
def _validate_CHARGE_EXTENDED(val,errorLog=[]):
  if val is not None:
    val = str(val).upper()

  if val in BOOL_VALS or (val is None):
    return val
  else:
    errorMessage = ("Invalid option for CHARGE_EXTENDED: {}. Valid options are: {}".format(
                     val,BOOL_VALS))
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'PRINT/TRAJECTORY',
                            'Variable':'CHARGE_EXTENDED','ErrorMessage':errorMessage})
    raise TypeError

    
def _validate_CHARGE_OCCUP(val,errorLog=[]):
  if val is not None:
    val = str(val).upper()

  if val in BOOL_VALS or (val is None):
    return val
  else:
    errorMessage = ("Invalid option for CHARGE_OCCUP: {}. Valid options are: {}".format(
                     val,BOOL_VALS))
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'PRINT/TRAJECTORY',
                            'Variable':'CHARGE_OCCUP','ErrorMessage':errorMessage})
    raise TypeError
    


def _validate_COMMON_ITERATION_LEVELS(val,errorLog=[]):
  if utilities.is_positive_integer(val) or (val is None):
    return val
  else:
    errorMessage = "COMMON_ITERATION_LEVELS level must be a positive integer."
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'PRINT/TRAJECTORY',
                            'Variable':'COMMON_ITERATION_LEVELS','ErrorMessage':errorMessage})
    raise TypeError

def _validate_FORMAT(val,errorLog=[]):
  if val is not None:
    val = str(val).upper()

  if val in FORMAT_VALS or (val is None):
    return val
  else:
    errorMessage = ("Invalid option for FORMAT: {}. Valid options are: {}".format(
                     val,SECTION_PARAMETERS_VALS))
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'PRINT/TRAJECTORY',
                            'Variable':'FORMAT','ErrorMessage':errorMessage})
    raise TypeError



def _validate_FILENAME(val,errorLog=[]):
    return val



def _validate_LOG_PRINT_KEY(val,errorLog=[]):
  if val is not None:
    val = str(val).upper()

  if val in BOOL_VALS or (val is None):
    return val
  else:
    errorMessage = ("Invalid option for LOG_PRINT_KEY: {}. Valid options are: {}".format(
                     val,BOOL_VALS))
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'PRINT/TRAJECTORY',
                            'Variable':'LOG_PRINT_KEY','ErrorMessage':errorMessage})
    raise TypeError


def _validate_UNIT(val,errorLog=[]):
    return val

class TRAJECTORY:

  def __init__(self,SECTION_PARAMETERS=None, ADD_LAST=None,COMMON_ITERATION_LEVELS=None,FILENAME=None,FORMAT=None,LOG_PRINT_KEY=None,UNIT=None,CHARGE_BETA=None,CHARGE_EXTENDED=None, CHARGE_OCCUP=None, errorLog=[],changeLog=[],location=""):

    self.__errorLog  = errorLog
    self.__changeLog = changeLog
    self.__SECTION_PARAMETERS = _validate_SECTION_PARAMETERS(SECTION_PARAMETERS, errorLog=self.__errorLog)
    self.__ADD_LAST = _validate_ADD_LAST(ADD_LAST, errorLog=self.__errorLog)
    self.__COMMON_ITERATION_LEVELS = _validate_COMMON_ITERATION_LEVELS(COMMON_ITERATION_LEVELS,errorLog=self.__errorLog)
    self.__FILENAME = _validate_FILENAME(FILENAME, errorLog=self.__errorLog)
    self.__LOG_PRINT_KEY = _validate_LOG_PRINT_KEY(LOG_PRINT_KEY, errorLog=self.__errorLog)
    self.__UNIT = _validate_UNIT(UNIT, errorLog=self.__errorLog)
    self.__FORMAT = _validate_FORMAT(FORMAT, errorLog=self.__errorLog)
    self.__CHARGE_BETA=_validate_CHARGE_BETA(CHARGE_BETA,errorLog=self.__errorLog)
    self.__CHARGE_EXTENDED=_validate_CHARGE_EXTENDED(CHARGE_EXTENDED,errorLog=self.__errorLog)
    self.__CHARGE_OCCUP=_validate_CHARGE_OCCUP(CHARGE_OCCUP,errorLog=self.__errorLog)

    

    self.__location  = "{}/TRAJECTORY".format(location)

    #each subsections
    self.__EACH      = EACH.EACH(errorLog=self.__errorLog,changeLog=self.__changeLog,
                         location=self.__location)

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
  def ADD_LAST(self):
    return self.__ADD_LAST

  @property
  def CHARGE_BETA(self):
    return self.__CHARGE_BETA

  @property
  def CHARGE_EXTENDED(self):
    return self.__CHARGE_EXTENDED

  @property
  def CHARGE_OCCUP(self):
    return self.__CHARGE_OCCUP

  @property
  def COMMON_ITERATION_LEVELS(self):
    return self.__COMMON_ITERATION_LEVELS

  @property
  def FILENAME(self):
    return self.__FILENAME

  @property
  def FORMAT(self):
      return self.__FORMAT

  @property
  def LOG_PRINT_KEY(self):
    return self.__LOG_PRINT_KEY

  @property
  def UNIT(self):
      return self.__UNIT

  @property
  def EACH(self):
    return self.__EACH

  @SECTION_PARAMETERS.setter
  def SECTION_PARAMETERS(self, val):
    val = str(val).upper()
    if val in SECTION_PARAMETERS_VALS:
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'PRINT/TRAJECTORY', 'Variable': 'SECTION_PARAMETERS',
                               'Success': True, 'Previous': self.__SECTION_PARAMETERS, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__SECTION_PARAMETERS = val
    else:
      errorMessage = ("Invalid option for SECTION_PARAMETERS: {}. Valid options are: {}".format(val, SECTION_PARAMETERS_VALS))
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'PRINT/TRAJECTORY', 'Variable': 'SECTION_PARAMETERS',
                               'Success': False, 'Previous': self.__SECTION_PARAMETERS, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'PRINT/TRAJECTORY',
                              'Variable': 'SECTION_PARAMETERS', 'ErrorMessage': errorMessage,
                              'Location': self.__location})

  @ADD_LAST.setter
  def ADD_LAST(self, val):
    self.__changeLog.append(
      {'Date': datetime.datetime.now(), 'Module': 'PRINT/TRAJECTORY', 'Variable': 'ADD_LAST', 'Success': True,
       'Previous': self.__ADD_LAST, 'New': val, 'ErrorMessage': None, 'Location': self.__location})
    self.__ADD_LAST = val

  @CHARGE_BETA.setter
  def CHARGE_BETA(self, val):
      val = str(val).upper()
      if val in BOOL_VALS:
          self.__changeLog.append(
              {'Date': datetime.datetime.now(), 'Module': 'PRINT/TRAJECTORY', 'Variable': 'CHARGE_BETA',
               'Success': True, 'Previous': self.__CHARGE_BETA, 'New': val,
               'ErrorMessage': None, 'Location': self.__location})
          self.__CHARGE_BETA = val
      else:
          errorMessage = ("Invalid option for LOG_PRINT_KEY: {}. Valid options are: {}".format(val, BOOL_VALS))
          self.__changeLog.append(
              {'Date': datetime.datetime.now(), 'Module': 'PRINT/TRAJECTORY', 'Variable': 'CHARGE_BETA',
               'Success': False, 'Previous': self.__CHARGE_BETA, 'New': val,
               'ErrorMessage': errorMessage, 'Location': self.__location})
          self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'PRINT/TRAJECTORY',
                                  'Variable': ' CHARGE_BETA', 'ErrorMessage': errorMessage,
                                  'Location': self.__location})

  @CHARGE_EXTENDED.setter
  def CHARGE_EXTENDED(self, val):
      val = str(val).upper()
      if val in BOOL_VALS:
          self.__changeLog.append(
              {'Date': datetime.datetime.now(), 'Module': 'PRINT/TRAJECTORY', 'Variable': 'CHARGE_EXTENDED',
               'Success': True, 'Previous': self.__CHARGE_EXTENDED, 'New': val,
               'ErrorMessage': None, 'Location': self.__location})
          self.__CHARGE_EXTENDED = val
      else:
          errorMessage = ("Invalid option for CHARGE_EXTENDED: {}. Valid options are: {}".format(val, BOOL_VALS))
          self.__changeLog.append(
              {'Date': datetime.datetime.now(), 'Module': 'PRINT/TRAJECTORY', 'Variable': 'CHARGE_EXTENDED',
               'Success': False, 'Previous': self.__CHARGE_EXTENDED, 'New': val,
               'ErrorMessage': errorMessage, 'Location': self.__location})
          self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'PRINT/TRAJECTORY',
                                  'Variable': ' CHARGE_EXTENDED', 'ErrorMessage': errorMessage,
                                  'Location': self.__location})

  @CHARGE_OCCUP.setter
  def CHARGE_OCCUP(self, val):
      val = str(val).upper()
      if val in BOOL_VALS:
          self.__changeLog.append(
              {'Date': datetime.datetime.now(), 'Module': 'PRINT/TRAJECTORY', 'Variable': 'CHARGE_OCCUP',
               'Success': True, 'Previous': self.__CHARGE_OCCUP, 'New': val,
               'ErrorMessage': None, 'Location': self.__location})
          self.__CHARGE_OCCUP = val
      else:
          errorMessage = ("Invalid option for CHARGE_OCCUP: {}. Valid options are: {}".format(val, BOOL_VALS))
          self.__changeLog.append(
              {'Date': datetime.datetime.now(), 'Module': 'PRINT/TRAJECTORY', 'Variable': 'CHARGE_OCCUP',
               'Success': False, 'Previous': self.__CHARGE_OCCUP, 'New': val,
               'ErrorMessage': errorMessage, 'Location': self.__location})
          self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'PRINT/TRAJECTORY',
                                  'Variable': 'CHARGE_OCCUP', 'ErrorMessage': errorMessage,
                                  'Location': self.__location})




  @COMMON_ITERATION_LEVELS.setter
  def COMMON_ITERATION_LEVELS(self, val):
    if utilities.is_positive_integer(val):
      self.__changeLog.append(
        {'Date': datetime.datetime.now(), 'Module': 'PRINT/TRAJECTORY', 'Variable': 'COMMON_ITERATION_LEVELS',
         'Success': True, 'Previous': self.__COMMON_ITERATION_LEVELS, 'New': val,
         'ErrorMessage': None, 'Location': self.__location})
      self.__COMMON_ITERATION_LEVELS = val
    else:
      errorMessage = "COMMON_ITERATION_LEVELS must be a positive integer."
      self.__changeLog.append(
        {'Date': datetime.datetime.now(), 'Module': 'PRINT/TRAJECTORY', 'Variable': 'COMMON_ITERATION_LEVELS',
         'Success': False, 'Previous': self.__COMMON_ITERATION_LEVELS, 'New': val,
         'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'PRINT/TRAJECTORY',
                              'Variable': 'COMMON_ITERATION_LEVELS', 'ErrorMessage': errorMessage,
                              'Location': self.__location})

  @FILENAME.setter
  def FILENAME(self, val):
    self.FILENAME = val

  @FORMAT.setter
  def FORMAT(self, val):
      val = str(val).upper()
      if val in FORMAT_VALS:
          self.__changeLog.append(
              {'Date': datetime.datetime.now(), 'Module': 'PRINT/TRAJECTORY', 'Variable': 'FORMAT',
               'Success': True, 'Previous': self.__FORMAT, 'New': val,
               'ErrorMessage': None, 'Location': self.__location})
          self.__FORMAT = val
      else:
          errorMessage = ("Invalid option for FORMAT: {}. Valid options are: {}".format(val, FORMAT_VALS))
          self.__changeLog.append(
              {'Date': datetime.datetime.now(), 'Module': 'PRINT/TRAJECTORY', 'Variable': 'FORMAT',
               'Success': False, 'Previous': self.__FORMAT, 'New': val,
               'ErrorMessage': errorMessage, 'Location': self.__location})
          self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'PRINT/TRAJECTORY',
                                  'Variable': 'FORMAT', 'ErrorMessage': errorMessage,
                                  'Location': self.__location})

  @LOG_PRINT_KEY.setter
  def LOG_PRINT_KEY(self, val):
    val = str(val).upper()
    if val in BOOL_VALS:
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'PRINT/TRAJECTORY', 'Variable': 'LOG_PRINT_KEY',
                               'Success': True, 'Previous': self.__LOG_PRINT_KEY, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__LOG_PRINT_KEY = val
    else:
      errorMessage = ("Invalid option for LOG_PRINT_KEY: {}. Valid options are: {}".format(val, BOOL_VALS))
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'PRINT/TRAJECTORY', 'Variable': 'LOG_PRINT_KEY',
                               'Success': False, 'Previous': self.__LOG_PRINT_KEY, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'PRINT/TRAJECTORY',
                              'Variable': ' LOG_PRINT_KEY', 'ErrorMessage': errorMessage,
                              'Location': self.__location})
  @UNIT.setter
  def UNIT(self, val):
    val = str(val).upper()
    self.UNIT=val