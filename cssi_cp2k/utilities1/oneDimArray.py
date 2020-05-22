import datetime

class oneDimArray(object):

  def __init__(self,length,errorLog=[],changeLog=[],location="",var=""):
    self._data      = {i+1:None for i in range(length)}
    self._length    = length
    self._errorLog  = errorLog
    self._changeLog = changeLog
    self._location  = location
    self._var       = var

  def __getitem__(self,pos):
    if type(pos) != int:
      errorMessage = "Index must be an integer."
      self._errorLog.append({"ErrorMessage":errorMessage,'Location':self._location,'Variable':self._var})
      raise IndexError(errorMessage)
    elif  self._length < pos < 0:
      errorMessage = "Index out of bounds."
      self._errorLog.append({"ErrorMessage":errorMessage,'Location':self._location,'Variable':self._var})
      raise IndexError(errorMessage)
    else:
      return self._data[pos]


  def __setitem__(self,pos,val):
    if type(pos) != int:
      errorMessage = "Index must be an integer."
      self._errorLog.append({"ErrorMessage":errorMessage,'Location':self._location,'Variable':self._var})
      raise IndexError(errorMessage)
    elif  self._length < pos < 0:
      errorMessage = "Index out of bounds."
      self._errorLog.append({"ErrorMessage":errorMessage,'Location':self._location,'Variable':self._var})
      raise IndexError(errorMessage)
    else:
      self._changeLog.append({'Date':datetime.datetime.now(),'Location':self._location,'Index':pos,
                               'Variable':self._var,'Success':True,'Previous':self._data[pos],'New':val,
                               'ErrorMessage':None})
      self._data[pos] = val

  def __repr__(self):
    rep = '['
    for i in range(self._length-1):
      rep += '{}, '.format(repr(self._data[i+1]))
    rep += '{}]'.format(repr(self._data[self._length]))
    return rep

  def unrolledString(self):
    string = ""
    for i in range(1,self._length+1):
      string += "{} ".format(self._data[i])
    return string

  @classmethod
  def listToData(cls,val):
    length = len(val)
    return {i+1:val[i] for i in range(length)}

  @classmethod
  def listToODA(cls,val,errorLog=[],changeLog=[],location="",var=""):
    length = len(val)
    myODA = oneDimArray(length=length,errorLog=errorLog,changeLog=changeLog,location=location,var=var)
    for i in range(length):
      myODA[i+1] = val[i]
    return myODA

  def dataAsArray(self):
    return [self._data[i+1] for i in range(self._length)]

  @property
  def data(self):
    return self._data

  @property
  def errorLog(self):
    return self._errorLog

  @property
  def changeLog(self):
    return self._changeLog

  @property
  def location(self):
    return self._location

  @property
  def var(self):
    return self._var

  @property
  def length(self):
    return self._length
