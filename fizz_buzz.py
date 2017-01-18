def fizz_buzz(n):
#for no.s divisible by both 3 and 5
	if n%3 == 0 and n%5 == 0:
		return 'FizzBuzz'
#for no.s divisible by 3
	elif n%3 == 0:
		return 'Fizz'
#for no.s divisible by 5
	elif n%5 == 0:
		return 'Buzz'
	else:
#no.s divisible by neither 3 or 5
		return n