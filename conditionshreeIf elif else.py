'''
#1
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
 
if a >= b and a >= c:
    print("Largest number is:", a)
elif b >= a and b >= c:
    print("Largest number is:", b)
else:
    print("Largest number is:", c)
#2
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
 
if a <= b and a <= c:
    print("Smallest number is:", a)
elif b <= a and b <= c:
    print("Smallest number is:", b)
else:
    print("Smallest number is:", c)
#3
n = int(input("Enter a number: "))
 
if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")
'''
#4
class Library:
    def __init__(self, days_late):
        self.days_late = days_late
 
    def calculate_fine(self):
        days = self.days_late
 
        if days <= 5:
            fine = days * 0.40
        elif days <= 10:
            fine = (5 * 0.40) + (days - 5) * 0.65
        else:
            fine = (5 * 0.40) + (5 * 0.65) + (days - 10) * 0.80
 
        print("Number of days late:", days)
        print("Fine amount: Rs.", round(fine, 2))
 
 
days_late = int(input("Enter number of days book was returned late: "))
lib = Library(days_late)
lib.calculate_fine()

#5
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (+, -, x, /): ")
 
if operation == '+':
    print("Result:", num1 + num2)
elif operation == '-':
    print("Result:", num1 - num2)
elif operation == 'x':
    print("Result:", num1 * num2)
elif operation == '/':
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Division by zero is not allowed")
else:
    print("Invalid operation")

#6
n = int(input("Enter a number: "))
 
if n % 5 == 0:
    print(n, "is a multiple of 5")
elif n % 3 == 0:
    print(n, "is a multiple of 3")
elif n % 7 == 0:
    print(n, "is a multiple of 7")
else:
    print(n, "is not a multiple of 5, 3, or 7")

#7
weight = float(input("Enter weight of parcel (in gm): "))
booking = input("Enter type of booking (O for Ordinary, E for Express): ").upper()
 
if booking == 'O':
    if weight <= 100:
        charge = 80
    elif weight <= 500:
        charge = 150
    elif weight <= 1000:
        charge = 210
    else:
        charge = 250
    print("Charges for Ordinary booking: Rs.", charge)
 
elif booking == 'E':
    if weight <= 100:
        charge = 100
    elif weight <= 500:
        charge = 200
    elif weight <= 1000:
        charge = 250
    else:
        charge = 300
    print("Charges for Express booking: Rs.", charge)
 
else:
    print("Invalid booking type entered")

#8
price = float(input("Enter price of laptop: "))
 
if price <= 50000:
    discount_rate = 0
elif price <= 100000:
    discount_rate = 10
elif price <= 150000:
    discount_rate = 15
else:
    discount_rate = 20
 
discount = (price * discount_rate) / 100
total_price = price - discount
 
print("Price of laptop :", price)
print("Discount         :", discount)
print("Total Price      :", total_price)

