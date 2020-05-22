import datetime
import cssi_cp2k.utilities 

TYPE_OF_MATRIX_MULTIPLICATION_VALS = ["DBCSR_MM","PDGEMM"]

class FM:

  def __init__(self,FORCE_BLOCK_SIZE=None,NCOL_BLOCKS=None,NROW_BLOCKS=None,
               TYPE_OF_MATRIX_MULTIPLICATION=None,errorLog=[],changeLog=[],
               location=""):
    
    self.__FORCE_BLOCK_SIZE              = FORCE_BLOCK_SIZE
    self.__NCOL_BLOCKS                   = NCOL_BLOCKS
    self.__NROW_BLOCKS                   = NROW_BLOCKS
    self.__TYPE_OF_MATRIX_MULTIPLICATION = TYPE_OF_MATRIX_MULTIPLICATION
    self.__errorLog                      = errorLog
    self.__changeLog                     = changeLog
    self.__location                      = "{}/FM".format(location)

  @property
  def FORCE_BLOCK_SIZE(self):
    return self.__FORCE_BLOCK_SIZE

  @property
  def NCOL_BLOCKS(self):
    return self.__NCOL_BLOCKS

  @property
  def NROW_BLOCKS(self):
    return self.__NROW_BLOCKS

  @property
  def TYPE_OF_MATRIX_MULTIPLICATION(self):
    return self.__TYPE_OF_MATRIX_MULTIPLICATION

  @property
  def errorLog(self):
    return self.__errorLog

  @property
  def changeLog(self):
    return self.__changeLog

  @property
  def location(self):
    return self.__location

  @FORCE_BLOCK_SIZE.setter
  def FORCE_BLOCK_SIZE(self,val):
    if isinstance(val,bool):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'DBCSR',
                               'Variable':'FORCE_BLOCK_SIZE','Success':True,
                               'Previous':self.__FORCE_BLOCK_SIZE,'New':val,'ErrorMessage':None,
                               'Location':self.__location})
      self.__FORCE_BLOCK_SIZE = val
    else:
      errorMessage = "FORCE_BLOCK_SIZE must be a boolean. You passed {}.".format(val)
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'DBCSR',
                               'Variable':'FORCE_BLOCK_SIZE','Success':False,
                               'Previous':self.__FORCE_BLOCK_SIZE,'New':val,'ErrorMessage':errorMessage,
                               'Location':self.__location})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Module':'DBCSR',
                              'Variable':'FORCE_BLOCK_SIZE','ErrorMessage':errorMessage,
                              'Location':self.__location})

  @NCOL_BLOCKS.setter
  def NCOL_BLOCKS(self,val):
    if utilities.is_positive_integer(val):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'DBCSR',
                               'Variable':'NCOL_BLOCKS','Success':True,
                               'Previous':self.__NCOL_BLOCKS,'New':val,'ErrorMessage':None,
                               'Location':self.__location})
      self.__NCOL_BLOCKS = val
    else:
      errorMessage = "NCOL_BLOCKS must be a positive integer. You passed {}.".format(val)
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'DBCSR',
                               'Variable':'NCOL_BLOCKS','Success':False,
                               'Previous':self.__NCOL_BLOCKS,'New':val,'ErrorMessage':errorMessage,
                               'Location':self.__location})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Module':'DBCSR',
                              'Variable':'NCOL_BLOCKS','ErrorMessage':errorMessage,
                              'Location':self.__location})

  @NROW_BLOCKS.setter
  def NROW_BLOCKS(self,val):
    if utilities.is_positive_integer(val):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'DBCSR',
                               'Variable':'NROW_BLOCKS','Success':True,
                               'Previous':self.__NROW_BLOCKS,'New':val,'ErrorMessage':None,
                               'Location':self.__location})
      self.__NROW_BLOCKS = val
    else:
      errorMessage = "NROW_BLOCKS must be a positive integer. You passed {}.".format(val)
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'DBCSR',
                               'Variable':'NROW_BLOCKS','Success':False,
                               'Previous':self.__NROW_BLOCKS,'New':val,'ErrorMessage':errorMessage,
                               'Location':self.__location})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Module':'DBCSR',
                              'Variable':'NROW_BLOCKS','ErrorMessage':errorMessage,
                              'Location':self.__location})

  @TYPE_OF_MATRIX_MULTIPLICATION.setter
  def TYPE_OF_MATRIX_MULTIPLICATION(self,val):
    val = str(val).upper()
    if val in TYPE_OF_MATRIX_MULTIPLICATION_VALS:
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'DBCSR',
                               'Variable':'TYPE_OF_MATRIX_MULTIPLICATION','Success':True,
                               'Previous':self.__TYPE_OF_MATRIX_MULTIPLICATION,'New':val,'ErrorMessage':None,
                               'Location':self.__location})
      self.__TYPE_OF_MATRIX_MULTIPLICATION = val
    else:
      errorMessage = ("TYPE_OF_MATRIX_MULTIPLICATION val {} not understood. Possible values are: {}"
                      "".format(val,TYPE_OF_MATRIX_MULTIPLICATION_VALS))
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'DBCSR',
                               'Variable':'TYPE_OF_MATRIX_MULTIPLICATION','Success':False,
                               'Previous':self.__TYPE_OF_MATRIX_MULTIPLICATION,'New':val,'ErrorMessage':errorMessage,
                               'Location':self.__location})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Module':'DBCSR',
                              'Variable':'TYPE_OF_MATRIX_MULTIPLICATION','ErrorMessage':errorMessage,
                              'Location':self.__location})
