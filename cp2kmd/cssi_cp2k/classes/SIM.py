import os
import random
import cssi_cp2k.utilities as utilities
import cssi_cp2k.FileWriters as FileWriters
from cssi_cp2k.classes import GLOBAL
from cssi_cp2k.utilities1 import oneDimArray as oda
from cssi_cp2k.utilities1 import objectArray as oba
from cssi_cp2k.classes import MOTION
from cssi_cp2k.classes import FORCE_EVAL

class SIM:

  def __init__(self):
    
    self.__prod               = False
    self.__nstep              = 0
    self.__time               = 0.0e0
    self.__errorLog           = []
    self.__changeLog          = []
    self.__restartWFN         = "RESTART.wfn"
    self.__homeDirectory      = os.getcwd()
    self.__scratchDirectory   = "/tmp/cssi-cp2k-{}".format(int(random.random()*123456789))
    # Some sections occur in multiple places (e.g. a PRINT/EACH section). Passing this string
    # allows each module to track their full path within the Simulation object structure. Care
    # needs to be taken, though, since Python passes by reference.
    self.__location           = "SIM"
    # SIM subsections. Most correspond to sections of the CP2K input file structure.
    self.__GLOBAL             = GLOBAL.GLOBAL(errorLog=self.__errorLog,changeLog=self.__changeLog,
                                  location=self.__location)
    self.__MOTION             = MOTION.MOTION(errorLog=self.__errorLog,changeLog=self.__changeLog,
                                  location=self.__location)
    self.__FORCE_EVAL= FORCE_EVAL.FORCE_EVAL(errorLog=self.__errorLog, changeLog=self.__changeLog,
                                  location=self.__location)
    
  @property
  def prod(self):
    return self.__prod
  
  @property
  def nstep(self):
    return self.__nstep

  @property
  def time(self):
    return self.__time

  @property
  def errorLog(self):
    return self.__errorLog

  @property
  def changeLog(self):
    return self.__changeLog

  @property
  def restartWFN(self):
    return self.__restartWFN

  @property
  def homeDirectory(self):
    return self.__homeDirectory

  @property
  def scratchDirectory(self):
    return self.__scratchDirectory

  @property
  def location(self):
    return self.__location

  @property
  def GLOBAL(self):
    return self.__GLOBAL

  @property
  def MOTION(self):
    return self.__MOTION

  @property
  def FORCE_EVAL(self):
    return self.__FORCE_EVAL

  @restartWFN.setter
  def restartWFN(self,val):
    if os.path.isfile(val):
      self.__restartWFN = val
    else:
      errorMessage = ("Type: Setter\nVar.: restartWFN\nErr.: Couldn't set restart wavefunction file to "
        "{} because file wasn't found.".format(val))
      self.__errorLog.append(errorMessage)

  @homeDirectory.setter
  def homeDirectory(self,val):
    self.__homeDirectory = val

  @scratchDirectory.setter
  def scratchDirectory(self,val):
    self.__scratchDirectory = scratchDirectory

  def write_errorLog(self,fn=None):
    # No argument or explicit None prints to screen
    if fn is None:
      for error in self.__errorLog:
        print(error)

  def write_changeLog(self,success=None,keys=None,fn=None):

    logString = ""

    if keys is not None: 
      keys = [str(key).upper() for key in keys]

    for change in self.__changeLog:
      if keys is None:
        if success is None:
          logString += "{}/{}\n\n".format(change["Location"],change["Variable"])
          logString += "{}: {}\n".format("New",change["New"])
          logString += "{}: {}\n".format("Previous",change["Previous"])
          logString += "{}: {}\n".format("Date",utilities.datetimePrettify(change["Date"]))
          logString += "{}: {}\n".format("Success",change["Success"])
          logString += "{}: {}\n\n".format("ErrorMessage",change["ErrorMessage"])
        elif success in [True,False]:
          if change["Success"] == success:
            logString += "{}/{}\n\n".format(change["Location"],change["Variable"])
            logString += "{}: {}\n".format("New",change["New"])
            logString += "{}: {}\n".format("Previous",change["Previous"])
            logString += "{}: {}\n".format("Date",utilities.datetimePrettify(change["Date"]))
            logString += "{}: {}\n\n".format("ErrorMessage",change["ErrorMessage"])
        else:
          print("Invalid value for success passed to write_changeLog")
          raise ValueError
 
      else:
        if success is None:
          logString += "{}/{}\n\n".format(change["Location"],change["Variable"])
          if "NEW" in keys:
            logString += "{}: {}\n".format("New",change["New"])
          if "PREVIOUS" in keys:
            logString += "{}: {}\n".format("Previous",change["Previous"])
          if "DATE" in keys:
            logString += "{}: {}\n".format("Date",utilities.datetimePrettify(change["Date"]))
          if "SUCCESS" in keys:
            logString += "{}: {}\n".format("Success",change["Success"])
          if "ERRORMESSAGE" in keys:
            logString += "{}: {}\n\n".format("ErrorMessage",change["ErrorMessage"])
        elif success in [True,False]:
          if change["Success"] == success:
            logString += "{}/{}\n\n".format(change["Location"],change["Variable"])
            if "NEW" in keys:
              logString += "{}: {}\n".format("New",change["New"])
            if "PREVIOUS" in keys:
              logString += "{}: {}\n".format("Previous",change["Previous"])
            if "DATE" in keys:
              logString += "{}: {}\n".format("Date",utilities.datetimePrettify(change["Date"]))
            if "ERRORMESSAGE" in keys:
              logString += "{}: {}\n\n".format("ErrorMessage",change["ErrorMessage"])
        else:
          print("Invalid value for success passed to write_changeLog")
          raise ValueError

    # No argument or explicit None prints to screen
    if fn is None:
      print(logString)
    else:
      with open(fn,"w") as out:
        out.write(logString)

  def write_inputFile(self,fn=None):
    inputFile = FileWriters.write_input(self)
    if fn is None:
      print(inputFile)
    else:
      with open(fn,"w") as out:
        out.write(inputFile)
