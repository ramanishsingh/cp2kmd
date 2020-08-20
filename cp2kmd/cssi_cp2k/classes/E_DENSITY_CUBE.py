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
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'FORCE_EVAL/DFT/PRINT/E_DENSITY_CUBE',
                            'Variable':'SECTION_PARAMETERS','ErrorMessage':errorMessage})
    raise TypeError


def _validate_ADD_LAST(val,errorLog=[]):
    return val


def _validate_APPEND(val,errorLog=[]):
  if val is not None:
    val = str(val).upper()

  if val in BOOL_VALS or (val is None):
    return val
  else:
    errorMessage = ("Invalid option for APPEND: {}. Valid options are: {}".format(
                     val,BOOL_VALS))
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'FORCE_EVAL/DFT/PRINT/E_DENSITY_CUBE',
                            'Variable':'APPEND','ErrorMessage':errorMessage})
    raise TypeError

    
    
    
def _validate_COMMON_ITERATION_LEVELS(val,errorLog=[]):
  if utilities.is_positive_integer(val) or (val is None):
    return val
  else:
    errorMessage = "COMMON_ITERATION_LEVELS level must be a positive integer."
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'FORCE_EVAL/DFT/PRINT/E_DENSITY_CUBE',
                            'Variable':'COMMON_ITERATION_LEVELS','ErrorMessage':errorMessage})
    raise TypeError

    
    

def _validate_FILENAME(val,errorLog=[]):
    return val

    
def _validate_COMMON_ITERATION_LEVELS(val,errorLog=[]):
  if utilities.is_positive_integer(val) or (val is None):
    return val
  else:
    errorMessage = "COMMON_ITERATION_LEVELS level must be a positive integer."
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'FORCE_EVAL/DFT/PRINT/E_DENSITY_CUBE',
                            'Variable':'COMMON_ITERATION_LEVELS','ErrorMessage':errorMessage})
    raise TypeError




def _validate_LOG_PRINT_KEY(val,errorLog=[]):
  if val is not None:
    val = str(val).upper()

  if val in BOOL_VALS or (val is None):
    return val
  else:
    errorMessage = ("Invalid option for LOG_PRINT_KEY: {}. Valid options are: {}".format(
                     val,BOOL_VALS))
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'FORCE_EVAL/DFT/PRINT/E_DENSITY_CUBE',
                            'Variable':'LOG_PRINT_KEY','ErrorMessage':errorMessage})
    raise TypeError

    
def _validate_NGAUSS(val,errorLog=[]):
  if utilities.is_positive_integer(val) or (val is None):
    return val
  else:
    errorMessage = "NGAUSS level must be a positive integer."
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'FORCE_EVAL/DFT/PRINT/E_DENSITY_CUBE',
                            'Variable':'NGAUSS','ErrorMessage':errorMessage})
    raise TypeError

def _validate_STRIDE(val,errorLog=[]):
  if utilities.is_positive_integer(val) or (val is None):
    return val
  else:
    errorMessage = "STRIDE level must be a positive integer."
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'FORCE_EVAL/DFT/PRINT/E_DENSITY_CUBE',
                            'Variable':'STRIDE','ErrorMessage':errorMessage})
    raise TypeError

    

def _validate_TOTAL_DENSITY(val,errorLog=[]):
  if val is not None:
    val = str(val).upper()

  if val in BOOL_VALS or (val is None):
    return val
  else:
    errorMessage = ("Invalid option for TOTAL_DENSITY: {}. Valid options are: {}".format(
                     val,BOOL_VALS))
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'FORCE_EVAL/DFT/PRINT/E_DENSITY_CUBE',
                            'Variable':'TOTAL_DENSITY','ErrorMessage':errorMessage})
    raise TypeError

    
    
    
 
