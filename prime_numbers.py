#this code is an expression of a working function that generates prime numbers from 0 to n
first_no = int(raw_input("Enter the first number: "))
print first_no
#Here the user is required to insert the first number in the range, in this case zero (0).
second_no = int(raw_input("Enter the second number: "))
print second_no
#Here the user is required to insert the second number in the range (n), which can be for example, 100.
for num in range(first_no,second_no):
#this range of numbers as specified by the input section above it, e.g includes numbers between 0 - 100.
	for a in range(2,num):
		if (num%a==0):
#if num divide by no.s in the range is equal to zero the function breaks at this point
#For example, if num is 8 and it is divided by 2,3,4,5,6,7, it will have a remainder == 0 for 2 and 4
#Therefore, it breaks because 8 is not a prime number.
			break
		else:
			print(num)
#prints the prime numbers within the list.
        