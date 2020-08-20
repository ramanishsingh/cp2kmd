import datetime
import cssi_cp2k.utilities as utilities
from cssi_cp2k.classes import EACH
from cssi_cp2k.classes import OT
from cssi_cp2k.classes import SCF_PRINT
from cssi_cp2k.classes import OUTER_SCF
BOOL_VALS   = [".TRUE.",".FALSE"]
CHOLESKY_VALS=['INVERSE','INVERSE_DBCSR','OFF','REDUCE','RESTORE']
ROKS_SCHEME_VALS=['GENERAL','HIGH-SPIN']
SCF_GUESS_VALS=['ATOMIC','CORE','HISTORY_RESTART','MOPAC','NONE','RANDOM','RESTART','SPARSE']

def _validate_ADDED_MOS(val,errorLog=[]):
  if utilities.is_integer(val) or (val is None):
    return val
  else:
    errorMessage = "ADDED_MOS  must be AN integer."
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'SCF',
                            'Variable':'ADDED_MOS','ErrorMessage':errorMessage})
    raise TypeError



def _validate_CHOLESKY(val,errorLog=[]):
  if val is not None:
    val = str(val).upper()

  if val in CHOLESKY_VALS or (val is None):
    return val
  else:
    errorMessage = ("Invalid option for CHOLESKY: {}. Valid options are: {}".format(
                     val,CHOLESKY_VALS))
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'SCF',
                            'Variable':'CHOLESKY','ErrorMessage':errorMessage})
    raise TypeError


def _validate_EPS_DIIS(val,errorLog=[]):
    return val
def _validate_EPS_EIGVAL(val,errorLog=[]):
    return val
def _validate_EPS_LUMO(val,errorLog=[]):
    return val
def _validate_EPS_SCF(val,errorLog=[]):
    return val
def _validate_EPS_SCF_HISTORY(val,errorLog=[]):
    return val
def _validate_LEVEL_SHIFT(val,errorLog=[]):
    return val



def _validate_MAX_DIIS(val,errorLog=[]):
  if utilities.is_integer(val) or (val is None):
    return val
  else:
    errorMessage = "MAX_DIIS  must be AN integer."
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'SCF',
                            'Variable':'MAX_DIIS','ErrorMessage':errorMessage})
    raise TypeError

def _validate_MAX_ITER_LUMO(val,errorLog=[]):
  if utilities.is_integer(val) or (val is None):
    return val
  else:
    errorMessage = "MAX_ITER_LUMO  must be AN integer."
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'SCF',
                            'Variable':'MAX_ITER_LUMO','ErrorMessage':errorMessage})
    raise TypeError

def _validate_MAX_SCF(val,errorLog=[]):
  if utilities.is_integer(val) or (val is None):
    return val
  else:
    errorMessage = "MAX_SCF  must be AN integer."
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'SCF',
                            'Variable':'MAX_SCF','ErrorMessage':errorMessage})
    raise TypeError

def _validate_MAX_SCF_HISTORY(val,errorLog=[]):
  if utilities.is_integer(val) or (val is None):
    return val
  else:
    errorMessage = "MAX_SCF_HISTORY  must be AN integer."
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'SCF',
                            'Variable':'MAX_SCF_HISTORY','ErrorMessage':errorMessage})
    raise TypeError

def _validate_NCOL_BLOCK(val,errorLog=[]):
  if utilities.is_integer(val) or (val is None):
    return val
  else:
    errorMessage = "NCOL_BLOCK  must be AN integer."
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'SCF',
                            'Variable':'NCOL_BLOCK','ErrorMessage':errorMessage})
    raise TypeError

    
    
    

def _validate_NOTCONV_STOPALL(val,errorLog=[]):
  if val is not None:
    val = str(val).upper()

  if val in BOOL_VALS or (val is None):
    return val
  else:
    errorMessage = ("Invalid option for NOTCONV_STOPALL: {}. Valid options are: {}".format(
                     val,BOOL_VALS))
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'SCF',
                            'Variable':'NOTCONV_STOPALL','ErrorMessage':errorMessage})
    raise TypeError
 




