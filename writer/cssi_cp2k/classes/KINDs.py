import datetime
import cssi_cp2k.utilities as utilities

from cssi_cp2k.utilities1 import oneDimArray as oda
from cssi_cp2k.utilities1 import objectArray as oba



BOOL_VALS   = [".TRUE.",".FALSE."]




def _validate_SECTION_PARAMETERS(val,errorLog=[]):

  return val

def _validate_AUX_BASIS_SET(val,errorLog=[]):

  return val

def _validate_AUX_FIT_BASIS_SET(val,errorLog=[]):

  return val

def _validate_BASIS_SET(val,errorLog=[]):

  return val

def _validate_CORE_CORRECTION(val,errorLog=[]):

  return val
def _validate_DFTB3_PARAM(val,errorLog=[]):

  return val

def _validate_ELEC_CONF(val,errorLog=[]):
  if utilities.is_integer(val) or (val is None):
    return val
  else:
    errorMessage = "ELEC_CONF must be an integer."
    errorLog.append({'Date': datetime.datetime.now(), 'Type': 'init', 'Module': 'SUBSYS.KIND',
                     'Variable': 'ELEC_CONF', 'ErrorMessage': errorMessage})
    raise TypeError
    
def _validate_ELEMENT(val,errorLog=[]):

  return val




def _validate_FLOATING_BASIS_CENTER(val,errorLog=[]):
  if val is not None:
    val = str(val).upper()
  
  if val in BOOL_VALS or (val is None):
        return val
  else:
    errorMessage = ("Invalid option for FLOATING_BASIS_CENTER: {}. Valid options are: {}".format(
                     val,BOOL_VALS))
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'SUBSYS.KIND',
                            'Variable':'FLOATING_BASIS_CENTER','ErrorMessage':errorMessage})
    raise TypeError 
    
def _validate_GHOST(val,errorLog=[]):
  if val is not None:
    val = str(val).upper()
  
  if val in BOOL_VALS or (val is None):
        return val
  else:
    errorMessage = ("Invalid option for GHOST: {}. Valid options are: {}".format(
                     val,BOOL_VALS))
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'SUBSYS.KIND',
                            'Variable':'GHOST','ErrorMessage':errorMessage})
    raise TypeError


def _validate_GPW_TYPE(val,errorLog=[]):
  if val is not None:
    val = str(val).upper()
  
  if val in BOOL_VALS or (val is None):
        return val
  else:
    errorMessage = ("Invalid option for GPW_TYPE: {}. Valid options are: {}".format(
                     val,BOOL_VALS))
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'SUBSYS.KIND',
                            'Variable':'GPW_TYPE','ErrorMessage':errorMessage})
    raise TypeError 
    
 

def _validate_HARD_EXP_RADIUS(val,errorLog=[]):

  return val

def _validate_KG_POTENTIAL(val,errorLog=[]):

  return val
def _validate_KG_POTENTIAL_FILE_NAME(val,errorLog=[]):

  return val



def _validate_LEBEDEV_GRID(val,errorLog=[]):
  if utilities.is_integer(val) or (val is None):
    return val
  else:
    errorMessage = "LEBEDEV_GRID must be an integer."
    errorLog.append({'Date': datetime.datetime.now(), 'Type': 'init', 'Module': 'SUBSYS.KIND',
                     'Variable': 'LEBEDEV_GRID', 'ErrorMessage': errorMessage})
    raise TypeError
    
def _validate_ELEMENT(val,errorLog=[]):

  return val

def _validate_LMAX_DFTB(val,errorLog=[]):
  if utilities.is_integer(val) or (val is None):
    return val
  else:
    errorMessage = "LMAX_DFTB must be an integer."
    errorLog.append({'Date': datetime.datetime.now(), 'Type': 'init', 'Module': 'SUBSYS.KIND',
                     'Variable': 'LMAX_DFTB', 'ErrorMessage': errorMessage})
    raise TypeError
    
def _validate_ELEMENT(val,errorLog=[]):

  return val


def _validate_LRI_BASIS_SET(val,errorLog=[]):

  return val
def _validate_MAGNETIZATION(val,errorLog=[]):

  return val


