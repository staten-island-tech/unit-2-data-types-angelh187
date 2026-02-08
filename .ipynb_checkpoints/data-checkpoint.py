""" x = 6
y = float(7)
print(x,y) """

"""
bill = float (input('how much was the bill?'))
tip = int(input('how much do you want to tip?'))

def total(bill, tip):
    print(bill,tip)
    total = float(bill + tip)
    print("The Final Bill: ", total)

total(bill, tip)
"""
 
"""
values = [1,2.23,5,7,2,30,15]
print(values)
for i in values:
    print(i)
print(values[1])
print(values[2])
"""


"""
def discount(isMember, Age, isResident):
    if((isMember) or (Age >= 65 or Age <= 12) or (isResident)):
        print('discount')
    else:
        print('No discount')


discount(False, 18, True)
"""
""" 
"test"
["t","e","s","t"] """

""" x = "this is a thing"
y = x.split()
z = y[0]
print(y)
print(z) """

""" sentence = input("input a sentence") """
""" 
sentence = input("input a sentence") """

""" day_of_week = input("what day is it?")
if day_of_week == "Friday":
    print("correct")
else:
    print("incorrect") """
""" 
x = "test"
print(f"hello {x}") """

""" 
temp = 75
if temp > 68:
    print('warm')
elif temp == 68:
    print('perfect')
else:
    print('cold') """

"""
Number = int(input("What number is it?"))

if (Number % 2) == 0 :
        print ("Even Number")
else:
        print("Odd Number")
"""
"""
Bill = float(input("How much was your bill?"))
Tip = input("How was your service? bad or okay or good or great: ")
if Tip == "bad":
   print("The total is: ", Bill)
elif Tip == "okay":
   print("The total is: ", round(Bill*1.15, 2))
elif Tip == "good":
   print("The total is:", round(Bill*1.2, 2))
elif Tip == "great":
   print("The total is:", round(Bill*1.25, 2))
else:
    print("I don't understand you")
"""

"""
number = int(input("What is your number?"))
for i in range(1, number + 1):
    if number % i == 0:
        print("One of factor is: ", i)
"""

def greatestCF(number1, number2):
    result = 0
    if number1 > number2:
        for i in range(1, number1 + 1):
            if (number1 % i) == 0 and (number2 % i) == 0:
               result = i
    elif number2 > number1:
        for i in range(1, number2 +1):
            if (number2 % i)  == 0 and (number1 % i) == 0:
                result = i
    else:
        result = number1
        
    print("The greatest common factor: ", result)

number1 = int(input("What is your first number"))
number2 = int(input("What is your second number"))

greatestCF(number1, number2)










































