import numpy as np
import datetime

# Numerical stuff
def is_number(val):
  try:
    v = float(val)
    return True
  except (ValueError,TypeError):
    return False

def is_integer(val):
  return (isinstance(val,int) or isinstance(val,np.int8) or isinstance(val,np.int16) or 
          isinstance(val,np.int32) or isinstance(val,np.int64))

def is_positive_integer(val):
  if is_integer(val):
    return val >= 0
  else:
    return False

def is_positive_number(val):
  if is_number(val):
    return val >= 0
  else:
    return False

#Make datetime string prettier
def datetimePrettify(dt):
  return dt
