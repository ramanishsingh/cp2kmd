class REFERENCES:

  def __init__(self,errorLog=[],changeLog=[],location=""):

    self.__errorLog = errorLog
    self.__changeLog = changeLog

  @property
  def errorLog(self):
    return self.__errorLog

  @property
  def changeLog(self):
    return self.__changeLog

  @property
  def location(self):
    return self.__location
