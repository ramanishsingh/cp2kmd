import datetime
import cssi_cp2k.utilities as utilities
from cssi_cp2k.classes import QS
from cssi_cp2k.classes import POISSON
from cssi_cp2k.classes import DFT_PRINT
from cssi_cp2k.classes import SCF
from cssi_cp2k.classes import XC
from cssi_cp2k.classes import MGRID




BOOL_VALS   = [".TRUE.",".FALSE."]
EXCITATIONS_VALS=['NONE','TDDFT','TDLR'];
PLUS_U_METHOD_VALS=['LOWDIN','MULLIKEN','MULLIKEN_CHARGES'];
SURF_DIP_DIR_VALS=['X','Y','Z'];



def _validate_AUTO_BASIS(val,errorLog=[]):
  #if val is not None:
    #val = str(val).upper()

  #if val in SECTION_PARAMETERS_VALS or (val is None):
  return val
  #else:
   # errorMessage = ("Invalid option for SECTION_PARAMETERS: {}. Valid options are: {}".format(
    #                 val,SECTION_PARAMETERS_VALS))
    #errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'PRINT.ENERGY',
    #                        'Variable':'SECTION_PARAMETERS','ErrorMessage':errorMessage})
    #raise TypeError
    
def _validate_BASIS_SET_FILE_NAME(val,errorLog=[]):
  #if val is not None:
    #val = str(val).upper()

  #if val in SECTION_PARAMETERS_VALS or (val is None):
  return val

def _validate_CHARGE(val,errorLog=[]):
  if utilities.is_integer(val) or (val is None):
    return val
  else:
    errorMessage = "CHARGE must be an integer."
    errorLog.append({'Date': datetime.datetime.now(), 'Type': 'init', 'Module': 'DFT',
                     'Variable': 'CHARGE', 'ErrorMessage': errorMessage})
    raise TypeError


def _validate_EXCITATIONS(val,errorLog=[]):
  if val is not None:
    val = str(val).upper()
  
  if val in EXCITATIONS_VALS or (val is None):
        return val
  else:
    errorMessage = ("Invalid option for EXCITATIONS: {}. Valid options are: {}".format(
                     val,EXCITATIONS_VALS))
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'DFT',
                            'Variable':'EXCITATIONS','ErrorMessage':errorMessage})
    raise TypeError
    
    
def _validate_MULTIPLICITY(val,errorLog=[]):
  if utilities.is_integer(val) or (val is None):
    return val
  else:
    errorMessage = "MULTIPLICITY must be an integer."
    errorLog.append({'Date': datetime.datetime.now(), 'Type': 'init', 'Module': 'DFT',
                     'Variable': 'MULTIPLICITY', 'ErrorMessage': errorMessage})
    raise TypeError

def _validate_PLUS_U_METHOD(val,errorLog=[]):
  if val is not None:
    val = str(val).upper()
  
  if val in PLUS_U_METHOD_VALS or (val is None):
        return val
  else:
    errorMessage = ("Invalid option for PLUS_U_METHOD: {}. Valid options are: {}".format(
                     val,PLUS_U_METHOD_VALS))
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'DFT',
                            'Variable':'PLUS_U_METHOD','ErrorMessage':errorMessage})
    raise TypeError
    

def _validate_POTENTIAL_FILE_NAME(val,errorLog=[]):
    return val

def _validate_RELAX_MULTIPLICITY(val,errorLog=[]):
    return val

def _validate_ROKS(val,errorLog=[]):
  if val is not None:
    val = str(val).upper()
  
  if val in BOOL_VALS or (val is None):
        return val
  else:
    errorMessage = ("Invalid option for ROKS: {}. Valid options are: {}".format(
                     val,BOOL_VALS))
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'DFT',
                            'Variable':'ROKS','ErrorMessage':errorMessage})
    raise TypeError

    
    
def _validate_SUBCELLS(val,errorLog=[]):
    return val    
    


def _validate_SURFACE_DIPOLE_CORRECTION(val,errorLog=[]):
  if val is not None:
    val = str(val).upper()
  
  if val in BOOL_VALS or (val is None):
        return val
  else:
    errorMessage = ("Invalid option for SURFACE_DIPOLE_CORRECTION: {}. Valid options are: {}".format(
                     val,BOOL_VALS))
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'DFT',
                            'Variable':'SURFACE_DIPOLE_CORRECTION','ErrorMessage':errorMessage})
    raise TypeError    
    
    
    
