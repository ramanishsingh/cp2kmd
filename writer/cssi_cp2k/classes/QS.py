import datetime
import cssi_cp2k.utilities as utilities
BOOL_VALS   = [".TRUE.",".FALSE"]
CORE_PPL_VALS=['ANALYTIC','GRID'];
EXTRAPOLATION_VALS=['ASPC','FROZEN','LINEAR_P','LINEAR_PS','LINEAR_WF','PS','USE_GUESS', 'USE_PREV_P','USE_PREV_RHO_R','USE_PREV_WF'];
METHOD_VALS=['AM1','DFTB','GAPW','GAPW_XC','GPW','LRIGPW','MNDO','MNDOD','OFGPW','PDG','PM3','PM6','PM6-FM','PNNL','RIGPW','RM1','XTB',];
PW_GRID_VALS=['NS-FULLSPACE','NS-HALFSPACE','SPHERICAL'];
PW_GRID_BLOCKED_VALS=['FALSE','FREE','TRUE']
QUADRATURE_VALS=['GC_LOG','GC_SIMPLE','GC_TRANSFORMED']

def _validate_ALMO_SCF(val,errorLog=[]):
  if val is not None:
    val = str(val).upper()
  
  if val in BOOL_VALS or (val is None):
        return val
  else:
    errorMessage = ("Invalid option for ALMO_SCF: {}. Valid options are: {}".format(
                     val,BOOL_VALS))
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'DFT/QS',
                            'Variable':'ALMO_SCF','ErrorMessage':errorMessage})
    raise TypeError   



def _validate_ALPHA0_HARD(val,errorLog=[]):
  #if val is not None:
    #val = str(val).upper()

  #if val in SECTION_PARAMETERS_VALS or (val is None):
  return val
    
    
    
def _validate_CLUSTER_EMBED_SUBSYS(val,errorLog=[]):
  if val is not None:
    val = str(val).upper()
  
  if val in BOOL_VALS or (val is None):
        return val
  else:
    errorMessage = ("Invalid option for CLUSTER_EMBED_SUBSYS: {}. Valid options are: {}".format(
                     val,BOOL_VALS))
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'DFT/QS',
                            'Variable':'CLUSTER_EMBED_SUBSYS','ErrorMessage':errorMessage})
    raise TypeError
    
def _validate_CORE_PPL(val,errorLog=[]):
  if val is not None:
    val = str(val).upper()
  
  if val in CORE_PPL_VALS or (val is None):
        return val
  else:
    errorMessage = ("Invalid option for CORE_PPL: {}. Valid options are: {}".format(
                     val,CORE_PPL_VALS))
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'DFT/QS',
                            'Variable':'CORE_PPL','ErrorMessage':errorMessage})
    raise TypeError   
    
    
def _validate_DFET_EMBEDDED(val,errorLog=[]):
  if val is not None:
    val = str(val).upper()
  
  if val in BOOL_VALS or (val is None):
        return val
  else:
    errorMessage = ("Invalid option for DFET_EMBEDDED: {}. Valid options are: {}".format(
                     val,BOOL_VALS))
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'DFT/QS',
                            'Variable':'DFET_EMBEDDED','ErrorMessage':errorMessage})
    raise TypeError   
    
  


def _validate_DMFET_EMBEDDED(val,errorLog=[]):
  if val is not None:
    val = str(val).upper()
  
  if val in BOOL_VALS or (val is None):
        return val
  else:
    errorMessage = ("Invalid option for DMFET_EMBEDDED: {}. Valid options are: {}".format(
                     val,BOOL_VALS))
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'DFT/QS',
                            'Variable':'DMFET_EMBEDDED','ErrorMessage':errorMessage})
    raise TypeError 
    
def _validate_EMBED_CUBE_FILE_NAME(val,errorLog=[]):
  #if val is not None:
    #val = str(val).upper()

  #if val in SECTION_PARAMETERS_VALS or (val is None):
  return val 

def _validate_EMBED_RESTART_FILE_NAME(val,errorLog=[]):
  #if val is not None:
    #val = str(val).upper()

  #if val in SECTION_PARAMETERS_VALS or (val is None):
  return val

def _validate_EMBED_SPIN_CUBE_FILE_NAME(val,errorLog=[]):
  #if val is not None:
    #val = str(val).upper()

  #if val in SECTION_PARAMETERS_VALS or (val is None):
  return val
    
def _validate_EPSFIT(val,errorLog=[]):
  #if val is not None:
    #val = str(val).upper()

  #if val in SECTION_PARAMETERS_VALS or (val is None):
  return val

def _validate_EPSISO(val,errorLog=[]):

  return val


def _validate_EPSFIT(val,errorLog=[]):
  #if val is not None:
    #val = str(val).upper()

  #if val in SECTION_PARAMETERS_VALS or (val is None):
  return val



def _validate_EPSRHO0(val,errorLog=[]):

  return val




def _validate_EPSSVD(val,errorLog=[]):

  return val
def _validate_EPS_CORE_CHARGE(val,errorLog=[]):

  return val

def _validate_EPS_CPC(val,errorLog=[]):

  return val


def _validate_EPS_DEFAULT(val,errorLog=[]):

  return val


def _validate_EPS_FILTER_MATRIX(val,errorLog=[]):

    
  return val
    
    
def _validate_EPS_GVG_RSPACE(val,errorLog=[]):
  
  return val


def _validate_EPS_KG_ORB(val,errorLog=[]):

  return val


def _validate_EPS_PGF_ORB(val,errorLog=[]):

    
  return val
    
    
def _validate_EPS_PPL(val,errorLog=[]):
  
  return val


def _validate_EPS_PPNL(val,errorLog=[]):
  
  return val

def _validate_EPS_RHO(val,errorLog=[]):
  
  return val
def _validate_EPS_RHO_GSPACE(val,errorLog=[]):
  
  return val

def _validate_EPS_RHO_RSPACE(val,errorLog=[]):
  
  return val


def _validate_EXTRAPOLATION(val,errorLog=[]):
  if val is not None:
    val = str(val).upper()
  
  if val in EXTRAPOLATION_VALS or (val is None):
        return val
  else:
    errorMessage = ("Invalid option for EXTRAPOLATION: {}. Valid options are: {}".format(
                     val,EXTRAPOLATION_VALS))
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'DFT/QS',
                            'Variable':'EXTRAPOLATION','ErrorMessage':errorMessage})
    raise TypeError

