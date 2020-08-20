import datetime
import cssi_cp2k.utilities as utilities
SECTION_PARAMETERS_VALS  = [".TRUE.",".FALSE"]
BOOL_VALS   = [".TRUE.",".FALSE"]
ALGORITHM_VALS=['IRAC','STRICT']
CHOLESKY_VALS=['INVERSE','INVERSE_DBCSR','OFF','REDUCE','RESTORE']
LINESEARCH_VALS=['2PNT','3PNT','GOLD','NONE']
MINIMIZER_VALS=['BROYDEN','CG','DIIS','SD']
PRECONDITIONER_VALS=['FULL_ALL','FULL_KINETIC','FULL_SINGLE','FULL_SINGLE_INVERSE','FULL_S_INVERSE','NONE']
ORTHO_IRAC_VALS=['CHOL','POLY','LWDN'];

PRECOND_SOLVER_VALS=['DEFAULT','DIRECT','INVERSE_CHOLESKY','INVERSE_UPDATE']


def _validate_SECTION_PARAMETERS(val,errorLog=[]):
  if val is not None:
    val = str(val).upper()

  if val in SECTION_PARAMETERS_VALS or (val is None):
    return val
  else:
    errorMessage = ("Invalid option for SECTION_PARAMETERS: {}. Valid options are: {}".format(
                     val,SECTION_PARAMETERS_VALS))
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'SCF OT',
                            'Variable':'SECTION_PARAMETERS','ErrorMessage':errorMessage})
    raise TypeError

def _validate_ALGORITHM(val,errorLog=[]):
  if val is not None:
    val = str(val).upper()

  if val in ALGORITHM_VALS or (val is None):
    return val
  else:
    errorMessage = ("Invalid option for ALGORITHM: {}. Valid options are: {}".format(
                     val,ALGORITHM_VALS))
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'SCF OT',
                            'Variable':'ALGORITHM','ErrorMessage':errorMessage})
    raise TypeError

def _validate_BROYDEN_ADAPTIVE_SIGMA(val,errorLog=[]):
  if val is not None:
    val = str(val).upper()

  if val in BOOL_VALS or (val is None):
    return val
  else:
    errorMessage = ("Invalid option for BROYDEN_ADAPTIVE_SIGMA: {}. Valid options are: {}".format(
                     val,BOOL_VALS))
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'SCF OT',
                            'Variable':'BROYDEN_ADAPTIVE_SIGMA','ErrorMessage':errorMessage})
    raise TypeError

    
def _validate_BROYDEN_BETA(val,errorLog=[]):
    return val    
    
    
def _validate_BROYDEN_ENABLE_FLIP(val,errorLog=[]):
  if val is not None:
    val = str(val).upper()

  if val in BOOL_VALS or (val is None):
    return val
  else:
    errorMessage = ("Invalid option for BROYDEN_ENABLE_FLIP: {}. Valid options are: {}".format(
                     val,BOOL_VALS))
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'SCF OT',
                            'Variable':'BROYDEN_ENABLE_FLIP','ErrorMessage':errorMessage})
    raise TypeError

    
def _validate_BROYDEN_ETA(val,errorLog=[]):
    return val  


    
def _validate_BROYDEN_FORGET_HISTORY(val,errorLog=[]):
  if val is not None:
    val = str(val).upper()

  if val in BOOL_VALS or (val is None):
    return val
  else:
    errorMessage = ("Invalid option for BROYDEN_FORGET_HISTORY: {}. Valid options are: {}".format(
                     val,BOOL_VALS))
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'SCF OT',
                            'Variable':'BROYDEN_FORGET_HISTORY','ErrorMessage':errorMessage})
    raise TypeError




def _validate_BROYDEN_GAMMA(val,errorLog=[]):
    return val  


def _validate_BROYDEN_OMEGA(val,errorLog=[]):
    return val  



def _validate_BROYDEN_SIGMA(val,errorLog=[]):
    return val  



def _validate_BROYDEN_SIGMA_DECREASE(val,errorLog=[]):
    return val  


def _validate_BROYDEN_SIGMA_MIN(val,errorLog=[]):
    return val  

    
def _validate_CHOLESKY(val,errorLog=[]):
  if val is not None:
    val = str(val).upper()

  if val in CHOLESKY_VALS or (val is None):
    return val
  else:
    errorMessage = ("Invalid option for CHOLESKY: {}. Valid options are: {}".format(
                     val,CHOLESKY_VALS))
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'SCF OT',
                            'Variable':'CHOLESKY','ErrorMessage':errorMessage})
    raise TypeError
    
    
        
def _validate_ENERGIES(val,errorLog=[]):
  if val is not None:
    val = str(val).upper()

  if val in BOOL_VALS or (val is None):
    return val
  else:
    errorMessage = ("Invalid option for ENERGIES: {}. Valid options are: {}".format(
                     val,BOOL_VALS))
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'SCF OT',
                            'Variable':'ENERGIES','ErrorMessage':errorMessage})
    raise TypeError



def _validate_ENERGY_GAP(val,errorLog=[]):
    return val  


def _validate_EPS_IRAC(val,errorLog=[]):
    return val  



def _validate_EPS_IRAC_FILTER_MATRIX(val,errorLog=[]):
    return val  



