def data_type(dat):
  if type(dat) == str:
    return len(dat)
  elif type(dat) == None:
      return 'no value'
  elif type(dat) == bool:
    return dat
  elif type(dat) == int:
    if dat > 100:
      return 'more than 100'
    elif dat == 100:
      return 'equal to 100'
    else:
      return 'less than 100'
  else:
    if type(dat) == list:
      if len(dat) < 3:
        return None
      else:
        return dat[2]