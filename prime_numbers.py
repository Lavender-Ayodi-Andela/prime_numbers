first_no = int(raw_input("Enter the first number: "))
print first_no
second_no = int(raw_input("Enter the second number: "))
print first_no
for num in range(first_no,second_no):
	for a in range(2,num):
        if (num%a==0):
            break
    else:
        print(num)