def _validate_EXTRAPOLATION_ORDER(val,errorLog=[]):
  if utilities.is_integer(val) or (val is None):
    return val
  else:
    errorMessage = "EXTRAPOLATION_ORDER must be an integer."
    errorLog.append({'Date': datetime.datetime.now(), 'Type': 'init', 'Module': 'DFT/QS',
                     'Variable': 'EXTRAPOLATION_ORDER', 'ErrorMessage': errorMessage})
    raise TypeError

    
    
    
def _validate_FORCE_PAW(val,errorLog=[]):
  if val is not None:
    val = str(val).upper()
  
  if val in BOOL_VALS or (val is None):
        return val
  else:
    errorMessage = ("Invalid option for FORCE_PAW: {}. Valid options are: {}".format(
                     val,BOOL_VALS))
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'DFT/QS',
                            'Variable':'FORCE_PAW','ErrorMessage':errorMessage})
    raise TypeError 
    
    
def _validate_HIGH_LEVEL_EMBED_SUBSYS(val,errorLog=[]):
  if val is not None:
    val = str(val).upper()
  
  if val in BOOL_VALS or (val is None):
        return val
  else:
    errorMessage = ("Invalid option for HIGH_LEVEL_EMBED_SUBSYS: {}. Valid options are: {}".format(
                     val,BOOL_VALS))
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'DFT/QS',
                            'Variable':'HIGH_LEVEL_EMBED_SUBSYS','ErrorMessage':errorMessage})
    raise TypeError 
 

def _validate_KG_METHOD(val,errorLog=[]):
  if val is not None:
    val = str(val).upper()
  
  if val in BOOL_VALS or (val is None):
        return val
  else:
    errorMessage = ("Invalid option for KG_METHOD: {}. Valid options are: {}".format(
                     val,BOOL_VALS))
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'DFT/QS',
                            'Variable':'KG_METHOD','ErrorMessage':errorMessage})
    raise TypeError 
    
    
    

def _validate_LADDN0(val,errorLog=[]):
  if utilities.is_integer(val) or (val is None):
    return val
  else:
    errorMessage = "LADDN0 must be an integer."
    errorLog.append({'Date': datetime.datetime.now(), 'Type': 'init', 'Module': 'DFT/QS',
                     'Variable': 'LADDN0', 'ErrorMessage': errorMessage})
    raise TypeError
    

def _validate_LMAXN0(val,errorLog=[]):
  if utilities.is_integer(val) or (val is None):
    return val
  else:
    errorMessage = "LMAXN0 must be an integer."
    errorLog.append({'Date': datetime.datetime.now(), 'Type': 'init', 'Module': 'DFT/QS',
                     'Variable': 'LMAXN0', 'ErrorMessage': errorMessage})
    raise TypeError
    
    
def _validate_LMAXN1(val,errorLog=[]):
  if utilities.is_integer(val) or (val is None):
    return val
  else:
    errorMessage = "LMAXN1 must be an integer."
    errorLog.append({'Date': datetime.datetime.now(), 'Type': 'init', 'Module': 'DFT/QS',
                     'Variable': 'LMAXN1', 'ErrorMessage': errorMessage})
    raise TypeError
    
    
    
def _validate_LS_SCF(val,errorLog=[]):
  if val is not None:
    val = str(val).upper()
  
  if val in BOOL_VALS or (val is None):
        return val
  else:
    errorMessage = ("Invalid option for LS_SCF: {}. Valid options are: {}".format(
                     val,BOOL_VALS))
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'DFT/QS',
                            'Variable':'LS_SCF','ErrorMessage':errorMessage})
    raise TypeError 
    
    
    
def _validate_MAP_CONSISTENT(val,errorLog=[]):
  if val is not None:
    val = str(val).upper()
  
  if val in BOOL_VALS or (val is None):
        return val
  else:
    errorMessage = ("Invalid option for MAP_CONSISTENT: {}. Valid options are: {}".format(
                     val,BOOL_VALS))
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'DFT/QS',
                            'Variable':'MAP_CONSISTENT','ErrorMessage':errorMessage})
    raise TypeError 
    
    
    
def _validate_MAX_RAD_LOCAL(val,errorLog=[]):
  
  return val
    
    
    
def _validate_METHOD(val,errorLog=[]):
  if val is not None:
    val = str(val).upper()
  
  if val in METHOD_VALS or (val is None):
        return val
  else:
    errorMessage = ("Invalid option for METHOD: {}. Valid options are: {}".format(
                     val,BOOL_VALS))
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'DFT/QS',
                            'Variable':'METHOD','ErrorMessage':errorMessage})
    raise TypeError 
    
def _validate_PW_GRID(val,errorLog=[]):
  if val is not None:
    val = str(val).upper()
  
  if val in PW_GRID_VALS or (val is None):
        return val
  else:
    errorMessage = ("Invalid option for PW_GRID: {}. Valid options are: {}".format(
                     val,BOOL_VALS))
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'DFT/QS',
                            'Variable':'PW_GRID','ErrorMessage':errorMessage})
    raise TypeError 

    
def _validate_PW_GRID_BLOCKED(val,errorLog=[]):
  if val is not None:
    val = str(val).upper()
  
  if val in PW_GRID_BLOCKED_VALS or (val is None):
        return val
  else:
    errorMessage = ("Invalid option for PW_GRID_BLOCKED: {}. Valid options are: {}".format(
                     val,BOOL_VALS))
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'DFT/QS',
                            'Variable':'PW_GRID_BLOCKED','ErrorMessage':errorMessage})
    raise TypeError 

    
def _validate_PW_GRID_LAYOUT(val,errorLog=[]):
  if utilities.is_integer(val) or (val is None):
    return val
  else:
    errorMessage = "PW_GRID_LAYOUT must be an integer."
    errorLog.append({'Date': datetime.datetime.now(), 'Type': 'init', 'Module': 'DFT/QS',
                     'Variable': 'PW_GRID_LAYOUT', 'ErrorMessage': errorMessage})
    raise TypeError
    
    
    
