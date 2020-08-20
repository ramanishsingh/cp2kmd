import datetime
import cssi_cp2k.utilities as utilities






BOOL_VALS   = [".TRUE.",".FALSE"]
TYPE_VALS=['DFTD2','DFTD3','DFTD3(BJ)'];




    
def _validate_ATOMPARM(val,errorLog=[]):
  #if val is not None:
    #val = str(val).upper()

  #if val in SECTION_PARAMETERS_VALS or (val is None):
  return val

def _validate_ATOM_COORDINATION_NUMBERS(val,errorLog=[]):
  #if val is not None:
    #val = str(val).upper()

  #if val in SECTION_PARAMETERS_VALS or (val is None):
  return val

def _validate_CALCULATE_C9_TERM(val,errorLog=[]):
  if val is not None:
    val = str(val).upper()
  
  if val in BOOL_VALS or (val is None):
        return val
  else:
    errorMessage = ("Invalid option for CALCULATE_C9_TERM: {}. Valid options are: {}".format(
                     val,BOOL_VALS))
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'XC/VDW_POTENTIAL/PAIR_POTENTIAL',
                            'Variable':'CALCULATE_C9_TERM','ErrorMessage':errorMessage})
    raise TypeError
    
def _validate_D3BJ_SCALING(val,errorLog=[]):
  #if val is not None:
    #val = str(val).upper()

  #if val in SECTION_PARAMETERS_VALS or (val is None):
  return val

def _validate_D3_EXCLUDE_KIND(val,errorLog=[]):
  if utilities.is_integer(val) or (val is None):
    return val
  else:
    errorMessage = "D3_EXCLUDE_KIND must be an integer."
    errorLog.append({'Date': datetime.datetime.now(), 'Type': 'init', 'Module': 'XC/VDW_POTENTIAL/PAIR_POTENTIAL',
                     'Variable': 'D3_EXCLUDE_KIND', 'ErrorMessage': errorMessage})
    raise TypeError
    
def _validate_D3_SCALING(val,errorLog=[]):
  #if val is not None:
    #val = str(val).upper()

  #if val in SECTION_PARAMETERS_VALS or (val is None):
  return val   
    
def _validate_EPS_CN(val,errorLog=[]):
  #if val is not None:
    #val = str(val).upper()

  #if val in SECTION_PARAMETERS_VALS or (val is None):
  return val 

def _validate_EXP_PRE(val,errorLog=[]):
  #if val is not None:
    #val = str(val).upper()

  #if val in SECTION_PARAMETERS_VALS or (val is None):
  return val   

def _validate_KIND_COORDINATION_NUMBERS(val,errorLog=[]):
  #if val is not None:
    #val = str(val).upper()

  #if val in SECTION_PARAMETERS_VALS or (val is None):
  return val     



def _validate_LONG_RANGE_CORRECTION(val,errorLog=[]):
  if val is not None:
    val = str(val).upper()
  
  if val in BOOL_VALS or (val is None):
        return val
  else:
    errorMessage = ("Invalid option for LONG_RANGE_CORRECTION: {}. Valid options are: {}".format(
                     val,BOOL_VALS))
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'XC/VDW_POTENTIAL/PAIR_POTENTIAL',
                            'Variable':'LONG_RANGE_CORRECTION','ErrorMessage':errorMessage})
    raise TypeError
    
def _validate_MOLECULE_CORRECTION(val,errorLog=[]):
  if val is not None:
    val = str(val).upper()
  
  if val in BOOL_VALS or (val is None):
        return val
  else:
    errorMessage = ("Invalid option for MOLECULE_CORRECTION: {}. Valid options are: {}".format(
                     val,BOOL_VALS))
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'XC/VDW_POTENTIAL/PAIR_POTENTIAL',
                            'Variable':'MOLECULE_CORRECTION','ErrorMessage':errorMessage})
    raise TypeError
    
    
def _validate_MOLECULE_CORRECTION_C8(val,errorLog=[]):
  #if val is not None:
    #val = str(val).upper()

  #if val in SECTION_PARAMETERS_VALS or (val is None):
  return val

def _validate_PARAMETER_FILE_NAME(val,errorLog=[]):
  #if val is not None:
    #val = str(val).upper()

  #if val in SECTION_PARAMETERS_VALS or (val is None):
  return val
    