def _validate_EPS_IRAC_QUICK_EXIT(val,errorLog=[]):
    return val  


def _validate_EPS_IRAC_SWITCH(val,errorLog=[]):
    return val  




def _validate_EPS_TAYLOR(val,errorLog=[]):
    return val  


def _validate_GOLD_TARGET(val,errorLog=[]):
    return val  
def _validate_IRAC_DEGREE(val,errorLog=[]):
  if utilities.is_integer(val) or (val is None):
    return val
  else:
    errorMessage = "IRAC_DEGREE  must be AN integer."
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'SCF OT',
                            'Variable':'IRAC_DEGREE','ErrorMessage':errorMessage})
    raise TypeError
        
def _validate_LINESEARCH(val,errorLog=[]):
  if val is not None:
    val = str(val).upper()

  if val in LINESEARCH_VALS or (val is None):
    return val
  else:
    errorMessage = ("Invalid option for LINESEARCH: {}. Valid options are: {}".format(
                     val,LINESEARCH_VALS))
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'SCF OT',
                            'Variable':'LINESEARCH','ErrorMessage':errorMessage})
    raise TypeError

    
    

def _validate_MAX_IRAC(val,errorLog=[]):
  if utilities.is_integer(val) or (val is None):
    return val
  else:
    errorMessage = "MAX_IRAC  must be AN integer."
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'SCF OT',
                            'Variable':'MAX_IRAC','ErrorMessage':errorMessage})
    raise TypeError

def _validate_MAX_TAYLOR(val,errorLog=[]):
  if utilities.is_integer(val) or (val is None):
    return val
  else:
    errorMessage = "MAX_TAYLOR  must be AN integer."
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'SCF OT',
                            'Variable':'MAX_TAYLOR','ErrorMessage':errorMessage})
    raise TypeError



def _validate_MINIMIZER(val,errorLog=[]):
  if val is not None:
    val = str(val).upper()

  if val in MINIMIZER_VALS or (val is None):
    return val
  else:
    errorMessage = ("Invalid option for MINIMIZER: {}. Valid options are: {}".format(
                     val,MINIMIZER_VALS))
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'SCF',
                            'Variable':'MINIMIZER','ErrorMessage':errorMessage})
    raise TypeError

    
    
    
    
def _validate_NONDIAG_ENERGY(val,errorLog=[]):
  if val is not None:
    val = str(val).upper()

  if val in BOOL_VALS or (val is None):
    return val
  else:
    errorMessage = ("Invalid option for NONDIAG_ENERGY: {}. Valid options are: {}".format(
                     val,BOOL_VALS))
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'SCF OT',
                            'Variable':'NONDIAG_ENERGY','ErrorMessage':errorMessage})
    raise TypeError


def _validate_NONDIAG_ENERGY_STRENGTH(val,errorLog=[]):
    return val  
 
def _validate_N_HISTORY_VEC(val,errorLog=[]):
  if utilities.is_integer(val) or (val is None):
    return val
  else:
    errorMessage = "N_HISTORY_VEC  must be AN integer."
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'SCF OT',
                            'Variable':'N_HISTORY_VEC','ErrorMessage':errorMessage})
    raise TypeError

def _validate_OCCUPATION_PRECONDITIONER(val,errorLog=[]):
  if val is not None:
    val = str(val).upper()

  if val in BOOL_VALS or (val is None):
    return val
  else:
    errorMessage = ("Invalid option for OCCUPATION_PRECONDITIONER: {}. Valid options are: {}".format(
                     val,BOOL_VALS))
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'SCF OT',
                            'Variable':'OCCUPATION_PRECONDITIONER','ErrorMessage':errorMessage})
    raise TypeError

def _validate_ON_THE_FLY_LOC(val,errorLog=[]):
  if val is not None:
    val = str(val).upper()

  if val in BOOL_VALS or (val is None):
    return val
  else:
    errorMessage = ("Invalid option for ON_THE_FLY_LOC: {}. Valid options are: {}".format(
                     val,BOOL_VALS))
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'SCF OT',
                            'Variable':'ON_THE_FLY_LOC','ErrorMessage':errorMessage})
    raise TypeError

def _validate_ORTHO_IRAC(val,errorLog=[]):
  if val is not None:
    val = str(val).upper()

  if val in ORTHO_IRAC_VALS or (val is None):
    return val
  else:
    errorMessage = ("Invalid option for ORTHO_IRAC: {}. Valid options are: {}".format(
                     val,ORTHO_IRAC_VALS))
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'SCF OT',
                            'Variable':'ORTHO_IRAC','ErrorMessage':errorMessage})
    raise TypeError    
    
def _validate_PRECONDITIONER(val,errorLog=[]):
  if val is not None:
    val = str(val).upper()

  if val in PRECONDITIONER_VALS or (val is None):
    return val
  else:
    errorMessage = ("Invalid option for PRECONDITIONER: {}. Valid options are: {}".format(
                     val,PRECONDITIONER_VALS))
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'SCF OT',
                            'Variable':'PRECONDITIONER','ErrorMessage':errorMessage})
    raise TypeError   

