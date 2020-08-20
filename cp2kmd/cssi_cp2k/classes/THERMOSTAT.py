import datetime
import cssi_cp2k.utilities as utilities
from cssi_cp2k.classes import NOSE
from cssi_cp2k.classes import GLE

REGION_VALS = ["DEFINED","GLOBAL","MASSIVE","MOLECULE","NONE"]
TYPE_VALS   = ["AD_LANGEVIN","CSVR","GLE","NOSE"]

def _validate_region(val,errorLog=[]):

  if val is not None:
    val = str(val).upper()

  if val in REGION_VALS or (val is None):
    return val
  else:
    errorMessage = ("Invalid option for MD THERMOSTAT REGION: {}. Valid options are: {}".format(
                     val,REGION_VALS))
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'THERMOSTAT',
                            'Variable':'REGION','ErrorMessage':errorMessage})
    raise TypeError

def _validate_type(val,errorLog=[]):

  if val is not None:
    val = str(val).upper()

  if val in TYPE_VALS or (val is None):
    return val
  else:
    errorMessage = ("Invalid option for MD THERMOSTAT TYPE: {}. Valid options are: {}".format(
                     val,TYPE_VALS))
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'THERMOSTAT',
                            'Variable':'TYPE','ErrorMessage':errorMessage})
    raise TypeError

class THERMOSTAT:

  def __init__(self,TYPE=None,REGION=None,errorLog=[],changeLog=[],location=""):
    """

    :param TYPE:
    :param REGION:
    :param errorLog:
    :type errorLog: list
    :param changeLog:
    :type changeLog: list
    :param location:
    :returns None
    """

    self.__errorLog  = errorLog
    self.__changeLog = changeLog
    self.__TYPE      = _validate_type(TYPE,errorLog=self.__errorLog)
    self.__REGION    = _validate_region(REGION,errorLog=self.__errorLog)
    self.__location  = "{}/THERMOSTAT".format(location)
    #THERMOSTAT subsections
    self.__NOSE      = NOSE.NOSE(errorLog=self.__errorLog,changeLog=self.__changeLog,
                         location=self.__location)
    self.__GLE = GLE.GLE(errorLog=self.__errorLog, changeLog=self.__changeLog,
                            location=self.__location)

  @property
  def REGION(self):
    return self.__REGION

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

  @property
  def NOSE(self):
    return self.__NOSE

  @property
  def GLE(self):
    return self.__GLE

  @REGION.setter
  def REGION(self,val):
    val = str(val).upper()
    if val in REGION_VALS:
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'THERMOSTAT','Variable':'REGION',
                               'Success':True,'Previous':self.__REGION,'New':val,
                               'ErrorMessage':None,'Location':self.__location})
      self.__REGION = val
    else:
      errorMessage = ("Invalid option for MD THERMOSTAT REGION: {}. Valid options are: {}".format(val,
                       REGION_VALS))
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'THERMOSTAT','Variable':'REGION',
                               'Success':False,'Previous':self.__REGION,'New':val,
                               'ErrorMessage':errorMessage,'Location':self.__location})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Module':'THERMOSTAT',
                              'Variable':'REGION','ErrorMessage':errorMessage,'Location':self.__location})

  @TYPE.setter
  def TYPE(self,val):
    val = str(val).upper()
    if val in TYPE_VALS:
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'THERMOSTAT','Variable':'TYPE',
                               'Success':True,'Previous':self.__TYPE,'New':val,
                               'ErrorMessage':None,'Location':self.__location})
      self.__TYPE = val
    else:
      errorMessage = ("Invalid option for MD THERMOSTAT TYPE: {}. Valid options are: {}".format(val,
                       TYPE_VALS))
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'THERMOSTAT','Variable':'TYPE',
                               'Success':False,'Previous':self.__TYPE,'New':val,
                               'ErrorMessage':errorMessage,'Location':self.__location})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Module':'THERMOSTAT',
                              'Variable':'TYPE','ErrorMessage':errorMessage,'Location':self.__location})