def _validate_QUADRATURE(val,errorLog=[]):
  if val is not None:
    val = str(val).upper()
  
  if val in QUADRATURE_VALS or (val is None):
        return val
  else:
    errorMessage = ("Invalid option for QUADRATURE: {}. Valid options are: {}".format(
                     val,BOOL_VALS))
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'DFT/QS',
                            'Variable':'QUADRATURE','ErrorMessage':errorMessage})
    raise TypeError     
  


def _validate_REF_EMBED_SUBSYS(val,errorLog=[]):
  if val is not None:
    val = str(val).upper()
  
  if val in BOOL_VALS or (val is None):
        return val
  else:
    errorMessage = ("Invalid option for REF_EMBED_SUBSYS: {}. Valid options are: {}".format(
                     val,BOOL_VALS))
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'DFT/QS',
                            'Variable':'REF_EMBED_SUBSYS','ErrorMessage':errorMessage})
    raise TypeError 
    
    
    
def _validate_STO_NG(val,errorLog=[]):
  if utilities.is_integer(val) or (val is None):
    return val
  else:
    errorMessage = "STO_NG must be an integer."
    errorLog.append({'Date': datetime.datetime.now(), 'Type': 'init', 'Module': 'DFT/QS',
                     'Variable': 'STO_NG', 'ErrorMessage': errorMessage})
    raise TypeError    
    

def _validate_TRANSPORT(val,errorLog=[]):
  if val is not None:
    val = str(val).upper()
  
  if val in BOOL_VALS or (val is None):
        return val
  else:
    errorMessage = ("Invalid option for TRANSPORT: {}. Valid options are: {}".format(
                     val,BOOL_VALS))
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'DFT/QS',
                            'Variable':'TRANSPORT','ErrorMessage':errorMessage})
    raise TypeError     
    
    
    
    
 