def _validate_NROW_BLOCK(val,errorLog=[]):
  if utilities.is_integer(val) or (val is None):
    return val
  else:
    errorMessage = "NROW_BLOCK level must be AN integer."
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'SCF',
                            'Variable':'NROW_BLOCK','ErrorMessage':errorMessage})
    raise TypeError
    
    
def _validate_ROKS_F(val,errorLog=[]):
    return val    



    
def _validate_ROKS_PARAMETERS(val,errorLog=[]):
    return val




def _validate_ROKS_SCHEME(val,errorLog=[]):
  if val is not None:
    val = str(val).upper()

  if val in ROKS_SCHEME_VALS or (val is None):
    return val
  else:
    errorMessage = ("Invalid option for ROKS_SCHEME: {}. Valid options are: {}".format(
                     val,ROKS_SCHEME_VALS))
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'SCF',
                            'Variable':'ROKS_SCHEME','ErrorMessage':errorMessage})
    raise TypeError

    
    
    


def _validate_SCF_GUESS(val,errorLog=[]):
  if val is not None:
    val = str(val).upper()

  if val in SCF_GUESS_VALS or (val is None):
    return val
  else:
    errorMessage = ("Invalid option for SCF_GUESS: {}. Valid options are: {}".format(
                     val,SCF_GUESS_VALS))
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'SCF',
                            'Variable':'SCF_GUESS','ErrorMessage':errorMessage})
    raise TypeError
    
    
    
