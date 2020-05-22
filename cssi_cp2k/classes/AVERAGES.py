import datetime
import cssi_cp2k.utilities as utilities

BOOL_VALS = [".TRUE.",".FALSE."]


def _validate_SECTION_PARAMETERS(val,errorLog=[]):

  if val is not None:
    val = str(val).upper()

  if val in BOOL_VALS or (val is None):
    return val
  else:
    errorMessage = ("Invalid option for SECTION_PARAMETERS: {}. Valid options are: {}".format(
                     val,BOOL_VALS))
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'AVERAGES',
                            'Variable':'SECTION_PARAMETERS','ErrorMessage':errorMessage})
    raise TypeError

def _validate_ACQUISITION_START_TIME(val,errorLog=[]):


  if utilities.is_positive_number(val) or (val is None):
    return val
  else:
    errorMessage = ("Invalid option for ACQUISITION_START_TIME: {}. Must be a positive number".format(
                     val))
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'AVERAGES',
                            'Variable':'ACQUISITION_START_TIME','ErrorMessage':errorMessage})
    raise TypeError

def _validate_AVERAGE_COLVAR(val,errorLog=[]):

  if val is not None:
    val = str(val).upper()

  if val in BOOL_VALS or (val is None):
    return val
  else:
    errorMessage = ("Invalid option for AVERAGE_COLVAR: {}. Valid options are: {}".format(
                     val,BOOL_VALS))
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'AVERAGES',
                            'Variable':'AVERAGE_COLVAR','ErrorMessage':errorMessage})
    raise TypeError

class AVERAGES:

  def __init__(self,SECTION_PARAMETERS=None,ACQUISITION_START_TIME=None,AVERAGE_COLVAR=None,errorLog=[],changeLog=[],location=""):

    self.__errorLog  = errorLog
    self.__changeLog = changeLog
    self.__SECTION_PARAMETERS      = _validate_SECTION_PARAMETERS(SECTION_PARAMETERS,errorLog=self.__errorLog)
    self.__ACQUISITION_START_TIME    = _validate_ACQUISITION_START_TIME(ACQUISITION_START_TIME,errorLog=self.__errorLog)
    self.__AVERAGE_COLVAR = _validate_AVERAGE_COLVAR(ACQUISITION_START_TIME, errorLog=self.__errorLog)
    self.__location  = "{}/AVERAGES".format(location)
    #AVERAGES subsections
    #self.__PRINT_AVERAGES      = PRINT_AVERAGES.PRINT_AVERAGES(errorLog=self.__errorLog,changeLog=self.__changeLog,
    #                     location=self.__location)
    #self.__RESTART_AVERAGES = RESTART_AVERAGES.RESTART_AVERAGES(errorLog=self.__errorLog, changeLog=self.__changeLog,
    #                       location=self.__location)

  @property
  def SECTION_PARAMETERS(self):
    return self.__SECTION_PARAMETERS

  @property
  def ACQUISITION_START_TIME(self):
    return self.__ACQUISITION_START_TIME

  @property
  def AVERAGE_COLVAR(self):
      return self.__AVERAGE_COLVAR

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
  def PRINT_AVERAGES(self):
    return self.__PRINT_AVERAGES

  @property
  def RESTART_AVERAGES(self):
    return self.__RESTART_AVERAGES

  @property
  def AVERAGE_COLVAR(self):
      return self.__AVERAGE_COLVAR

  @SECTION_PARAMETERS.setter
  def SECTION_PARAMETERS(self,val):
    val = str(val).upper()
    if val in BOOL_VALS:
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'AVERAGES','Variable':'SECTION_PARAMETERS',
                               'Success':True,'Previous':self.__SECTION_PARAMETERS,'New':val,
                               'ErrorMessage':None,'Location':self.__location})
      self.__SECTION_PARAMETERS = val
    else:
      errorMessage = ("Invalid option for SECTION_PARAMETERS: {}. Valid options are: {}".format(
                        val,BOOL_VALS))
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'AVERAGES','Variable':'SECTION_PARAMETERS',
                               'Success':False,'Previous':self.__SECTION_PARAMETERS,'New':val,
                               'ErrorMessage':errorMessage,'Location':self.__location})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Module':'AVERAGES',
                              'Variable':'SECTION_PARAMETERS','ErrorMessage':errorMessage,'Location':self.__location})


  @ACQUISITION_START_TIME.setter
  def ACQUISITION_START_TIME(self, val):
      if utilities.is_positive_number(val):

          self.__changeLog.append(
              {'Date': datetime.datetime.now(), 'Module': 'AVERAGES', 'Variable': 'ACQUISITION_START_TIME',
               'Success': True, 'Previous': self.__ACQUISITION_START_TIME, 'New': val,
               'ErrorMessage': None, 'Location': self.__location})
          self.__ACQUISITION_START_TIME = val
      else:
          errorMessage = ("Invalid option for ACQUISITION_START_TIME: {}".format(
              val))
          self.__changeLog.append(
              {'Date': datetime.datetime.now(), 'Module': 'AVERAGES', 'Variable': 'ACQUISITION_START_TIME',
               'Success': False, 'Previous': self.__ACQUISITION_START_TIME, 'New': val,
               'ErrorMessage': errorMessage, 'Location': self.__location})
          self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'AVERAGES',
                                  'Variable': 'ACQUISITION_START_TIME', 'ErrorMessage': errorMessage,
                                  'Location': self.__location})

  @AVERAGE_COLVAR.setter
  def AVERAGE_COLVAR(self, val):
      val = str(val).upper()
      if val in BOOL_VALS:
          self.__changeLog.append(
              {'Date': datetime.datetime.now(), 'Module': 'AVERAGES', 'Variable': 'AVERAGE_COLVAR',
               'Success': True, 'Previous': self.__AVERAGE_COLVAR, 'New': val,
               'ErrorMessage': None, 'Location': self.__location})
          self.__AVERAGE_COLVAR = val
      else:
          errorMessage = ("Invalid option for AVERAGE_COLVAR: {}. Valid options are: {}".format(
              val, BOOL_VALS))
          self.__changeLog.append(
              {'Date': datetime.datetime.now(), 'Module': 'AVERAGES', 'Variable': 'AVERAGE_COLVAR',
               'Success': False, 'Previous': self.__AVERAGE_COLVAR, 'New': val,
               'ErrorMessage': errorMessage, 'Location': self.__location})
          self.__errorLog.append({'Date': datetime.datetime.now(), 'Type': 'Setter', 'Module': 'AVERAGES',
                                  'Variable': 'AVERAGE_COLVAR', 'ErrorMessage': errorMessage,
                                  'Location': self.__location})
