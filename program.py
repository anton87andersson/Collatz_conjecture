"""
Anton Anderssons function for the Collatz conjecture.
It takes any positive int and uses the rule

:::::::::::::::::::::::::::
if even take n / 2	    :::
:::::::::::::::::::::::::::
if not even take n * 3 + 1:
:::::::::::::::::::::::::::

It will always end up with a loop with 4 2 1 and cannot be solved.


"""

def collatz(number_to_test):
	count = 0
	while number_to_test != 1:
		if number_to_test % 2:
			number_to_test = number_to_test * 3 + 1
			print(number_to_test)
		else:
			number_to_test = number_to_test / 2
			print(number_to_test)	
		count += 1
	return "It took " + str(count) + " steps to reach the loop"

# run the program

while True:
	input_raw = input("Enter number to test: ")
	if len(input_raw) != 0 and input_raw.isnumeric() == True:
		input_number_user = int(input_raw)
		if input_number_user >= 1:
			print(collatz(input_number_user))
	else: 
		print("Not a valid input, needs to be a positive number.")



	

