# You are tasked with writing a program that asks the user to input a number and prints out the result of the number squared. However, the program should also handle the following exceptions:
# If the user inputs a non-numeric value, the program should print an error message and ask the user to input a valid number.
# If the user inputs a negative number, the program should print an error message and ask the user to input a positive number.
# Write a Python program that implements the above requirements. Your program should use the try and except statements to catch and handle the exceptions. The program should keep asking the user for input until a valid number is provided, and then print out the squared result.
while True:
    try:
        user= float(input('input a number '))
        if user < 0:
         raise ValueError('Invalid number')
    except ValueError:
         print('hmm... this is wrong... type in a proper number')
    answer = user**2
    print ('the square of', user,'is', answer)
     