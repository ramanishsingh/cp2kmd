import datetime
import cssi_cp2k.utilities as utilities


def _validate_length(val):
  if utilities.is_positive_integer(val) or (val is None):
    return val
  else:
    errorMessage = "Nose LENGTH must be a positive integer."
    self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'NOSE',
                            'Variable':'LENGTH','ErrorMessage':errorMessage})
    raise TypeError

def _validate_yoshida(val):
  if utilities.is_positive_integer(val) or (val is None):
    return val
  else:
    errorMessage = "Nose YOSHIDA integrator order must be a positive integer."
    self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'NOSE',
                            'Variable':'YOSHIDA','ErrorMessage':errorMessage})
    raise TypeError

def _validate_timecon(val):
  if utilities.is_positive_number(val) or (val is None):
    return val
  else:
    errorMessage = "Nose TIMECON must be a positive number."
    self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'NOSE',
                            'Variable':'YOSHIDA','ErrorMessage':errorMessage})
    raise TypeError

def _validate_mts(val):
  if utilities.is_positive_integer(val) or (val is None):
    return val
  else:
    errorMessage = "Nose MTS must be a positive number."
    self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'NOSE',
                            'Variable':'YOSHIDA','ErrorMessage':errorMessage})
    raise TypeError

class NOSE:

  def __init__(self,LENGTH=None,MTS=None,TIMECON=None,YOSHIDA=None,errorLog=[],changeLog=[],
               location=""):
    
    self.__LENGTH    = _validate_length(LENGTH)
    self.__MTS       = _validate_mts(MTS)
    self.__TIMECON   = _validate_timecon(TIMECON)
    self.__YOSHIDA   = _validate_yoshida(YOSHIDA)
    self.__errorLog  = errorLog
    self.__changeLog = changeLog
    self.__location  = "{}/NOSE".format(location)

  @property
  def LENGTH(self):
    return self.__LENGTH

  @property
  def MTS(self):
    return self.__MTS

  @property
  def TIMECON(self):
    return self.__TIMECON

  @property
  def YOSHIDA(self):
    return self.__YOSHIDA

  @property
  def errorLog(self):
    return self.__errorLog
  
  @property
  def changeLog(self):
    return self.__changeLog

  @property
  def location(self):
    return self.__location

  @LENGTH.setter
  def LENGTH(self,val):
    if utilities.is_positive_integer(val):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'NOSE','Variable':'LENGTH',
                               'Success':True,'Previous':self.__LENGTH,'New':val,'ErrorMessage':None,
                               'Location':self.__location})
      self.__LENGTH = val
    else:
      errorMessage = "Nose LENGTH must be a positive integer."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'NOSE','Variable':'LENGTH',
                               'Success':False,'Previous':self.__LENGTH,'New':val,
                               'ErrorMessage':errorMessage,'Location':self.__location})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Module':'NOSE',
                              'Variable':'LENGTH','ErrorMessage':errorMessage,'Location':self.__location})

  @MTS.setter
  def MTS(self,val):
    if utilities.is_positive_integer(val):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'NOSE','Variable':'MTS',
                               'Success':True,'Previous':self.__MTS,'New':val,'ErrorMessage':None,
                               'Location':self.__location})
      self.__MTS = val
    else:
      errorMessage = "Nose number of multiple time steps (MTS) must be a positive integer."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'NOSE','Variable':'MTS',
                               'Success':False,'Previous':self.__MTS,'New':val,
                               'ErrorMessage':errorMessage,'Location':self.__location})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Module':'NOSE',
                              'Variable':'MTS','ErrorMessage':errorMessage,'Location':self.__location})

  @TIMECON.setter
  def TIMECON(self,val):
    if utilities.is_positive_number(val):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'NOSE','Variable':'TIMECON',
                               'Success':True,'Previous':self.__MTS,'New':val,'ErrorMessage':None,
                               'Location':self.__location})
      self.__TIMECON = val
    else:
      errorMessage = "Nose TIMECON must be a positive number."
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Module':'NOSE',
                              'Variable':'TIMECON','ErrorMessage':errorMessage,'Location':self.__location})
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'NOSE','Variable':'TIMECON',
                               'Success':False,'Previous':self.__TIMECON,'New':val,
                               'ErrorMessage':errorMessage,'Location':self.__location})

  @YOSHIDA.setter
  def YOSHIDA(self,val):
    if utilities.is_positive_integer(val):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'NOSE','Variable':'YOSHIDA',
                               'Success':True,'Previous':self.__YOSHIDA,'New':val,'ErrorMessage':None,
                               'Location':self.__location})
      self.__YOSHIDA = val
    else:
      errorMessage = "Nose YOSHIDA integrator order must be a positive integer."
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Module':'NOSE',
                              'Variable':'YOSHIDA','ErrorMessage':errorMessage,'Location':self.__location})
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'NOSE','Variable':'YOSHIDA',
                               'Success':False,'Previous':self.__YOSHIDA,'New':val,
                               'ErrorMessage':errorMessage,'Location':self.__location})
