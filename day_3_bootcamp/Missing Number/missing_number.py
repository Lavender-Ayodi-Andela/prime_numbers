def find_missing(listone, listtwo):

    if len(listone)==0 and len(listtwo)==0:
        return 0

    elif len(listone)==len(listtwo):
        return 0

    else:
    	missing_number = list(set(listtwo) - set(listone))
    	return missing_number
