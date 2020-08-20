from cssi_cp2k.classes import FORCES as forces
from cssi_cp2k.classes import RESTART_HISTORY as rest
from cssi_cp2k.classes import RESTART as restart
from cssi_cp2k.classes import TRAJECTORY as traj
from cssi_cp2k.classes import VELOCITIES as vel
from cssi_cp2k.classes import STRESS 



class PRINT:

  def __init__(self,errorLog=[],changeLog=[],location=""):

    self.__errorLog  = errorLog
    self.__changeLog = changeLog
    self.__location  = "{}/PRINT".format(location)
    #self.__FORCES
    self.__FORCES=forces.FORCES(errorLog=self.__errorLog,changeLog=self.__changeLog,
                          location=self.__location)
    self.__RESTART_HISTORY = rest.RESTART_HISTORY(errorLog=self.__errorLog, changeLog=self.__changeLog,
                                  location=self.__location)
    self.__RESTART = restart.RESTART(errorLog=self.__errorLog, changeLog=self.__changeLog,
                                  location=self.__location)
    self.__TRAJECTORY = traj.TRAJECTORY(errorLog=self.__errorLog, changeLog=self.__changeLog,
                                     location=self.__location)
    self.__VELOCITIES = vel.VELOCITIES(errorLog=self.__errorLog, changeLog=self.__changeLog,
                                        location=self.__location)
    self.__STRESS = STRESS.STRESS(errorLog=self.__errorLog, changeLog=self.__changeLog,
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
  def FORCES(self):
    return self.__FORCES

  @property
  def RESTART_HISTORY(self):
    return self.__RESTART_HISTORY

  @property
  def RESTART(self):
    return self.__RESTART

  @property
  def TRAJECTORY(self):
    return self.__TRAJECTORY

  @property
  def VELOCITIES(self):
    return self.__VELOCITIES

  @property
  def STRESS(self):
    return self.__STRESS
