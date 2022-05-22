1'''
______
PART 1
______
The code below prompts the user to enter two numbers, and then prints out the smaller of the numbers entered. Modify so that it prompts the user to enter THREE numbers, and then prints the smallest of the three numbers entered in a sentence.

(Hint: You'll need to be careful for the cases when the user enters the same number twice or all three times.)

An example of what should appear on the console when the code is run:

Enter a number: 11
Enter another number: 2
Enter another number: 5

The smallest number is 2
'''
______
PART 2
______
In the code below, the user is asked to enter three numbers, and then prints a single statement depending on how many of the input numbers are equal. However, there are (at least) 6 syntax errors in the code that need to be fixed. Even after all the syntax errors are fixed and the code runs without errors, there is still a bug. Fix the code so that it runs the way it should.

(Hint: If you see a red squiggly line in the code, that probably means there is a syntax error there.)
'''

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
num3 = int(input("Enter another number: "))

if(num1 == num2 == num3)
  print("All three numbers are equal.")

if(num1 = num2 or num2 = num3 or num1 = num3):
print("Exactly two of the numbers are equal.")

else
  print("None of the numbers are equal.")
