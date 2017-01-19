	#new list to include minimum and maximum number
	#add minimum and maximum from list to min_max_list
def find_max_min(num):
	try:
		min_max_list = []

		for x in num:
			min_max_list.append (min(num))
			min_max_list.append (max(num))
			return min_max_list

	except Exception as e:
		return 'invalid entry'
		



