def find_missing(listone, listtwo):
    #empty list
    if len(listone)==0 and len(listtwo)==0:
        return 0
    #same entries
    elif len(listone)==len(listtwo):
        return 0
    #missing numbers
    else:
    	missing_number = list(set(listtwo) - set(listone))
    	return missing_number
