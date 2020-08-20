import datetime
import cssi_cp2k.utilities as utilities
from cssi_cp2k.classes import PRINT
from cssi_cp2k.classes import MD
from cssi_cp2k.classes import DFT
from cssi_cp2k.classes import SUBSYS

METHOD_VALS=['EIP','EMBED','FIST','MIXED','QMMM','QS','QUICKSTEP','SIRIUS']
STRESS_TENSOR_VALS=['ANALYTICAL','DIAGONAL_ANALYTICAL','DIAGONAL_NUMERICAL','NUMERICAL','NONE']

def _validate_METHOD(val,errorLog=[]):
  if val is not None:
    val = str(val).upper()

  if val in METHOD_VALS or (val is None):
    return val
  else:
    errorMessage = ("Invalid option for METHOD: {}. Valid options are: {}".format(
                     val,METHOD_VALS))
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'FORCE_EVAL',
                            'Variable':'METHOD','ErrorMessage':errorMessage})
    raise TypeError
    
    
    
def _validate_STRESS_TENSOR(val,errorLog=[]):
  if val is not None:
    val = str(val).upper()

  if val in STRESS_TENSOR_VALS or (val is None):
    return val
  else:
    errorMessage = ("Invalid option for STRESS_TENSOR: {}. Valid options are: {}".format(
                     val,STRESS_TENSOR_VALS))
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'FORCE_EVAL',
                            'Variable':'STRESS_TENSOR','ErrorMessage':errorMessage})
    raise TypeError




class FORCE_EVAL:

  def __init__(self,METHOD=None, STRESS_TENSOR=None, errorLog=[],changeLog=[],location=""):
    
    self.__errorLog  = errorLog
    self.__changeLog = changeLog
    self.__location  = "{}/MOTION".format(location)
    self.__METHOD = _validate_METHOD(METHOD, errorLog=self.__errorLog)
    self.__STRESS_TENSOR = _validate_STRESS_TENSOR(STRESS_TENSOR, errorLog=self.__errorLog)
    # Subsections of MOTION
    self.__PRINT     = PRINT.PRINT(errorLog=self.__errorLog,changeLog=self.__changeLog,
                         location=self.__location)
    self.__MD        = MD.MD(errorLog=self.__errorLog,changeLog=self.__changeLog,
                         location=self.__location)
    self.__DFT        = DFT.DFT(errorLog=self.__errorLog,changeLog=self.__changeLog,
                         location=self.__location)
    self.__SUBSYS        = SUBSYS.SUBSYS(errorLog=self.__errorLog,changeLog=self.__changeLog,
                         location=self.__location)
    
  @property
  def METHOD(self):
    return self.__METHOD

  @property
  def STRESS_TENSOR(self):
    return self.__STRESS_TENSOR

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
  def PRINT(self):
    return self.__PRINT

  @property
  def MD(self):
    return self.__MD

  @property
  def DFT(self):
    return self.__DFT
  @property
  def SUBSYS(self):
    return self.__SUBSYS



  @METHOD.setter
  def METHOD(self, val):
    val = str(val).upper()
    if val in METHOD_VALS:
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'FORCE_EVAL', 'Variable': 'METHOD',
                               'Success': True, 'Previous': self.__METHOD, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__METHOD = val
    else:
      errorMessage = ("Invalid option for METHOD: {}. Valid options are: {}".format(val, METHOD_VALS))
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'FORCE_EVAL', 'Variable': 'METHOD',
                               'Success': False, 'Previous': self.__METHOD, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'FORCE_EVAL',
                              'Variable': 'METHOD', 'ErrorMessage': errorMessage,
                              'Location': self.__location})
    
    
  @STRESS_TENSOR.setter
  def STRESS_TENSOR(self, val):
    val = str(val).upper()
    if val in STRESS_TENSOR_VALS:
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'FORCE_EVAL', 'Variable': 'STRESS_TENSOR',
                               'Success': True, 'Previous': self.__METHOD, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__STRESS_TENSOR = val
    else:
      errorMessage = ("Invalid option for METHOD: {}. Valid options are: {}".format(val, METHOD_VALS))
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'FORCE_EVAL', 'Variable': 'STRESS_TENSOR',
                               'Success': False, 'Previous': self.__METHOD, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'FORCE_EVAL',
                              'Variable': 'STRESS_TENSOR', 'ErrorMessage': errorMessage,
                              'Location': self.__location})
    
    
    