def _validate_PRECOND_SOLVER(val,errorLog=[]):
  if val is not None:
    val = str(val).upper()

  if val in PRECOND_SOLVER_VALS or (val is None):
    return val
  else:
    errorMessage = ("Invalid option for PRECOND_SOLVER: {}. Valid options are: {}".format(
                     val,PRECONDITIONER_VALS))
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'SCF OT',
                            'Variable':'PRECOND_SOLVER','ErrorMessage':errorMessage})
    raise TypeError   

def _validate_ROTATION(val,errorLog=[]):
  if val is not None:
    val = str(val).upper()

  if val in BOOL_VALS or (val is None):
    return val
  else:
    errorMessage = ("Invalid option for ROTATION: {}. Valid options are: {}".format(
                     val,BOOL_VALS))
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'SCF OT',
                            'Variable':'ROTATION','ErrorMessage':errorMessage})
    raise TypeError
    

    
    
def _validate_SAFE_DIIS(val,errorLog=[]):
  if val is not None:
    val = str(val).upper()

  if val in BOOL_VALS or (val is None):
    return val
  else:
    errorMessage = ("Invalid option for SAFE_DIIS: {}. Valid options are: {}".format(
                     val,BOOL_VALS))
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'SCF OT',
                            'Variable':'SAFE_DIIS','ErrorMessage':errorMessage})
    raise TypeError
    
    
    
    
    
def _validate_STEPSIZE(val,errorLog=[]):
    return val


