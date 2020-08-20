import datetime
import cssi_cp2k.utilities as utilities
from cssi_cp2k.classes import EWALD

PERIODIC_VALS   = ['NONE','X','XY','XYZ','XZ','Y','YZ','Z']
POISSON_SOLVER_VALS =['ANALYTIC','IMPLICIT','MT','MULTIPOLE','PERIODIC','WAVELET']


def _validate_PERIODIC(val,errorLog=[]):
  if val is not None:
    val = str(val).upper()
  
  if val in PERIODIC_VALS or (val is None):
        return val
  else:
    errorMessage = ("Invalid option for PERIODIC: {}. Valid options are: {}".format(
                     val,PERIODIC_VALS))
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'DFT/POISSON',
                            'Variable':'PERIODIC','ErrorMessage':errorMessage})
    raise TypeError   


def _validate_POISSON_SOLVER(val,errorLog=[]):
  if val is not None:
    val = str(val).upper()
  
  if val in POISSON_SOLVER_VALS or (val is None):
        return val
  else:
    errorMessage = ("Invalid option for POISSON_SOLVER: {}. Valid options are: {}".format(
                     val,POISSON_SOLVER_VALS))
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'DFT/POISSON',
                            'Variable':'POISSON_SOLVER','ErrorMessage':errorMessage})
    raise TypeError 
    
 
class POISSON:

  def __init__(self,PERIODIC=None,POISSON_SOLVER=None, errorLog=[],changeLog=[],location=""):
    self.__errorLog = errorLog
    self.__changeLog = changeLog
    self.__location  = "{}/POISSON".format(location)
    self.__PERIODIC=_validate_PERIODIC(PERIODIC, errorLog=self.__errorLog)
    self.__POISSON_SOLVER=_validate_POISSON_SOLVER(POISSON_SOLVER, errorLog=self.__errorLog)
    self.__EWALD = EWALD.EWALD(errorLog=self.__errorLog, changeLog=self.__changeLog,
                         location=self.__location)

    

    
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
  def PERIODIC(self):
    return self.__PERIODIC

  @property
  def POISSON_SOLVER(self):
    return self.__POISSON_SOLVER

  @property
  def EWALD(self):
    return self.__EWALD

  
    
    
  @PERIODIC.setter
  def PERIODIC(self, val):
    val = str(val).upper()
    if val in PERIODIC_VALS:
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT/POISSON', 'Variable': 'PERIODIC',
                               'Success': True, 'Previous': self.__PERIODIC, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__PERIODIC = val
    else:
      errorMessage = ("Invalid option for PERIODIC: {}. Valid options are: {}".format(val, BOOL_VALS))
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT/POISSON', 'Variable': 'PERIODIC',
                               'Success': False, 'Previous': self.__PERIODIC, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'DFT/POISSON',
                              'Variable': ' PERIODIC', 'ErrorMessage': errorMessage,
                              'Location': self.__location}) 
    
    
    
  @POISSON_SOLVER.setter
  def POISSON_SOLVER(self, val):
    val = str(val).upper()
    if val in POISSON_SOLVER_VALS:
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT/POISSON', 'Variable': 'POISSON_SOLVER',
                               'Success': True, 'Previous': self.__POISSON_SOLVER, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__POISSON_SOLVER = val
    else:
      errorMessage = ("Invalid option for POISSON_SOLVER: {}. Valid options are: {}".format(val, BOOL_VALS))
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT/POISSON', 'Variable': 'POISSON_SOLVER',
                               'Success': False, 'Previous': self.__POISSON_SOLVER, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'DFT/POISSON',
                              'Variable': ' POISSON_SOLVER', 'ErrorMessage': errorMessage,
                              'Location': self.__location}) 
 