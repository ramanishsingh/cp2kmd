import datetime
import cssi_cp2k.utilities as utilities
from cssi_cp2k.classes import SCF_RESTART

BOOL_VALS   = [".TRUE.",".FALSE"]

def _validate_DM_RESTART_WRITE(val,errorLog=[]):

  if val is not None:
    val = str(val).upper()

  if val in BOOL_VALS or (val is None):
    return val
  else:
    errorMessage = ("Invalid option for DM_RESTART_WRITE: {}. Valid options are: {}".format(
                     val,BOOL_VALS))
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'SCF_PRINT',
                            'Variable':'DM_RESTART_WRITE','ErrorMessage':errorMessage})
    raise TypeError


class PRINT:

  def __init__(self,DM_RESTART_WRITE=None,errorLog=[],changeLog=[],location=""):

    self.__errorLog  = errorLog
    self.__changeLog = changeLog
    self.__DM_RESTART_WRITE      = _validate_DM_RESTART_WRITE(DM_RESTART_WRITE,errorLog=self.__errorLog)
    self.__location  = "{}/SCF_PRINT".format(location)
    self.__RESTART=SCF_RESTART.RESTART(errorLog=self.__errorLog,changeLog=self.__changeLog,location=self.__location)
    
    #THERMOSTAT subsections


  @property
  def DM_RESTART_WRITE(self):
    return self.__DM_RESTART_WRITE

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
  def RESTART(self):
    return self.__RESTART



  @DM_RESTART_WRITE.setter
  def DM_RESTART_WRITE(self,val):
    val = str(val).upper()
    if val in BOOL_VALS:
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'SCF.PRINT','Variable':'DM_RESTART_WRITE',
                               'Success':True,'Previous':self.__DM_RESTART_WRITE,'New':val,
                               'ErrorMessage':None,'Location':self.__location})
      self.__DM_RESTART_WRITE= val
    else:
      errorMessage = ("Invalid option for DM_RESTART_WRITE: {}. Valid options are: {}".format(val,
                       REGION_VALS))
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'SCF.PRINT','Variable':'DM_RESTART_WRITE',
                               'Success':False,'Previous':self.__DM_RESTART_WRITE,'New':val,
                               'ErrorMessage':errorMessage,'Location':self.__location})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Module':'SCF.PRINT',
                              'Variable':'DM_RESTART_WRITE','ErrorMessage':errorMessage,'Location':self.__location})