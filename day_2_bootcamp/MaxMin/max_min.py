	#new list to include minimum and maximum number
	#add minimum and maximum from list to min_max_list
def find_max_min(num):
	try:

		for x in num:
			minimum = min(num)
			maximum = max(num)

			if minimum != maximum:
				return [minimum,maximum]
			else:
				return len([num])

	except Exception:
		return 'invalid entry'
		



