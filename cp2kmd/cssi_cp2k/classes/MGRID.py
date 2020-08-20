import datetime
import cssi_cp2k.utilities as utilities




BOOL_VALS   = [".TRUE.",".FALSE."]



def _validate_COMMENSURATE(val,errorLog=[]):
  if val is not None:
    val = str(val).upper()
  
  if val in BOOL_VALS or (val is None):
        return val
  else:
    errorMessage = ("Invalid option for COMMENSURATE: {}. Valid options are: {}".format(
                     val,BOOL_VALS))
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'DFT.MGRID',
                            'Variable':'COMMENSURATE','ErrorMessage':errorMessage})
    raise TypeError 
    
def _validate_CUTOFF(val,errorLog=[]):
  #if val is not None:
    #val = str(val).upper()

  #if val in SECTION_PARAMETERS_VALS or (val is None):
  return val

    
def _validate_MULTIGRID_CUTOFF(val,errorLog=[]):
  #if val is not None:
    #val = str(val).upper()

  #if val in SECTION_PARAMETERS_VALS or (val is None):
  return val


def _validate_MULTIGRID_SET(val,errorLog=[]):
  if val is not None:
    val = str(val).upper()
  
  if val in BOOL_VALS or (val is None):
        return val
  else:
    errorMessage = ("Invalid option for MULTIGRID_SET: {}. Valid options are: {}".format(
                     val,BOOL_VALS))
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'DFT.MGRID',
                            'Variable':'MULTIGRID_SET','ErrorMessage':errorMessage})
    raise TypeError 
    
def _validate_NGRIDS(val,errorLog=[]):
  if utilities.is_integer(val) or (val is None):
    return val
  else:
    errorMessage = "NGRIDS must be an integer."
    errorLog.append({'Date': datetime.datetime.now(), 'Type': 'init', 'Module': 'DFT.MGRID',
                     'Variable': 'NGRIDS', 'ErrorMessage': errorMessage})
    raise TypeError
    
def _validate_PROGRESSION_FACTOR(val,errorLog=[]):
  #if val is not None:
    #val = str(val).upper()

  #if val in SECTION_PARAMETERS_VALS or (val is None):
  return val


def _validate_REALSPACE(val,errorLog=[]):
  if val is not None:
    val = str(val).upper()
  
  if val in BOOL_VALS or (val is None):
        return val
  else:
    errorMessage = ("Invalid option for REALSPACE: {}. Valid options are: {}".format(
                     val,BOOL_VALS))
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'DFT.MGRID',
                            'Variable':'REALSPACE','ErrorMessage':errorMessage})
    raise TypeError 
    
    
def _validate_REL_CUTOFF(val,errorLog=[]):
  #if val is not None:
    #val = str(val).upper()

  #if val in SECTION_PARAMETERS_VALS or (val is None):
  return val



def _validate_SKIP_LOAD_BALANCE_DISTRIBUTED(val,errorLog=[]):
  if val is not None:
    val = str(val).upper()
  
  if val in BOOL_VALS or (val is None):
        return val
  else:
    errorMessage = ("Invalid option for SKIP_LOAD_BALANCE_DISTRIBUTED: {}. Valid options are: {}".format(
                     val,BOOL_VALS))
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'DFT.MGRID',
                            'Variable':'SKIP_LOAD_BALANCE_DISTRIBUTED','ErrorMessage':errorMessage})
    raise TypeError

 

