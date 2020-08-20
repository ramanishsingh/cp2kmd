import datetime
import cssi_cp2k.utilities as utilities


VIRIAL_VALS = ["X","XY","XYZ","XZ","Y","YZ","Z"]


def _validate_virial(val,errorLog=[]):

  if val is not None:
    val = str(val).upper()

  if val in VIRIAL_VALS or (val is None):
    return val
  else:
    errorMessage = ("Invalid option for MD BAROSTAT VIRIAL: {}. Valid options are: {}".format(
                     val,VIRIAL_VALS))
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'BAROSTAT',
                            'Variable':'VIRIAL','ErrorMessage':errorMessage})
    raise TypeError

def _validate_pressure(val,errorLog=[]):
  if utilities.is_number(val) or (val is None):
    return val
  else:
    errorMessage = "PRESSURE must be a number."
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'BAROSTAT',
                            'Variable':'PRESSURE','ErrorMessage':errorMessage})
    raise TypeError   
    
def _validate_temperature(val,errorLog=[]):
  if utilities.is_number(val) or (val is None):
    return val
  else:
    errorMessage = "BAROSTAT TEMPERATURE must be a number."
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'BAROSTAT',
                            'Variable':'TEMPERATURE','ErrorMessage':errorMessage})
    raise TypeError  
    
def _validate_temp_tol(val,errorLog=[]):
  if utilities.is_number(val) or (val is None):
    return val
  else:
    errorMessage = "BAROSTAT TEMP_TOL must be a number."
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'BAROSTAT',
                            'Variable':'TEMP_TOL','ErrorMessage':errorMessage})
    raise TypeError
    
def _validate_timecon(val,errorLog=[]):
  if utilities.is_number(val) or (val is None):
    return val
  else:
    errorMessage = "BAROSTAT TIMECON must be a number."
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'BAROSTAT',
                            'Variable':'TIMECON','ErrorMessage':errorMessage})
    raise TypeError

class BAROSTAT:
    


  def __init__(self,PRESSURE=None,TEMPERATURE=None, TEMP_TOL=None, TIMECON=None, VIRIAL=None,errorLog=[],changeLog=[],location=""):
    """

   
    """

    self.__errorLog  = errorLog
    self.__changeLog = changeLog
    self.__VIRIAL    = _validate_virial(VIRIAL,errorLog=self.__errorLog)
    self.__PRESSURE    = _validate_pressure(PRESSURE,errorLog=self.__errorLog)
    self.__TEMPERATURE    = _validate_temperature(TEMPERATURE,errorLog=self.__errorLog)
    self.__TEMP_TOL    = _validate_temp_tol(TEMP_TOL,errorLog=self.__errorLog)
    self.__TIMECON    = _validate_timecon(TIMECON,errorLog=self.__errorLog)
   
    self.__location  = "{}/BAROSTAT".format(location)
    

  @property
  def PRESSURE(self):
    return self.__PRESSURE

  @property
  def TEMPERATURE(self):
    return self.__TEMPERATURE
  @property
  def TEMP_TOL(self):
    return self.__TEMP_TOL
  @property
  def TIMECON(self):
    return self.__TIMECON
  @property
  def VIRIAL(self):
    return self.__VIRIAL

  @property
  def errorLog(self):
    return self.__errorLog

  @property
  def changeLog(self):
    return self.__changeLog

  @property
  def location(self):
    return self.__location



  @VIRIAL.setter
  def VIRIAL(self,val):
    val = str(val).upper()
    if val in VIRIAL_VALS:
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'BAROSTAT','Variable':'VIRIAL',
                               'Success':True,'Previous':self.__VIRIAL,'New':val,
                               'ErrorMessage':None,'Location':self.__location})
      self.__VIRIAL = val
    else:
      errorMessage = ("Invalid option for MD BAROSTAT VIRIAL: {}. Valid options are: {}".format(val,
                       VIRIAL_VALS))
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'BAROSTAT','Variable':'VIRIAL',
                               'Success':False,'Previous':self.__VIRIAL,'New':val,
                               'ErrorMessage':errorMessage,'Location':self.__location})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Module':'BAROSTAT',
                              'Variable':'VIRIAL','ErrorMessage':errorMessage,'Location':self.__location})

  
  @PRESSURE.setter
  def PRESSURE(self, val):
    if utilities.is_number(val):
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'BAROSTAT', 'Variable': 'PRESSURE',
                               'Success': True, 'Previous': self.__PRESSURE, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__PRESSURE = val
    else:
      errorMessage = "PRESSURE must be a number."
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'BAROSTAT', 'Variable': 'PRESSURE',
                               'Success': False, 'Previous': self.__PRESSURE, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'BAROSTAT',
                              'Variable': 'PRESSURE', 'ErrorMessage': errorMessage,
                              'Location': self.__location})
    
  @TEMPERATURE.setter
  def TEMPERATURE(self, val):
    if utilities.is_number(val):
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'BAROSTAT', 'Variable': 'TEMPERATURE',
                               'Success': True, 'Previous': self.__TEMPERATURE, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__TEMPERATURE = val
    else:
      errorMessage = "PRESSURE must be a number."
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'BAROSTAT', 'Variable': 'TEMPERATURE',
                               'Success': False, 'Previous': self.__TEMPERATURE, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'BAROSTAT',
                              'Variable': 'TEMPERATURE', 'ErrorMessage': errorMessage,
                              'Location': self.__location})
    
  @TEMP_TOL.setter
  def TEMP_TOL(self, val):
    if utilities.is_number(val):
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'BAROSTAT', 'Variable': 'TEMP_TOL',
                               'Success': True, 'Previous': self.__TEMP_TOL, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__TEMP_TOL = val
    else:
      errorMessage = "PRESSURE must be a number."
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'BAROSTAT', 'Variable': 'TEMP_TOL',
                               'Success': False, 'Previous': self.__TEMP_TOL, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'BAROSTAT',
                              'Variable': 'TEMP_TOL', 'ErrorMessage': errorMessage,
                              'Location': self.__location})
    
  @TIMECON.setter
  def TIMECON(self, val):
    if utilities.is_number(val):
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'BAROSTAT', 'Variable': 'TIMECON',
                               'Success': True, 'Previous': self.__TIMECON, 'New': val,
                               'ErrorMessage': None, 'Location': self.__location})
      self.__TIMECON = val
    else:
      errorMessage = "PRESSURE must be a number."
      self.__changeLog.append({'Date': datetime.datetime.now(), 'Module': 'BAROSTAT', 'Variable': 'TIMECON',
                               'Success': False, 'Previous': self.__TIMECON, 'New': val,
                               'ErrorMessage': errorMessage, 'Location': self.__location})
      self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'BAROSTAT',
                              'Variable': 'TIMECON', 'ErrorMessage': errorMessage,
                              'Location': self.__location})
 