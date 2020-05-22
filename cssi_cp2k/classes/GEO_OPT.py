import datetime
import cssi_cp2k.utilities as utilities


OPTIMIZER_VALS = ["BFGS","CG","LBFGS"]
TYPE_VALS = ["MINIMIZATION","TRANSITION_STATE"]

def _validate_optimizer(val,errorLog=[]):
  if val is not None:
    val = str(val).upper()
  if val in OPTIMIZER_VALS or (val is None):
    return val
  else:
    errorMessage = "Invalid option for GEO_OPT optimizer: {}. Valid options are: {}".format(val,OPTIMIZER_VALS)
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'GEO_OPT',
                            'Variable':'OPTIMIZER','ErrorMessage':errorMessage})
    raise TypeError("{}".format(val))

def _validate_RMS_DR(val,errorLog=[]):


  return val

def _validate_RMS_FORCE(val,errorLog=[]):


  return val

def _validate_MAX_DR(val,errorLog=[]):


  return val

def _validate_MAX_FORCE(val,errorLog=[]):


  return val

def _validate_MAX_ITER(val,errorLog=[]):
  if utilities.is_positive_integer(val) or (val is None):
    return val
  else:
    errorMessage = "GEO_OPT MAX_ITER must be an integer."
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'GEO_OPT',
                            'Variable':'MAX_ITER','ErrorMessage':errorMessage})
    raise TypeError

  return val

def _validate_STEP_START_VAL(val,errorLog=[]):
  if utilities.is_positive_integer(val) or (val is None):
    return val
  else:
    errorMessage = "The starting step value for the GEO_OPT module must be an integer."
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'GEO_OPT',
                            'Variable':'STEP_START_VAL','ErrorMessage':errorMessage})
    raise TypeError

  return val

def _validate_TYPE(val,errorLog=[]):
  if val is not None:
    val = str(val).upper()
  if val in TYPE_VALS or (val is None):
    return val
  else:
    errorMessage = "Invalid option for kind of geometry optimization to perform: {}. Valid options are: {}".format(val,OPTIMIZER_VALS)
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'GEO_OPT',
                            'Variable':'TYPE','ErrorMessage':errorMessage})
    raise TypeError("{}".format(val))