def _validate_XRD_INTERFACE(val,errorLog=[]):
  if val is not None:
    val = str(val).upper()

  if val in BOOL_VALS or (val is None):
    return val
  else:
    errorMessage = ("Invalid option for XRD_INTERFACE: {}. Valid options are: {}".format(
                     val,BOOL_VALS))
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'FORCE_EVAL/DFT/PRINT/E_DENSITY_CUBE',
                            'Variable':'XRD_INTERFACE','ErrorMessage':errorMessage})
    raise TypeError

    
    


class E_DENSITY_CUBE:

  def __init__(self,SECTION_PARAMETERS=None, ADD_LAST=None,APPEND=None, COMMON_ITERATION_LEVELS=None,FILENAME=None,NGAUSS=None,LOG_PRINT_KEY=None,STRIDE=None,TOTAL_DENSITY=None,XRD_INTERFACE=None, errorLog=[],changeLog=[],location=""):

    self.__errorLog  = errorLog
    self.__changeLog = changeLog
    
    self.__SECTION_PARAMETERS = _validate_SECTION_PARAMETERS(SECTION_PARAMETERS, errorLog=self.__errorLog)
    self.__ADD_LAST = _validate_ADD_LAST(ADD_LAST, errorLog=self.__errorLog)
    self.__APPEND = _validate_APPEND(APPEND,errorLog=self.__errorLog)
    self.__FILENAME = _validate_FILENAME(FILENAME, errorLog=self.__errorLog)
    self.__LOG_PRINT_KEY = _validate_LOG_PRINT_KEY(LOG_PRINT_KEY, errorLog=self.__errorLog)
    self.__COMMON_ITERATION_LEVELS = _validate_COMMON_ITERATION_LEVELS(COMMON_ITERATION_LEVELS, errorLog=self.__errorLog)
    self.__NGAUSS = _validate_NGAUSS(NGAUSS, errorLog=self.__errorLog)
    self.__STRIDE = _validate_STRIDE(STRIDE, errorLog=self.__errorLog)
    self.__TOTAL_DENSITY = _validate_TOTAL_DENSITY(TOTAL_DENSITY, errorLog=self.__errorLog)
    self.__XRD_INTERFACE = _validate_XRD_INTERFACE(XRD_INTERFACE, errorLog=self.__errorLog)



    self.__location  = "{}/PRINT".format(location)



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
  def APPEND(self):
    return self.__APPEND

  @property
  def COMMON_ITERATION_LEVELS(self):
    return self.__COMMON_ITERATION_LEVELS

  @property
  def FILENAME(self):
    return self.__FILENAME

  @property
  def NGAUSS(self):
      return self.__NGAUSS

  @property
  def LOG_PRINT_KEY(self):
    return self.__LOG_PRINT_KEY

  @property
  def STRIDE(self):
      return self.__STRIDE
    
  @property
  def TOTAL_DENSITY(self):
      return self.__TOTAL_DENSITY
    
    
  @property
  def XRD_INTERFACE(self):
      return self.__XRD_INTERFACE



  @SECTION_PARAMETERS.setter
  def SECTION_PARAMETERS(self, val):
    val = str(val).upper()
    if val in SECTION_PARAMETERS_VALS:
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'FORCE_EVAL/DFT/PRINT/E_DENSITY_CUBE', 'Variable': 'SECTION_PARAMETERS',
                               'Success': True, 'Previous': self.__SECTION_PARAMETERS, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__SECTION_PARAMETERS = val
    else:
      errorMessage = ("Invalid option for SECTION_PARAMETERS: {}. Valid options are: {}".format(val, SECTION_PARAMETERS_VALS))
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'FORCE_EVAL/DFT/PRINT/E_DENSITY_CUBE', 'Variable': 'SECTION_PARAMETERS',
                               'Success': False, 'Previous': self.__SECTION_PARAMETERS, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'FORCE_EVAL/DFT/PRINT/E_DENSITY_CUBE',
                              'Variable': 'SECTION_PARAMETERS', 'ErrorMessage': errorMessage,
                              'Location': self.__location})

  @ADD_LAST.setter
  def ADD_LAST(self, val):
    self.__changeLog.append(
      {'Date': datetime.datetime.now(), 'Module': 'FORCE_EVAL/DFT/PRINT/E_DENSITY_CUBE', 'Variable': 'ADD_LAST', 'Success': True,
       'Previous': self.__ADD_LAST, 'New': val, 'ErrorMessage': None, 'Location': self.__location})
    self.__ADD_LAST = val

    
    
    
  @APPEND.setter
  def APPEND(self, val):
    val = str(val).upper()
    if val in BOOL_VALS:
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'FORCE_EVAL/DFT/PRINT/E_DENSITY_CUBE', 'Variable': 'APPEND',
                               'Success': True, 'Previous': self.__APPEND, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__APPEND = val
    else:
      errorMessage = ("Invalid option for LOG_PRINT_KEY: {}. Valid options are: {}".format(val, BOOL_VALS))
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'FORCE_EVAL/DFT/PRINT/E_DENSITY_CUBE', 'Variable': 'APPEND',
                               'Success': False, 'Previous': self.__APPEND, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'FORCE_EVAL/DFT/PRINT/E_DENSITY_CUBE',
                              'Variable': ' APPEND', 'ErrorMessage': errorMessage,
                              'Location': self.__location})
    
    
    
  @COMMON_ITERATION_LEVELS.setter
  def COMMON_ITERATION_LEVELS(self, val):
    if utilities.is_positive_integer(val):
      self.__changeLog.append(
        {'Date': datetime.datetime.now(), 'Module': 'FORCE_EVAL/DFT/PRINT/E_DENSITY_CUBE', 'Variable': 'COMMON_ITERATION_LEVELS',
         'Success': True, 'Previous': self.__COMMON_ITERATION_LEVELS, 'New': val,
         'ErrorMessage': None, 'Location': self.__location})
      self.__COMMON_ITERATION_LEVELS = val
    else:
      errorMessage = "COMMON_ITERATION_LEVELS must be a positive integer."
      self.__changeLog.append(
        {'Date': datetime.datetime.now(), 'Module': 'FORCE_EVAL/DFT/PRINT/E_DENSITY_CUBE', 'Variable': 'COMMON_ITERATION_LEVELS',
         'Success': False, 'Previous': self.__COMMON_ITERATION_LEVELS, 'New': val,
         'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'FORCE_EVAL/DFT/PRINT/E_DENSITY_CUBE',
                              'Variable': 'COMMON_ITERATION_LEVELS', 'ErrorMessage': errorMessage,
                              'Location': self.__location})

  @FILENAME.setter
  def FILENAME(self, val):
    self.FILENAME = val


  @LOG_PRINT_KEY.setter
  def LOG_PRINT_KEY(self, val):
    val = str(val).upper()
    if val in BOOL_VALS:
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'FORCE_EVAL/DFT/PRINT/E_DENSITY_CUBE', 'Variable': 'LOG_PRINT_KEY',
                               'Success': True, 'Previous': self.__LOG_PRINT_KEY, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__LOG_PRINT_KEY = val
    else:
      errorMessage = ("Invalid option for LOG_PRINT_KEY: {}. Valid options are: {}".format(val, BOOL_VALS))
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'FORCE_EVAL/DFT/PRINT/E_DENSITY_CUBE', 'Variable': 'LOG_PRINT_KEY',
                               'Success': False, 'Previous': self.__LOG_PRINT_KEY, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'FORCE_EVAL/DFT/PRINT/E_DENSITY_CUBE',
                              'Variable': ' LOG_PRINT_KEY', 'ErrorMessage': errorMessage,
                              'Location': self.__location})
    
    
  @NGAUSS.setter
  def NGAUSS(self, val):
    if utilities.is_positive_integer(val):
      self.__changeLog.append(
        {'Date': datetime.datetime.now(), 'Module': 'FORCE_EVAL/DFT/PRINT/E_DENSITY_CUBE', 'Variable': 'NGAUSS',
         'Success': True, 'Previous': self.__NGAUSS, 'New': val,
         'ErrorMessage': None, 'Location': self.__location})
      self.__NGAUSS = val
    else:
      errorMessage = "COMMON_ITERATION_LEVELS must be a positive integer."
      self.__changeLog.append(
        {'Date': datetime.datetime.now(), 'Module': 'FORCE_EVAL/DFT/PRINT/E_DENSITY_CUBE', 'Variable': 'NGAUSS',
         'Success': False, 'Previous': self.__NGAUSS, 'New': val,
         'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'FORCE_EVAL/DFT/PRINT/E_DENSITY_CUBE',
                              'Variable': 'NGAUSS', 'ErrorMessage': errorMessage,
                              'Location': self.__location})
    
    
  @STRIDE.setter
  def STRIDE(self, val):
    if utilities.is_positive_integer(val):
      self.__changeLog.append(
        {'Date': datetime.datetime.now(), 'Module': 'FORCE_EVAL/DFT/PRINT/E_DENSITY_CUBE', 'Variable': 'STRIDE',
         'Success': True, 'Previous': self.__STRIDE, 'New': val,
         'ErrorMessage': None, 'Location': self.__location})
      self.__STRIDE = val
    else:
      errorMessage = "COMMON_ITERATION_LEVELS must be a positive integer."
      self.__changeLog.append(
        {'Date': datetime.datetime.now(), 'Module': 'FORCE_EVAL/DFT/PRINT/E_DENSITY_CUBE', 'Variable': 'STRIDE',
         'Success': False, 'Previous': self.__STRIDE, 'New': val,
         'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'FORCE_EVAL/DFT/PRINT/E_DENSITY_CUBE',
                              'Variable': 'STRIDE', 'ErrorMessage': errorMessage,
                              'Location': self.__location})
    
    
    
  @TOTAL_DENSITY.setter
  def TOTAL_DENSITY(self, val):
    val = str(val).upper()
    if val in BOOL_VALS:
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'FORCE_EVAL/DFT/PRINT/E_DENSITY_CUBE', 'Variable': 'TOTAL_DENSITY',
                               'Success': True, 'Previous': self.__TOTAL_DENSITY, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__LOG_PRINT_KEY = val
    else:
      errorMessage = ("Invalid option for LOG_PRINT_KEY: {}. Valid options are: {}".format(val, BOOL_VALS))
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'FORCE_EVAL/DFT/PRINT/E_DENSITY_CUBE', 'Variable': 'TOTAL_DENSITY',
                               'Success': False, 'Previous': self.__TOTAL_DENSITY, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'FORCE_EVAL/DFT/PRINT/E_DENSITY_CUBE',
                              'Variable': ' TOTAL_DENSITY', 'ErrorMessage': errorMessage,
                              'Location': self.__location})
    
    
  @XRD_INTERFACE.setter
  def XRD_INTERFACE(self, val):
    val = str(val).upper()
    if val in BOOL_VALS:
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'FORCE_EVAL/DFT/PRINT/E_DENSITY_CUBE', 'Variable': 'XRD_INTERFACE',
                               'Success': True, 'Previous': self.__XRD_INTERFACE, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__LOG_PRINT_KEY = val
    else:
      errorMessage = ("Invalid option for LOG_PRINT_KEY: {}. Valid options are: {}".format(val, BOOL_VALS))
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'FORCE_EVAL/DFT/PRINT/E_DENSITY_CUBE', 'Variable': 'XRD_INTERFACE',
                               'Success': False, 'Previous': self.__XRD_INTERFACE, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'FORCE_EVAL/DFT/PRINT/E_DENSITY_CUBE',
                              'Variable': ' XRD_INTERFACE', 'ErrorMessage': errorMessage,
                              'Location': self.__location})
    
    
    
    
    
    