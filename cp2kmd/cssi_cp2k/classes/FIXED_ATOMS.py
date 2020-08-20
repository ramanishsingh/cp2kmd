import datetime
import cssi_cp2k.utilities as utilities


COMPONENTS_VALS = ["X","XY","XYZ","XZ","Y","YZ","Z"]
#TYPE_VALS = ["MINIMIZATION","TRANSITION_STATE"]

def _validate_COMPONENTS_TO_FIX(val,errorLog=[]):
  if val is not None:
    val = str(val).upper()
  if val in COMPONENTS_VALS or (val is None):
    return val
  else:
    errorMessage = "Invalid option for COMPONENTS_VALS FIXED_ATOMS: {}. Valid options are: {}".format(val,COMPONENTS_VALS)
    errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'FIXED_ATOMS',
                            'Variable':'COMPONENTS_VALS','ErrorMessage':errorMessage})
    raise TypeError("{}".format(val))
    
def _validate_LIST(val,errorLog=[]):
  return val



class FIXED_ATOMS:

  def __init__(self,COMPONENTS_TO_FIX=None,LIST=None, errorLog=[],changeLog=[],
               location=""):

    self.__errorLog    = errorLog
    self.__changeLog   = changeLog
    self.__COMPONENTS_TO_FIX    = _validate_COMPONENTS_TO_FIX(COMPONENTS_TO_FIX,errorLog=self.__errorLog)
    self.__LIST       = _validate_LIST(LIST,errorLog=self.__errorLog)
    
    self.__location    = "{}/FIXED_ATOMS".format(location)
    #MD subesctions


    #self.__BFGS  = bfgs.BFGS(errorLog=self.__errorLog,changeLog=self.__changeLog,
     #                      location=self.__location)

  @property
  def COMPONENTS_TO_FIX(self):
    return self.__COMPONENTS_TO_FIX

  @property
  def LIST(self):
    return self.__LIST



  @property
  def errorLog(self):
    return self.__errorLog

  @property
  def changeLog(self):
    return self.__changeLog

  @property
  def location(self):
    return self.__location

  #@property
  #def THERMOSTAT(self):
  #  return self.__THERMOSTAT


  @COMPONENTS_TO_FIX.setter
  def COMPONENTS_TO_FIX(self,val):
    val = str(val).upper()
    if val in COMPONENTS_VALS:
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'GEO_OPT','Variable':'COMPONENTS_TO_FIX',
                               'Success':True,'Previous':self.__COMPONENTS_TO_FIX,'New':val,'ErrorMessage':None,
                               'Location':self.__location})
      self.__COMPONENTS_TO_FIX = val
    else:
      errorMessage = "Invalid option for COMPONENTS_TO_FIX in GEO_OPT: {}. Valid options are: {}".format(COMPONENTS_VALS)
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'GEO_OPT','Variable':'COMPONENTS_TO_FIX',
                               'Success':False,'Previous':self.__OPTIMIZER,'New':val,
                               'ErrorMessage':errorMessage,'Location':self.__location})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Module':'GEO_OPT',
                              'Variable':'COMPONENTS_TO_FIX','ErrorMessage':errorMessage,'Location':self.__location})
    
  @LIST.setter
  def LIST(self,val):
    
    
    self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'fixed_atoms','Variable':'LIST',
                               'Success':True,'Previous':self.__LIST,'New':val,'ErrorMessage':None,
                               'Location':self.__location})
    self.__LIST = val
    
 