def _validate_MAO(val,errorLog=[]):
  if utilities.is_integer(val) or (val is None):
    return val
  else:
    errorMessage = "MAO must be an integer."
    errorLog.append({'Date': datetime.datetime.now(), 'Type': 'init', 'Module': 'SUBSYS.KIND',
                     'Variable': 'MAO', 'ErrorMessage': errorMessage})
    raise TypeError
    
    
def _validate_MASS(val,errorLog=[]):

  return val


def _validate_MAX_RAD_LOCAL(val,errorLog=[]):

  return val
def _validate_MM_RADIUS(val,errorLog=[]):

  return val

def _validate_NO_OPTIMIZE(val,errorLog=[]):
  if val is not None:
    val = str(val).upper()
  
  if val in BOOL_VALS or (val is None):
        return val
  else:
    errorMessage = ("Invalid option for NO_OPTIMIZE: {}. Valid options are: {}".format(
                     val,BOOL_VALS))
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'SUBSYS.KIND',
                            'Variable':'NO_OPTIMIZE','ErrorMessage':errorMessage})
    raise TypeError 
    
def _validate_PAO_BASIS_SIZE(val,errorLog=[]):
  if utilities.is_integer(val) or (val is None):
    return val
  else:
    errorMessage = "PAO_BASIS_SIZE must be an integer."
    errorLog.append({'Date': datetime.datetime.now(), 'Type': 'init', 'Module': 'SUBSYS.KIND',
                     'Variable': 'PAO_BASIS_SIZE', 'ErrorMessage': errorMessage})
    raise TypeError
    
     
def _validate_POTENTIAL(val,errorLog=[]):

  return val


def _validate_POTENTIAL_FILE_NAME(val,errorLog=[]):

  return val
def _validate_POTENTIAL_TYPE(val,errorLog=[]):

  return val


def _validate_RADIAL_GRID(val,errorLog=[]):
  if utilities.is_integer(val) or (val is None):
    return val
  else:
    errorMessage = "RADIAL_GRID must be an integer."
    errorLog.append({'Date': datetime.datetime.now(), 'Type': 'init', 'Module': 'SUBSYS.KIND',
                     'Variable': 'RADIAL_GRID', 'ErrorMessage': errorMessage})
    raise TypeError





def _validate_RHO0_EXP_RADIUS(val,errorLog=[]):

  return val
def _validate_RI_AUX_BASIS_SET(val,errorLog=[]):

  return val



    
    
def _validate_SE_P_ORBITALS_ON_H(val,errorLog=[]):
  if val is not None:
    val = str(val).upper()
  
  if val in BOOL_VALS or (val is None):
        return val
  else:
    errorMessage = ("Invalid option for SE_P_ORBITALS_ON_H: {}. Valid options are: {}".format(
                     val,BOOL_VALS))
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'SUBSYS.KIND',
                            'Variable':'SE_P_ORBITALS_ON_H','ErrorMessage':errorMessage})
    raise TypeError 
    

    