class SCF:

  def __init__(self,ADDED_MOS=None, CHOLESKY=None,EPS_DIIS=None,EPS_EIGVAL=None,EPS_LUMO=None,EPS_SCF=None,EPS_SCF_HISTORY=None,LEVEL_SHIFT=None,MAX_DIIS=None,MAX_ITER_LUMO=None,MAX_SCF=None,MAX_SCF_HISTORY=None,NCOL_BLOCK=None,NOTCONV_STOPALL=None,NROW_BLOCK=None,ROKS_F=None,ROKS_PARAMETERS=None,ROKS_SCHEME=None,SCF_GUESS=None, errorLog=[],changeLog=[],location=""):
    self.__errorLog = errorLog
    self.__changeLog = changeLog
    self.__ADDED_MOS=_validate_ADDED_MOS(ADDED_MOS, errorLog=self.__errorLog)
    self.__CHOLESKY=_validate_CHOLESKY(CHOLESKY, errorLog=self.__errorLog)
    self.__EPS_DIIS=_validate_EPS_DIIS(EPS_DIIS, errorLog=self.__errorLog)
    self.__EPS_EIGVAL=_validate_EPS_EIGVAL(EPS_EIGVAL,errorLog=self.__errorLog)
    self.__EPS_LUMO=_validate_EPS_LUMO(EPS_LUMO,errorLog=self.__errorLog)
    self.__EPS_SCF=_validate_EPS_SCF(EPS_SCF,errorLog=self.__errorLog)
    self.__EPS_SCF_HISTORY=_validate_EPS_SCF_HISTORY(EPS_SCF_HISTORY,errorLog=self.__errorLog)
    self.__LEVEL_SHIFT=_validate_LEVEL_SHIFT(LEVEL_SHIFT,errorLog=self.__errorLog)
    self.__MAX_DIIS=_validate_MAX_DIIS(MAX_DIIS,errorLog=self.__errorLog)
    self.__MAX_ITER_LUMO=_validate_MAX_ITER_LUMO(MAX_ITER_LUMO,errorLog=self.__errorLog)
    self.__MAX_SCF=_validate_MAX_SCF(MAX_SCF,errorLog=self.__errorLog)
    self.__MAX_SCF_HISTORY=_validate_MAX_SCF_HISTORY(MAX_SCF_HISTORY,errorLog=self.__errorLog)
    self.__NCOL_BLOCK=_validate_NCOL_BLOCK(NCOL_BLOCK,errorLog=self.__errorLog)
    self.__NOTCONV_STOPALL=_validate_NOTCONV_STOPALL(NOTCONV_STOPALL,errorLog=self.__errorLog)
    self.__NROW_BLOCK=_validate_NROW_BLOCK(NROW_BLOCK,errorLog=self.__errorLog)
    self.__ROKS_F=_validate_ROKS_F(ROKS_F,errorLog=self.__errorLog)
    self.__ROKS_PARAMETERS=_validate_ROKS_PARAMETERS(ROKS_PARAMETERS,errorLog=self.__errorLog)
    self.__ROKS_SCHEME=_validate_ROKS_SCHEME(ROKS_SCHEME,errorLog=self.__errorLog)
    self.__SCF_GUESS=_validate_SCF_GUESS(SCF_GUESS,errorLog=self.__errorLog)


    

    self.__location  = "{}/SCF".format(location)
    self.__OT=OT.OT(errorLog=self.__errorLog,changeLog=self.__changeLog,location=self.__location)
    self.__PRINT=SCF_PRINT.PRINT(errorLog=self.__errorLog,changeLog=self.__changeLog,location=self.__location)
    self.__OUTER_SCF=OUTER_SCF.OUTER_SCF(errorLog=self.__errorLog,changeLog=self.__changeLog,location=self.__location)
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
  def ADDED_MOS(self):
    return self.__ADDED_MOS

  @property
  def CHOLESKY(self):
    return self.__CHOLESKY

  @property
  def EPS_DIIS(self):
    return self.__EPS_DIIS


  @property
  def EPS_EIGVAL(self):
    return self.__EPS_EIGVAL

  @property
  def EPS_LUMO(self):
    return self.__EPS_LUMO

  @property
  def EPS_SCF(self):
    return self.__EPS_SCF

  @property
  def EPS_SCF_HISTORY(self):
    return self.__EPS_SCF_HISTORY

  @property
  def LEVEL_SHIFT(self):
    return self.__LEVEL_SHIFT


  @property
  def MAX_DIIS(self):
    return self.__MAX_DIIS
  @property
  def MAX_ITER_LUMO(self):
    return self.__MAX_ITER_LUMO

  @property
  def MAX_SCF(self):
    return self.__MAX_SCF

  @property
  def MAX_SCF_HISTORY(self):
    return self.__MAX_SCF_HISTORY

  @property
  def NCOL_BLOCK(self):
    return self.__NCOL_BLOCK

  @property
  def NOTCONV_STOPALL(self):
    return self.__NOTCONV_STOPALL

  @property
  def NROW_BLOCK(self):
    return self.__NROW_BLOCK


  @property
  def ROKS_F(self):
    return self.__ROKS_F

  @property
  def ROKS_PARAMETERS(self):
    return self.__ROKS_PARAMETERS

  @property
  def ROKS_SCHEME(self):
    return self.__ROKS_SCHEME


  @property
  def SCF_GUESS(self):
    return self.__SCF_GUESS

  @property
  def OT(self):
    return self.__OT
  @property
  def PRINT(self):
    return self.__PRINT
  @property
  def OUTER_SCF(self):
    return self.__OUTER_SCF

