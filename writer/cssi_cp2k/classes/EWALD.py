import datetime
import cssi_cp2k.utilities as utilities

BOOL_VALS   = [".TRUE.",".FALSE"]
EWALD_TYPE_VALS=['EWALD','NONE','PME','SPME'];


def _validate_ALPHA(val,errorLog=[]):

  return val

def _validate_EPSILON(val,errorLog=[]):

  return val

def _validate_EWALD_ACCURACY(val,errorLog=[]):

  return val


def _validate_EWALD_TYPE(val,errorLog=[]):
  if val is not None:
    val = str(val).upper()
  
  if val in EWALD_TYPE_VALS or (val is None):
        return val
  else:
    errorMessage = ("Invalid option for EWALD_TYPE: {}. Valid options are: {}".format(
                     val,EWALD_TYPE_VALS))
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'DFT/POISSON/EWALD.',
                            'Variable':'EWALD_TYPE','ErrorMessage':errorMessage})
    raise TypeError  

    
    
    
def _validate_GMAX(val,errorLog=[]):
  if utilities.is_integer(val) or (val is None):
    return val
  else:
    errorMessage = "GMAX must be an integer."
    errorLog.append({'Date': datetime.datetime.now(), 'Type': 'init', 'Module': 'DFT/POISSON/EWALD',
                     'Variable': 'GMAX', 'ErrorMessage': errorMessage})
    raise TypeError
    
    
def _validate_NS_MAX(val,errorLog=[]):
  if utilities.is_integer(val) or (val is None):
    return val
  else:
    errorMessage = "NS_MAX must be an integer."
    errorLog.append({'Date': datetime.datetime.now(), 'Type': 'init', 'Module': 'NS_MAX',
                     'Variable': 'NS_MAX', 'ErrorMessage': errorMessage})
    raise TypeError
    
def _validate_O_SPLINE(val,errorLog=[]):
  if utilities.is_integer(val) or (val is None):
    return val
  else:
    errorMessage = "O_SPLINE must be an integer."
    errorLog.append({'Date': datetime.datetime.now(), 'Type': 'init', 'Module': 'DFT/POISSON/EWALD',
                     'Variable': 'O_SPLINE', 'ErrorMessage': errorMessage})
    raise TypeError
    
    
def _validate_RCUT(val,errorLog=[]):

  return val


 
class EWALD:

  def __init__(self,ALPHA=None,EPSILON=None,EWALD_ACCURACY=None,EWALD_TYPE=None,GMAX=None,NS_MAX=None, O_SPLINE=None, RCUT=None,  errorLog=[],changeLog=[],location=""):
    self.__errorLog = errorLog
    self.__changeLog = changeLog
    self.__location= location
    self.__ALPHA=_validate_ALPHA(ALPHA, errorLog=self.__errorLog)
    self.__EPSILON=_validate_EPSILON(EPSILON, errorLog=self.__errorLog)
    self.__EWALD_ACCURACY=_validate_EWALD_ACCURACY(EWALD_ACCURACY, errorLog=self.__errorLog)
    self.__EWALD_TYPE=_validate_EWALD_TYPE(EWALD_TYPE,errorLog=self.__errorLog)
    self.__GMAX=_validate_GMAX(GMAX,errorLog=self.__errorLog)
    self.__NS_MAX=_validate_NS_MAX(NS_MAX,errorLog=self.__errorLog)
    self.__O_SPLINE=_validate_O_SPLINE(O_SPLINE,errorLog=self.__errorLog)
    self.__RCUT=_validate_RCUT(RCUT,errorLog=self.__errorLog)


    

    self.__location  = "{}/EWALD".format(location)
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
  def ALPHA(self):
    return self.__ALPHA

  @property
  def EPSILON(self):
    return self.__EPSILON

  @property
  def EWALD_ACCURACY(self):
    return self.__EWALD_ACCURACY


  @property
  def EWALD_TYPE(self):
    return self.__EWALD_TYPE

  @property
  def GMAX(self):
    return self.__GMAX

  @property
  def NS_MAX(self):
    return self.__NS_MAX

  @property
  def O_SPLINE(self):
    return self.__O_SPLINE




  @property
  def RCUT(self):
    return self.__RCUT



  @ALPHA.setter
  def ALPHA(self, val):
    
    
    self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT/POISSON/EWALD', 'Variable': 'ALPHA',
                               'Success': True, 'Previous': self.__ALPHA, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
    self.__ALPHA= val 
    
    
  @EPSILON.setter
  def EPSILON(self, val):
    
    
    self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT/POISSON/EWALD', 'Variable': 'EPSILON',
                               'Success': True, 'Previous': self.__EPSILON, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
    self.__EPSILON= val 
    
  @EWALD_ACCURACY.setter
  def EWALD_ACCURACY(self, val):
    
    
    self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT/POISSON/EWALD', 'Variable': 'EWALD_ACCURACY',
                               'Success': True, 'Previous': self.__EWALD_ACCURACY, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
    self.__EWALD_ACCURACY= val 
      


  @GMAX.setter
  def GMAX(self, val):
    if utilities.is_integer(val):
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT/POISSON/EWALD', 'Variable': 'GMAX',
                               'Success': True, 'Previous': self.__GMAX, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__GMAX = val
    else:
      errorMessage = "GMAX must be aN integer."
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT/POISSON/EWALD', 'Variable': 'GMAX',
                               'Success': False, 'Previous': self.__GMAX, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'DFT/POISSON/EWALD',
                              'Variable': 'GMAX', 'ErrorMessage': errorMessage,
                              'Location': self.__location}) 
    
    
  @NS_MAX.setter
  def NS_MAX(self, val):
    if utilities.is_integer(val):
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT/POISSON/EWALD', 'Variable': 'NS_MAX',
                               'Success': True, 'Previous': self.__NS_MAX, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__NS_MAX = val
    else:
      errorMessage = "NS_MAX must be aN integer."
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT/POISSON/EWALD', 'Variable': 'NS_MAX',
                               'Success': False, 'Previous': self.__NS_MAX, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'DFT/POISSON/EWALD',
                              'Variable': 'NS_MAX', 'ErrorMessage': errorMessage,
                              'Location': self.__location}) 
    
    
  @O_SPLINE.setter
  def O_SPLINE(self, val):
    if utilities.is_integer(val):
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT/POISSON/EWALD', 'Variable': 'O_SPLINE',
                               'Success': True, 'Previous': self.__O_SPLINE, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__O_SPLINE = val
    else:
      errorMessage = "O_SPLINE must be aN integer."
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT/POISSON/EWALD', 'Variable': 'O_SPLINE',
                               'Success': False, 'Previous': self.__O_SPLINE, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'DFT/POISSON/EWALD',
                              'Variable': 'O_SPLINE', 'ErrorMessage': errorMessage,
                              'Location': self.__location}) 
    
  @RCUT.setter
  def RCUT(self, val):
    
    
    self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT/POISSON/EWALD', 'Variable': 'RCUT',
                               'Success': True, 'Previous': self.__RCUT, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
    self.__RCUT= val   
  