import datetime
import cssi_cp2k.utilities as utilities
from cssi_cp2k.classes import PRINT
from cssi_cp2k.classes import MD
from cssi_cp2k.classes import GEO_OPT
from cssi_cp2k.classes import CONSTRAINT 

class MOTION:

  def __init__(self,errorLog=[],changeLog=[],location=""):
    
    self.__errorLog  = errorLog
    self.__changeLog = changeLog
    self.__location  = "{}/MOTION".format(location)
    # Subsections of MOTION
    self.__PRINT     = PRINT.PRINT(errorLog=self.__errorLog,changeLog=self.__changeLog,
                         location=self.__location)
    self.__MD        = MD.MD(errorLog=self.__errorLog,changeLog=self.__changeLog,
                         location=self.__location)
    self.__GEO_OPT        = GEO_OPT.GEO_OPT(errorLog=self.__errorLog,changeLog=self.__changeLog,
                         location=self.__location)
    self.__CONSTRAINT        = CONSTRAINT.CONSTRAINT(errorLog=self.__errorLog,changeLog=self.__changeLog,
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
  def PRINT(self):
    return self.__PRINT

  @property
  def MD(self):
    return self.__MD

  @property
  def GEO_OPT(self):
    return self.__GEO_OPT

  @property
  def CONSTRAINT(self):
    return self.__CONSTRAINT
