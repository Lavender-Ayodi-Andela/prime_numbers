data = int(raw_input("Insert element to know data type: "))
def type_of_data(data):
	if type(data) == str:
		return "This is a string"
	elif type(data) == int:
		return "This is an integer"
    elif type(data) == float:
    	return "This is a float"
    elif type(data) == bool:
    	return "This is a Boolean Value"
    elif type(data) == list:
    	return "This is a list"
    else:
    	return "This is a dictionary"
#this interface enables/assists the users to identify different data types; largerthan.py.