class GEO_OPT:

  def __init__(self,MAX_DR=None,MAX_FORCE=None,MAX_ITER=None,OPTIMIZER=None,RMS_DR=None,RMS_FORCE=None,STEP_START_VAL=None,TYPE=None, errorLog=[],changeLog=[],
               location=""):

    self.__errorLog    = errorLog
    self.__changeLog   = changeLog
    self.__MAX_DR    = _validate_MAX_DR(MAX_DR,errorLog=self.__errorLog)
    self.__MAX_FORCE       = _validate_MAX_FORCE(MAX_FORCE,errorLog=self.__errorLog)
    self.__MAX_ITER    = _validate_MAX_ITER(MAX_ITER,errorLog=self.__errorLog)
    self.__OPTIMIZER = _validate_optimizer(OPTIMIZER,errorLog=self.__errorLog)
    self.__RMS_DR = _validate_RMS_DR(RMS_DR, errorLog=self.__errorLog)
    self.__RMS_FORCE = _validate_RMS_FORCE(RMS_FORCE, errorLog=self.__errorLog)
    self.__STEP_START_VAL = _validate_STEP_START_VAL(STEP_START_VAL, errorLog=self.__errorLog)
    self.__TYPE = _validate_TYPE(TYPE, errorLog=self.__errorLog)
    self.__location    = "{}/GEO_OPT".format(location)
    #MD subesctions


    #self.__BFGS  = bfgs.BFGS(errorLog=self.__errorLog,changeLog=self.__changeLog,
     #                      location=self.__location)

  @property
  def MAX_DR(self):
    return self.__MAX_DR

  @property
  def MAX_FORCE(self):
    return self.__MAX_FORCE

  @property
  def MAX_ITER(self):
    return self.__MAX_ITER

  @property
  def OPTIMIZER(self):
    return self.__OPTIMIZER

  @property
  def RMS_DR(self):
    return self.__RMS_DR

  @property
  def RMS_FORCE(self):
    return self.__RMS_FORCE

  @property
  def STEP_START_VAL(self):
    return self.__STEP_START_VAL

  @property
  def TYPE(self):
    return self.__TYPE

  @property
  def errorLog(self):
    return self.__errorLog

  @property
  def changeLog(self):
    return self.__changeLog

  @property
  def location(self):
    return self.__location

  #@property
  #def THERMOSTAT(self):
  #  return self.__THERMOSTAT


  @OPTIMIZER.setter
  def OPTIMIZER(self,val):
    val = str(val).upper()
    if val in OPTIMIZER_VALS:
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'GEO_OPT','Variable':'MAX_DR',
                               'Success':True,'Previous':self.__OPTIMIZER,'New':val,'ErrorMessage':None,
                               'Location':self.__location})
      self.__OPTIMIZER = val
    else:
      errorMessage = "Invalid option for OPTIMIZER in GEO_OPT: {}. Valid options are: {}".format(MD_ENSEMBLE_VALS)
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'GEO_OPT','Variable':'OPTIMIZER',
                               'Success':False,'Previous':self.__OPTIMIZER,'New':val,
                               'ErrorMessage':errorMessage,'Location':self.__location})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Module':'GEO_OPT',
                              'Variable':'OPTIMIZER','ErrorMessage':errorMessage,'Location':self.__location})


  @TYPE.setter
  def TYPE(self,val):
    val = str(val).upper()
    if val in TYPE_VALS:
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'GEO_OPT','Variable':'TYPE',
                               'Success':True,'Previous':self.__TYPE,'New':val,'ErrorMessage':None,
                               'Location':self.__location})
      self.__TYPE = val
    else:
      errorMessage = "Invalid option for TYPE in GEO_OPT: {}. Valid options are: {}".format(val, TYPE_VALS)
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'GEO_OPT','Variable':'TYPE',
                               'Success':False,'Previous':self.__TYPE,'New':val,
                               'ErrorMessage':errorMessage,'Location':self.__location})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Module':'GEO_OPT',
                              'Variable':'TYPE','ErrorMessage':errorMessage,'Location':self.__location})
     
  @MAX_DR.setter
  def MAX_DR(self,val):
    if utilities.is_positive_integer(val):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'GEO_OPT','Variable':'MAX_DR',
                               'Success':True,'Previous':self.__MAX_DR,'New':val,'ErrorMessage':None,
                               'Location':self.__location})
      self.__MAX_DR = val
    else:
      errorMessage = "MAX_DR must be a positive integer."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'GEO_OPT','Variable':'MAX_DR',
                               'Success':False,'Previous':self.__MAX_DR,'New':val,
                               'ErrorMessage':errorMessage,'Location':self.__location})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Module':'GEO_OPT',
                              'Variable':'MAX_DR','ErrorMessage':errorMessage,'Location':self.__location})

  @MAX_FORCE.setter
  def MAX_DR(self, val):
    if utilities.is_positive_number(val):
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'GEO_OPT', 'Variable': 'MAX_FORCE',
                               'Success': True, 'Previous': self.__MAX_FORCE, 'New': val, 'ErrorMessage': None,
                               'Location': self.__location})
      self.__MAX_FORCE = val
    else:
      errorMessage = "MAX_FORCE must be a positive NUMBER."
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'GEO_OPT', 'Variable': 'MAX_FORCE',
                               'Success': False, 'Previous': self.__MAX_DR, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'GEO_OPT',
                              'Variable': 'MAX_FORCE', 'ErrorMessage': errorMessage, 'Location': self.__location})

  @MAX_ITER.setter
  def MAX_ITER(self, val):
      if utilities.is_positive_integer(val):
          self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'GEO_OPT', 'Variable': 'MAX_ITER',
                                   'Success': True, 'Previous': self.__MAX_ITER, 'New': val, 'ErrorMessage': None,
                                   'Location': self.__location})
          self.__MAX_ITER = val
      else:
          errorMessage = "MAX_ITER must be a positive integer."
          self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'GEO_OPT', 'Variable': 'MAX_ITER',
                                   'Success': False, 'Previous': self.__MAX_ITER, 'New': val,
                                   'ErrorMessage': errorMessage, 'Location': self.__location})
          self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'GEO_OPT',
                                  'Variable': 'MAX_ITER', 'ErrorMessage': errorMessage, 'Location': self.__location})

  @RMS_DR.setter
  def RMS_DR(self, val):
      if utilities.is_positive_number(val):
          self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'GEO_OPT', 'Variable': 'RMS_DR',
                                   'Success': True, 'Previous': self.__RMS_DR, 'New': val, 'ErrorMessage': None,
                                   'Location': self.__location})
          self.__RMS_DR = val
      else:
          errorMessage = "RMS_DR must be a positive NUMBER."
          self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'GEO_OPT', 'Variable': 'RMS_DR',
                                   'Success': False, 'Previous': self.__MAX_DR, 'New': val,
                                   'ErrorMessage': errorMessage, 'Location': self.__location})
          self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'GEO_OPT',
                                  'Variable': 'RMS_DR', 'ErrorMessage': errorMessage, 'Location': self.__location})

  @RMS_FORCE.setter
  def RMS_FORCE(self, val):
      if utilities.is_positive_number(val):
          self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'GEO_OPT', 'Variable': 'RMS_FORCE',
                                   'Success': True, 'Previous': self.__RMS_FORCE, 'New': val, 'ErrorMessage': None,
                                   'Location': self.__location})
          self.__RMS_FORCE = val
      else:
          errorMessage = "RMS_FORCE must be a positive NUMBER."
          self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'GEO_OPT', 'Variable': 'RMS_FORCE',
                                   'Success': False, 'Previous': self.__RMS_FORCE, 'New': val,
                                   'ErrorMessage': errorMessage, 'Location': self.__location})
          self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'GEO_OPT',
                                  'Variable': 'RMS_FORCE', 'ErrorMessage': errorMessage, 'Location': self.__location})

  @STEP_START_VAL.setter
  def STEP_START_VAL(self, val):
      if utilities.is_positive_integer(val):
          self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'GEO_OPT', 'Variable': 'STEP_START_VAL',
                                   'Success': True, 'Previous': self.__STEP_START_VAL, 'New': val, 'ErrorMessage': None,
                                   'Location': self.__location})
          self.__STEP_START_VAL = val
      else:
          errorMessage = "STEP_START_VAL must be a positive integer."
          self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'GEO_OPT', 'Variable': 'STEP_START_VAL',
                                   'Success': False, 'Previous': self.__STEP_START_VAL, 'New': val,
                                   'ErrorMessage': errorMessage, 'Location': self.__location})
          self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'GEO_OPT',
                                  'Variable': 'STEP_START_VAL', 'ErrorMessage': errorMessage, 'Location': self.__location})

