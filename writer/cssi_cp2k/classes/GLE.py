import datetime
import cssi_cp2k.utilities as utilities


#def _validate_a_list(val):
#  if utilities.is_positive_integer(val) or (val is None):
#    return val
#  else:
#    errorMessage = "Nose LENGTH must be a positive integer."
#    self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'NOSE',
#                            'Variable':'LENGTH','ErrorMessage':errorMessage})
#    raise TypeError

def _validate_a_scale(val):
  if utilities.is_positive_integer(val) or (val is None):
    return val
  else:
    errorMessage = "scaling factor for matrix A (for generic matrix A, depends on the characteristic frequency of the system). must be a positive integer."
    self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'GLE',
                            'Variable':'A_SCALE','ErrorMessage':errorMessage})
    raise TypeError

#def _validate_c_list(val):
#  if utilities.is_positive_number(val) or (val is None):
#    return val
#  else:
#    errorMessage = "Nose TIMECON must be a positive number."
#    self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'NOSE',
#                            'Variable':'YOSHIDA','ErrorMessage':errorMessage})
#    raise TypeError

def _validate_ndim(val):
  if utilities.is_positive_integer(val) or (val is None):
    return val
  else:
    errorMessage = "GLE NDIM {Integer} Size of the gle matrix  must be a positive number."
    self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'init','Module':'GLE',
                            'Variable':'NDIM','ErrorMessage':errorMessage})
    raise TypeError

class GLE:

  def __init__(self,A_LIST=None,A_SCALE=None,C_LIST=None,NDIM=None,errorLog=[],changeLog=[],
               location=""):
    
    self.__A_SCALE    = _validate_a_scale(A_SCALE)
    self.__NDIM       = _validate_ndim(NDIM)
    self.__C_LIST     =  C_LIST
    self.__A_LIST     =  A_LIST
    self.__errorLog  = errorLog
    self.__changeLog = changeLog
    self.__location  = "{}/GLE".format(location)

  @property
  def A_SCALE(self):
    return self.__A_SCALE

  @property
  def A_LIST(self):
    return self.__A_LIST

  @property
  def C_LIST(self):
    return self.__C_LIST

  @property
  def NDIM(self):
    return self.__NDIM

  @property
  def errorLog(self):
    return self.__errorLog
  
  @property
  def changeLog(self):
    return self.__changeLog

  @property
  def location(self):
    return self.__location

  @A_LIST.setter
  def A_LIST(self,val):
    #if utilities.is_positive_integer(val):
    #  self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'NOSE','Variable':'LENGTH',
    #                          'Success':True,'Previous':self.__LENGTH,'New':val,'ErrorMessage':None,
    #                          'Location':self.__location})
    self.__A_LIST = val
    #else:
     # errorMessage = "Nose LENGTH must be a positive integer."
      #self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'NOSE','Variable':'LENGTH',
       #                        'Success':False,'Previous':self.__LENGTH,'New':val,
        #                       'ErrorMessage':errorMessage,'Location':self.__location})
      #self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Module':'NOSE',
           #                   'Variable':'LENGTH','ErrorMessage':errorMessage,'Location':self.__location})

  @A_SCALE.setter
  def A_SCALE(self,val):
    #if utilities.is_positive_integer(val):
    #  self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'NOSE','Variable':'MTS',
     #                          'Success':True,'Previous':self.__MTS,'New':val,'ErrorMessage':None,
      #                         'Location':self.__location})
    self.__A_SCALE = val
    #else:
     # errorMessage = "Nose number of multiple time steps (MTS) must be a positive integer."
      #self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'NOSE','Variable':'MTS',
       #                        'Success':False,'Previous':self.__MTS,'New':val,
        #                       'ErrorMessage':errorMessage,'Location':self.__location})
      #self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Module':'NOSE',
                 #             'Variable':'MTS','ErrorMessage':errorMessage,'Location':self.__location})

  @C_LIST.setter
  def C_LIST(self,val):
    #if utilities.is_positive_number(val):
     # self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'NOSE','Variable':'TIMECON',
      #                         'Success':True,'Previous':self.__MTS,'New':val,'ErrorMessage':None,
       #                        'Location':self.__location})
    self.__C_LIST = val
    #else:
     # errorMessage = "Nose TIMECON must be a positive number."
      #self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Module':'NOSE',
       #                       'Variable':'TIMECON','ErrorMessage':errorMessage,'Location':self.__location})
      #self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'NOSE','Variable':'TIMECON',
       #                        'Success':False,'Previous':self.__TIMECON,'New':val,
        #                       'ErrorMessage':errorMessage,'Location':self.__location})

  @NDIM.setter
  def NDIM(self,val):
    #if utilities.is_positive_integer(val):
     # self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'NOSE','Variable':'YOSHIDA',
      #                         'Success':True,'Previous':self.__YOSHIDA,'New':val,'ErrorMessage':None,
       #                        'Location':self.__location})
    self.__NDIM = val
    #else:
     # errorMessage = "Nose YOSHIDA integrator order must be a positive integer."
      #self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Module':'NOSE',
       #                       'Variable':'YOSHIDA','ErrorMessage':errorMessage,'Location':self.__location})
      #self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'NOSE','Variable':'YOSHIDA',
       #                        'Success':False,'Previous':self.__YOSHIDA,'New':val,
        #                       'ErrorMessage':errorMessage,'Location':self.__location})