class MGRID:

  def __init__(self,COMMENSURATE=None,CUTOFF=None,MULTIGRID_CUTOFF=None,MULTIGRID_SET=None,NGRIDS=None,PROGRESSION_FACTOR=None, REALSPACE=None, REL_CUTOFF=None, SKIP_LOAD_BALANCE_DISTRIBUTED=None, errorLog=[],changeLog=[],location=""):
    self.__errorLog = errorLog
    self.__changeLog = changeLog
    self.__location  = "{}/MGRID".format(location)
    self.__COMMENSURATE=_validate_COMMENSURATE(COMMENSURATE, errorLog=self.__errorLog)
    self.__CUTOFF=_validate_CUTOFF(CUTOFF, errorLog=self.__errorLog)
    self.__MULTIGRID_CUTOFF=_validate_MULTIGRID_CUTOFF(MULTIGRID_CUTOFF, errorLog=self.__errorLog)
    self.__MULTIGRID_SET=_validate_MULTIGRID_SET(MULTIGRID_SET,errorLog=self.__errorLog)
    self.__NGRIDS=_validate_NGRIDS(NGRIDS,errorLog=self.__errorLog)
    self.__PROGRESSION_FACTOR=_validate_PROGRESSION_FACTOR(PROGRESSION_FACTOR,errorLog=self.__errorLog)
    self.__REALSPACE=_validate_REALSPACE(REALSPACE,errorLog=self.__errorLog)
    self.__REL_CUTOFF=_validate_REL_CUTOFF(REL_CUTOFF,errorLog=self.__errorLog)
    self.__SKIP_LOAD_BALANCE_DISTRIBUTED=_validate_SKIP_LOAD_BALANCE_DISTRIBUTED(SKIP_LOAD_BALANCE_DISTRIBUTED,errorLog=self.__errorLog)
    
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
  def COMMENSURATE(self):
    return self.__COMMENSURATE

  @property
  def MULTIGRID_CUTOFF(self):
    return self.__MULTIGRID_CUTOFF

  @property
  def CUTOFF(self):
    return self.__CUTOFF

  @property
  def MULTIGRID_SET(self):
    return self.__MULTIGRID_SET

  @property
  def NGRIDS(self):
    return self.__NGRIDS

  @property
  def PROGRESSION_FACTOR(self):
    return self.__PROGRESSION_FACTOR




  @property
  def REALSPACE(self):
    return self.__REALSPACE

  @property
  def REL_CUTOFF(self):
    return self.__REL_CUTOFF

  @property
  def SKIP_LOAD_BALANCE_DISTRIBUTED(self):
    return self.__SKIP_LOAD_BALANCE_DISTRIBUTED

    
    
    
  @COMMENSURATE.setter
  def COMMENSURATE(self, val):
    val = str(val).upper()
    if val in BOOL_VALS:
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT.MGRID', 'Variable': 'COMMENSURATE',
                               'Success': True, 'Previous': self.__COMMENSURATE, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__COMMENSURATE = val
    else:
      errorMessage = ("Invalid option for COMMENSURATE: {}. Valid options are: {}".format(val, BOOL_VALS))
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT.MGRID', 'Variable': 'COMMENSURATE',
                               'Success': False, 'Previous': self.__COMMENSURATE, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'DFT.MGRID',
                              'Variable': ' COMMENSURATE', 'ErrorMessage': errorMessage,
                              'Location': self.__location})
    
    
    

  @CUTOFF.setter
  def CUTOFF(self, val):
    
    
    self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT.GRID', 'Variable': 'CUTOFF',
                               'Success': True, 'Previous': self.__CUTOFF, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
    self.__CUTOFF= val
    
    

  @MULTIGRID_CUTOFF.setter
  def MULTIGRID_CUTOFF(self, val):
    
    
    self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT.GRID', 'Variable': 'MULTIGRID_CUTOFF',
                               'Success': True, 'Previous': self.__MULTIGRID_CUTOFF, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
    self.__MULTIGRID_CUTOFF= val

  @MULTIGRID_SET.setter
  def MULTIGRID_SET(self, val):
    val = str(val).upper()
    if val in BOOL_VALS:
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT.MGRID', 'Variable': 'MULTIGRID_SET',
                               'Success': True, 'Previous': self.__MULTIGRID_SET, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__MULTIGRID_SET = val
    else:
      errorMessage = ("Invalid option for MULTIGRID_SET: {}. Valid options are: {}".format(val, BOOL_VALS))
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT.MGRID', 'Variable': 'MULTIGRID_SET',
                               'Success': False, 'Previous': self.__MULTIGRID_SET, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'DFT.MGRID',
                              'Variable': ' MULTIGRID_SET', 'ErrorMessage': errorMessage,
                              'Location': self.__location})
    
    
    
    
  @NGRIDS.setter
  def NGRIDS(self, val):
    if utilities.is_integer(val):
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT.MGRID', 'Variable': 'NGRIDS',
                               'Success': True, 'Previous': self.__NGRIDS, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__NGRIDS = val
    else:
      errorMessage = "NGRIDS must be aN integer."
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT.MGRID', 'Variable': 'NGRIDS',
                               'Success': False, 'Previous': self.__NGRIDS, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'DFT.MGRID',
                              'Variable': 'NGRIDS', 'ErrorMessage': errorMessage,
                              'Location': self.__location})
    
  @PROGRESSION_FACTOR.setter
  def PROGRESSION_FACTOR(self, val):
    
    
    self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT.GRID', 'Variable': 'PROGRESSION_FACTOR',
                               'Success': True, 'Previous': self.__PROGRESSION_FACTOR, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
    self.__PROGRESSION_FACTOR= val

  @REALSPACE.setter
  def REALSPACE(self, val):
    val = str(val).upper()
    if val in BOOL_VALS:
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT.MGRID', 'Variable': 'REALSPACE',
                               'Success': True, 'Previous': self.__REALSPACE, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__REALSPACE = val
    else:
      errorMessage = ("Invalid option for REALSPACE: {}. Valid options are: {}".format(val, BOOL_VALS))
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT.MGRID', 'Variable': 'REALSPACE',
                               'Success': False, 'Previous': self.__REALSPACE, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'DFT.MGRID',
                              'Variable': ' REALSPACE', 'ErrorMessage': errorMessage,
                              'Location': self.__location})
  @REL_CUTOFF.setter
  def REL_CUTOFF(self, val):
    
    
    self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT.GRID', 'Variable': 'REL_CUTOFF',
                               'Success': True, 'Previous': self.__REL_CUTOFF, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
    self.__REL_CUTOFF= val    
    
  @SKIP_LOAD_BALANCE_DISTRIBUTED.setter
  def SKIP_LOAD_BALANCE_DISTRIBUTED(self, val):
    val = str(val).upper()
    if val in BOOL_VALS:
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT.MGRID', 'Variable': 'SKIP_LOAD_BALANCE_DISTRIBUTED',
                               'Success': True, 'Previous': self.__SKIP_LOAD_BALANCE_DISTRIBUTED, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__SKIP_LOAD_BALANCE_DISTRIBUTED = val
    else:
      errorMessage = ("Invalid option for SKIP_LOAD_BALANCE_DISTRIBUTED: {}. Valid options are: {}".format(val, BOOL_VALS))
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT.MGRID', 'Variable': 'SKIP_LOAD_BALANCE_DISTRIBUTED',
                               'Success': False, 'Previous': self.__SKIP_LOAD_BALANCE_DISTRIBUTED, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'DFT.MGRID',
                              'Variable': ' SKIP_LOAD_BALANCE_DISTRIBUTED', 'ErrorMessage': errorMessage,
                              'Location': self.__location})