def _validate_SURF_DIP_DIR(val,errorLog=[]):
  if val is not None:
    val = str(val).upper()
  
  if val in SURF_DIP_DIR_VALS or (val is None):
        return val
  else:
    errorMessage = ("Invalid option for SURF_DIP_DIR: {}. Valid options are: {}".format(
                     val,SURF_DIP_DIR_VALS))
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'DFT',
                            'Variable':'SURF_DIP_DIR','ErrorMessage':errorMessage})
    raise TypeError
    
    
def _validate_UKS(val,errorLog=[]):
  if val is not None:
    val = str(val).upper()
  
  if val in BOOL_VALS or (val is None):
        return val
  else:
    errorMessage = ("Invalid option for UKS: {}. Valid options are: {}".format(
                     val,BOOL_VALS))
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'DFT',
                            'Variable':'UKS','ErrorMessage':errorMessage})
    raise TypeError  
    
def _validate_WFN_RESTART_FILE_NAME(val,errorLog=[]):
    return val     
    


class DFT:

  def __init__(self,AUTO_BASIS=None,BASIS_SET_FILE_NAME=None,CHARGE=None,EXCITATIONS=None,MULTIPLICITY=None,PLUS_U_METHOD=None, POTENTIAL_FILE_NAME=None, RELAX_MULTIPLICITY=None, ROKS=None, SUBCELLS=None, SURFACE_DIPOLE_CORRECTION=None, SURF_DIP_DIR=None,WFN_RESTART_FILE_NAME=None, UKS=None, errorLog=[],changeLog=[],location=""):
    self.__errorLog = errorLog
    self.__changeLog = changeLog
    self.__location  = "{}/DFT".format(location)
    self.__AUTO_BASIS=_validate_AUTO_BASIS(AUTO_BASIS, errorLog=self.__errorLog)
    self.__BASIS_SET_FILE_NAME=_validate_BASIS_SET_FILE_NAME(BASIS_SET_FILE_NAME, errorLog=self.__errorLog)
    self.__CHARGE=_validate_CHARGE(CHARGE, errorLog=self.__errorLog)
    self.__EXCITATIONS=_validate_EXCITATIONS(EXCITATIONS,errorLog=self.__errorLog)
    self.__MULTIPLICITY=_validate_MULTIPLICITY(MULTIPLICITY,errorLog=self.__errorLog)
    self.__PLUS_U_METHOD=_validate_PLUS_U_METHOD(PLUS_U_METHOD,errorLog=self.__errorLog)
    self.__POTENTIAL_FILE_NAME=_validate_POTENTIAL_FILE_NAME(POTENTIAL_FILE_NAME,errorLog=self.__errorLog)
    self.__RELAX_MULTIPLICITY=_validate_RELAX_MULTIPLICITY(RELAX_MULTIPLICITY,errorLog=self.__errorLog)
    self.__ROKS=_validate_ROKS(ROKS,errorLog=self.__errorLog)
    self.__SUBCELLS=_validate_SUBCELLS(SUBCELLS,errorLog=self.__errorLog)
    self.__SURFACE_DIPOLE_CORRECTION=_validate_SURFACE_DIPOLE_CORRECTION(SURFACE_DIPOLE_CORRECTION,errorLog=self.__errorLog)
    self.__SURF_DIP_DIR=_validate_SURF_DIP_DIR(SURF_DIP_DIR,errorLog=self.__errorLog)
    self.__UKS=_validate_UKS(UKS,errorLog=self.__errorLog)
    self.__WFN_RESTART_FILE_NAME=_validate_WFN_RESTART_FILE_NAME(WFN_RESTART_FILE_NAME,errorLog=self.__errorLog)
    self.__QS = QS.QS(errorLog=self.__errorLog, changeLog=self.__changeLog,
                         location=self.__location)
    self.__POISSON = POISSON.POISSON(errorLog=self.__errorLog, changeLog=self.__changeLog,
                         location=self.__location)
    self.__PRINT       = DFT_PRINT.PRINT(errorLog=self.__errorLog,changeLog=self.__changeLog,
                           location=self.__location)
    self.__SCF       = SCF.SCF(errorLog=self.__errorLog,changeLog=self.__changeLog,
                           location=self.__location)
    self.__XC       = XC.XC(errorLog=self.__errorLog,changeLog=self.__changeLog,
                           location=self.__location)
    self.__MGRID      = MGRID.MGRID(errorLog=self.__errorLog,changeLog=self.__changeLog,
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
  def AUTO_BASIS(self):
    return self.__AUTO_BASIS

  @property
  def BASIS_SET_FILE_NAME(self):
    return self.__BASIS_SET_FILE_NAME

  @property
  def CHARGE(self):
    return self.__CHARGE

  @property
  def EXCITATIONS(self):
    return self.__EXCITATIONS

  @property
  def MULTIPLICITY(self):
    return self.__MULTIPLICITY

  @property
  def PLUS_U_METHOD(self):
    return self.__PLUS_U_METHOD




  @property
  def POTENTIAL_FILE_NAME(self):
    return self.__POTENTIAL_FILE_NAME

  @property
  def RELAX_MULTIPLICITY(self):
    return self.__RELAX_MULTIPLICITY

  @property
  def ROKS(self):
    return self.__ROKS

  @property
  def SUBCELLS(self):
    return self.__SUBCELLS

  @property
  def SURFACE_DIPOLE_CORRECTION(self):
    return self.__SURFACE_DIPOLE_CORRECTION

  @property
  def SURF_DIP_DIR(self):
    return self.__SURF_DIP_DIR

  @property
  def UKS(self):
    return self.__UKS

  @property
  def WFN_RESTART_FILE_NAME(self):
    return self.__WFN_RESTART_FILE_NAME

  @property
  def QS(self):
      return self.__QS
    
  @property
  def POISSON(self):
      return self.__POISSON
  @property
  def PRINT(self):
      return self.__PRINT

  @property
  def SCF(self):
      return self.__SCF
  @property
  def XC(self):
      return self.__XC
    
  @property
  def MGRID(self):
      return self.__MGRID

  @AUTO_BASIS.setter
  def AUTO_BASIS(self, val):
    
    
    self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT', 'Variable': 'AUTO_BASIS',
                               'Success': True, 'Previous': self.__AUTO_BASIS, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
    self.__AUTO_BASIS= val
    
    

  @BASIS_SET_FILE_NAME.setter
  def BASIS_SET_FILE_NAME(self, val):
    
    
    self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT', 'Variable': 'ABASIS_SET_FILE_NAME',
                               'Success': True, 'Previous': self.__BASIS_SET_FILE_NAME, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
    self.__BASIS_SET_FILE_NAME= val

    
    
  @CHARGE.setter
  def CHARGE(self, val):
    if utilities.is_integer(val):
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT', 'Variable': 'CHARGE',
                               'Success': True, 'Previous': self.__CHARGE, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__CHARGE = val
    else:
      errorMessage = "CHARGE must be aN integer."
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT', 'Variable': 'CHARGE',
                               'Success': False, 'Previous': self.__CHARGE, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'DFT',
                              'Variable': 'CHARGE', 'ErrorMessage': errorMessage,
                              'Location': self.__location})
    
    
    
    

  @EXCITATIONS.setter
  def EXCITATIONS(self, val):
    val = str(val).upper()
    if val in EXCITATIONS_VALS:
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT', 'Variable': 'EXCITATIONS',
                               'Success': True, 'Previous': self.__EXCITATIONS, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__EXCITATIONS = val
    else:
      errorMessage = ("Invalid option for EXCITATIONS: {}. Valid options are: {}".format(val, EXCITATIONS_VALS))
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT', 'Variable': 'EXCITATIONS',
                               'Success': False, 'Previous': self.__EXCITATIONS, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'DFT',
                              'Variable': ' EXCITATIONS', 'ErrorMessage': errorMessage,
                              'Location': self.__location})    
    
    
    
    
   
  @MULTIPLICITY.setter
  def MULTIPLICITY(self, val):
    if utilities.is_integer(val):
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT', 'Variable': 'MULTIPLICITY',
                               'Success': True, 'Previous': self.__MULTIPLICITY, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__MULTIPLICITY = val
    else:
      errorMessage = "MULTIPLICITY must be an  integer."
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT', 'Variable': 'MULTIPLICITY',
                               'Success': False, 'Previous': self.__MULTIPLICITY, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'DFT',
                              'Variable': 'MULTIPLICITY', 'ErrorMessage': errorMessage,
                              'Location': self.__location})    
    
  @PLUS_U_METHOD.setter
  def PLUS_U_METHOD(self, val):
    val = str(val).upper()
    if val in PLUS_U_METHOD_VALS:
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT', 'Variable': 'PLUS_U_METHOD',
                               'Success': True, 'Previous': self.__PLUS_U_METHOD, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__PLUS_U_METHOD = val
    else:
      errorMessage = ("Invalid option for PLUS_U_METHOD: {}. Valid options are: {}".format(val, PLUS_U_METHOD_VALS))
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT', 'Variable': 'PLUS_U_METHOD',
                               'Success': False, 'Previous': self.__PLUS_U_METHOD, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'DFT',
                              'Variable': ' PLUS_U_METHOD', 'ErrorMessage': errorMessage,
                              'Location': self.__location})  

    
    
  @POTENTIAL_FILE_NAME.setter
  def POTENTIAL_FILE_NAME(self, val):
    
    
    self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT', 'Variable': 'POTENTIAL_FILE_NAME',
                               'Success': True, 'Previous': self.__POTENTIAL_FILE_NAME, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
    self.__POTENTIAL_FILE_NAME= val
    
    
    
  @RELAX_MULTIPLICITY.setter
  def RELAX_MULTIPLICITY(self, val):
    
    
    self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT', 'Variable': 'RELAX_MULTIPLICITY',
                               'Success': True, 'Previous': self.__RELAX_MULTIPLICITY, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
    self.__RELAX_MULTIPLICITY= val
    
    
    
  @ROKS.setter
  def ROKS(self, val):
    val = str(val).upper()
    if val in BOOL_VALS:
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT', 'Variable': 'ROKS',
                               'Success': True, 'Previous': self.__ROKS, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__ROKS = val
    else:
      errorMessage = ("Invalid option for ROKS: {}. Valid options are: {}".format(val, BOOL_VALS))
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT', 'Variable': 'ROKS',
                               'Success': False, 'Previous': self.__ROKS, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'DFT',
                              'Variable': ' ROKS', 'ErrorMessage': errorMessage,
                              'Location': self.__location}) 
    
    
    
    
  @SUBCELLS.setter
  def SUBCELLS(self, val):
    
    
    self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT', 'Variable': 'SUBCELLS',
                               'Success': True, 'Previous': self.__SUBCELLS, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
    self.__SUBCELLS= val
    
    
  @SURFACE_DIPOLE_CORRECTION.setter
  def SURFACE_DIPOLE_CORRECTION(self, val):
    val = str(val).upper()
    if val in BOOL_VALS:
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT', 'Variable': 'SURFACE_DIPOLE_CORRECTION',
                               'Success': True, 'Previous': self.__SURFACE_DIPOLE_CORRECTION, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__SURFACE_DIPOLE_CORRECTION = val
    else:
      errorMessage = ("Invalid option for SURFACE_DIPOLE_CORRECTION: {}. Valid options are: {}".format(val, BOOL_VALS))
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT', 'Variable': 'SURFACE_DIPOLE_CORRECTION',
                               'Success': False, 'Previous': self.__SURFACE_DIPOLE_CORRECTION, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'DFT',
                              'Variable': ' SURFACE_DIPOLE_CORRECTION', 'ErrorMessage': errorMessage,
                              'Location': self.__location})
    
    
    
    
  @SURF_DIP_DIR.setter
  def SURF_DIP_DIR(self, val):
    
    
    self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT', 'Variable': 'SURF_DIP_DIR',
                               'Success': True, 'Previous': self.__SURF_DIP_DIR, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
    self.__SURF_DIP_DIR= val
    
    
    
  @UKS.setter
  def UKS(self, val):
    val = str(val).upper()
    if val in BOOL_VALS:
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT', 'Variable': 'UKS',
                               'Success': True, 'Previous': self.__UKS, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__UKS = val
    else:
      errorMessage = ("Invalid option for UKS: {}. Valid options are: {}".format(val, BOOL_VALS))
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT', 'Variable': 'UKS',
                               'Success': False, 'Previous': self.__UKS, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'DFT',
                              'Variable': ' UKS', 'ErrorMessage': errorMessage,
                              'Location': self.__location})
    
    
    
  @WFN_RESTART_FILE_NAME.setter
  def WFN_RESTART_FILE_NAME(self, val):
    
    
    self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT', 'Variable': 'WFN_RESTART_FILE_NAME',
                               'Success': True, 'Previous': self.__WFN_RESTART_FILE_NAME, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
    self.__WFN_RESTART_FILE_NAME= val
    
    
    
    
   