#





  @ADDED_MOS.setter
  def ADDED_MOS(self, val):
    if utilities.is_integer(val):
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SCF', 'Variable': 'ADDED_MOS',
                               'Success': True, 'Previous': self.__ADDED_MOS, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__ADDED_MOS = val
    else:
      errorMessage = "ADDED_MOS must be a positive integer."
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SCF', 'Variable': 'ADDED_MOS',
                               'Success': False, 'Previous': self.__ADDED_MOS, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'SCF',
                              'Variable': 'ADDED_MOS', 'ErrorMessage': errorMessage,
                              'Location': self.__location})

    
    

  @CHOLESKY.setter
  def CHOLESKY(self, val):
    val = str(val).upper()
    if val in CHOLESKY_VALS:
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SCF', 'Variable': 'CHOLESKY',
                               'Success': True, 'Previous': self.__CHOLESKY, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__CHOLESKY= val
    else:
      errorMessage = ("Invalid option for CHOLESKY: {}. Valid options are: {}".format(val,CHOLESKY_VALS))
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SCF', 'Variable': 'CHOLESKY',
                               'Success': False, 'Previous': self.__CHOLESKY, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'SCF',
                              'Variable': 'CHOLESKY', 'ErrorMessage': errorMessage, 'Location': self.__location})
    
    
    
    
    
  @EPS_DIIS.setter
  def EPS_DIIS(self,val):
    self.__EPS_DIIS=val
 

    
  @EPS_EIGVAL.setter
  def EPS_EIGVAL(self,val):
    self.__EPS_EIGVAL=val
 
    
  @EPS_LUMO.setter
  def EPS_LUMO(self,val):
    self.__EPS_LUMO=val
 
    
  @EPS_SCF.setter
  def EPS_SCF(self,val):
    self.__EPS_SCF=val
 
    
  @EPS_SCF_HISTORY.setter
  def EPS_SCF_HISTORY(self,val):
    self.__EPS_SCF_HISTORY=val
 
    
  @LEVEL_SHIFT.setter
  def LEVEL_SHIFT(self,val):
    self.__LEVEL_SHIFT=val
 





  @MAX_DIIS.setter
  def MAX_DIIS(self, val):
    if utilities.is_integer(val):
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SCF', 'Variable': 'MAX_DIIS',
                               'Success': True, 'Previous': self.__MAX_DIIS, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__MAX_DIIS = val
    else:
      errorMessage = "MAX_DIIS must be a positive integer."
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SCF', 'Variable': 'MAX_DIIS',
                               'Success': False, 'Previous': self.__MAX_DIIS, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'SCF',
                              'Variable': 'MAX_DIIS', 'ErrorMessage': errorMessage,
                              'Location': self.__location})

    
  @MAX_DIIS.setter
  def MAX_DIIS(self, val):
    if utilities.is_integer(val):
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SCF', 'Variable': 'MAX_DIIS',
                               'Success': True, 'Previous': self.__MAX_DIIS, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__MAX_DIIS = val
    else:
      errorMessage = "MAX_DIIS must be a positive integer."
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SCF', 'Variable': 'MAX_DIIS',
                               'Success': False, 'Previous': self.__MAX_DIIS, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'SCF',
                              'Variable': 'MAX_DIIS', 'ErrorMessage': errorMessage,
                              'Location': self.__location})

    
  @MAX_ITER_LUMO.setter
  def MAX_ITER_LUMO(self, val):
    if utilities.is_integer(val):
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SCF', 'Variable': 'MAX_ITER_LUMO',
                               'Success': True, 'Previous': self.__MAX_ITER_LUMO, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__MAX_ITER_LUMO = val
    else:
      errorMessage = "MAX_ITER_LUMO must be a positive integer."
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SCF', 'Variable': 'MAX_ITER_LUMO',
                               'Success': False, 'Previous': self.__MAX_ITER_LUMO, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'SCF',
                              'Variable': 'MAX_ITER_LUMO', 'ErrorMessage': errorMessage,
                              'Location': self.__location})

    
    
  @MAX_SCF.setter
  def MAX_SCF(self, val):
    if utilities.is_integer(val):
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SCF', 'Variable': 'MAX_SCF',
                               'Success': True, 'Previous': self.__MAX_SCF, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__MAX_SCF = val
    else:
      errorMessage = "MAX_SCF must be a positive integer."
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SCF', 'Variable': 'MAX_SCF',
                               'Success': False, 'Previous': self.__MAX_SCF, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'SCF',
                              'Variable': 'MAX_SCF', 'ErrorMessage': errorMessage,
                              'Location': self.__location})

    
    
  @MAX_SCF_HISTORY.setter
  def MAX_SCF_HISTORY(self, val):
    if utilities.is_integer(val):
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SCF', 'Variable': 'MAX_SCF_HISTORY',
                               'Success': True, 'Previous': self.__MAX_SCF_HISTORY, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__MAX_SCF_HISTORY = val
    else:
      errorMessage = "MAX_SCF_HISTORY must be a positive integer."
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SCF', 'Variable': 'MAX_SCF_HISTORY',
                               'Success': False, 'Previous': self.__MAX_SCF_HISTORY, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'SCF',
                              'Variable': 'MAX_SCF_HISTORY', 'ErrorMessage': errorMessage,
                              'Location': self.__location})

    
    
  @NCOL_BLOCK.setter
  def NCOL_BLOCK(self, val):
    if utilities.is_integer(val):
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SCF', 'Variable': 'NCOL_BLOCK',
                               'Success': True, 'Previous': self.__NCOL_BLOCK, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__NCOL_BLOCK = val
    else:
      errorMessage = "NCOL_BLOCK must be a positive integer."
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SCF', 'Variable': 'NCOL_BLOCK',
                               'Success': False, 'Previous': self.__NCOL_BLOCK, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'SCF',
                              'Variable': 'NCOL_BLOCK', 'ErrorMessage': errorMessage,
                              'Location': self.__location})
    
    
    
  @NOTCONV_STOPALL.setter
  def NOTCONV_STOPALL(self, val):
    val = str(val).upper()
    if val in BOOL_VALS:
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SCF', 'Variable': 'NOTCONV_STOPALL',
                               'Success': True, 'Previous': self.__NOTCONV_STOPALL, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__NOTCONV_STOPALL= val
    else:
      errorMessage = ("Invalid option for NOTCONV_STOPALL: {}. Valid options are: {}".format(val,BOOL_VALS))
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SCF', 'Variable': 'NOTCONV_STOPALL',
                               'Success': False, 'Previous': self.__NOTCONV_STOPALL, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'SCF',
                              'Variable': 'NOTCONV_STOPALL', 'ErrorMessage': errorMessage, 'Location': self.__location})
    

  @NROW_BLOCK.setter
  def NROW_BLOCK(self, val):
    if utilities.is_integer(val):
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SCF', 'Variable': 'NROW_BLOCK',
                               'Success': True, 'Previous': self.__NROW_BLOCK, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__NROW_BLOCK = val
    else:
      errorMessage = "NROW_BLOCK must be a positive integer."
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SCF', 'Variable': 'NROW_BLOCK',
                               'Success': False, 'Previous': self.__NROW_BLOCK, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'SCF',
                              'Variable': 'NROW_BLOCK', 'ErrorMessage': errorMessage,
                              'Location': self.__location})   
    
    
  @ROKS_F.setter
  def ROKS_F(self,val):
    self.__ROKS_F=val
 
    
  @ROKS_PARAMETERS.setter
  def ROKS_PARAMETERS(self,val):
    self.__ROKS_PARAMETERS=val
    
    
  @ROKS_SCHEME.setter
  def ROKS_SCHEME(self, val):
    if utilities.is_integer(val):
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SCF', 'Variable': 'ROKS_SCHEME',
                               'Success': True, 'Previous': self.__ROKS_SCHEME, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__ROKS_SCHEME = val
    else:
      errorMessage = "ROKS_SCHEME must be a positive integer."
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SCF', 'Variable': 'ROKS_SCHEME',
                               'Success': False, 'Previous': self.__ROKS_SCHEME, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'SCF',
                              'Variable': 'ROKS_SCHEME', 'ErrorMessage': errorMessage,
                              'Location': self.__location}) 
    

    
    
  @SCF_GUESS.setter
  def SCF_GUESS(self, val):
    val = str(val).upper()
    if val in SCF_GUESS_VALS:
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SCF', 'Variable': 'SCF_GUESS',
                               'Success': True, 'Previous': self.__SCF_GUESS, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__SCF_GUESS= val
    else:
      errorMessage = ("Invalid option for SCF_GUESS: {}. Valid options are: {}".format(val,SCF_GUESS_VALS))
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'SCF', 'Variable': 'SCF_GUESS',
                               'Success': False, 'Previous': self.__SCF_GUESS, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'SCF',
                              'Variable': 'SCF_GUESS', 'ErrorMessage': errorMessage, 'Location': self.__location})
    
    
 