import datetime
import cssi_cp2k.utilities
from cssi_cp2k.classes import ACC

MM_DRIVER_VALS = ["AUTO","BLAS","MATMUL","SMM","XSMM"]

class DBCSR:

  def __init__(self,AVG_ELEMENTS_IMAGES=None,COMM_THREAD_LOAD=None,MAX_ELEMENTS_PER_BLOCK=None,
               MM_DRIVER=None,MM_STACK_SIZE=None,MULTREC_LIMIT=None,NUM_LAYERS_3D=None,
               NUM_MULT_IMAGES=None,N_SIZE_MNK_STACKS=None,USE_COMM_THREAD=None,
               USE_MPI_ALLOCATOR=None,USE_MPI_RMA=None,errorLog=[],changeLog=[],
               location=""):

    self.__AVG_ELEMENTS_IMAGES    = AVG_ELEMENTS_IMAGES
    self.__COMM_THREAD_LOAD       = COMM_THREAD_LOAD
    self.__MAX_ELEMENTS_PER_BLOCK = MAX_ELEMENTS_PER_BLOCK
    self.__MM_DRIVER              = MM_DRIVER
    self.__MM_STACK_SIZE          = MM_STACK_SIZE
    self.__MULTREC_LIMIT          = MULTREC_LIMIT
    self.__NUM_LAYERS_3D          = NUM_LAYERS_3D
    self.__NUM_MULT_IMAGES        = NUM_MULT_IMAGES
    self.__N_SIZE_MNK_STACKS      = N_SIZE_MNK_STACKS
    self.__USE_COMM_THREAD        = USE_COMM_THREAD
    self.__USE_MPI_ALLOCATOR      = USE_MPI_ALLOCATOR
    self.__USE_MPI_RMA            = USE_MPI_RMA
    self.__errorLog               = errorLog
    self.__changeLog              = changeLog
    self.__location               = "{}/DBCSR".format(location)
    self.__ACC                    = ACC.ACC(errorLog=[],changeLog=[],location=self.__location)

  @property
  def AVG_ELEMENTS_IMAGES(self):
    return self.__AVG_ELEMENTS_IMAGES

  @property
  def COMM_THREAD_LOAD(self):
    return self.__COMM_THREAD_LOAD

  @property
  def MAX_ELEMENTS_PER_BLOCK(self):
    return self.__MAX_ELEMENTS_PER_BLOCK

  @property
  def MM_DRIVER(self):
    return self.__MM_DRIVER

  @property
  def MM_STACK_SIZE(self):
    return self.__MM_STACK_SIZE

  @property
  def MULTREC_LIMIT(self):
    return self.__MULTREC_LIMIT

  @property
  def NUM_LAYERS_3D(self):
    return self.__NUM_LAYERS_3D

  @property
  def NUM_MULT_IMAGES(self):
    return self.__NUM_MULT_IMAGES

  @property
  def N_SIZE_MNK_STACKS(self):
    return self.__N_SIZE_MNK_STACKS

  @property
  def USE_COMM_THREAD(self):
    return self.__USE_COMM_THREAD

  @property
  def USE_MPI_ALLOCATOR(self):
    return self.__USE_MPI_ALLOCATOR

  @property
  def USE_MPI_RMA(self):
    return self.__USE_MPI_RMA

  @property
  def errorLog(self):
    return self.__errorLog
 
  @property
  def changeLog(self):
    return self.__changeLog

  @AVG_ELEMENTS_IMAGES.setter
  def AVG_ELEMENTS_IMAGES(self,val):
    if utilities.is_positive_integer(val):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'DBCSR',
                               'Variable':'AVG_ELEMENTS_IMAGES','Success':True,
                               'Previous':self.__AVG_ELEMENTS_IMAGES,'New':val,'ErrorMessage':None,
                               'Location':self.__location})
      self.__AVG_ELEMENTS_IMAGES = val
    else:
      errorMessage = "AVG_ELEMENTS_IMAGES must be a positive integer. You passed {}.".format(val)
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'DBCSR',
                               'Variable':'AVG_ELEMENTS_IMAGES','Success':False,
                               'Previous':self.__AVG_ELEMENTS_IMAGE,'New':val,'ErrorMessage':errorMessage,
                               'Location':self.__location})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Module':'DBCSR',
                              'Variable':'AVG_ELEMENTS_IMAGES','ErrorMessage':errorMessage,
                              'Location':self.__location})

  @COMM_THREAD_LOAD.setter
  def COMM_THREAD_LOAD(self,val):
    if utilities.is_positive_integer(val):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'DBCSR',
                               'Variable':'COMM_THREAD_LOAD','Success':True,
                               'Previous':self.__COMM_THREAD_LOAD,'New':val,'ErrorMessage':None,
                               'Location':self.__location})
      self.__COMM_THREAD_LOAD = val
    else:
      errorMessage = "COMM_THREAD_LOAD must be a positive integer. You passed {}.".format(val)
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'DBCSR',
                               'Variable':'COMM_THREAD_LOAD','Success':False,
                               'Previous':self.__COMM_THREAD_LOAD,'New':val,'ErrorMessage':errorMessage,
                               'Location':self.__location})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Module':'DBCSR',
                              'Variable':'COMM_THREAD_LOAD','ErrorMessage':errorMessage,
                              'Location':self.__location})

  @MAX_ELEMENTS_PER_BLOCK.setter
  def MAX_ELEMENTS_PER_BLOCK(self,val):
    if utilities.is_positive_integer(val):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'DBCSR',
                               'Variable':'MAX_ELEMENTS_PER_BLOCK','Success':True,
                               'Previous':self.__MAX_ELEMENTS_PER_BLOCK,'New':val,'ErrorMessage':None,
                               'Location':self.__location})
      self.__MAX_ELEMENTS_PER_BLOCK = val
    else:
      errorMessage = "MAX_ELEMENTS_PER_BLOCK must be a positive integer. You passed {}.".format(val)
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'DBCSR',
                               'Variable':'MAX_ELEMENTS_PER_BLOCK','Success':False,
                               'Previous':self.__COMM_THREAD_LOAD,'New':val,'ErrorMessage':errorMessage,
                               'Location':self.__location})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Module':'DBCSR',
                              'Variable':'MAX_ELEMENTS_PER_BLOCK','ErrorMessage':errorMessage,
                              'Location':self.__location})

  @MM_DRIVER.setter
  def MM_DRIVER(self,val):
    val = str(val).upper()
    if val in DBCSR.MM_DRIVER_VALS:
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'DBCSR',
                               'Variable':'MM_DRIVER','Success':True,
                               'Previous':self.__MM_DRIVER,'New':val,'ErrorMessage':None,
                               'Location':self.__location})
      self.__MM_DRIVER = val
    else:
      errorMessage = ("MM_DRIVER val can't be understood. You passed {}. Allowed values for MM_DRIVER are"
                      " (case-insensitive): {}.".format(val))
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'DBCSR',
                               'Variable':'MM_DRIVER','Success':False,
                               'Previous':self.__MM_DRIVER,'New':val,'ErrorMessage':errorMessage,
                               'Location':self.__location})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Module':'DBCSR',
                              'Variable':'MM_DRIVER','ErrorMessage':errorMessage,
                              'Location':self.__location})

  @MM_STACK_SIZE.setter
  def MM_STACK_SIZE(self,val):
    if utilities.is_integer(val):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'DBCSR',
                               'Variable':'MM_STACK_SIZE','Success':True,
                               'Previous':self.__MM_STACK_SIZE,'New':val,'ErrorMessage':None,
                               'Location':self.__location})
      self.__MM_STACK_SIZE = val
    else:
      errorMessage = "MM_STACK_SIZE must be an integer. You passed {}.".format(val)
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'DBCSR',
                               'Variable':'MM_STACK_SIZE','Success':False,
                               'Previous':self.__MM_STACK_SIZE,'New':val,'ErrorMessage':errorMessage,
                               'Location':self.__location})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Module':'DBCSR',
                              'Variable':'MM_STACK_SIZE','ErrorMessage':errorMessage,
                              'Location':self.__location})

  @MULTREC_LIMIT.setter
  def MULTREC_LIMIT(self,val):
    if utilities.is_positive_integer(val):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'DBCSR',
                               'Variable':'MULTREC_LIMIT','Success':True,
                               'Previous':self.__MULTREC_LIMIT,'New':val,'ErrorMessage':None,
                               'Location':self.__location})
      self.__MULTREC_LIMIT = val
    else:
      errorMessage = "MULTREC_LIMIT must be a positive integer. You passed {}.".format(val)
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'DBCSR',
                               'Variable':'MULTREC_LIMIT','Success':False,
                               'Previous':self.__MULTREC_LIMIT,'New':val,'ErrorMessage':errorMessage,
                               'Location':self.__location})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Module':'DBCSR',
                              'Variable':'MULTREC_LIMIT','ErrorMessage':errorMessage,
                              'Location':self.__location})

  @NUM_LAYERS_3D.setter
  def NUM_LAYERS_3D(self,val):
    if utilities.is_positive_integer(val):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'DBCSR',
                               'Variable':'NUM_LAYERS_3D','Success':True,
                               'Previous':self.__NUM_LAYERS_3D,'New':val,'ErrorMessage':None,
                               'Location':self.__location})
      self.__NUM_LAYERS_3D = val
    else:
      errorMessage = "NUM_LAYERS_3D must be a positive integer. You passed {}.".format(val)
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'DBCSR',
                               'Variable':'NUM_LAYERS_3D','Success':False,
                               'Previous':self.__NUM_LAYERS_3D,'New':val,'ErrorMessage':errorMessage,
                               'Location':self.__location})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Module':'DBCSR',
                              'Variable':'NUM_LAYERS_3D','ErrorMessage':errorMessage,
                              'Location':self.__location})

  @NUM_MULT_IMAGES.setter
  def NUM_MULT_IMAGES(self,val):
    if utilities.is_positive_integer(val):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'DBCSR',
                               'Variable':'NUM_MULT_IMAGES','Success':True,
                               'Previous':self.__NUM_MULT_IMAGES,'New':val,'ErrorMessage':None,
                               'Location':self.__location})
      self.__NUM_MULT_IMAGES = val
    else:
      errorMessage = "NUM_MULT_IMAGES must be a positive integer. You passed {}.".format(val)
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'DBCSR',
                               'Variable':'NUM_MULT_IMAGES','Success':False,
                               'Previous':self.__NUM_MULT_IMAGES,'New':val,'ErrorMessage':errorMessage,
                               'Location':self.__location})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Module':'DBCSR',
                              'Variable':'NUM_MULT_IMAGES','ErrorMessage':errorMessage,
                              'Location':self.__location})

  @N_SIZE_MNK_STACKS.setter
  def N_SIZE_MNK_STACKS(self,val):
    if utilities.is_positive_integer(val):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'DBCSR',
                               'Variable':'N_SIZE_MNK_STACKS','Success':True,
                               'Previous':self.__N_SIZE_MNK_STACKS,'New':val,'ErrorMessage':None,
                               'Location':self.__location})
      self.__N_SIZE_MNK_STACKS = val
    else:
      errorMessage = "N_SIZE_MNK_STACKS must be a positive integer. You passed {}.".format(val)
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'DBCSR',
                               'Variable':'N_SIZE_MNK_STACKS','Success':False,
                               'Previous':self.__N_SIZE_MNK_STACKS,'New':val,'ErrorMessage':errorMessage,
                               'Location':self.__location})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Module':'DBCSR',
                              'Variable':'N_SIZE_MNK_STACKS','ErrorMessage':errorMessage,
                              'Location':self.__location})

  @USE_COMM_THREAD.setter
  def USE_COMM_THREAD(self,val):
    if isinstance(val,bool):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'DBCSR',
                               'Variable':'USE_COMM_THREAD','Success':True,
                               'Previous':self.__USE_COMM_THREAD,'New':val,'ErrorMessage':None,
                               'Location':self.__location})
      self.__USE_COMM_THREAD = val
    else:
      errorMessage = "USE_COMM_THREAD must be a boolean. You passed {}.".format(val)
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'DBCSR',
                               'Variable':'USE_COMM_THREAD','Success':False,
                               'Previous':self.__USE_COMM_THREAD,'New':val,'ErrorMessage':errorMessage,
                               'Location':self.__location})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Module':'DBCSR',
                              'Variable':'USE_COMM_THREAD','ErrorMessage':errorMessage,
                              'Location':self.__location})

  @USE_MPI_ALLOCATOR.setter
  def USE_MPI_ALLOCATOR(self,val):
    if isinstance(val,bool):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'DBCSR',
                               'Variable':'USE_MPI_ALLOCATOR','Success':True,
                               'Previous':self.__USE_MPI_ALLOCATOR,'New':val,'ErrorMessage':None,
                               'Location':self.__location})
      self.__USE_MPI_ALLOCATOR = val
    else:
      errorMessage = "USE_MPI_ALLOCATOR must be a boolean. You passed {}.".format(val)
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'DBCSR',
                               'Variable':'USE_MPI_ALLOCATOR','Success':False,
                               'Previous':self.__USE_MPI_ALLOCATOR,'New':val,'ErrorMessage':errorMessage,
                               'Location':self.__location})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Module':'DBCSR',
                              'Variable':'USE_MPI_ALLOCATOR','ErrorMessage':errorMessage,
                              'Location':self.__location})

  @USE_MPI_RMA.setter
  def USE_MPI_RMA(self,val):
    if isinstance(val,bool):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'DBCSR',
                               'Variable':'USE_MPI_RMA','Success':True,
                               'Previous':self.__USE_MPI_RMA,'New':val,'ErrorMessage':None,
                               'Location':self.__location})
      self.__USE_MPI_RMA = val
    else:
      errorMessage = "USE_MPI_RMA must be a boolean. You passed {}.".format(val)
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'DBCSR',
                               'Variable':'USE_MPI_RMA','Success':False,
                               'Previous':self.__USE_MPI_RMA,'New':val,'ErrorMessage':errorMessage,
                               'Location':self.__location})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Module':'DBCSR',
                              'Variable':'USE_MPI_RMA','ErrorMessage':errorMessage,
                              'Location':self.__location})