def _validate_REFERENCE_C9_TERM(val,errorLog=[]):
  if val is not None:
    val = str(val).upper()
  
  if val in BOOL_VALS or (val is None):
        return val
  else:
    errorMessage = ("Invalid option for REFERENCE_C9_TERM: {}. Valid options are: {}".format(
                     val,BOOL_VALS))
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'XC/VDW_POTENTIAL/PAIR_POTENTIAL',
                            'Variable':'REFERENCE_C9_TERM','ErrorMessage':errorMessage})
    raise TypeError
    
def _validate_REFERENCE_FUNCTIONAL(val,errorLog=[]):
  #if val is not None:
    #val = str(val).upper()

  #if val in SECTION_PARAMETERS_VALS or (val is None):
  return val    

def _validate_R_CUTOFF(val,errorLog=[]):
  #if val is not None:
    #val = str(val).upper()

  #if val in SECTION_PARAMETERS_VALS or (val is None):
  return val    

def _validate_SCALING(val,errorLog=[]):
  #if val is not None:
    #val = str(val).upper()

  #if val in SECTION_PARAMETERS_VALS or (val is None):
  return val 

def _validate_SHORT_RANGE_CORRECTION(val,errorLog=[]):
  if val is not None:
    val = str(val).upper()
  
  if val in BOOL_VALS or (val is None):
        return val
  else:
    errorMessage = ("Invalid option for SHORT_RANGE_CORRECTION: {}. Valid options are: {}".format(
                     val,BOOL_VALS))
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'XC/VDW_POTENTIAL/PAIR_POTENTIAL',
                            'Variable':'SHORT_RANGE_CORRECTION','ErrorMessage':errorMessage})
    raise TypeError
    
def _validate_SHORT_RANGE_CORRECTION_PARAMETERS(val,errorLog=[]):
  #if val is not None:
    #val = str(val).upper()

  #if val in SECTION_PARAMETERS_VALS or (val is None):
  return val 

def _validate_TYPE(val,errorLog=[]):
  if val is not None:
    val = str(val).upper()
  
  if val in TYPE_VALS or (val is None):
        return val
  else:
    errorMessage = ("Invalid option for TYPE: {}. Valid options are: {}".format(
                     val,TYPE_VALS))
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'XC/VDW_POTENTIAL/PAIR_POTENTIAL',
                            'Variable':'TYPE','ErrorMessage':errorMessage})
    raise TypeError
    
    
    
def _validate_VERBOSE_OUTPUT(val,errorLog=[]):
  if val is not None:
    val = str(val).upper()
  
  if val in BOOL_VALS or (val is None):
        return val
  else:
    errorMessage = ("Invalid option for VERBOSE_OUTPUT: {}. Valid options are: {}".format(
                     val,BOOL_VALS))
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'XC/VDW_POTENTIAL/PAIR_POTENTIAL',
                            'Variable':'VERBOSE_OUTPUT','ErrorMessage':errorMessage})
    raise TypeError
    
    
    
    
    





