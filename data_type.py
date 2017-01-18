def data_type(dat):
  if type(dat) == str:
    return len(dat)
#if this data type is a string the return value will be the length of the string in numbers.
  elif type(dat) == None:
      return 'no value'
#if the data type in empty/none the return value will be "no value"
  elif type(dat) == bool:
    return dat
#if the data type is a boolean value (True or False), the return value should be the name itself
  elif type(dat) == int:
    if dat > 100:
      return 'more than 100'
    elif dat == 100:
      return 'equal to 100'
    else:
      return 'less than 100'
#the data is required to identify the integer, and the is subjected through an if formula.
  else:
    if type(dat) == list:
      if len(dat) < 3:
        return None
        #required to identify a list
      else:
        return dat[2]