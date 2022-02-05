#importing random
from random import randint
j = 0
#taking password
passcode = input()
#storing numbere for cracking
password = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
# creating an empty string for guesses
code = ""
#creating a loop to find the right password
while code != passcode:
	code = ""
	print("processing...")
	j += 1
	
	for number in range(len(passcode)):
		code_number= password[randint(0,9)]
		code = str(code_number) + str(code)
print('your password is  ' ,code)
print(" it took",j," times to get it")