class PAIR_POTENTIAL:

  def __init__(self,ATOMPARM=None,ATOM_COORDINATION_NUMBERS=None,CALCULATE_C9_TERM=None,D3BJ_SCALING=None,D3_EXCLUDE_KIND=None,D3_SCALING=None, EPS_CN=None, EXP_PRE=None, KIND_COORDINATION_NUMBERS=None, LONG_RANGE_CORRECTION=None, MOLECULE_CORRECTION=None, MOLECULE_CORRECTION_C8=None,PARAMETER_FILE_NAME=None, REFERENCE_C9_TERM=None,REFERENCE_FUNCTIONAL=None,R_CUTOFF=None,SCALING=None,SHORT_RANGE_CORRECTION=None,SHORT_RANGE_CORRECTION_PARAMETERS=None, TYPE=None,VERBOSE_OUTPUT=None,errorLog=[],changeLog=[],location=""):
    self.__errorLog = errorLog
    self.__changeLog = changeLog
    self.__location  = "{}/PAIR_POTENTIAL".format(location)
    self.__ATOMPARM=_validate_ATOMPARM(ATOMPARM, errorLog=self.__errorLog)
    self.__ATOM_COORDINATION_NUMBERS=_validate_ATOM_COORDINATION_NUMBERS(ATOM_COORDINATION_NUMBERS, errorLog=self.__errorLog)
    self.__CALCULATE_C9_TERM=_validate_CALCULATE_C9_TERM(CALCULATE_C9_TERM, errorLog=self.__errorLog)
    self.__D3BJ_SCALING=_validate_D3BJ_SCALING(D3BJ_SCALING,errorLog=self.__errorLog)
    self.__D3_EXCLUDE_KIND=_validate_D3_EXCLUDE_KIND(D3_EXCLUDE_KIND,errorLog=self.__errorLog)
    self.__D3_SCALING=_validate_D3_SCALING(D3_SCALING,errorLog=self.__errorLog)
    self.__EPS_CN=_validate_EPS_CN(EPS_CN,errorLog=self.__errorLog)
    self.__EXP_PRE=_validate_EXP_PRE(EXP_PRE,errorLog=self.__errorLog)
    self.__KIND_COORDINATION_NUMBERS=_validate_KIND_COORDINATION_NUMBERS(KIND_COORDINATION_NUMBERS,errorLog=self.__errorLog)
    self.__LONG_RANGE_CORRECTION=_validate_LONG_RANGE_CORRECTION(LONG_RANGE_CORRECTION,errorLog=self.__errorLog)
    self.__MOLECULE_CORRECTION=_validate_MOLECULE_CORRECTION(MOLECULE_CORRECTION,errorLog=self.__errorLog)
    self.__MOLECULE_CORRECTION_C8=_validate_MOLECULE_CORRECTION_C8(MOLECULE_CORRECTION_C8,errorLog=self.__errorLog)
    self.__PARAMETER_FILE_NAME=_validate_PARAMETER_FILE_NAME(PARAMETER_FILE_NAME,errorLog=self.__errorLog)
    self.__REFERENCE_C9_TERM=_validate_REFERENCE_C9_TERM(REFERENCE_C9_TERM,errorLog=self.__errorLog)
    self.__REFERENCE_FUNCTIONAL=_validate_REFERENCE_FUNCTIONAL(REFERENCE_FUNCTIONAL,errorLog=self.__errorLog)
    self.__R_CUTOFF=_validate_R_CUTOFF(R_CUTOFF,errorLog=self.__errorLog)
    self.__SCALING=_validate_SCALING(SCALING,errorLog=self.__errorLog)
    self.__SHORT_RANGE_CORRECTION=_validate_SHORT_RANGE_CORRECTION(SHORT_RANGE_CORRECTION,errorLog=self.__errorLog)
    self.__SHORT_RANGE_CORRECTION_PARAMETERS=_validate_SHORT_RANGE_CORRECTION_PARAMETERS(SHORT_RANGE_CORRECTION_PARAMETERS,errorLog=self.__errorLog)
    self.__TYPE=_validate_TYPE(TYPE,errorLog=self.__errorLog)
    self.__VERBOSE_OUTPUT=_validate_VERBOSE_OUTPUT(VERBOSE_OUTPUT,errorLog=self.__errorLog)
 
    
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
  def ATOMPARM(self):
    return self.__ATOMPARM

  @property
  def ATOM_COORDINATION_NUMBERS(self):
    return self.__ATOM_COORDINATION_NUMBERS

  @property
  def CALCULATE_C9_TERM(self):
    return self.__CALCULATE_C9_TERM

  @property
  def D3BJ_SCALING(self):
    return self.__D3BJ_SCALING

  @property
  def D3_EXCLUDE_KIND(self):
    return self.__D3_EXCLUDE_KIND

  @property
  def D3_SCALING(self):
    return self.__D3_SCALING




  @property
  def EPS_CN(self):
    return self.__EPS_CN

  @property
  def EXP_PRE(self):
    return self.__EXP_PRE

  @property
  def KIND_COORDINATION_NUMBERS(self):
    return self.__KIND_COORDINATION_NUMBERS

  @property
  def LONG_RANGE_CORRECTION(self):
    return self.__LONG_RANGE_CORRECTION

  @property
  def MOLECULE_CORRECTION(self):
    return self.__MOLECULE_CORRECTION

  @property
  def MOLECULE_CORRECTION_C8(self):
    return self.__MOLECULE_CORRECTION_C8

  @property
  def PARAMETER_FILE_NAME(self):
    return self.__PARAMETER_FILE_NAME

  @property
  def REFERENCE_C9_TERM(self):
    return self.__REFERENCE_C9_TERM
  @property
  def REFERENCE_FUNCTIONAL(self):
    return self.__REFERENCE_FUNCTIONAL
  @property
  def R_CUTOFF(self):
    return self.__R_CUTOFF
  @property
  def SCALING(self):
    return self.__SCALING
  @property
  def SHORT_RANGE_CORRECTION(self):
    return self.__SHORT_RANGE_CORRECTION
  @property
  def SHORT_RANGE_CORRECTION_PARAMETERS(self):
    return self.__SHORT_RANGE_CORRECTION_PARAMETERS
  @property
  def TYPE(self):
    return self.__TYPE

  @property
  def VERBOSE_OUTPUT(self):
      return self.__VERBOSE_OUTPUT
    
  

  @ATOMPARM.setter
  def ATOMPARM(self, val):
    
    
    self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT.XC.VDW_POT.PAIR_POT', 'Variable': 'ATOMPARM',
                               'Success': True, 'Previous': self.__ATOMPARM, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
    self.__ATOMPARM= val
    
  @ATOMPARM.setter
  def ATOM_COORDINATION_NUMBERS(self, val):
    
    
    self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT.XC.VDW_POT.PAIR_POT', 'Variable': 'ATOM_COORDINATION_NUMBERS',
                               'Success': True, 'Previous': self.__ATOM_COORDINATION_NUMBERS, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
    self.__ATOM_COORDINATION_NUMBERS= val
    
    
  @CALCULATE_C9_TERM.setter
  def CALCULATE_C9_TERM(self, val):
    val = str(val).upper()
    if val in BOOL_VALS:
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT.XC.VDW_POT.PAIR_POT', 'Variable': 'CALCULATE_C9_TERM',
                               'Success': True, 'Previous': self.__CALCULATE_C9_TERM, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__CALCULATE_C9_TERM = val
    else:
      errorMessage = ("Invalid option for CALCULATE_C9_TERM: {}. Valid options are: {}".format(val, BOOL_VALS))
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT.XC.VDW_POT.PAIR_POT', 'Variable': 'CALCULATE_C9_TERM',
                               'Success': False, 'Previous': self.__CALCULATE_C9_TERM, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'DFT.XC.VDW_POT.PAIR_POT',
                              'Variable': ' CALCULATE_C9_TERM', 'ErrorMessage': errorMessage,
                              'Location': self.__location}) 
    

    
    
  @D3BJ_SCALING.setter
  def D3BJ_SCALING(self, val):
    
    
    self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT.XC.VDW_POT.PAIR_POT', 'Variable': 'D3BJ_SCALING',
                               'Success': True, 'Previous': self.__D3BJ_SCALING, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
    self.__D3BJ_SCALING= val 
    
    
  @D3_EXCLUDE_KIND.setter
  def D3_EXCLUDE_KIND(self, val):
    if utilities.is_integer(val):
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT.XC.VDW_POT.PAIR_POT', 'Variable': 'D3_EXCLUDE_KIND',
                               'Success': True, 'Previous': self.__D3_EXCLUDE_KIND, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__D3_EXCLUDE_KIND = val
    else:
      errorMessage = "D3_EXCLUDE_KIND must be aN integer."
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT.XC.VDW_POT.PAIR_POT', 'Variable': 'D3_EXCLUDE_KIND',
                               'Success': False, 'Previous': self.__D3_EXCLUDE_KIND, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'DFT.XC.VDW_POT.PAIR_POT',
                              'Variable': 'D3_EXCLUDE_KIND', 'ErrorMessage': errorMessage,
                              'Location': self.__location})
    
  @D3_SCALING.setter
  def D3_SCALING(self, val):
    
    
    self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT.XC.VDW_POT.PAIR_POT', 'Variable': 'D3_SCALING',
                               'Success': True, 'Previous': self.__D3_SCALING, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
    self.__D3_SCALING= val 
    
  @EPS_CN.setter
  def EPS_CN(self, val):
    
    
    self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT.XC.VDW_POT.PAIR_POT', 'Variable': 'EPS_CN',
                               'Success': True, 'Previous': self.__EPS_CN, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
    self.__EPS_CN= val   
    
  @EXP_PRE.setter
  def EXP_PRE(self, val):
    
    
    self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT.XC.VDW_POT.PAIR_POT', 'Variable': 'EXP_PRE',
                               'Success': True, 'Previous': self.__EXP_PRE, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
    self.__EXP_PRE= val     
    

  @KIND_COORDINATION_NUMBERS.setter
  def KIND_COORDINATION_NUMBERS(self, val):
    
    
    self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT', 'Variable': 'KIND_COORDINATION_NUMBERS',
                               'Success': True, 'Previous': self.__KIND_COORDINATION_NUMBERS, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
    self.__KIND_COORDINATION_NUMBERS= val

  @LONG_RANGE_CORRECTION.setter
  def LONG_RANGE_CORRECTION(self, val):
    val = str(val).upper()
    if val in BOOL_VALS:
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT.XC.VDW_POT.PAIR_POT', 'Variable': 'LONG_RANGE_CORRECTION',
                               'Success': True, 'Previous': self.__LONG_RANGE_CORRECTION, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__LONG_RANGE_CORRECTION = val
    else:
      errorMessage = ("Invalid option for LONG_RANGE_CORRECTION: {}. Valid options are: {}".format(val, BOOL_VALS))
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT.XC.VDW_POT.PAIR_POT', 'Variable': 'LONG_RANGE_CORRECTION',
                               'Success': False, 'Previous': self.__LONG_RANGE_CORRECTION, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'DFT.XC.VDW_POT.PAIR_POT',
                              'Variable': ' LONG_RANGE_CORRECTION', 'ErrorMessage': errorMessage,
                              'Location': self.__location}) 
    
  @MOLECULE_CORRECTION.setter
  def MOLECULE_CORRECTION(self, val):
    val = str(val).upper()
    if val in BOOL_VALS:
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT.XC.VDW_POT.PAIR_POT', 'Variable': 'MOLECULE_CORRECTION',
                               'Success': True, 'Previous': self.__MOLECULE_CORRECTION, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__MOLECULE_CORRECTION = val
    else:
      errorMessage = ("Invalid option for MOLECULE_CORRECTION: {}. Valid options are: {}".format(val, BOOL_VALS))
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT.XC.VDW_POT.PAIR_POT', 'Variable': 'MOLECULE_CORRECTION',
                               'Success': False, 'Previous': self.__MOLECULE_CORRECTION, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'DFT.XC.VDW_POT.PAIR_POT',
                              'Variable': ' MOLECULE_CORRECTION', 'ErrorMessage': errorMessage,
                              'Location': self.__location}) 
    
  @MOLECULE_CORRECTION_C8.setter
  def MOLECULE_CORRECTION_C8(self, val):
    
    
    self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT.XC.VDW_POT.PAIR_POT', 'Variable': 'MOLECULE_CORRECTION_C8',
                               'Success': True, 'Previous': self.__MOLECULE_CORRECTION_C8, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
    self.__MOLECULE_CORRECTION_C8= val  
    
  @PARAMETER_FILE_NAME.setter
  def PARAMETER_FILE_NAME(self, val):
    
    
    self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT.XC.VDW_POT.PAIR_POT', 'Variable': 'PARAMETER_FILE_NAME',
                               'Success': True, 'Previous': self.__PARAMETER_FILE_NAME, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
    self.__PARAMETER_FILE_NAME= val    
    
    
    
  @REFERENCE_C9_TERM.setter
  def REFERENCE_C9_TERM(self, val):
    val = str(val).upper()
    if val in BOOL_VALS:
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT.XC.VDW_POT.PAIR_POT', 'Variable': 'REFERENCE_C9_TERM',
                               'Success': True, 'Previous': self.__REFERENCE_C9_TERM, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__REFERENCE_C9_TERM = val
    else:
      errorMessage = ("Invalid option for REFERENCE_C9_TERM: {}. Valid options are: {}".format(val, BOOL_VALS))
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT.XC.VDW_POT.PAIR_POT', 'Variable': 'REFERENCE_C9_TERM',
                               'Success': False, 'Previous': self.__REFERENCE_C9_TERM, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'DFT.XC.VDW_POT.PAIR_POT',
                              'Variable': ' REFERENCE_C9_TERM', 'ErrorMessage': errorMessage,
                              'Location': self.__location}) 
    
  @REFERENCE_FUNCTIONAL.setter
  def REFERENCE_FUNCTIONAL(self, val):
    
    
    self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT.XC.VDW_POT.PAIR_POT', 'Variable': 'REFERENCE_FUNCTIONAL',
                               'Success': True, 'Previous': self.__REFERENCE_FUNCTIONAL, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
    self.__REFERENCE_FUNCTIONAL= val   
    
  @R_CUTOFF.setter
  def R_CUTOFF(self, val):
    
    
    self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT.XC.VDW_POT.PAIR_POT', 'Variable': 'R_CUTOFF',
                               'Success': True, 'Previous': self.__R_CUTOFF, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
    self.__R_CUTOFF= val 
    
        
  @SCALING.setter
  def SCALING(self, val):
    
    
    self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT.XC.VDW_POT.PAIR_POT', 'Variable': 'SCALING',
                               'Success': True, 'Previous': self.__SCALING, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
    self.__SCALING= val
       
   


    
  @SHORT_RANGE_CORRECTION.setter
  def SHORT_RANGE_CORRECTION(self, val):
    val = str(val).upper()
    if val in BOOL_VALS:
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT.XC.VDW_POT.PAIR_POT', 'Variable': 'SHORT_RANGE_CORRECTION',
                               'Success': True, 'Previous': self.__SHORT_RANGE_CORRECTION, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__SHORT_RANGE_CORRECTION = val
    else:
      errorMessage = ("Invalid option for SHORT_RANGE_CORRECTION: {}. Valid options are: {}".format(val, BOOL_VALS))
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT.XC.VDW_POT.PAIR_POT', 'Variable': 'SHORT_RANGE_CORRECTION',
                               'Success': False, 'Previous': self.__SHORT_RANGE_CORRECTION, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'DFT.XC.VDW_POT.PAIR_POT',
                              'Variable': ' SHORT_RANGE_CORRECTION', 'ErrorMessage': errorMessage,
                              'Location': self.__location}) 
   

  @SHORT_RANGE_CORRECTION_PARAMETERS.setter
  def SHORT_RANGE_CORRECTION_PARAMETERS(self, val):
    
    
    self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT.XC.VDW_POT.PAIR_POT', 'Variable': 'SHORT_RANGE_CORRECTION_PARAMETERS',
                               'Success': True, 'Previous': self.__SHORT_RANGE_CORRECTION_PARAMETERS, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
    self.__SHORT_RANGE_CORRECTION_PARAMETERS= val
    
 

  @TYPE.setter
  def TYPE(self, val):
    val = str(val).upper()
    if val in TYPE_VALS:
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT.XC.VDW_POT.PAIR_POT', 'Variable': 'TYPE',
                               'Success': True, 'Previous': self.__TYPE, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__TYPE = val
    else:
      errorMessage = ("Invalid option for TYPE: {}. Valid options are: {}".format(val, BTYPE_VALS))
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT.XC.VDW_POT.PAIR_POT', 'Variable': 'TYPE',
                               'Success': False, 'Previous': self.__TYPE, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'DFT.XC.VDW_POT.PAIR_POT',
                              'Variable': ' TYPE', 'ErrorMessage': errorMessage,
                              'Location': self.__location})

  @VERBOSE_OUTPUT.setter
  def VERBOSE_OUTPUT(self, val):
    val = str(val).upper()
    if val in BOOL_VALS:
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT.XC.VDW_POT.PAIR_POT', 'Variable': 'VERBOSE_OUTPUT',
                               'Success': True, 'Previous': self.__VERBOSE_OUTPUT, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__VERBOSE_OUTPUT = val
    else:
      errorMessage = ("Invalid option for VERBOSE_OUTPUT: {}. Valid options are: {}".format(val, BOOL_VALS))
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT.XC.VDW_POT.PAIR_POT', 'Variable': 'VERBOSE_OUTPUT',
                               'Success': False, 'Previous': self.__VERBOSE_OUTPUT, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'DFT.XC.VDW_POT.PAIR_POT',
                              'Variable': ' VERBOSE_OUTPUT', 'ErrorMessage': errorMessage,
                              'Location': self.__location}) 
    
    
    
   
