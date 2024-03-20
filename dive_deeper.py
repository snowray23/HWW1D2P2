number = input("Enter a number:")

if int(number) > 0:
    print("The number is positive.")
elif int(number) == 0:
    print("The number is zero.")
else:
    print("The number is negative.")

num1 = input("enter a number:")
num2 = input("enter a second number:")
num3 = input("enter a third number:")

if int(num1) >= int(num2) and int(num1) >= int(num3):
    print("the largest is num1")
elif int(num2) >= int(num1) and int(num2) >= int(num3):
    print("the larges is num2")
else:
    print("the largest is num3")
if int(num1) <= int(num2) and int(num1) <= int(num3):
    print("the smallest is num1")
elif int(num2) <= int(num1) and int(num2) <= int(num3):
    print("the smallest is num2")
else:
    print("the smallest is num3")
if int(num1) == int(num2) or int(num1) == int(num3):
    print("num1 equals another number")
elif int(num2) == int(num1) or int (num2) == int(num3):
    print("num2 equals another number")
else:
    print("no numbers match")

   





year = input("enter a year:")
if (int(year)) % 400 == 0 and (int(year)) % 100 == 0:
    print("this is a leap year")
elif (int(year)) % 4 == 0 and (int(year)) % 100 != 0:
    print("this is a leap year")
else:
    print("not a leap year sorry")