class KINDs:

  def __init__(self,SECTION_PARAMETERS=None,AUX_BASIS_SET=None,AUX_FIT_BASIS_SET=None,BASIS_SET=None,CORE_CORRECTION=None,DFTB3_PARAM=None, ELEC_CONF=None, ELEMENT=None, FLOATING_BASIS_CENTER=None, GHOST=None, GPW_TYPE=None, HARD_EXP_RADIUS=None,KG_POTENTIAL=None, KG_POTENTIAL_FILE_NAME=None, LEBEDEV_GRID=None,LMAX_DFTB=None,LRI_BASIS_SET=None,MAGNETIZATION=None,MAO=None,MASS=None,MAX_RAD_LOCAL=None,MM_RADIUS=None,NO_OPTIMIZE=None,PAO_BASIS_SIZE=None,POTENTIAL=None,POTENTIAL_FILE_NAME=None,POTENTIAL_TYPE=None,RADIAL_GRID=None,RHO0_EXP_RADIUS=None,RI_AUX_BASIS_SET=None,SE_P_ORBITALS_ON_H=None,errorLog=[],changeLog=[],location="",number=None):
    self.__errorLog = errorLog
    self.__changeLog = changeLog
    self.__location  = "{}/KIND".format(location)
    self.__SECTION_PARAMETERS=_validate_SECTION_PARAMETERS(SECTION_PARAMETERS, errorLog=self.__errorLog)
    self.__AUX_BASIS_SET=_validate_AUX_BASIS_SET(AUX_BASIS_SET, errorLog=self.__errorLog)
    self.__AUX_FIT_BASIS_SET=_validate_AUX_FIT_BASIS_SET(AUX_FIT_BASIS_SET, errorLog=self.__errorLog)
    self.__BASIS_SET=_validate_BASIS_SET(BASIS_SET,errorLog=self.__errorLog)
    self.__CORE_CORRECTION=_validate_CORE_CORRECTION(CORE_CORRECTION,errorLog=self.__errorLog)
    self.__DFTB3_PARAM=_validate_DFTB3_PARAM(DFTB3_PARAM,errorLog=self.__errorLog)
    self.__ELEC_CONF=_validate_ELEC_CONF(ELEC_CONF,errorLog=self.__errorLog)
    self.__ELEMENT=_validate_ELEMENT(ELEMENT,errorLog=self.__errorLog)
    self.__FLOATING_BASIS_CENTER=_validate_FLOATING_BASIS_CENTER(FLOATING_BASIS_CENTER,errorLog=self.__errorLog)
    self.__GHOST=_validate_GHOST(GHOST,errorLog=self.__errorLog)
    self.__GPW_TYPE=_validate_GPW_TYPE(GPW_TYPE,errorLog=self.__errorLog)
    self.__HARD_EXP_RADIUS=_validate_HARD_EXP_RADIUS(HARD_EXP_RADIUS,errorLog=self.__errorLog)
    self.__KG_POTENTIAL=_validate_KG_POTENTIAL(KG_POTENTIAL,errorLog=self.__errorLog)
    self.__KG_POTENTIAL_FILE_NAME=_validate_KG_POTENTIAL_FILE_NAME(KG_POTENTIAL_FILE_NAME,errorLog=self.__errorLog)
    self.__LEBEDEV_GRID=_validate_LEBEDEV_GRID(LEBEDEV_GRID,errorLog=self.__errorLog)
    self.__LMAX_DFTB=_validate_LMAX_DFTB(LMAX_DFTB,errorLog=self.__errorLog)
    self.__LRI_BASIS_SET=_validate_LRI_BASIS_SET(LRI_BASIS_SET,errorLog=self.__errorLog)
    self.__MAGNETIZATION=_validate_MAGNETIZATION(MAGNETIZATION,errorLog=self.__errorLog)
    self.__MAO=_validate_MAO(MAO,errorLog=self.__errorLog)
    self.__MASS=_validate_MASS(MASS,errorLog=self.__errorLog)
    self.__MAX_RAD_LOCAL=_validate_MAX_RAD_LOCAL(MAX_RAD_LOCAL,errorLog=self.__errorLog)
    self.__MM_RADIUS=_validate_MM_RADIUS(MM_RADIUS,errorLog=self.__errorLog)
    self.__NO_OPTIMIZE=_validate_NO_OPTIMIZE(NO_OPTIMIZE,errorLog=self.__errorLog)
    self.__PAO_BASIS_SIZE=_validate_PAO_BASIS_SIZE(PAO_BASIS_SIZE,errorLog=self.__errorLog)
    self.__POTENTIAL=_validate_POTENTIAL(POTENTIAL,errorLog=self.__errorLog)
    
    self.__POTENTIAL_FILE_NAME=_validate_POTENTIAL_FILE_NAME(POTENTIAL_FILE_NAME,errorLog=self.__errorLog)
    self.__POTENTIAL_TYPE=_validate_POTENTIAL_TYPE(POTENTIAL_TYPE,errorLog=self.__errorLog)
    self.__RADIAL_GRID=_validate_RADIAL_GRID(RADIAL_GRID,errorLog=self.__errorLog)
    self.__RHO0_EXP_RADIUS=_validate_RHO0_EXP_RADIUS(RHO0_EXP_RADIUS,errorLog=self.__errorLog)
    self.__RI_AUX_BASIS_SET=_validate_RI_AUX_BASIS_SET(RI_AUX_BASIS_SET,errorLog=self.__errorLog)
    self.__SE_P_ORBITALS_ON_H=_validate_SE_P_ORBITALS_ON_H(SE_P_ORBITALS_ON_H,errorLog=self.__errorLog)

    
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
  def SECTION_PARAMETERS(self):
    return self.__SECTION_PARAMETERS

  @property
  def AUX_BASIS_SET(self):
    return self.__AUX_BASIS_SET

  @property
  def AUX_FIT_BASIS_SET(self):
    return self.__AUX_FIT_BASIS_SET

  @property
  def BASIS_SET(self):
    return self.__BASIS_SET

  @property
  def CORE_CORRECTION(self):
    return self.__CORE_CORRECTION

  @property
  def DFTB3_PARAM(self):
    return self.__DFTB3_PARAM




  @property
  def ELEC_CONF(self):
    return self.__ELEC_CONF

  @property
  def ELEMENT(self):
    return self.__ELEMENT

  @property
  def FLOATING_BASIS_CENTER(self):
    return self.__FLOATING_BASIS_CENTER

  @property
  def GHOST(self):
    return self.__GHOST

  @property
  def GPW_TYPE(self):
    return self.__GPW_TYPE

  @property
  def HARD_EXP_RADIUS(self):
    return self.__HARD_EXP_RADIUS

  @property
  def KG_POTENTIAL(self):
    return self.__KG_POTENTIAL

  @property
  def KG_POTENTIAL_FILE_NAME(self):
    return self.__KG_POTENTIAL_FILE_NAME

  @property
  def LEBEDEV_GRID(self):
    return self.__LEBEDEV_GRID

  @property
  def LMAX_DFTB(self):
    return self.__LMAX_DFTB

  @property
  def LRI_BASIS_SET(self):
    return self.__LRI_BASIS_SET

  @property
  def MAGNETIZATION(self):
    return self.__MAGNETIZATION

  @property
  def MAO(self):
    return self.__MAO

  @property
  def MASS(self):
    return self.__MASS

  @property
  def MAX_RAD_LOCAL(self):
    return self.__MAX_RAD_LOCAL

  @property
  def MM_RADIUS(self):
    return self.__MM_RADIUS

  @property
  def NO_OPTIMIZE(self):
    return self.__NO_OPTIMIZE

  @property
  def PAO_BASIS_SIZE(self):
    return self.__PAO_BASIS_SIZE

  @property
  def POTENTIAL(self):
    return self.__POTENTIAL

  @property
  def POTENTIAL_FILE_NAME(self):
    return self.__POTENTIAL_FILE_NAME



  @property
  def POTENTIAL_TYPE(self):
    return self.__POTENTIAL_TYPE

  @property
  def RADIAL_GRID(self):
    return self.__RADIAL_GRID



  @property
  def RHO0_EXP_RADIUS(self):
    return self.__RHO0_EXP_RADIUS

  @property
  def RI_AUX_BASIS_SET(self):
    return self.__RI_AUX_BASIS_SET



  @property
  def SE_P_ORBITALS_ON_H(self):
    return self.__SE_P_ORBITALS_ON_H






  @SECTION_PARAMETERS.setter
  def SECTION_PARAMETERS(self, val):
    
    
    self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SUBSYS.KIND', 'Variable': 'SECTION_PARAMETERS',
                               'Success': True, 'Previous': self.__SECTION_PARAMETERS, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
    self.__SECTION_PARAMETERS= val
    
    
    
  @AUX_BASIS_SET.setter
  def AUX_BASIS_SET(self, val):
    
    
    self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SUBSYS.KIND', 'Variable': 'AUX_BASIS_SET',
                               'Success': True, 'Previous': self.__AUX_BASIS_SET, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
    self.__AUX_BASIS_SET= val
    
    
    

  @AUX_FIT_BASIS_SET.setter
  def AUX_FIT_BASIS_SET(self, val):
    
    
    self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SUBSYS.KIND', 'Variable': 'AUX_FIT_BASIS_SET',
                               'Success': True, 'Previous': self.__AUX_FIT_BASIS_SET, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
    self.__AUX_FIT_BASIS_SET= val
    
    
  @BASIS_SET.setter
  def BASIS_SET(self, val):
    
    
    self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SUBSYS.KIND', 'Variable': 'BASIS_SET',
                               'Success': True, 'Previous': self.__BASIS_SET, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
    self.__BASIS_SET= val
    
    
    
  @CORE_CORRECTION.setter
  def CORE_CORRECTION(self, val):
    
    
    self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SUBSYS.KIND', 'Variable': 'CORE_CORRECTION',
                               'Success': True, 'Previous': self.__CORE_CORRECTION, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
    self.__CORE_CORRECTION= val
    
  @DFTB3_PARAM.setter
  def DFTB3_PARAM(self, val):
    
    
    self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SUBSYS.KIND', 'Variable': 'DFTB3_PARAM',
                               'Success': True, 'Previous': self.__DFTB3_PARAM, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
    self.__DFTB3_PARAM =val
    
    
  @ELEC_CONF.setter
  def ELEC_CONF(self, val):
    if utilities.is_integer(val):
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SUBSYS.KIND', 'Variable': 'ELEC_CONF',
                               'Success': True, 'Previous': self.__ELEC_CONF, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__ELEC_CONF = val
    else:
      errorMessage = "ELEC_CONF must be aN integer."
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SUBSYS.KIND', 'Variable': 'ELEC_CONF',
                               'Success': False, 'Previous': self.__ELEC_CONF, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'subsys.kind',
                              'Variable': 'ELEC_CONF', 'ErrorMessage': errorMessage,
                              'Location': self.__location})
    
  @ELEMENT.setter
  def ELEMENT(self, val):
    
    
    self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SUBSYS.KIND', 'Variable': 'ELEMENT',
                               'Success': True, 'Previous': self.__ELEMENT, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
    self.__ELEMENT =val
    
  @FLOATING_BASIS_CENTER.setter
  def FLOATING_BASIS_CENTER(self, val):
    val = str(val).upper()
    if val in BOOL_VALS:
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SUBSYS.KIND', 'Variable': 'FLOATING_BASIS_CENTER',
                               'Success': True, 'Previous': self.__FLOATING_BASIS_CENTER, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__FLOATING_BASIS_CENTER = val
    else:
      errorMessage = ("Invalid option for FLOATING_BASIS_CENTER: {}. Valid options are: {}".format(val, BOOL_VALS))
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SUBSYS.KIND', 'Variable': 'FLOATING_BASIS_CENTER',
                               'Success': False, 'Previous': self.__FLOATING_BASIS_CENTER, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'SUBSYS.KIND',
                              'Variable': ' FLOATING_BASIS_CENTER', 'ErrorMessage': errorMessage,
                              'Location': self.__location})  
    
  @GHOST.setter
  def GHOST(self, val):
    val = str(val).upper()
    if val in BOOL_VALS:
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SUBSYS.KIND', 'Variable': 'GHOST',
                               'Success': True, 'Previous': self.__GHOST, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__GHOST = val
    else:
      errorMessage = ("Invalid option for GHOST: {}. Valid options are: {}".format(val, BOOL_VALS))
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SUBSYS.KIND', 'Variable': 'GHOST',
                               'Success': False, 'Previous': self.__GHOST, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'SUBSYS.KIND',
                              'Variable': ' GHOST', 'ErrorMessage': errorMessage,
                              'Location': self.__location})  
    
  @GPW_TYPE.setter
  def GPW_TYPE(self, val):
    val = str(val).upper()
    if val in BOOL_VALS:
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SUBSYS.KIND', 'Variable': 'GPW_TYPE',
                               'Success': True, 'Previous': self.__GPW_TYPE, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__GPW_TYPE = val
    else:
      errorMessage = ("Invalid option for GPW_TYPE: {}. Valid options are: {}".format(val, BOOL_VALS))
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SUBSYS.KIND', 'Variable': 'GPW_TYPE',
                               'Success': False, 'Previous': self.__GPW_TYPE, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'SUBSYS.KIND',
                              'Variable': ' GPW_TYPE', 'ErrorMessage': errorMessage,
                              'Location': self.__location})  
       
    
  @HARD_EXP_RADIUS.setter
  def HARD_EXP_RADIUS(self, val):
    
    
    self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SUBSYS.KIND', 'Variable': 'HARD_EXP_RADIUS',
                               'Success': True, 'Previous': self.__HARD_EXP_RADIUS, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
    self.__HARD_EXP_RADIUS =val
    
    
  @KG_POTENTIAL.setter
  def KG_POTENTIAL(self, val):
    
    
    self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SUBSYS.KIND', 'Variable': 'KG_POTENTIAL',
                               'Success': True, 'Previous': self.__KG_POTENTIAL, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
    self.__KG_POTENTIAL =val
    
    
  @KG_POTENTIAL_FILE_NAME.setter
  def KG_POTENTIAL_FILE_NAME(self, val):
    
    
    self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SUBSYS.KIND', 'Variable': 'KG_POTENTIAL_FILE_NAME',
                               'Success': True, 'Previous': self.__KG_POTENTIAL_FILE_NAME, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
    self.__KG_POTENTIAL_FILE_NAME =val
    
    
 

   
  @LEBEDEV_GRID.setter
  def LEBEDEV_GRID(self, val):
    if utilities.is_integer(val):
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SUBSYS.KIND', 'Variable': 'LEBEDEV_GRID',
                               'Success': True, 'Previous': self.__LEBEDEV_GRID, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__LEBEDEV_GRID = val
    else:
      errorMessage = "LEBEDEV_GRID must be aN integer."
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SUBSYS.KIND', 'Variable': 'LEBEDEV_GRID',
                               'Success': False, 'Previous': self.__LEBEDEV_GRID, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'SUBSYS.KIND',
                              'Variable': 'LEBEDEV_GRID', 'ErrorMessage': errorMessage,
                              'Location': self.__location})
    
    
    
     
  @LMAX_DFTB.setter
  def LMAX_DFTB(self, val):
    if utilities.is_integer(val):
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SUBSYS.KIND', 'Variable': 'LMAX_DFTB',
                               'Success': True, 'Previous': self.__LMAX_DFTB, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__LMAX_DFTB = val
    else:
      errorMessage = "LMAX_DFTB must be aN integer."
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SUBSYS.KIND', 'Variable': 'LMAX_DFTB',
                               'Success': False, 'Previous': self.__LMAX_DFTB, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'SUBSYS.KIND',
                              'Variable': 'LMAX_DFTB', 'ErrorMessage': errorMessage,
                              'Location': self.__location})
    
    
    
    
  @LRI_BASIS_SET.setter
  def LRI_BASIS_SET(self, val):
    
    
    self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SUBSYS.KIND', 'Variable': 'LRI_BASIS_SET',
                               'Success': True, 'Previous': self.__LRI_BASIS_SET, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
    self.__LRI_BASIS_SET =val
    
    
    
     
  @MAGNETIZATION.setter
  def MAGNETIZATION(self, val):
    
    
    self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SUBSYS.KIND', 'Variable': 'MAGNETIZATION',
                               'Success': True, 'Previous': self.__MAGNETIZATION, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
    self.MAGNETIZATION =val
    
    
    
   


    
  @MAO.setter
  def MAO(self, val):
    if utilities.is_integer(val):
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SUBSYS.KIND', 'Variable': 'MAO',
                               'Success': True, 'Previous': self.__MAO, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__MAO = val
    else:
      errorMessage = "MAO must be aN integer."
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SUBSYS.KIND', 'Variable': 'MAO',
                               'Success': False, 'Previous': self.__MAO, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'subsys.kind',
                              'Variable': 'MAO', 'ErrorMessage': errorMessage,
                              'Location': self.__location})
    
    
  @MASS.setter
  def MASS(self, val):
    
    
    self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SUBSYS.KIND', 'Variable': 'MASS',
                               'Success': True, 'Previous': self.__MASS, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
    self.MASS =val
    
    
    
  @MAX_RAD_LOCAL.setter
  def MAX_RAD_LOCAL(self, val):
    
    
    self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SUBSYS.KIND', 'Variable': 'MAX_RAD_LOCAL',
                               'Success': True, 'Previous': self.__MAX_RAD_LOCAL, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
    self.MAX_RAD_LOCAL =val
    
  @MM_RADIUS.setter
  def MM_RADIUS(self, val):
    
    
    self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SUBSYS.KIND', 'Variable': 'MM_RADIUS',
                               'Success': True, 'Previous': self.__MM_RADIUS, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
    self.MM_RADIUS=val
    
    
  @NO_OPTIMIZE.setter
  def NO_OPTIMIZE(self, val):
    val = str(val).upper()
    if val in BOOL_VALS:
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SUBSYS.KIND', 'Variable': 'NO_OPTIMIZE',
                               'Success': True, 'Previous': self.__NO_OPTIMIZE, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__NO_OPTIMIZE = val
    else:
      errorMessage = ("Invalid option for NO_OPTIMIZE: {}. Valid options are: {}".format(val, BOOL_VALS))
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SUBSYS.KIND', 'Variable': 'NO_OPTIMIZE',
                               'Success': False, 'Previous': self.__NO_OPTIMIZE, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'SUBSYS.KIND',
                              'Variable': ' NO_OPTIMIZE', 'ErrorMessage': errorMessage,
                              'Location': self.__location})  
  @PAO_BASIS_SIZE.setter
  def PAO_BASIS_SIZE(self, val):
    if utilities.is_integer(val):
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SUBSYS.KIND', 'Variable': 'PAO_BASIS_SIZE',
                               'Success': True, 'Previous': self.__PAO_BASIS_SIZE, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__PAO_BASIS_SIZE = val
    else:
      errorMessage = "PAO_BASIS_SIZE must be aN integer."
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SUBSYS.KIND', 'Variable': 'PAO_BASIS_SIZE',
                               'Success': False, 'Previous': self.__PAO_BASIS_SIZE, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'subsys.kind',
                              'Variable': 'PAO_BASIS_SIZE', 'ErrorMessage': errorMessage,
                              'Location': self.__location})        
   
  @POTENTIAL.setter
  def POTENTIAL(self, val):
    
    
    self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SUBSYS.KIND', 'Variable': 'POTENTIAL',
                               'Success': True, 'Previous': self.__POTENTIAL, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
    self.__POTENTIAL =val

    
    
    
  @POTENTIAL_FILE_NAME.setter
  def POTENTIAL_FILE_NAME(self, val):
    
    
    self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SUBSYS.KIND', 'Variable': 'POTENTIAL_FILE_NAME',
                               'Success': True, 'Previous': self.__POTENTIAL_FILE_NAME, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
    self.POTENTIAL_FILE_NAME =val
    
  @POTENTIAL_TYPE.setter
  def POTENTIAL_TYPE(self, val):
    
    
    self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SUBSYS.KIND', 'Variable': 'POTENTIAL_TYPE',
                               'Success': True, 'Previous': self.__POTENTIAL_TYPE, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
    self.POTENTIAL_TYPE=val
    

  @RADIAL_GRID.setter
  def RADIAL_GRID(self, val):
    if utilities.is_integer(val):
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SUBSYS.KIND', 'Variable': 'RADIAL_GRID',
                               'Success': True, 'Previous': self.__RADIAL_GRID, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__RADIAL_GRID = val
    else:
      errorMessage = "RADIAL_GRID must be aN integer."
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SUBSYS.KIND', 'Variable': 'RADIAL_GRID',
                               'Success': False, 'Previous': self.__RADIAL_GRID, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'subsys.kind',
                              'Variable': 'RADIAL_GRID', 'ErrorMessage': errorMessage,
                              'Location': self.__location}) 
    
        
  @RHO0_EXP_RADIUS.setter
  def RHO0_EXP_RADIUS(self, val):
    
    
    self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SUBSYS.KIND', 'Variable': 'RHO0_EXP_RADIUS',
                               'Success': True, 'Previous': self.__RHO0_EXP_RADIUS, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
    self.RHO0_EXP_RADIUS =val
    
  @RI_AUX_BASIS_SET.setter
  def RI_AUX_BASIS_SET(self, val):
    
    
    self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SUBSYS.KIND', 'Variable': 'RI_AUX_BASIS_SET',
                               'Success': True, 'Previous': self.__RI_AUX_BASIS_SET, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
    self.RI_AUX_BASIS_SET=val
    


    
    
    
  @SE_P_ORBITALS_ON_H.setter
  def SE_P_ORBITALS_ON_H(self, val):
    val = str(val).upper()
    if val in BOOL_VALS:
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SUBSYS.KIND', 'Variable': 'SE_P_ORBITALS_ON_H',
                               'Success': True, 'Previous': self.__SE_P_ORBITALS_ON_H, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__SE_P_ORBITALS_ON_H = val
    else:
      errorMessage = ("Invalid option for SE_P_ORBITALS_ON_H: {}. Valid options are: {}".format(val, BOOL_VALS))
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SUBSYS.KIND', 'Variable': 'SE_P_ORBITALS_ON_H',
                               'Success': False, 'Previous': self.__SE_P_ORBITALS_ON_H, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'SUBSYS.KIND',
                              'Variable': ' SE_P_ORBITALS_ON_H', 'ErrorMessage': errorMessage,
                              'Location': self.__location})  
    
    
    