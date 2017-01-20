def find_missing(listone, listtwo):
    #returns zero for empty list and same entries
    if len(listone)==0 and len(listtwo)==0 and len(listone)==len(listtwo):
        return 0
    #missing numbers
    else:
    	missing_number = list(set(listtwo) - set(listone))
    	return missing_number