class QS:

  def __init__(self,ALMO_SCF=None,ALPHA0_HARD=None,CLUSTER_EMBED_SUBSYS=None,CORE_PPL=None,DFET_EMBEDDED=None,DMFET_EMBEDDED=None, EMBED_CUBE_FILE_NAME=None, EMBED_RESTART_FILE_NAME=None, EMBED_SPIN_CUBE_FILE_NAME=None, EPSFIT=None, EPSISO=None, EPSRHO0=None,EPSSVD=None, EPS_CORE_CHARGE=None,EPS_CPC=None, EPS_DEFAULT=None, EPS_FILTER_MATRIX=None,EPS_GVG_RSPACE=None, EPS_KG_ORB=None, EPS_PGF_ORB=None, EPS_PPL=None, EPS_PPNL=None, EPS_RHO=None, EPS_RHO_GSPACE=None, EPS_RHO_RSPACE=None, EXTRAPOLATION=None, EXTRAPOLATION_ORDER=None, FORCE_PAW=None, KG_METHOD=None, HIGH_LEVEL_EMBED_SUBSYS=None,  LADDN0=None, LMAXN0=None, LMAXN1=None, LS_SCF=None, MAP_CONSISTENT=None, MAX_RAD_LOCAL=None, METHOD=None, PW_GRID=None, PW_GRID_BLOCKED=None, PW_GRID_LAYOUT=None, QUADRATURE=None, REF_EMBED_SUBSYS=None, STO_NG=None, TRANSPORT=None, errorLog=[],changeLog=[],location=""):
    self.__errorLog = errorLog
    self.__changeLog = changeLog
    self.__ALMO_SCF=_validate_ALMO_SCF(ALMO_SCF, errorLog=self.__errorLog)
    self.__ALPHA0_HARD=_validate_ALPHA0_HARD(ALPHA0_HARD, errorLog=self.__errorLog)
    self.__CLUSTER_EMBED_SUBSYS=_validate_CLUSTER_EMBED_SUBSYS(CLUSTER_EMBED_SUBSYS, errorLog=self.__errorLog)
    self.__CORE_PPL=_validate_CORE_PPL(CORE_PPL,errorLog=self.__errorLog)
    self.__DFET_EMBEDDED=_validate_DFET_EMBEDDED(DFET_EMBEDDED,errorLog=self.__errorLog)
    self.__DMFET_EMBEDDED=_validate_DMFET_EMBEDDED(DMFET_EMBEDDED,errorLog=self.__errorLog)
    self.__EMBED_CUBE_FILE_NAME=_validate_EMBED_CUBE_FILE_NAME(EMBED_CUBE_FILE_NAME,errorLog=self.__errorLog)
    self.__EMBED_RESTART_FILE_NAME=_validate_EMBED_RESTART_FILE_NAME(EMBED_RESTART_FILE_NAME,errorLog=self.__errorLog)
    self.__EMBED_SPIN_CUBE_FILE_NAME=_validate_EMBED_SPIN_CUBE_FILE_NAME(EMBED_SPIN_CUBE_FILE_NAME,errorLog=self.__errorLog)
    self.__EPSFIT=_validate_EPSFIT(EPSFIT,errorLog=self.__errorLog)
    self.__EPSISO=_validate_EPSISO(EPSISO,errorLog=self.__errorLog)
    self.__EPSRHO0=_validate_EPSRHO0(EPSRHO0,errorLog=self.__errorLog)
    self.__EPSSVD=_validate_EPSSVD(EPSSVD,errorLog=self.__errorLog)
    self.__EPS_CORE_CHARGE=_validate_EPS_CORE_CHARGE(EPS_CORE_CHARGE,errorLog=self.__errorLog)
    self.__EPS_CPC=_validate_EPS_CPC(EPS_CPC,errorLog=self.__errorLog)
    self.__EPS_DEFAULT=_validate_EPS_DEFAULT(EPS_DEFAULT,errorLog=self.__errorLog)
    self.__EPS_FILTER_MATRIX=_validate_EPS_FILTER_MATRIX(EPS_FILTER_MATRIX,errorLog=self.__errorLog)
    self.__EPS_GVG_RSPACE=_validate_EPS_GVG_RSPACE(EPS_GVG_RSPACE,errorLog=self.__errorLog)
    self.__EPS_KG_ORB=_validate_EPS_KG_ORB(EPS_KG_ORB,errorLog=self.__errorLog)
    self.__EPS_PGF_ORB=_validate_EPS_PGF_ORB(EPS_PGF_ORB,errorLog=self.__errorLog)
    self.__EPS_PPL=_validate_EPS_PPL(EPS_PPL,errorLog=self.__errorLog)
    self.__EPS_PPNL=_validate_EPS_PPNL(EPS_PPNL,errorLog=self.__errorLog)
    self.__EPS_RHO=_validate_EPS_RHO(EPS_RHO,errorLog=self.__errorLog)
    self.__EPS_RHO_GSPACE=_validate_EPS_RHO_GSPACE(EPS_RHO_GSPACE,errorLog=self.__errorLog)
    self.__EPS_RHO_RSPACE=_validate_EPS_RHO_RSPACE(EPS_RHO_RSPACE,errorLog=self.__errorLog)
    self.__EXTRAPOLATION=_validate_EXTRAPOLATION(EXTRAPOLATION,errorLog=self.__errorLog)
    self.__EXTRAPOLATION_ORDER=_validate_EXTRAPOLATION_ORDER(EXTRAPOLATION_ORDER,errorLog=self.__errorLog)
    self.__FORCE_PAW=_validate_FORCE_PAW(FORCE_PAW,errorLog=self.__errorLog)
    self.__HIGH_LEVEL_EMBED_SUBSYS=_validate_HIGH_LEVEL_EMBED_SUBSYS(HIGH_LEVEL_EMBED_SUBSYS,errorLog=self.__errorLog)
    self.__KG_METHOD=_validate_KG_METHOD(KG_METHOD,errorLog=self.__errorLog)
    self.__LADDN0=_validate_LADDN0(LADDN0,errorLog=self.__errorLog)
    self.__LMAXN0=_validate_LMAXN0(LMAXN0,errorLog=self.__errorLog)
    self.__LMAXN1=_validate_LMAXN1(LMAXN1,errorLog=self.__errorLog)
    self.__LS_SCF=_validate_LS_SCF(LS_SCF,errorLog=self.__errorLog)
    self.__MAP_CONSISTENT=_validate_MAP_CONSISTENT(MAP_CONSISTENT,errorLog=self.__errorLog)
    self.__MAX_RAD_LOCAL=_validate_MAX_RAD_LOCAL(MAX_RAD_LOCAL,errorLog=self.__errorLog)
    self.__METHOD=_validate_METHOD(METHOD,errorLog=self.__errorLog)
    self.__PW_GRID=_validate_PW_GRID(PW_GRID,errorLog=self.__errorLog)
    self.__PW_GRID_BLOCKED=_validate_PW_GRID_BLOCKED(PW_GRID_BLOCKED,errorLog=self.__errorLog)
    self.__PW_GRID_LAYOUT=_validate_PW_GRID_LAYOUT(PW_GRID_LAYOUT,errorLog=self.__errorLog)
    self.__QUADRATURE=_validate_QUADRATURE(QUADRATURE,errorLog=self.__errorLog)
    self.__REF_EMBED_SUBSYS=_validate_REF_EMBED_SUBSYS(REF_EMBED_SUBSYS,errorLog=self.__errorLog)
    self.__STO_NG=_validate_STO_NG(STO_NG,errorLog=self.__errorLog)
    self.__TRANSPORT=_validate_TRANSPORT(TRANSPORT,errorLog=self.__errorLog)

    

    self.__location  = "{}/ENERGY".format(location)
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
  def ALMO_SCF(self):
    return self.__ALMO_SCF

  @property
  def ALPHA0_HARD(self):
    return self.__ALPHA0_HARD

  @property
  def CLUSTER_EMBED_SUBSYS(self):
    return self.__CLUSTER_EMBED_SUBSYS

  @property
  def CORE_PPL(self):
    return self.__CORE_PPL

  @property
  def DFET_EMBEDDED(self):
    return self.__DFET_EMBEDDED

  @property
  def DMFET_EMBEDDED(self):
    return self.__DMFET_EMBEDDED




  @property
  def EMBED_CUBE_FILE_NAME(self):
    return self.__EMBED_CUBE_FILE_NAME

  @property
  def EMBED_RESTART_FILE_NAME(self):
    return self.__EMBED_RESTART_FILE_NAME

  @property
  def EMBED_SPIN_CUBE_FILE_NAME(self):
    return self.__EMBED_SPIN_CUBE_FILE_NAME

  @property
  def EPSFIT(self):
    return self.__EPSFIT

  @property
  def EPSISO(self):
    return self.__EPSISO

  @property
  def EPSRHO0(self):
    return self.__EPSRHO0

  @property
  def EPSSVD(self):
    return self.__EPSSVD

  @property
  def EPS_CORE_CHARGE(self):
    return self.__EPS_CORE_CHARGE

  @property
  def EPS_CPC(self):
    return self.__EPS_CPC

  @property
  def EPS_DEFAULT(self):
    return self.__EPS_DEFAULT

  @property
  def EPS_FILTER_MATRIX(self):
    return self.__EPS_FILTER_MATRIX

  @property
  def EPS_GVG_RSPACE(self):
    return self.__EPS_GVG_RSPACE

  @property
  def EPS_KG_ORB(self):
    return self.__EPS_KG_ORB

  @property
  def EPS_PGF_ORB(self):
    return self.__EPS_PGF_ORB

  @property
  def EPS_PPL(self):
    return self.__EPS_PPL

  @property
  def EPS_PPNL(self):
    return self.__EPS_PPNL

  @property
  def EPS_RHO(self):
    return self.__EPS_RHO

  @property
  def EPS_RHO_GSPACE(self):
    return self.__EPS_RHO_GSPACE

  @property
  def EPS_RHO_RSPACE(self):
    return self.__EPS_RHO_RSPACE

  @property
  def EXTRAPOLATION(self):
    return self.__EXTRAPOLATION

  @property
  def EXTRAPOLATION_ORDER(self):
    return self.__EXTRAPOLATION_ORDER

  @property
  def FORCE_PAW(self):
    return self.__FORCE_PAW

  @property
  def HIGH_LEVEL_EMBED_SUBSYS(self):
    return self.__HIGH_LEVEL_EMBED_SUBSYS

  @property
  def KG_METHOD(self):
    return self.__KG_METHOD

  @property
  def LADDN0(self):
    return self.__LADDN0

  @property
  def LMAXN0(self):
    return self.__LMAXN0

  @property
  def LMAXN1(self):
    return self.__LMAXN1

  @property
  def LS_SCF(self):
    return self.__LS_SCF

  @property
  def MAP_CONSISTENT(self):
    return self.__MAP_CONSISTENT

  @property
  def MAX_RAD_LOCAL(self):
    return self.__MAX_RAD_LOCAL

  @property
  def METHOD(self):
    return self.__METHOD


  @property
  def PW_GRID(self):
    return self.__PW_GRID

  @property
  def PW_GRID_BLOCKED(self):
    return self.__PW_GRID_BLOCKED


  @property
  def PW_GRID_LAYOUT(self):
    return self.__PW_GRID_LAYOUT

  @property
  def QUADRATURE(self):
    return self.__QUADRATURE


  @property
  def REF_EMBED_SUBSYS(self):
    return self.__REF_EMBED_SUBSYS

  @property
  def STO_NG(self):
    return self.__STO_NG


  @property
  def TRANSPORT(self):
    return self.__TRANSPORT


  
    
    
  @ALMO_SCF.setter
  def ALMO_SCF(self, val):
    val = str(val).upper()
    if val in BOOL_VALS:
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT/QS', 'Variable': 'ALMO_SCF',
                               'Success': True, 'Previous': self.__ALMO_SCF, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__ALMO_SCF = val
    else:
      errorMessage = ("Invalid option for ALMO_SCF: {}. Valid options are: {}".format(val, BOOL_VALS))
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT/QS', 'Variable': 'ALMO_SCF',
                               'Success': False, 'Previous': self.__ALMO_SCF, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'DFT/QS',
                              'Variable': ' ALMO_SCF', 'ErrorMessage': errorMessage,
                              'Location': self.__location}) 
    
  @ALPHA0_HARD.setter
  def ALPHA0_HARD(self, val):
    
    
    self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT/QS', 'Variable': 'ALPHA0_HARD',
                               'Success': True, 'Previous': self.__ALPHA0_HARD, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
    self.__ALPHA0_HARD= val   
    
    
  @CLUSTER_EMBED_SUBSYS.setter
  def CLUSTER_EMBED_SUBSYS(self, val):
    val = str(val).upper()
    if val in BOOL_VALS:
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT/QS', 'Variable': 'CLUSTER_EMBED_SUBSYS',
                               'Success': True, 'Previous': self.__CLUSTER_EMBED_SUBSYS, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__CLUSTER_EMBED_SUBSYS = val
    else:
      errorMessage = ("Invalid option for CLUSTER_EMBED_SUBSYS: {}. Valid options are: {}".format(val, BOOL_VALS))
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT/QS', 'Variable': 'CLUSTER_EMBED_SUBSYS',
                               'Success': False, 'Previous': self.__CLUSTER_EMBED_SUBSYS, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'DFT/QS',
                              'Variable': ' CLUSTER_EMBED_SUBSYS', 'ErrorMessage': errorMessage,
                              'Location': self.__location})   
   

  @CORE_PPL.setter
  def CORE_PPL(self, val):
    val = str(val).upper()
    if val in CORE_PPL_VALS:
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT/QS', 'Variable': 'CORE_PPL',
                               'Success': True, 'Previous': self.__CORE_PPL, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__CORE_PPL = val
    else:
      errorMessage = ("Invalid option for CORE_PPL: {}. Valid options are: {}".format(val, CORE_PPL_VALS))
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT/QS', 'Variable': 'CORE_PPL',
                               'Success': False, 'Previous': self.__CORE_PPL, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'DFT/QS',
                              'Variable': ' CORE_PPL', 'ErrorMessage': errorMessage,
                              'Location': self.__location})  
   


  @DFET_EMBEDDED.setter
  def DFET_EMBEDDED(self, val):
    val = str(val).upper()
    if val in BOOL_VALS:
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT/QS', 'Variable': 'DFET_EMBEDDED',
                               'Success': True, 'Previous': self.__DFET_EMBEDDED ,'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__DFET_EMBEDDED = val
    else:
      errorMessage = ("Invalid option for DFET_EMBEDDED: {}. Valid options are: {}".format(val, BOOL_VALS))
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT/QS', 'Variable': 'DFET_EMBEDDED',
                               'Success': False, 'Previous': self.__DFET_EMBEDDED, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'DFT/QS',
                              'Variable': ' DFET_EMBEDDED', 'ErrorMessage': errorMessage,
                              'Location': self.__location})  
    
  @DMFET_EMBEDDED.setter
  def DMFET_EMBEDDED(self, val):
    val = str(val).upper()
    if val in BOOL_VALS:
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT/QS', 'Variable': 'DMFET_EMBEDDED',
                               'Success': True, 'Previous': self.__DMFET_EMBEDDED ,'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__DMFET_EMBEDDED = val
    else:
      errorMessage = ("Invalid option for DMFET_EMBEDDED: {}. Valid options are: {}".format(val, BOOL_VALS))
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT/QS', 'Variable': 'DMFET_EMBEDDED',
                               'Success': False, 'Previous': self.__DMFET_EMBEDDED, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'DFT/QS',
                              'Variable': ' DMFET_EMBEDDED', 'ErrorMessage': errorMessage,
                              'Location': self.__location})
    

    
  @EMBED_CUBE_FILE_NAME.setter
  def EMBED_CUBE_FILE_NAME(self, val):
    
    
    self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT/QS', 'Variable': 'EMBED_CUBE_FILE_NAME',
                               'Success': True, 'Previous': self.__EMBED_CUBE_FILE_NAME, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
    self.__EMBED_CUBE_FILE_NAME= val 
    
    
  @EMBED_RESTART_FILE_NAME.setter
  def EMBED_RESTART_FILE_NAME(self, val):
    
    
    self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT/QS', 'Variable': 'EMBED_RESTART_FILE_NAME',
                               'Success': True, 'Previous': self.__EMBED_CUBE_FILE_NAME, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
    self.__EMBED_RESTART_FILE_NAME= val 
    
       
  @EMBED_SPIN_CUBE_FILE_NAME.setter
  def EMBED_SPIN_CUBE_FILE_NAME(self, val):
    
    
    self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT/QS', 'Variable': 'EMBED_SPIN_CUBE_FILE_NAME',
                               'Success': True, 'Previous': self.__EMBED_CUBE_FILE_NAME, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
    self.__EMBED_SPIN_CUBE_FILE_NAME= val 
    
       
  @EPSFIT.setter
  def EPSFIT(self, val):
    
    
    self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT/QS', 'Variable': 'EPSFIT',
                               'Success': True, 'Previous': self.__EPSFIT, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
    self.__EPSFIT= val 
    
  @EPSISO.setter
  def EPSISO(self, val):
    
    
    self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT/QS', 'Variable': 'EPSISO',
                               'Success': True, 'Previous': self.__EPSISO, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
    self.__EPSISO= val 
  


  @EPSRHO0.setter
  def EPSRHO0(self, val):
    
    
    self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT/QS', 'Variable': 'EPSRHO0',
                               'Success': True, 'Previous': self.__EPSRHO0, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
    self.__EPSRHO0= val 
    
  @EPSSVD.setter
  def EPSSVD(self, val):
    
    
    self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT/QS', 'Variable': 'EPSSVD',
                               'Success': True, 'Previous': self.__EPSSVD, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
    self.__EPSSVD= val
    
  @EPS_CORE_CHARGE.setter
  def EPS_CORE_CHARGE(self, val):
    
    
    self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT/QS', 'Variable': 'EPS_CORE_CHARGE',
                               'Success': True, 'Previous': self.__EPS_CORE_CHARGE, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
    self.__EPS_CORE_CHARGE= val
    
    
    
  @EPS_CPC.setter
  def EPS_CPC(self, val):
    
    
    self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT/QS', 'Variable': 'EPS_CPC',
                               'Success': True, 'Previous': self.__EPS_CPC, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
    self.__EPS_CPC= val  
    
  @EPS_DEFAULT.setter
  def EPS_DEFAULT(self, val):
    
    
    self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT/QS', 'Variable': 'EPS_DEFAULT',
                               'Success': True, 'Previous': self.__EPS_DEFAULT, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
    self.__EPS_DEFAULT= val
    
    
  @EPS_FILTER_MATRIX.setter
  def EPS_FILTER_MATRIX(self, val):
    
    
    self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT/QS', 'Variable': 'EPS_FILTER_MATRIX',
                               'Success': True, 'Previous': self.__EPS_FILTER_MATRIX, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
    self.__EPS_FILTER_MATRIX= val
    
  @EPS_GVG_RSPACE.setter
  def EPS_GVG_RSPACE(self, val):
    
    
    self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT/QS', 'Variable': 'EPS_GVG_RSPACE',
                               'Success': True, 'Previous': self.__EPS_GVG_RSPACE, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
    self.__EPS_GVG_RSPACE= val
    
  @EPS_KG_ORB.setter
  def EPS_KG_ORB(self, val):
    
    
    self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT/QS', 'Variable': 'EPS_KG_ORB',
                               'Success': True, 'Previous': self.__EPS_KG_ORB, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
    self.__EPS_KG_ORB= val
    
  @EPS_PGF_ORB.setter
  def EPS_PGF_ORB(self, val):
    
    
    self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT/QS', 'Variable': 'EPS_PGF_ORB',
                               'Success': True, 'Previous': self.__EPS_PGF_ORB, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
    self.__EPS_PGF_ORB= val
    
  @EPS_PGF_ORB.setter
  def EPS_PGF_ORB(self, val):
    
    
    self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT/QS', 'Variable': 'EPS_PGF_ORB',
                               'Success': True, 'Previous': self.__EPS_PGF_ORB, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
    self.__EPS_PGF_ORB= val
    
  @EPS_PPL.setter
  def EPS_PPL(self, val):
    
    
    self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT/QS', 'Variable': 'EPS_PPL',
                               'Success': True, 'Previous': self.__EPS_PPL, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
    self.__EPS_PPL= val
    
    
  @EPS_PPNL.setter
  def EPS_PPNL(self, val):
    
    
    self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT/QS', 'Variable': 'EPS_PPNL',
                               'Success': True, 'Previous': self.__EPS_PPNL, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
    self.__EPS_PPNL= val
    
    
  @EPS_RHO.setter
  def EPS_RHO(self, val):
    
    
    self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT/QS', 'Variable': 'EPS_RHO',
                               'Success': True, 'Previous': self.__EPS_RHO, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
    self.__EPS_RHO= val
    
    
  @EPS_RHO_GSPACE.setter
  def EPS_RHO_GSPACE(self, val):
    
    
    self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT/QS', 'Variable': 'EPS_RHO_GSPACE',
                               'Success': True, 'Previous': self.__EPS_RHO_GSPACE, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
    self.__EPS_RHO_GSPACE= val
    
    
    
  @EPS_RHO_RSPACE.setter
  def EPS_RHO_RSPACE(self, val):
    
    
    self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT/QS', 'Variable': 'EPS_RHO_RSPACE',
                               'Success': True, 'Previous': self.__EPS_RHO_RSPACE, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
    self.__EPS_RHO_RSPACE= val
    
    
    
    
    
  @EXTRAPOLATION.setter
  def EXTRAPOLATION(self, val):
    val = str(val).upper()
    if val in EXTRAPOLATION_VALS:
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT/QS', 'Variable': 'EXTRAPOLATION',
                               'Success': True, 'Previous': self.__EXTRAPOLATION ,'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__EXTRAPOLATION= val
    else:
      errorMessage = ("Invalid option for EXTRAPOLATION: {}. Valid options are: {}".format(val, EXTRAPOLATION_VALS))
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT/QS', 'Variable': 'EXTRAPOLATION',
                               'Success': False, 'Previous': self.__EXTRAPOLATION, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'DFT/QS',
                              'Variable': ' EXTRAPOLATION', 'ErrorMessage': errorMessage,
                              'Location': self.__location})
    
    
    
  @EXTRAPOLATION_ORDER.setter
  def EXTRAPOLATION_ORDER(self, val):
    if utilities.is_integer(val):
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT/QS', 'Variable': 'EXTRAPOLATION_ORDER',
                               'Success': True, 'Previous': self.__EXTRAPOLATION_ORDER, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__EXTRAPOLATION_ORDER = val
    else:
      errorMessage = "EXTRAPOLATION_ORDER must be aN integer."
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT/QS', 'Variable': 'EXTRAPOLATION_ORDER',
                               'Success': False, 'Previous': self.__EXTRAPOLATION_ORDER, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'DFT/QS',
                              'Variable': 'EXTRAPOLATION_ORDER', 'ErrorMessage': errorMessage,
                              'Location': self.__location}) 
    
  @FORCE_PAW.setter
  def FORCE_PAW(self, val):
    val = str(val).upper()
    if val in BOOL_VALS:
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT/QS', 'Variable': 'FORCE_PAW',
                               'Success': True, 'Previous': self.__FORCE_PAW ,'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__FORCE_PAW= val
    else:
      errorMessage = ("Invalid option for FORCE_PAW: {}. Valid options are: {}".format(val, BOOL_VALS))
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT/QS', 'Variable': 'FORCE_PAW',
                               'Success': False, 'Previous': self.__FORCE_PAW, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'DFT/QS',
                              'Variable': ' FORCE_PAW', 'ErrorMessage': errorMessage,
                              'Location': self.__location})
    
  @HIGH_LEVEL_EMBED_SUBSYS.setter
  def HIGH_LEVEL_EMBED_SUBSYS(self, val):
    val = str(val).upper()
    if val in BOOL_VALS:
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT/QS', 'Variable': 'HIGH_LEVEL_EMBED_SUBSYS',
                               'Success': True, 'Previous': self.__HIGH_LEVEL_EMBED_SUBSYS ,'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__HIGH_LEVEL_EMBED_SUBSYS= val
    else:
      errorMessage = ("Invalid option for HIGH_LEVEL_EMBED_SUBSYS: {}. Valid options are: {}".format(val, BOOL_VALS))
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT/QS', 'Variable': 'HIGH_LEVEL_EMBED_SUBSYS',
                               'Success': False, 'Previous': self.__HIGH_LEVEL_EMBED_SUBSYS, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'DFT/QS',
                              'Variable': ' HIGH_LEVEL_EMBED_SUBSYS', 'ErrorMessage': errorMessage,
                              'Location': self.__location})
    
    
  @KG_METHOD.setter
  def KG_METHOD(self, val):
    val = str(val).upper()
    if val in BOOL_VALS:
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT/QS', 'Variable': 'KG_METHOD',
                               'Success': True, 'Previous': self.__KG_METHOD ,'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__KG_METHOD= val
    else:
      errorMessage = ("Invalid option for KG_METHOD: {}. Valid options are: {}".format(val, BOOL_VALS))
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT/QS', 'Variable': 'KG_METHOD',
                               'Success': False, 'Previous': self.__KG_METHOD, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'DFT/QS',
                              'Variable': ' KG_METHOD', 'ErrorMessage': errorMessage,
                              'Location': self.__location})
    
    
  @LADDN0.setter
  def LADDN0(self, val):
    if utilities.is_integer(val):
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT/QS', 'Variable': 'LADDN0',
                               'Success': True, 'Previous': self.__LADDN0, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__LADDN0 = val
    else:
      errorMessage = "LADDN0 must be aN integer."
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT/QS', 'Variable': 'LADDN0',
                               'Success': False, 'Previous': self.__LADDN0, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'DFT/QS',
                              'Variable': 'LADDN0', 'ErrorMessage': errorMessage,
                              'Location': self.__location}) 
  @LMAXN0.setter
  def LMAXN0(self, val):
    if utilities.is_integer(val):
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT/QS', 'Variable': 'LMAXN0',
                               'Success': True, 'Previous': self.__LMAXN0, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__LMAXN0 = val
    else:
      errorMessage = "LMAXN0 must be aN integer."
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT/QS', 'Variable': 'LMAXN0',
                               'Success': False, 'Previous': self.__LMAXN0, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'DFT/QS',
                              'Variable': 'LMAXN0', 'ErrorMessage': errorMessage,
                              'Location': self.__location}) 
    
  @LMAXN1.setter
  def LMAXN1(self, val):
    if utilities.is_integer(val):
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT/QS', 'Variable': 'LMAXN1',
                               'Success': True, 'Previous': self.__LMAXN1, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__LMAXN1 = val
    else:
      errorMessage = "LMAXN1 must be aN integer."
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT/QS', 'Variable': 'LMAXN1',
                               'Success': False, 'Previous': self.__LMAXN1, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'DFT/QS',
                              'Variable': 'LMAXN1', 'ErrorMessage': errorMessage,
                              'Location': self.__location}) 
    
    
    
        
  @LS_SCF.setter
  def LS_SCF(self, val):
    val = str(val).upper()
    if val in BOOL_VALS:
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT/QS', 'Variable': 'LS_SCF',
                               'Success': True, 'Previous': self.__LS_SCF ,'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__LS_SCF= val
    else:
      errorMessage = ("Invalid option for LS_SCF: {}. Valid options are: {}".format(val, BOOL_VALS))
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT/QS', 'Variable': 'LS_SCF',
                               'Success': False, 'Previous': self.__LS_SCF, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'DFT/QS',
                              'Variable': ' LS_SCF', 'ErrorMessage': errorMessage,
                              'Location': self.__location})
    
    
        
  @MAP_CONSISTENT.setter
  def MAP_CONSISTENT(self, val):
    val = str(val).upper()
    if val in BOOL_VALS:
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT/QS', 'Variable': 'MAP_CONSISTENT',
                               'Success': True, 'Previous': self.__MAP_CONSISTENT ,'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__MAP_CONSISTENT= val
    else:
      errorMessage = ("Invalid option for MAP_CONSISTENT: {}. Valid options are: {}".format(val, BOOL_VALS))
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT/QS', 'Variable': 'MAP_CONSISTENT',
                               'Success': False, 'Previous': self.__MAP_CONSISTENT, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'DFT/QS',
                              'Variable': ' MAP_CONSISTENT', 'ErrorMessage': errorMessage,
                              'Location': self.__location})
    
    
  @MAX_RAD_LOCAL.setter
  def MAX_RAD_LOCAL(self, val):
    
    
    self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT/QS', 'Variable': 'MAX_RAD_LOCAL',
                               'Success': True, 'Previous': self.__MAX_RAD_LOCAL, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
    self.__MAX_RAD_LOCAL= val
    
    
    
    
    
  @METHOD.setter
  def METHOD(self, val):
    val = str(val).upper()
    if val in METHOD_VALS:
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT/QS', 'Variable': 'METHOD',
                               'Success': True, 'Previous': self.__METHOD ,'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__METHOD= val
    else:
      errorMessage = ("Invalid option for METHOD: {}. Valid options are: {}".format(val, METHOD_VALS))
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT/QS', 'Variable': 'METHOD',
                               'Success': False, 'Previous': self.__METHOD, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'DFT/QS',
                              'Variable': ' METHOD', 'ErrorMessage': errorMessage,
                              'Location': self.__location})
    
        
  @PW_GRID.setter
  def PW_GRID(self, val):
    val = str(val).upper()
    if val in PW_GRID_VALS:
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT/QS', 'Variable': 'PW_GRID',
                               'Success': True, 'Previous': self.__PW_GRID ,'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__PW_GRID= val
    else:
      errorMessage = ("Invalid option for PW_GRID: {}. Valid options are: {}".format(val, PW_GRID_VALS))
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT/QS', 'Variable': 'PW_GRID',
                               'Success': False, 'Previous': self.__PW_GRID, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'DFT/QS',
                              'Variable': ' PW_GRID', 'ErrorMessage': errorMessage,
                              'Location': self.__location})
    
    
        
  @PW_GRID_BLOCKED.setter
  def PW_GRID_BLOCKED(self, val):
    val = str(val).upper()
    if val in PW_GRID_BLOCKED_VALS:
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT/QS', 'Variable': 'PW_GRID_BLOCKED',
                               'Success': True, 'Previous': self.__PW_GRID_BLOCKED ,'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__PW_GRID_BLOCKED= val
    else:
      errorMessage = ("Invalid option for PW_GRID_BLOCKED: {}. Valid options are: {}".format(val, PW_GRID_BLOCKED_VALS))
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT/QS', 'Variable': 'PW_GRID_BLOCKED',
                               'Success': False, 'Previous': self.__PW_GRID_BLOCKED, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'DFT/QS',
                              'Variable': ' PW_GRID_BLOCKED', 'ErrorMessage': errorMessage,
                              'Location': self.__location})
    
    
    
    
  @PW_GRID_LAYOUT.setter
  def PW_GRID_LAYOUT(self, val):
    if utilities.is_integer(val):
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT/QS', 'Variable': 'PW_GRID_LAYOUT',
                               'Success': True, 'Previous': self.__PW_GRID_LAYOUT, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__PW_GRID_LAYOUT = val
    else:
      errorMessage = "PW_GRID_LAYOUT must be aN integer."
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT/QS', 'Variable': 'PW_GRID_LAYOUT',
                               'Success': False, 'Previous': self.__PW_GRID_LAYOUT, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'DFT/QS',
                              'Variable': 'PW_GRID_LAYOUT', 'ErrorMessage': errorMessage,
                              'Location': self.__location}) 
    
    
    
    
  @QUADRATURE.setter
  def QUADRATURE(self, val):
    val = str(val).upper()
    if val in QUADRATURE_VALS:
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT/QS', 'Variable': 'QUADRATURE',
                               'Success': True, 'Previous': self.__QUADRATURE ,'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__QUADRATURE= val
    else:
      errorMessage = ("Invalid option for PW_GRID_BLOCKED: {}. Valid options are: {}".format(val, QUADRATURE_VALS))
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT/QS', 'Variable': 'QUADRATURE',
                               'Success': False, 'Previous': self.__QUADRATURE, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'DFT/QS',
                              'Variable': ' QUADRATURE', 'ErrorMessage': errorMessage,
                              'Location': self.__location})

    
    
  @REF_EMBED_SUBSYS.setter
  def REF_EMBED_SUBSYS(self, val):
    val = str(val).upper()
    if val in BOOL_VALS:
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT/QS', 'Variable': 'REF_EMBED_SUBSYS',
                               'Success': True, 'Previous': self.__REF_EMBED_SUBSYS ,'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__REF_EMBED_SUBSYS= val
    else:
      errorMessage = ("Invalid option for REF_EMBED_SUBSYS: {}. Valid options are: {}".format(val, BOOL_VALS))
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT/QS', 'Variable': 'REF_EMBED_SUBSYS',
                               'Success': False, 'Previous': self.__REF_EMBED_SUBSYS, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'DFT/QS',
                              'Variable': ' REF_EMBED_SUBSYS', 'ErrorMessage': errorMessage,
                              'Location': self.__location})
    
    
  @STO_NG.setter
  def STO_NG(self, val):
    if utilities.is_integer(val):
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT/QS', 'Variable': 'STO_NG',
                               'Success': True, 'Previous': self.__STO_NG, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__STO_NG= val
    else:
      errorMessage = "STO_NG must be aN integer."
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT/QS', 'Variable': 'STO_NG',
                               'Success': False, 'Previous': self.__STO_NG, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'DFT/QS',
                              'Variable': 'STO_NG', 'ErrorMessage': errorMessage,
                              'Location': self.__location}) 
    
    
  @TRANSPORT.setter
  def TRANSPORT(self, val):
    val = str(val).upper()
    if val in BOOL_VALS:
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT/QS', 'Variable': 'TRANSPORT',
                               'Success': True, 'Previous': self.__TRANSPORT ,'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__TRANSPORT= val
    else:
      errorMessage = ("Invalid option for REF_EMBED_SUBSYS: {}. Valid options are: {}".format(val, BOOL_VALS))
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'DFT/QS', 'Variable': 'TRANSPORT',
                               'Success': False, 'Previous': self.__TRANSPORT, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'DFT/QS',
                              'Variable': ' TRANSPORT', 'ErrorMessage': errorMessage,
                              'Location': self.__location})
    
  