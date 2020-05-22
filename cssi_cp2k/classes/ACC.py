import datetime
import cssi_cp2k.utilities

class ACC:

  def __init__(self,AVOID_AFTER_BUSY=None,BINNING_BINSIZE=None,BINNING_NBINS=None,MIN_FLOP_PROCESS=None,
               MIN_FLOP_SORT=None,POSTERIOR_BUFFERS=None,POSTERIOR_STREAMS=None,PRIORITY_BUFFERS=None,
               PRIORITY_STREAMS=None,PROCESS_INHOMOGENOUS=None,STACK_SORT=None,errorLog=[],changeLog=[],
               location=""):

    self.__AVOID_AFTER_BUSY     = AVOID_AFTER_BUSY
    self.__BINNING_BINSIZE      = BINNING_BINSIZE
    self.__BINNING_NBINS        = BINNING_NBINS
    self.__MIN_FLOP_PROCESS     = MIN_FLOP_PROCESS
    self.__MIN_FLOP_SORT        = MIN_FLOP_SORT
    self.__POSTERIOR_BUFFERS    = POSTERIOR_BUFFERS
    self.__POSTERIOR_STREAMS    = POSTERIOR_STREAMS
    self.__PRIORITY_BUFFERS     = PRIORITY_BUFFERS
    self.__PRIORITY_STREAMS     = PRIORITY_STREAMS
    self.__PROCESS_INHOMOGENOUS = PROCESS_INHOMOGENOUS
    self.__STACK_SORT           = STACK_SORT
    self.__errorLog             = errorLog
    self.__changeLog            = changeLog
    self.__location             = "{}/ACC".format(location)

  @property
  def AVOID_AFTER_BUSY(self):
    return self.__AVOID_AFTER_BUSY

  @property
  def BINNING_BINSIZE(self):
    return self.__BINNING_BINSIZE

  @property
  def BINNING_NBINS(self):
    return self.__BINNING_NBINS

  @property
  def MIN_FLOP_PROCESS(self):
    return self.__MIN_FLOP_PROCESS

  @property
  def MIN_FLOP_SORT(self):
    return self.__MIN_FLOP_SORT

  @property
  def POSTERIOR_BUFFERS(self):
    return self.__POSTERIOR_BUFFERS

  @property
  def POSTERIOR_STREAMS(self):
    return self.__POSTERIOR_STREAMS

  @property
  def PRIORITY_BUFFERS(self):
    return self.__PRIORITY_BUFFERS

  @property
  def PRIORITY_STREAMS(self):
    return self.__PRIORITY_STREAMS

  @property
  def PROCESS_INHOMOGENOUS(self):
    return self.__PROCESS_INHOMOGENOUS

  @property
  def STACK_SORT(self):
    return self.__STACK_SORT

  @property
  def errorLog(self):
    return self.__errorLog

  @property
  def changeLog(self):
    return self.__changeLog

  @property
  def location(self):
    return self.__location

  @AVOID_AFTER_BUSY.setter
  def AVOID_AFTER_BUSY(self,val):
    if isinstance(val,bool):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'ACC',
                               'Variable':'AVOID_AFTER_BUSY','Success':True,
                               'Previous':self.__AVOID_AFTER_BUSY,'New':val,
                               'ErrorMessage':None,'Location':self.__location})
      self.__AVOID_AFTER_BUSY = val
    else:
      errorMessage = "AVOID_AFTER_BUSY must be a boolean. You passed {}.".format(val)
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'DBCSR',
                               'Variable':'AVOID_AFTER_BUSY','Success':False,
                               'Previous':self.__AVOID_AFTER_BUSY,'New':val,'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Module':'DBCSR',
                              'Variable':'AVOID_AFTER_BUSY','ErrorMessage':errorMessage,
                              'Location':self.__location})

  @BINNING_BINSIZE.setter
  def BINNING_BINSIZE(self,val):
    if utilities.is_positive_integer(val):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'ACC',
                               'Variable':'BINNING_BINSIZE','Success':True,
                               'Previous':self.__BINNING_BINSIZE,'New':val,'ErrorMessage':None,
                               'Location':self.__location})
      self.__BINNING_BINSIZE = val
    else:
      errorMessage = "BINNING_BINSIZE must be a positive integer. You passed {}.".format(val)
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'DBCSR',
                               'Variable':'BINNING_BINSIZE','Success':False,
                               'Previous':self.__BINNING_BINSIZE,'New':val,'ErrorMessage':errorMessage,
                               'Location':self.__location})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Module':'DBCSR',
                              'Variable':'BINNING_BINSIZE','ErrorMessage':errorMessage,
                              'Location':self.__location})
  
  @BINNING_NBINS.setter
  def BINNING_NBINS(self,val):
    if utilities.is_positive_integer(val):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'ACC',
                               'Variable':'BINNING_NBINS','Success':True,
                               'Previous':self.__BINNING_NBINS,'New':val,'ErrorMessage':None,
                               'Location':self.__location})
      self.__BINNING_NBINS = val
    else:
      errorMessage = "BINNING_NBINS must be a positive integer. You passed {}.".format(val)
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'DBCSR',
                               'Variable':'BINNING_NBINS','Success':False,
                               'Previous':self.__BINNING_NBINS,'New':val,'ErrorMessage':errorMessage,
                               'Location':self.__location})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Module':'DBCSR',
                              'Variable':'BINNING_NBINS','ErrorMessage':errorMessage,
                              'Location':self.__location})

  @MIN_FLOP_PROCESS.setter
  def MIN_FLOP_PROCESS(self,val):
    if utilities.is_integer(val):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'ACC',
                               'Variable':'MIN_FLOP_PROCESS','Success':True,
                               'Previous':self.__MIN_FLOP_PROCESS,'New':val,'ErrorMessage':None,
                               'Location':self.__location})
      self.__MIN_FLOP_PROCESS = val
    else:
      errorMessage = "MIN_FLOP_PROCESS must be an integer. You passed {}.".format(val)
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'DBCSR',
                               'Variable':'MIN_FLOP_PROCESS','Success':False,
                               'Previous':self.__MIN_FLOP_PROCESS,'New':val,'ErrorMessage':errorMessage,
                               'Location':self.__location})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Module':'DBCSR',
                              'Variable':'MIN_FLOP_PROCESS','ErrorMessage':errorMessage,
                              'Location':self.__location})

  @POSTERIOR_BUFFERS.setter
  def POSTERIOR_BUFFERS(self,val):
    if utilities.is_positive_integer(val):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'ACC',
                               'Variable':'POSTERIOR_BUFFERS','Success':True,
                               'Previous':self.__POSTERIOR_BUFFERS,'New':val,'ErrorMessage':None,
                               'Location':self.__location})
      self.__POSTERIOR_BUFFERS = val
    else:
      errorMessage = "POSTERIOR_BUFFERS must be a positive integer. You passed {}.".format(val)
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'DBCSR',
                               'Variable':'POSTERIOR_BUFFERS','Success':False,
                               'Previous':self.__POSTERIOR_BUFFERS,'New':val,'ErrorMessage':errorMessage,
                               'Location':self.__location})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Module':'DBCSR',
                              'Variable':'POSTERIOR_BUFFERS','ErrorMessage':errorMessage,
                              'Location':self.__location})

  @PRIORITY_BUFFERS.setter
  def PRIORITY_BUFFERS(self,val):
    if utilities.is_positive_integer(val):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'ACC',
                               'Variable':'PRIORITY_BUFFERS','Success':True,
                               'Previous':self.__PRIORITY_BUFFERS,'New':val,'ErrorMessage':None,
                               'Location':self.__location})
      self.__PRIORITY_BUFFERS = val
    else:
      errorMessage = "PRIORITY_BUFFERS must be a positive integer. You passed {}.".format(val)
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'DBCSR',
                               'Variable':'PRIORITY_BUFFERS','Success':False,
                               'Previous':self.__PRIORITY_BUFFERS,'New':val,'ErrorMessage':errorMessage,
                               'Location':self.__location})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Module':'DBCSR',
                              'Variable':'PRIORITY_BUFFERS','ErrorMessage':errorMessage,
                              'Location':self.__location})

  @PRIORITY_STREAMS.setter
  def PRIORITY_STREAMS(self,val):
    if utilities.is_positive_integer(val):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'ACC',
                               'Variable':'PRIORITY_STREAMS','Success':True,
                               'Previous':self.__PRIORITY_STREAMS,'New':val,'ErrorMessage':None,
                               'Location':self.__location})
      self.__PRIORITY_STREAMS = val
    else:
      errorMessage = "PRIORITY_STREAMS must be a positive integer. You passed {}.".format(val)
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'DBCSR',
                               'Variable':'PRIORITY_STREAMS','Success':False,
                               'Previous':self.__PRIORITY_STREAMS,'New':val,'ErrorMessage':errorMessage,
                               'Location':self.__location})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Module':'DBCSR',
                              'Variable':'PRIORITY_STREAMS','ErrorMessage':errorMessage,
                              'Location':self.__location})

  @PROCESS_INHOMOGENOUS.setter
  def PROCESS_INHOMOGENOUS(self,val):
    if isinstance(val,bool):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'ACC',
                               'Variable':'PROCESS_INHOMOGENOUS','Success':True,
                               'Previous':self.__PROCESS_INHOMOGENOUS,'New':val,'ErrorMessage':None,
                               'Location':self.__location})
      self.__PROCESS_INHOMOGENOUS = val
    else:
      errorMessage = "PROCESS_INHOMOGENOUS must be a boolean. You passed {}.".format(val)
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'DBCSR',
                               'Variable':'PROCESS_INHOMOGENOUS','Success':False,
                               'Previous':self.__PROCESS_INHOMOGENOUS,'New':val,'ErrorMessage':errorMessage,
                               'Location':self.__location})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Module':'DBCSR',
                              'Variable':'PROCESS_INHOMOGENOUS','ErrorMessage':errorMessage,
                              'Location':self.__location})

  @STACK_SORT.setter
  def STACK_SORT(self,val):
    if isinstance(val,bool):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'ACC',
                               'Variable':'STACK_SORT','Success':True,
                               'Previous':self.__STACK_SORT,'New':val,'ErrorMessage':None,
                               'Location':self.__location})
      self.__STACK_SORT = val
    else:
      errorMessage = "STACK_SORT must be a boolean. You passed {}.".format(val)
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'DBCSR',
                               'Variable':'STACK_SORT','Success':False,
                               'Previous':self.__STACK_SORT,'New':val,'ErrorMessage':errorMessage,
                               'Location':self.__location})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Module':'DBCSR',
                              'Variable':'STACK_SORT','ErrorMessage':errorMessage,
                              'Location':self.__location})
