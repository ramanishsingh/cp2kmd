import datetime
import cssi_cp2k.utilities as utilities





BOOL_VALS   = [".TRUE.",".FALSE."]
CELL_FILE_FORMAT_VALS   = ["CIF","CP2K","XSC"]
PERIODIC_VALS   = ["NONE","X","XY","XYZ","XZ","Y","YZ","Z"]
SYMMETRY_VALS   = ["CUBIC","HEXAGONAL","MONOCLINIC","MONOCLINIC_GAMMA_AB","NONE","ORTHORHOMBIC","RHOMBOHEDRAL","TETRAGONAL","TETRAGONAL_AB","TETRAGONAL_AC","TETRAGONAL_BC","TRICLINIC"]






def _validate_A(val,errorLog=[]):

  return val

def _validate_ABC(val,errorLog=[]):

  return val

def _validate_ALPHA_BETA_GAMMA(val,errorLog=[]):

  return val

def _validate_B(val,errorLog=[]):

  return val

def _validate_C(val,errorLog=[]):

  return val




def _validate_CELL_FILE_FORMAT(val,errorLog=[]):
  if val is not None:
    val = str(val).upper()
  
  if val in CELL_FILE_FORMAT_VALS or (val is None):
        return val
  else:
    errorMessage = ("Invalid option for CELL_FILE_FORMAT: {}. Valid options are: {}".format(
                     val,CELL_FILE_FORMAT_VALS))
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'SUBSYS.CELL',
                            'Variable':'CELL_FILE_FORMAT','ErrorMessage':errorMessage})
    raise TypeError 
    
def _validate_CELL_FILE_NAME(val,errorLog=[]):

  return val

def _validate_MULTIPLE_UNIT_CELL(val,errorLog=[]):

  return val

def _validate_PERIODIC(val,errorLog=[]):
  if val is not None:
    val = str(val).upper()
  
  if val in PERIODIC_VALS or (val is None):
        return val
  else:
    errorMessage = ("Invalid option for PERIODIC: {}. Valid options are: {}".format(
                     val,PERIODIC_VALS))
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'SUBSYS.CELL',
                            'Variable':'PERIODIC','ErrorMessage':errorMessage})
    raise TypeError
    
    
    
    
def _validate_SYMMETRY(val,errorLog=[]):
  if val is not None:
    val = str(val).upper()
  
  if val in SYMMETRY_VALS or (val is None):
        return val
  else:
    errorMessage = ("Invalid option for SYMMETRY: {}. Valid options are: {}".format(
                     val,SYMMETRY_VALS))
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'SUBSYS.CELL',
                            'Variable':'SYMMETRY','ErrorMessage':errorMessage})
    raise TypeError




