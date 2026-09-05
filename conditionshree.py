

#1
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a < b:
    print("Smallest number is:", a)
else:
    print("Smallest number is:", b)
#2

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a > b:
    print("Largest number is:", a)
else:
    print("Largest number is:", b)
#3
n = int(input("Enter a number: "))
if n < 0:
    print("Absolute value is:", -n)
else:
    print("Absolute value is:", n)

#4
n = int(input("Enter a number: "))
if n % 2 == 0:
    print(n, "is Even")
else:
    print(n, "is Odd")

#5
n = int(input("Enter a number: "))
if n % 5 == 0:
    print(n, "is a multiple of 5")
else:
    print(n, "is not a multiple of 5")

#6
n = int(input("Enter a number: "))
if n % 10 == 0:
    print(n, "is a multiple of 10")
else:
    print(n, "is not a multiple of 10")

#7
n = int(input("Enter a number: "))
if 10 <= n <= 99:
    print(n, "is a two-digit number")
else:
    print(n, "is not a two-digit number")

#8
n = int(input("Enter a number: "))
if 100 <= n <= 999:
    print(n, "is a three-digit number")
else:
    print(n, "is not a three-digit number")

#9
n = int(input("Enter a number: "))
if n % 10 == 0:
    print(n, "ends with zero")
else:
    print(n, "does not end with zero")

#10
n = int(input("Enter a number: "))
square = n * n
if square > 50:
    print("Square", square, "is above 50")
else:
    print("Square", square, "is below 50")

#11
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
diff = a - b
if diff == 0:
    print("Difference is 0")
else:
    print("Difference is not 0, it is:", diff)

#12
marks = int(input("Enter Computer Science marks: "))
if marks >= 50:
    print("Student has Passed")
else:
    print("Student has Failed")
#13
n = int(input("Enter a number: "))
if n % 10 == 0:
    print(n, "is divisible by 10")
else:
    print(n, "is not divisible by 10")

#14
n = int(input("Enter a two-digit number: "))
digit1 = n // 10   # tens place
digit2 = n % 10    # units place
if digit1 > digit2:
    print("Biggest digit is:", digit1)
else:
    print("Biggest digit is:", digit2)

#15
choice = int(input("Enter your choice: "))
if choice == 1:
    print("The exam will be easy")
else:
    print("The exam will be difficult")

#16
value = int(input("Enter value: "))
if value == 1:
    print("You can go out and play")
else:
    print("You cannot go out and play")

#17
length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))
if length == breadth:
    print("It's a Square")
else:
    print("It's a Rectangle")

#18
n = int(input("Enter a number: "))
if 65 <= n <= 90:
    print(n, "is ASCII value of an uppercase alphabet:", chr(n))
else:
    print(n, "is not ASCII value of an uppercase alphabet")

#19
n = int(input("Enter a number: "))
if 97 <= n <= 122:
    print(n, "is ASCII value of a lowercase alphabet:", chr(n))
else:
    print(n, "is not ASCII value of a lowercase alphabet")

#20
n = int(input("Enter a number: "))
if 48 <= n <= 57:
    print(n, "is ASCII value of a numeric character:", chr(n))
else:
    print(n, "is not ASCII value of a numeric character")

#21
n = int(input("Enter a number: "))
if n % 5 == 0 and n % 3 == 0:
    print(n, "is a multiple of both 5 and 3")
else:
    print(n, "is not a multiple of both 5 and 3")

#22
n = int(input("Enter a number: "))
if 100 <= n <= 999 and n % 10 == 0:
    print(n, "is a three-digit number and a multiple of 10")
else:
    print(n, "does not satisfy both conditions")

#23
n = int(input("Enter a number: "))
if 100 <= n <= 999 and n % 2 == 0 and n % 5 == 0 and n % 10 == 0:
    print(n, "is a three-digit number and multiple of 2, 5 and 10")
else:
    print(n, "does not satisfy all conditions")

#24
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a % 2 == 0 and b % 2 == 0:
    print("Both are even. Product is:", a * b)
else:
    print("Not both even. Sum is:", a + b)

#25
class BuzzNumber:
    def __init__(self, number):
        self.number = number
 
    def check_buzz(self):
        if self.number % 10 == 7 or self.number % 7 == 0:
            print(self.number, "is a Buzz Number")
        else:
            print(self.number, "is not a Buzz Number")
 
 
num = int(input("Enter a number: "))
obj = BuzzNumber(num)
obj.check_buzz()


