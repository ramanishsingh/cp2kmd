import datetime
from cssi_cp2k.classes import FIXED_ATOMS 


class CONSTRAINT:

  def __init__(self,errorLog=[],changeLog=[],location=""):
    
    self.__errorLog  = errorLog
    self.__changeLog = changeLog
    self.__location  = "{}/CONSTRAINT".format(location)
    # Subsections of MOTION
    self.__FIXED_ATOMS     = FIXED_ATOMS.FIXED_ATOMS(errorLog=self.__errorLog,changeLog=self.__changeLog,
                         location=self.__location)

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
  def FIXED_ATOMS(self):
    return self.__FIXED_ATOMS

