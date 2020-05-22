import datetime
import cssi_cp2k.utilities as utilities
from cssi_cp2k.classes import ENERGY
from cssi_cp2k.classes import PROGRAM_RUN_INFO

BOOL_VALS   = [".TRUE.",".FALSE"]

def _validate_FORCE_LAST(val,errorLog=[]):

  if val is not None:
    val = str(val).upper()

  if val in BOOL_VALS or (val is None):
    return val
  else:
    errorMessage = ("Invalid option for FORCE_LAST: {}. Valid options are: {}".format(
                     val,BOOL_VALS))
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'MD_PRINT',
                            'Variable':'FORCE_LAST','ErrorMessage':errorMessage})
    raise TypeError


class PRINT:

  def __init__(self,FORCE_LAST=None,errorLog=[],changeLog=[],location=""):

    self.__errorLog  = errorLog
    self.__changeLog = changeLog
    self.__FORCE_LAST      = _validate_FORCE_LAST(FORCE_LAST,errorLog=self.__errorLog)
    self.__location  = "{}/MD_PRINT".format(location)
    #THERMOSTAT subsections
    self.__ENERGY      = ENERGY.ENERGY(errorLog=self.__errorLog,changeLog=self.__changeLog,
                         location=self.__location)
    self.__PROGRAM_RUN_INFO = PROGRAM_RUN_INFO.PROGRAM_RUN_INFO(errorLog=self.__errorLog, changeLog=self.__changeLog,
                            location=self.__location)

  @property
  def FORCE_LAST(self):
    return self.__FORCE_LAST

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
  def ENERGY(self):
    return self.__ENERGY

  @property
  def PROGRAM_RUN_INFO(self):
    return self.__PROGRAM_RUN_INFO

  @FORCE_LAST.setter
  def FORCE_LAST(self,val):
    val = str(val).upper()
    if val in BOOL_VALS:
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'MD.PRINT','Variable':'FORCE_LAST',
                               'Success':True,'Previous':self.__FORCE_LAST,'New':val,
                               'ErrorMessage':None,'Location':self.__location})
      self.__FORCE_LAST = val
    else:
      errorMessage = ("Invalid option for FORCE_LAST: {}. Valid options are: {}".format(val,
                       REGION_VALS))
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'MD.PRINT','Variable':'FORCE_LAST',
                               'Success':False,'Previous':self.__FORCE_LAST,'New':val,
                               'ErrorMessage':errorMessage,'Location':self.__location})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Module':'MD.PRINT','Variable':'TYPE','ErrorMessage':errorMessage,'Location':self.__location})
