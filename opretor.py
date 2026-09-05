#1
print("hello world")
#2
a= int(input("enter first number: "))
b= int(input("enter secound number: "))
print(a+b)
print(a-b)
print(a*b)
print(a%b)
print(a/b)
#3
number= int(input("enter number: "))
square_root = number **0.5
print("Square Root:",square_root)
#4
base = float(input("Enter base: "))
height = float(input("Enter height: "))

area = 0.5 * base * height

print("Area of Triangle:", area)
#6
a = int(input("Enter a: "))
b = int(input("Enter b: "))

temp = a
a = b
b = temp

print("After swapping:")
print("a =", a)
print("b =", b)
#7
a= int(input("enter number: "))
b= int(input("enter number: "))

a,b = b,a

print("After swapping:")
print("a =",a)
print("b =",b)
#8
celsius = float(input("Enter Celsius: "))

fahrenheit = (celsius * 1.8) + 32

print("Fahrenheit:", fahrenheit)
#9
number= int(input("enter number"))
last_digit= number %10
print("Last Digit:",last_digit)
#10
number= int(input("enter number"))
last_digit= number %100
print("Last Digit:",last_digit)
#11