class CELL:

  def __init__(self,A=None,ABC=None,ALPHA_BETA_GAMMA=None,B=None,C=None,CELL_FILE_FORMAT=None, CELL_FILE_NAME=None, MULTIPLE_UNIT_CELL=None, PERIODIC=None, SYMMETRY=None,errorLog=[],changeLog=[],location=""):
    self.__errorLog = errorLog
    self.__changeLog = changeLog
    self.__location  = "{}/DFT".format(location)
    self.__A=_validate_A(A, errorLog=self.__errorLog)
    self.__ABC=_validate_ABC(ABC, errorLog=self.__errorLog)
    self.__ALPHA_BETA_GAMMA=_validate_ALPHA_BETA_GAMMA(ALPHA_BETA_GAMMA, errorLog=self.__errorLog)
    self.__B=_validate_B(B,errorLog=self.__errorLog)
    self.__C=_validate_C(C,errorLog=self.__errorLog)
    self.__CELL_FILE_FORMAT=_validate_CELL_FILE_FORMAT(CELL_FILE_FORMAT,errorLog=self.__errorLog)
    self.__CELL_FILE_NAME=_validate_CELL_FILE_NAME(CELL_FILE_NAME,errorLog=self.__errorLog)
    self.__MULTIPLE_UNIT_CELL=_validate_MULTIPLE_UNIT_CELL(MULTIPLE_UNIT_CELL,errorLog=self.__errorLog)
    self.__PERIODIC=_validate_PERIODIC(PERIODIC,errorLog=self.__errorLog)
    self.__SYMMETRY=_validate_SYMMETRY(SYMMETRY,errorLog=self.__errorLog)
    

    
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
  def A(self):
    return self.__A

  @property
  def ABC(self):
    return self.__ABC

  @property
  def ALPHA_BETA_GAMMA(self):
    return self.__ALPHA_BETA_GAMMA

  @property
  def B(self):
    return self.__B

  @property
  def C(self):
    return self.__C

  @property
  def CELL_FILE_FORMAT(self):
    return self.__CELL_FILE_FORMAT




  @property
  def CELL_FILE_NAME(self):
    return self.__CELL_FILE_NAME

  @property
  def MULTIPLE_UNIT_CELL(self):
    return self.__MULTIPLE_UNIT_CELL

  @property
  def PERIODIC(self):
    return self.__PERIODIC

  @property
  def SYMMETRY(self):
    return self.__SYMMETRY

  


  @A.setter
  def A(self, val):
    
    
    self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SUBSYS.CELL', 'Variable': 'A',
                               'Success': True, 'Previous': self.__A, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
    self.__A= val
    
    
    
  @ABC.setter
  def ABC(self, val):
    
    
    self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SUBSYS.CELL', 'Variable': 'ABC',
                               'Success': True, 'Previous': self.__ABC, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
    self.__ABC= val
    
    
    

  @ALPHA_BETA_GAMMA.setter
  def ALPHA_BETA_GAMMA(self, val):
    
    
    self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SUBSYS.CELL', 'Variable': 'ALPHA_BETA_GAMMA',
                               'Success': True, 'Previous': self.__ALPHA_BETA_GAMMA, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
    self.__ALPHA_BETA_GAMMA= val
    
  @B.setter
  def B(self, val):
    
    
    self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SUBSYS.CELL', 'Variable': 'B',
                               'Success': True, 'Previous': self.__B, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
    self.__B= val
    
  @C.setter
  def C(self, val):
    
    
    self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SUBSYS.CELL', 'Variable': 'C',
                               'Success': True, 'Previous': self.__C, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
    self.__C= val
    
    
    
  @CELL_FILE_FORMAT.setter
  def CELL_FILE_FORMAT(self, val):
    val = str(val).upper()
    if val in CELL_FILE_FORMAT_VALS:
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SUBSYS.CELL', 'Variable': 'CELL_FILE_FORMAT',
                               'Success': True, 'Previous': self.__CELL_FILE_FORMAT, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__CELL_FILE_FORMAT = val
    else:
      errorMessage = ("Invalid option for CELL_FILE_FORMAT: {}. Valid options are: {}".format(val, CELL_FILE_FORMAT_VALS))
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SUBSYS.CELL', 'Variable': 'CELL_FILE_FORMAT',
                               'Success': False, 'Previous': self.__CELL_FILE_FORMAT, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'SUBSYS.CELL',
                              'Variable': ' CELL_FILE_FORMAT', 'ErrorMessage': errorMessage,
                              'Location': self.__location}) 
    
  @CELL_FILE_NAME.setter
  def CELL_FILE_NAME(self, val):
    
    
    self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SUBSYS.CELL', 'Variable': 'CELL_FILE_NAME',
                               'Success': True, 'Previous': self.__B, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
    self.__CELL_FILE_NAME= val
    
  @MULTIPLE_UNIT_CELL.setter
  def MULTIPLE_UNIT_CELL(self, val):
    
    
    self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SUBSYS.CELL', 'Variable': 'MULTIPLE_UNIT_CELL',
                               'Success': True, 'Previous': self.__MULTIPLE_UNIT_CELL, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
    self.__MULTIPLE_UNIT_CELL= val  

  @PERIODIC.setter
  def PERIODIC(self, val):
    val = str(val).upper()
    if val in PERIODIC_VALS:
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SUBSYS.CELL', 'Variable': 'PERIODIC',
                               'Success': True, 'Previous': self.__PERIODIC, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__PERIODIC = val
    else:
      errorMessage = ("Invalid option for PERIODIC: {}. Valid options are: {}".format(val, PERIODIC_VALS))
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SUBSYS.CELL', 'Variable': 'PERIODIC',
                               'Success': False, 'Previous': self.__PERIODIC, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'SUBSYS.CELL',
                              'Variable': ' PERIODIC', 'ErrorMessage': errorMessage,
                              'Location': self.__location}) 
    
    
  @SYMMETRY.setter
  def SYMMETRY(self, val):
    val = str(val).upper()
    if val in SYMMETRY_VALS:
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SUBSYS.CELL', 'Variable': 'SYMMETRY',
                               'Success': True, 'Previous': self.__SYMMETRY, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__SYMMETRY = val
    else:
      errorMessage = ("Invalid option for SYMMETRY: {}. Valid options are: {}".format(val, SYMMETRY_VALS))
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SUBSYS.CELL', 'Variable': 'SYMMETRY',
                               'Success': False, 'Previous': self.__SYMMETRY, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'SUBSYS.CELL',
                              'Variable': ' SYMMETRY', 'ErrorMessage': errorMessage,
                              'Location': self.__location}) 
    
    