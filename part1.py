number1 = int(input("Enter a number: "))

number2 = int(input("Enter another number: "))

number3 = int(input("Enter another number: "))

if number1 <= number2 and number1 <= number3:
  smallest = number1
elif number2 <= number1 and number2 <= number3:
  smallest = number2
elif number3 <= number1 and number3 <= number2:
  smallest = number3
print("The smallest number is ", smallest)