class OT:

  def __init__(self,SECTION_PARAMETERS=None, ALGORITHM=None,BROYDEN_ADAPTIVE_SIGMA=None,BROYDEN_BETA=None,BROYDEN_ENABLE_FLIP=None,BROYDEN_ETA=None,BROYDEN_FORGET_HISTORY=None,BROYDEN_GAMMA=None,BROYDEN_OMEGA=None,BROYDEN_SIGMA=None,BROYDEN_SIGMA_DECREASE=None,BROYDEN_SIGMA_MIN=None,CHOLESKY=None,ENERGIES=None,ENERGY_GAP=None,EPS_IRAC=None,EPS_IRAC_FILTER_MATRIX=None,EPS_IRAC_QUICK_EXIT=None,EPS_IRAC_SWITCH=None, EPS_TAYLOR=None,GOLD_TARGET=None,IRAC_DEGREE=None,LINESEARCH=None,MAX_IRAC=None,MAX_TAYLOR=None,MINIMIZER=None,NONDIAG_ENERGY=None,NONDIAG_ENERGY_STRENGTH=None,N_HISTORY_VEC=None,OCCUPATION_PRECONDITIONER=None,ON_THE_FLY_LOC=None,ORTHO_IRAC=None,PRECONDITIONER=None,PRECOND_SOLVER=None,ROTATION=None,SAFE_DIIS=None,STEPSIZE=None,errorLog=[],changeLog=[],location=""):
    self.__errorLog = errorLog
    self.__changeLog = changeLog
    self.__SECTION_PARAMETERS=_validate_SECTION_PARAMETERS(SECTION_PARAMETERS, errorLog=self.__errorLog)
    self.__ALGORITHM=_validate_ALGORITHM(ALGORITHM, errorLog=self.__errorLog)
    self.__BROYDEN_ADAPTIVE_SIGMA=_validate_BROYDEN_ADAPTIVE_SIGMA(BROYDEN_ADAPTIVE_SIGMA, errorLog=self.__errorLog)
    self.__BROYDEN_BETA=_validate_BROYDEN_BETA(BROYDEN_BETA,errorLog=self.__errorLog)
    self.__BROYDEN_ENABLE_FLIP=_validate_BROYDEN_ENABLE_FLIP(BROYDEN_ENABLE_FLIP,errorLog=self.__errorLog)
    self.__BROYDEN_ETA=_validate_BROYDEN_ETA(BROYDEN_ETA,errorLog=self.__errorLog)
    self.__BROYDEN_FORGET_HISTORY=_validate_BROYDEN_FORGET_HISTORY(BROYDEN_FORGET_HISTORY,errorLog=self.__errorLog)
    self.__BROYDEN_GAMMA=_validate_BROYDEN_GAMMA(BROYDEN_GAMMA,errorLog=self.__errorLog)
    self.__BROYDEN_OMEGA=_validate_BROYDEN_OMEGA(BROYDEN_OMEGA,errorLog=self.__errorLog)
    self.__BROYDEN_SIGMA=_validate_BROYDEN_SIGMA(BROYDEN_SIGMA,errorLog=self.__errorLog)
    self.__BROYDEN_SIGMA_DECREASE=_validate_BROYDEN_SIGMA_DECREASE(BROYDEN_SIGMA_DECREASE,errorLog=self.__errorLog)
    self.__BROYDEN_SIGMA_MIN=_validate_BROYDEN_SIGMA_MIN(BROYDEN_SIGMA_MIN,errorLog=self.__errorLog)
    self.__CHOLESKY=_validate_CHOLESKY(CHOLESKY,errorLog=self.__errorLog)
    self.__ENERGIES=_validate_ENERGIES(ENERGIES,errorLog=self.__errorLog)
    self.__ENERGY_GAP=_validate_ENERGY_GAP(ENERGY_GAP,errorLog=self.__errorLog)
    self.__EPS_IRAC=_validate_EPS_IRAC(EPS_IRAC,errorLog=self.__errorLog)
    self.__EPS_IRAC_FILTER_MATRIX=_validate_EPS_IRAC_FILTER_MATRIX(EPS_IRAC_FILTER_MATRIX,errorLog=self.__errorLog)
    self.__EPS_IRAC_QUICK_EXIT=_validate_EPS_IRAC_QUICK_EXIT(EPS_IRAC_QUICK_EXIT,errorLog=self.__errorLog)
    self.__EPS_IRAC_SWITCH=_validate_EPS_IRAC_SWITCH(EPS_IRAC_SWITCH,errorLog=self.__errorLog)
    self.__EPS_TAYLOR=_validate_EPS_TAYLOR(EPS_TAYLOR,errorLog=self.__errorLog)
    self.__GOLD_TARGET=_validate_GOLD_TARGET(GOLD_TARGET,errorLog=self.__errorLog)
    self.__IRAC_DEGREE=_validate_IRAC_DEGREE(IRAC_DEGREE,errorLog=self.__errorLog)
    self.__LINESEARCH=_validate_LINESEARCH(LINESEARCH,errorLog=self.__errorLog)
    self.__MAX_IRAC=_validate_MAX_IRAC(MAX_IRAC,errorLog=self.__errorLog)
    self.__MAX_TAYLOR=_validate_MAX_TAYLOR(MAX_TAYLOR,errorLog=self.__errorLog)
    self.__MINIMIZER=_validate_MINIMIZER(MINIMIZER,errorLog=self.__errorLog)
    self.__NONDIAG_ENERGY=_validate_NONDIAG_ENERGY(NONDIAG_ENERGY,errorLog=self.__errorLog)
    self.__NONDIAG_ENERGY_STRENGTH=_validate_NONDIAG_ENERGY_STRENGTH(NONDIAG_ENERGY_STRENGTH,errorLog=self.__errorLog)
    self.__N_HISTORY_VEC=_validate_N_HISTORY_VEC(N_HISTORY_VEC,errorLog=self.__errorLog)
    self.__OCCUPATION_PRECONDITIONER=_validate_OCCUPATION_PRECONDITIONER(OCCUPATION_PRECONDITIONER,errorLog=self.__errorLog)
    self.__ON_THE_FLY_LOC=_validate_ON_THE_FLY_LOC(ON_THE_FLY_LOC,errorLog=self.__errorLog)
    self.__ORTHO_IRAC=_validate_ORTHO_IRAC(ORTHO_IRAC,errorLog=self.__errorLog)
    self.__PRECONDITIONER=_validate_PRECONDITIONER(PRECONDITIONER,errorLog=self.__errorLog)
    self.__PRECOND_SOLVER=_validate_PRECOND_SOLVER(PRECOND_SOLVER,errorLog=self.__errorLog)
    self.__ROTATION=_validate_ROTATION(ROTATION,errorLog=self.__errorLog)
    self.__SAFE_DIIS=_validate_SAFE_DIIS(SAFE_DIIS,errorLog=self.__errorLog)
    self.__STEPSIZE=_validate_STEPSIZE(STEPSIZE,errorLog=self.__errorLog)
    

    

    

    self.__location  = "{}/OT".format(location)
    #ENERGY subsections
    #self.__EACH      = EACH.EACH(errorLog=self.__errorLog,changeLog=self.__changeLog,
                      #   location=self.__location)

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
  def ALGORITHM(self):
    return self.__ALGORITHM

  @property
  def BROYDEN_ADAPTIVE_SIGMA(self):
    return self.__BROYDEN_ADAPTIVE_SIGMA


  @property
  def BROYDEN_BETA(self):
    return self.__BROYDEN_BETA

  @property
  def BROYDEN_ENABLE_FLIP(self):
    return self.__BROYDEN_ENABLE_FLIP

  @property
  def BROYDEN_ETA(self):
    return self.__BROYDEN_ETA

  @property
  def BROYDEN_FORGET_HISTORY(self):
    return self.__BROYDEN_FORGET_HISTORY

  @property
  def BROYDEN_GAMMA(self):
    return self.__BROYDEN_GAMMA


  @property
  def BROYDEN_OMEGA(self):
    return self.__BROYDEN_OMEGA
  @property
  def BROYDEN_SIGMA(self):
    return self.__BROYDEN_SIGMA

  @property
  def BROYDEN_SIGMA_DECREASE(self):
    return self.__BROYDEN_SIGMA_DECREASE

  @property
  def BROYDEN_SIGMA_MIN(self):
    return self.__BROYDEN_SIGMA_MIN

  @property
  def CHOLESKY(self):
    return self.__CHOLESKY

  @property
  def ENERGIES(self):
    return self.__ENERGIES

  @property
  def ENERGY_GAP(self):
    return self.__ENERGY_GAP


  @property
  def EPS_IRAC(self):
    return self.__EPS_IRAC

  @property
  def EPS_IRAC_FILTER_MATRIX(self):
    return self.__EPS_IRAC_FILTER_MATRIX

  @property
  def EPS_IRAC_QUICK_EXIT(self):
    return self.__EPS_IRAC_QUICK_EXIT


  @property
  def EPS_IRAC_SWITCH(self):
    return self.__EPS_IRAC_SWITCH

  @property
  def EPS_TAYLOR(self):
    return self.__EPS_TAYLOR


  @property
  def GOLD_TARGET(self):
    return self.__GOLD_TARGET

  @property
  def IRAC_DEGREE(self):
    return self.__IRAC_DEGREE

  @property
  def LINESEARCH(self):
    return self.__LINESEARCH

  @property
  def MAX_IRAC(self):
    return self.__MAX_IRAC

  @property
  def MAX_TAYLOR(self):
    return self.__MAX_TAYLOR

  @property
  def MINIMIZER(self):
    return self.__MINIMIZER

  @property
  def NONDIAG_ENERGY(self):
    return self.__NONDIAG_ENERGY

  @property
  def NONDIAG_ENERGY_STRENGTH(self):
    return self.__NONDIAG_ENERGY_STRENGTH

  @property
  def N_HISTORY_VEC(self):
    return self.__N_HISTORY_VEC

  @property
  def OCCUPATION_PRECONDITIONER(self):
    return self.__OCCUPATION_PRECONDITIONER


  @property
  def ON_THE_FLY_LOC(self):
    return self.__ON_THE_FLY_LOC

  @property
  def ORTHO_IRAC(self):
    return self.__ORTHO_IRAC

  @property
  def PRECONDITIONER(self):
    return self.__PRECONDITIONER

  @property
  def PRECOND_SOLVER(self):
    return self.__PRECOND_SOLVER


  @property
  def ROTATION(self):
    return self.__ROTATION

  @property
  def SAFE_DIIS(self):
    return self.__SAFE_DIIS

  @property
  def STEPSIZE(self):
    return self.__STEPSIZE




  @SECTION_PARAMETERS.setter
  def SECTION_PARAMETERS(self, val):
    val = str(val).upper()
    if val in SECTION_PARAMETERS_VALS:
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SCF OT', 'Variable': 'SECTION_PARAMETERS',
                               'Success': True, 'Previous': self.__SECTION_PARAMETERS, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__SECTION_PARAMETERS= val
    else:
      errorMessage = ("Invalid option for Section parameter OT: {}. Valid options are: {}".format(val,SECTION_PARAMETERS_VALS))
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SCF OT', 'Variable': 'SECTION_PARAMETERS',
                               'Success': False, 'Previous': self.__SECTION_PARAMETERS, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'SCF OT',
                              'Variable': 'SECTION_PARAMETERS', 'ErrorMessage': errorMessage, 'Location': self.__location})
    
  
  @ALGORITHM.setter
  def ALGORITHM(self, val):
    val = str(val).upper()
    if val in ALGORITHM_VALS:
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SCF OT', 'Variable': 'ALGORITHM',
                               'Success': True, 'Previous': self.__ALGORITHM, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__ALGORITHM= val
    else:
      errorMessage = ("Invalid option for ALGORITHM: {}. Valid options are: {}".format(val,ALGORITHM_VALS))
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SCF OT', 'Variable': 'ALGORITHM',
                               'Success': False, 'Previous': self.__ALGORITHM, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'SCF OT',
                              'Variable': 'ALGORITHM', 'ErrorMessage': errorMessage, 'Location': self.__location})  

  
  @BROYDEN_ADAPTIVE_SIGMA.setter
  def BROYDEN_ADAPTIVE_SIGMA(self, val):
    val = str(val).upper()
    if val in BOOL_VALS:
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SCF OT', 'Variable': 'BROYDEN_ADAPTIVE_SIGMA',
                               'Success': True, 'Previous': self.__BROYDEN_ADAPTIVE_SIGMA, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__BROYDEN_ADAPTIVE_SIGMA= val
    else:
      errorMessage = ("Invalid option for ALGORITHM: {}. Valid options are: {}".format(val,BOOL_VALS))
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SCF OT', 'Variable': 'BROYDEN_ADAPTIVE_SIGMA',
                               'Success': False, 'Previous': self.__BROYDEN_ADAPTIVE_SIGMA, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'SCF OT',
                              'Variable': 'BROYDEN_ADAPTIVE_SIGMA', 'ErrorMessage': errorMessage, 'Location': self.__location}) 
    
    
    
    
  @BROYDEN_BETA.setter
  def BROYDEN_BETA(self,val):
    self.__BROYDEN_BETA=val
    self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SCF OT', 'Variable': 'BROYDEN_BETA',
                               'Success': True, 'Previous': self.__BROYDEN_BETA, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
    
  @BROYDEN_ENABLE_FLIP.setter
  def BROYDEN_ENABLE_FLIP(self, val):
    val = str(val).upper()
    if val in BOOL_VALS:
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SCF OT', 'Variable': 'BROYDEN_ENABLE_FLIP',
                               'Success': True, 'Previous': self.__BROYDEN_ENABLE_FLIP, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__BROYDEN_ENABLE_FLIP= val
    else:
      errorMessage = ("Invalid option for BROYDEN_ENABLE_FLIP: {}. Valid options are: {}".format(val,BOOL_VALS))
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SCF OT', 'Variable': 'BROYDEN_ENABLE_FLIP',
                               'Success': False, 'Previous': self.__BROYDEN_ENABLE_FLIP, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'SCF OT',
                              'Variable': 'BROYDEN_ADAPTIVE_SIGMA', 'ErrorMessage': errorMessage, 'Location': self.__location}) 
    
    
    
  @BROYDEN_ETA.setter
  def BROYDEN_ETA(self,val):
    self.__BROYDEN_ETA=val
    self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SCF OT', 'Variable': 'BROYDEN_ETA',
                               'Success': True, 'Previous': self.__BROYDEN_ETA, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
    
  @BROYDEN_FORGET_HISTORY.setter
  def BROYDEN_FORGET_HISTORY(self, val):
    val = str(val).upper()
    if val in BOOL_VALS:
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SCF OT', 'Variable': 'BROYDEN_FORGET_HISTORY',
                               'Success': True, 'Previous': self.__BROYDEN_FORGET_HISTORY, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__BROYDEN_FORGET_HISTORY= val
    else:
      errorMessage = ("Invalid option for BROYDEN_FORGET_HISTORY: {}. Valid options are: {}".format(val,BOOL_VALS))
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SCF OT', 'Variable': 'BROYDEN_FORGET_HISTORY',
                               'Success': False, 'Previous': self.__BROYDEN_FORGET_HISTORY, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'SCF OT',
                              'Variable': 'BROYDEN_FORGET_HISTORY', 'ErrorMessage': errorMessage, 'Location': self.__location})
    
  @BROYDEN_GAMMA.setter
  def BROYDEN_GAMMA(self,val):
    self.__BROYDEN_GAMMA=val
    self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SCF OT', 'Variable': 'BROYDEN_GAMMA',
                               'Success': True, 'Previous': self.__BROYDEN_GAMMA, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
    
  @BROYDEN_OMEGA.setter
  def BROYDEN_OMEGA(self,val):
    self.__BROYDEN_OMEGA=val
    self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SCF OT', 'Variable': 'BROYDEN_OMEGA',
                               'Success': True, 'Previous': self.__BROYDEN_OMEGA, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
    
  @BROYDEN_SIGMA.setter
  def BROYDEN_SIGMA(self,val):
    self.__BROYDEN_SIGMA=val
    self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SCF OT', 'Variable': 'BROYDEN_SIGMA',
                               'Success': True, 'Previous': self.__BROYDEN_SIGMA, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
    
  @BROYDEN_SIGMA_DECREASE.setter
  def BROYDEN_SIGMA_DECREASE(self,val):
    self.__BROYDEN_SIGMA_DECREASE=val
    self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SCF OT', 'Variable': 'BROYDEN_SIGMA_DECREASE',
                               'Success': True, 'Previous': self.__BROYDEN_SIGMA_DECREASE, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
  @BROYDEN_SIGMA_MIN.setter
  def BROYDEN_SIGMA_MIN(self,val):
    self.__BROYDEN_SIGMA_MIN=val
    self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SCF OT', 'Variable': 'BROYDEN_SIGMA_MIN',
                               'Success': True, 'Previous': self.__BROYDEN_SIGMA_MIN, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
    
  @CHOLESKY.setter
  def CHOLESKY(self, val):
    val = str(val).upper()
    if val in CHOLESKY_VALS:
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SCF OT', 'Variable': 'CHOLESKY',
                               'Success': True, 'Previous': self.__CHOLESKY, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__CHOLESKY= val
    else:
      errorMessage = ("Invalid option for CHOLESKY: {}. Valid options are: {}".format(val,CHOLESKY_VALS))
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SCF OT', 'Variable': 'CHOLESKY',
                               'Success': False, 'Previous': self.__CHOLESKY, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'SCF OT',
                              'Variable': 'CHOLESKY', 'ErrorMessage': errorMessage, 'Location': self.__location}) 
  
  @ENERGIES.setter
  def ENERGIES(self, val):
    val = str(val).upper()
    if val in BOOL_VALS:
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SCF OT', 'Variable': 'ENERGIES',
                               'Success': True, 'Previous': self.__ENERGIES, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__ENERGIES= val
    else:
      errorMessage = ("Invalid option for ENERGIES: {}. Valid options are: {}".format(val,BOOL_VALS))
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SCF OT', 'Variable': 'ENERGIES',
                               'Success': False, 'Previous': self.__ENERGIES, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'SCF OT',
                              'Variable': 'ENERGIES', 'ErrorMessage': errorMessage, 'Location': self.__location})   
    
    
      
  @ENERGY_GAP.setter
  def ENERGY_GAP(self,val):
    self.__ENERGY_GAP=val
    self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SCF OT', 'Variable': 'ENERGY_GAP',
                               'Success': True, 'Previous': self.__ENERGY_GAP, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
    
  @EPS_IRAC.setter
  def EPS_IRAC(self,val):
    self.__EPS_IRAC=val
    self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SCF OT', 'Variable': 'EPS_IRAC',
                               'Success': True, 'Previous': self.__EPS_IRAC, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
    
  @EPS_IRAC_FILTER_MATRIX.setter
  def EPS_IRAC_FILTER_MATRIX(self,val):
    self.__EPS_IRAC_FILTER_MATRIX=val
    self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SCF OT', 'Variable': 'EPS_IRAC_FILTER_MATRIX',
                               'Success': True, 'Previous': self.__EPS_IRAC_FILTER_MATRIX, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
    
  @EPS_IRAC_QUICK_EXIT.setter
  def EPS_IRAC_QUICK_EXIT(self,val):
    self.__EPS_IRAC_QUICK_EXIT=val
    self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SCF OT', 'Variable': 'EPS_IRAC_QUICK_EXIT',
                               'Success': True, 'Previous': self.__EPS_IRAC_QUICK_EXIT, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
  @EPS_IRAC_SWITCH.setter
  def EPS_IRAC_SWITCH(self,val):
    self.__EPS_IRAC_SWITCH=val
    self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SCF OT', 'Variable': 'EPS_IRAC_SWITCH',
                               'Success': True, 'Previous': self.__EPS_IRAC_SWITCH, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
    
    
        
  @EPS_TAYLOR.setter
  def EPS_TAYLOR(self,val):
    self.__EPS_TAYLOR=val
    self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SCF OT', 'Variable': 'EPS_TAYLOR',
                               'Success': True, 'Previous': self.__EPS_TAYLOR, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
    
  @GOLD_TARGET.setter
  def GOLD_TARGET(self,val):
    self.__GOLD_TARGET=val
    self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SCF OT', 'Variable': 'GOLD_TARGET',
                               'Success': True, 'Previous': self.__GOLD_TARGET, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
    
  @IRAC_DEGREE.setter
  def IRAC_DEGREE(self,val):
    self.__IRAC_DEGREE=val
    self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SCF OT', 'Variable': 'IRAC_DEGREE',
                               'Success': True, 'Previous': self.__IRAC_DEGREE, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
    
    

  @LINESEARCH.setter
  def LINESEARCH(self, val):
    val = str(val).upper()
    if val in LINESEARCH_VALS:
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SCF OT', 'Variable': 'LINESEARCH',
                               'Success': True, 'Previous': self.__LINESEARCH, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__LINESEARCH= val
    else:
      errorMessage = ("Invalid option for LINESEARCH: {}. Valid options are: {}".format(val,LINESEARCH_VALS))
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SCF OT', 'Variable': 'LINESEARCH',
                               'Success': False, 'Previous': self.__LINESEARCH, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'SCF OT',
                              'Variable': 'LINESEARCH', 'ErrorMessage': errorMessage, 'Location': self.__location})  
    
  @MAX_IRAC.setter
  def MAX_IRAC(self,val):
    self.__MAX_IRAC=val
    self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SCF OT', 'Variable': 'MAX_IRAC',
                               'Success': True, 'Previous': self.__MAX_IRAC, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})   
    
  @MAX_TAYLOR.setter
  def MAX_TAYLOR(self,val):
    self.__MAX_TAYLOR=val
    self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SCF OT', 'Variable': 'MAX_TAYLOR',
                               'Success': True, 'Previous': self.__MAX_TAYLOR, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
    
    
  @MINIMIZER.setter
  def MINIMIZER(self, val):
    val = str(val).upper()
    if val in MINIMIZER_VALS:
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SCF OT', 'Variable': 'MINIMIZER',
                               'Success': True, 'Previous': self.__MINIMIZER, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__MINIMIZER= val
    else:
      errorMessage = ("Invalid option for MINIMIZER: {}. Valid options are: {}".format(val,MINIMIZER_VALS))
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SCF OT', 'Variable': 'MINIMIZER',
                               'Success': False, 'Previous': self.__MINIMIZER, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'SCF OT',
                              'Variable': 'MINIMIZER', 'ErrorMessage': errorMessage, 'Location': self.__location}) 
    
    
  @NONDIAG_ENERGY.setter
  def NONDIAG_ENERGY(self, val):
    val = str(val).upper()
    if val in BOOL_VALS:
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SCF OT', 'Variable': 'NONDIAG_ENERGY',
                               'Success': True, 'Previous': self.__NONDIAG_ENERGY, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__NONDIAG_ENERGY= val
    else:
      errorMessage = ("Invalid option for NONDIAG_ENERGY: {}. Valid options are: {}".format(val,BOOL_VALS))
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SCF OT', 'Variable': 'NONDIAG_ENERGY',
                               'Success': False, 'Previous': self.__NONDIAG_ENERGY, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'SCF OT',
                              'Variable': 'NONDIAG_ENERGY', 'ErrorMessage': errorMessage, 'Location': self.__location})
    
    
  @NONDIAG_ENERGY_STRENGTH.setter
  def NONDIAG_ENERGY_STRENGTH(self,val):
    self.__NONDIAG_ENERGY_STRENGTH=val
    self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SCF OT', 'Variable': 'NONDIAG_ENERGY_STRENGTH',
                               'Success': True, 'Previous': self.__NONDIAG_ENERGY_STRENGTH, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
    
  @N_HISTORY_VEC.setter
  def N_HISTORY_VEC(self,val):
    self.__N_HISTORY_VEC=val
    self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SCF OT', 'Variable': 'N_HISTORY_VEC',
                               'Success': True, 'Previous': self.__N_HISTORY_VEC, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
    
  @OCCUPATION_PRECONDITIONER.setter
  def OCCUPATION_PRECONDITIONER(self, val):
    val = str(val).upper()
    if val in BOOL_VALS:
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SCF OT', 'Variable': 'OCCUPATION_PRECONDITIONER',
                               'Success': True, 'Previous': self.__OCCUPATION_PRECONDITIONER, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__OCCUPATION_PRECONDITIONER= val
    else:
      errorMessage = ("Invalid option for OCCUPATION_PRECONDITIONER: {}. Valid options are: {}".format(val,BOOL_VALS))
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SCF OT', 'Variable': 'OCCUPATION_PRECONDITIONER',
                               'Success': False, 'Previous': self.__OCCUPATION_PRECONDITIONER, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'SCF OT',
                              'Variable': 'OCCUPATION_PRECONDITIONER', 'ErrorMessage': errorMessage, 'Location': self.__location})
    
    
    
  @ON_THE_FLY_LOC.setter
  def ON_THE_FLY_LOC(self, val):
    val = str(val).upper()
    if val in BOOL_VALS:
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SCF OT', 'Variable': 'ON_THE_FLY_LOC',
                               'Success': True, 'Previous': self.__ON_THE_FLY_LOC, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__ON_THE_FLY_LOC= val
    else:
      errorMessage = ("Invalid option for ON_THE_FLY_LOC: {}. Valid options are: {}".format(val,BOOL_VALS))
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SCF OT', 'Variable': 'ON_THE_FLY_LOC',
                               'Success': False, 'Previous': self.__ON_THE_FLY_LOC, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'SCF OT',
                              'Variable': 'ON_THE_FLY_LOC', 'ErrorMessage': errorMessage, 'Location': self.__location})
    
  @ORTHO_IRAC.setter
  def ORTHO_IRAC(self, val):
    val = str(val).upper()
    if val in ORTHO_IRAC_VALS:
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SCF OT', 'Variable': 'ORTHO_IRAC',
                               'Success': True, 'Previous': self.__ORTHO_IRAC, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__ORTHO_IRAC= val
    else:
      errorMessage = ("Invalid option for ORTHO_IRAC: {}. Valid options are: {}".format(val,ORTHO_IRAC_VALS))
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SCF OT', 'Variable': 'ORTHO_IRAC',
                               'Success': False, 'Previous': self.__ORTHO_IRAC, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'SCF OT',
                              'Variable': 'ORTHO_IRAC', 'ErrorMessage': errorMessage, 'Location': self.__location})
    
  @PRECONDITIONER.setter
  def PRECONDITIONER(self, val):
    val = str(val).upper()
    if val in PRECONDITIONER_VALS:
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SCF OT', 'Variable': 'PRECONDITIONER',
                               'Success': True, 'Previous': self.__PRECONDITIONER, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__PRECONDITIONER= val
    else:
      errorMessage = ("Invalid option for PRECONDITIONER: {}. Valid options are: {}".format(val,PRECONDITIONER_VALS))
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SCF OT', 'Variable': 'PRECONDITIONER',
                               'Success': False, 'Previous': self.__PRECONDITIONER, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'SCF OT',
                              'Variable': 'PRECONDITIONER', 'ErrorMessage': errorMessage, 'Location': self.__location})
    
  @PRECOND_SOLVER.setter
  def PRECOND_SOLVER(self, val):
    val = str(val).upper()
    if val in PRECOND_SOLVER_VALS:
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SCF OT', 'Variable': 'PRECOND_SOLVER',
                               'Success': True, 'Previous': self.__PRECOND_SOLVER, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__PRECOND_SOLVER= val
    else:
      errorMessage = ("Invalid option for PRECOND_SOLVER: {}. Valid options are: {}".format(val,PRECOND_SOLVER_VALS))
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SCF OT', 'Variable': 'PRECOND_SOLVER',
                               'Success': False, 'Previous': self.__PRECOND_SOLVER, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'SCF OT',
                              'Variable': 'PRECOND_SOLVER', 'ErrorMessage': errorMessage, 'Location': self.__location})
    
    
  @SAFE_DIIS.setter
  def SAFE_DIIS(self, val):
    val = str(val).upper()
    if val in BOOL_VALS:
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SCF OT', 'Variable': 'SAFE_DIIS',
                               'Success': True, 'Previous': self.__SAFE_DIIS, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.SAFE_DIIS= val
    else:
      errorMessage = ("Invalid option for SAFE_DIIS: {}. Valid options are: {}".format(val,BOOL_VALS))
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SCF OT', 'Variable': 'SAFE_DIIS',
                               'Success': False, 'Previous': self.__SAFE_DIIS, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'SCF OT',
                              'Variable': 'SAFE_DIIS', 'ErrorMessage': errorMessage, 'Location': self.__location})
    
  @ROTATION.setter
  def ROTATION(self, val):
    val = str(val).upper()
    if val in BOOL_VALS:
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SCF OT', 'Variable': 'ROTATION',
                               'Success': True, 'Previous': self.__ROTATION, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__ROTATIONC= val
    else:
      errorMessage = ("Invalid option for ROTATION: {}. Valid options are: {}".format(val,BOOL_VALS))
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SCF OT', 'Variable': 'ROTATION',
                               'Success': False, 'Previous': self.__ROTATION, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'SCF OT',
                              'Variable': 'ROTATION', 'ErrorMessage': errorMessage, 'Location': self.__location})
    
    
    
  @STEPSIZE.setter
  def STEPSIZE(self,val):
    self.__STEPSIZE=val
    self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SCF OT', 'Variable': 'STEPSIZE',
                               'Success': True, 'Previous': self.__STEPSIZE, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
    
    
    
    
  
 