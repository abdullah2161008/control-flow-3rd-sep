#!/usr/bin/env python
# coding: utf-8

# #Basic If-Else Statements:

# #1. Write a Python program to check if a given number is positive or negative.

# In[9]:


number=123
if number>0:
    print("The number is positive")
else:
    print("The number is negative")


# In[ ]:





# #2. Create a program that determines if a person is eligible to vote based on their age.

# In[12]:


age=int(input("What is your age? :"))
if age>=18:
    print("You can cast your Vote.")
else:
    print("Your are not eligible to cast your Vote.")


# In[ ]:





# #3. Develop a program to find the maximum of two numbers using if-else statements.

# In[15]:


num1=44
num2=43
if num1>num2:
    num_max=num1
else:
    num_max=num2
print(f"The maximum number is {num_max}")


# In[ ]:





# #4. Write a Python script to classify a given year as a leap year or not.

# In[22]:


year=int(input("Enter the year:"))
if year%4==0:
    print(f"{year} is a Leap year")
else:
    print(f"{year} is not a Leap Year")


# In[ ]:





# #5. Create a program that checks whether a character is a vowel or a consonant.

# In[49]:


character = input("Enter a character: ").lower()

if len(character) == 1:
    if character.isalpha():
        if character in 'aeiou':
            print(f"{character} is a vowel.")
        else:
            print(f"{character} is a consonant.")
    else:
        print(f"{character} is not an alphabet letter.")
else:
    print("Invalid input. Please enter a single character.")


# In[ ]:





# #6. Implement a program to determine whether a given number is even or odd.

# In[39]:


number=int(input("Enter the number:"))
if number%2==0:
    print(f"{number} is odd")
else:
    print(f" {number} is even")


# In[ ]:





# #7. Write a Python function to calculate the absolute value of a number without using the `abs()` function.

# In[42]:


def custom_abs(number):
    if number<0:
        return -number
    else:
        return number
num=float(input("Enter the number :"))
result=custom_abs(num)
print(f"The absolute value of {num} is {result}")


# In[ ]:





# #8. Develop a program that determines the largest of three given numbers using if-else statements.

# In[45]:


a=int(input("Enter the first number :"))
b=int(input("Enter the second number :"))
c=int(input("Enter the third number :"))
if a>b and a>c:
    print("a is largest number")
elif b>a and b>c:
    print("b is the largest number")
else:
    print("c is the largest number")


# In[ ]:





# #9. Create a program that checks if a given string is a palindrome.

# In[50]:


string=input("Enter a Word :")
if string ==string[-1::-1]:
    print("The string is palindrome ")
else:
    print("The string is not palindrome")


# In[ ]:





# #10. Write a Python program to calculate the grade based on a student's score.

# In[58]:


student_score=int(input("Enter the score :"))
if student_score>=90:
    print(f"{student_score}% = A+")
elif student_score>=80:
    print(f"{student_score}% = A ")
elif student_score>=70:
    print(f"{student_score}% = B")
elif student_score>=60:
    print(f"{student_score}% = C")
elif student_score>=50:
    print(f"{student_score}% = D")
else:
    print(f"{student_score}% = FAIL")


# In[ ]:





# #Nested If-Else Statements:

# #11. Write a program to find the largest among three numbers using nested if-else statements.

# In[76]:


number1=int(input("Enter the first number:"))
number2=int(input("Enter the second number:"))
number3=int(input("Enter the third number:"))
if number1>=number2:
    if number1>=number3:
        largest=number1
    else:
        largest=number3
else:
    if number2>=number3:
        largest=number2
    else:
        largest=number3
    
print(f"The largest number among {number1},{number2},{number3} is : {largest}")


# In[ ]:





# #12. Implement a program to determine if a triangle is equilateral, isosceles, or scalene.

# In[1]:


side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
side3 = float(input("Enter the length of the third side: "))

if (side1 +side2>side3) and (side1 + side3>side2) and (side2 +side3>side1):
    if side1==side2==side3:
        print("Equilibrium Triangle")
    elif side1==side2 or side2==side3 or side1==side3:
        print("Isosceles Triangle")
    else:
        print("Scalene triangle")
    
else:
    print("You entered the wrong lenghts of triangle")


# In[ ]:





# #13. Develop a program that checks if a year is a leap year and also if it is a century year.

# In[7]:


year = int(input("Enter a year: "))
is_leap_year = False

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            is_leap_year = True
    else:
        is_leap_year = True

is_century_year = year % 100 == 0

if is_leap_year:
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

if is_century_year:
    print(f"{year} is a century year.")
else:
    print(f"{year} is not a century year.")


# In[ ]:





# #14. Write a Python script to determine if a number is positive, negative, or zero.

# In[30]:


number = int(input("Enter a number: "))

if number >= 0:
    if number == 0:
        sign = "zero"
    else:
        sign = "positive"
else:
    sign = "negative"

print(f"The number is {sign}.")


# In[ ]:





# #15. Create a program to check if a person is a teenager (between 13 and 19 years old).

# In[16]:


age=int(input("Enter your age :"))
if age>=13:
    if age<=19:
        print("You are Teenager")
    else:
        print("You are not Teenager")
else:
    print("You are not Teenager")


# In[ ]:





# #16. Develop a program that determines the type of angle based on its measure (acute, obtuse, or right).

# In[28]:


angle=int(input("Enter the Angle :"))
if angle>0:
    if angle==90:
        print(f"{angle} is a Right Angle")
    elif angle>90 and angle<180:
        print(f"{angle} is a Obtuse Angle")
    elif angle<90:
        print(f"{angle} is a Acute Angle")
    else:
        print("Invalid")
        
else:
    print("Invalid")
    


# In[ ]:





# #17. Write a Python program to calculate the roots of a quadratic equation.

# In[32]:


a = int(input("Enter coefficient a: "))
b = int(input("Enter coefficient b: "))
c = int(input("Enter coefficient c: "))

discriminant = b**2 - 4*a*c

if discriminant > 0:
    root1 = (-b + (discriminant)**0.5) / (2*a)
    root2 = (-b - (discriminant)**0.5) / (2*a)
    print(f"Two distinct real roots: {root1} and {root2}")
elif discriminant == 0:
    root1 = -b / (2*a)
    print(f"One real root (repeated): {root1}")
else:
    realPart = -b / (2*a)
    imaginaryPart = ((-discriminant)**0.5) / (2*a)
    print(f"Complex roots: {realPart} + {imaginaryPart}i and {realPart} - {imaginaryPart}i")


# In[ ]:





# #18. Implement a program to determine the day of the week based on a user-provided number (1 for Monday, 2
# #for Tuesday, etc.).

# In[46]:


ask=int(input("Enter the number"))
if ask==0:
    print("Invalid input Please enter the number b\w 1-7.")
else:
    if ask==1:
        print(" its a Monday")
    elif ask==2:
        print(" its a Tuesday")
    elif ask==3:
        print(" its a Wednesday")
    elif ask==4:
        print("its a Thursday")
    elif ask==5:
        print("its a Friday")
    elif ask==6:
        print("its a Saturday")
    elif ask==7:
        print("its a Sunday")
    else:
        print("Invalid input Please enter the number b\w 1-7.")
        
        


# #19. Create a program that determines if a year is a leap year and also if it is evenly divisible by 400.

# In[65]:


year=int(input("Enter a Year :"))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("Its a leap Year and divisible by 400")
        else:
            print("Not Leap Year")
    else:
        print("Its a leap Year")
else:
    print("Not Leap Year")


# #20. Develop a program that checks if a given number is prime or not using nested if-else statements.

# In[17]:


number = int(input("Enter the number: "))

if number > 1:
    is_prime = True 
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")
else:
    print(f"{number} is not a prime number.")



# In[ ]:





# #Elif Statements:

# #21. Write a Python program to assign grades based on different ranges of scores using elif statements.

# In[4]:


score=int(input("Enter the Numbers :"))
if score>=90:
    print(" You Got 'A+' Grades")
elif score>=80:
    print("You Got 'A' Grade")
elif score>=70:
    print("You Got 'B' Grade")
elif score>=60:
    print("You Got 'C' Grade")
elif score>=50:
    print("You Got 'D' Grade")
else:
    print("Fail")


# In[ ]:





# 22. Implement a program to determine the type of a triangle based on its angles.

# In[8]:


angle=int(input("Enter your given Angle :"))
if angle==90:
    print("Right Angle")
elif angle<90 and angle>0:
    print("Acute Angle")
elif angle>90 and angle<180:
    print("Obtuse Angle")
else:
    print("Invalid input")


# In[ ]:





# 23. Develop a program to categorize a given person's BMI into underweight, normal, overweight, or obese using
# elif statements.

# In[6]:


height=float(input("Enter Your Height in meters :"))
weight=float(input("Enter Your Weight in kg :"))
bmi=weight / (height ** 2)
if weight / (height ** 2)>=16 and weight / (height ** 2)<18.4:
    print(f"Your BMI is {bmi} and you are Under Weight")
elif weight / (height ** 2)>=18.5 and weight / (height ** 2)<24.9:
    print(f" Your BMI is {bmi} and you are Normal")
elif weight / (height ** 2)>=25 and weight / (height ** 2)<29.9:
    print(f"Your BMI is {bmi} and you are Over Weight")
else:
    print("Obese")


# In[ ]:





# 24. Create a program that determines whether a given number is positive, negative, or zero using elif
# statements.

# In[11]:


given_number=int(input("Enter the Number :"))
if given_number>0:
    print("The number is Positive")
elif given_number<0:
    print("The number is Negative")
elif given_number==0:
    print("The number is Zero")
else:
    print("Invalid number")


# In[ ]:





# 25. Write a Python script to determine the type of a character (uppercase, lowercase, or special) using elif
# statements.

# In[7]:


given = input("Enter a single character: ")

if len(given) == 1:
    if given.isupper():
        print(f"{given} is an Upper Case Character")
    elif given.islower():
        print(f"{given} is a Lower Case Character")
    elif given in special_characters:
        print(f"{given} is a Special Character")
    else:
        print("It is not an Upper Case, Lower Case, or Special Character")
else:
    print("Invalid input. Please enter a single character.")


# In[ ]:





# 26. Implement a program to calculate the discounted price based on different purchase amounts using elif
# statements.

# In[10]:


purchase_amount = float(input("Enter the purchase amount: "))

discount_rate = 0.0

if purchase_amount < 100:
    discount_rate = 0.0  
elif purchase_amount < 500:
    discount_rate = 0.05  
elif purchase_amount < 1000:
    discount_rate = 0.1   
else:
    discount_rate = 0.15  

discounted_price = purchase_amount - (purchase_amount * discount_rate)

print(f"Original Price: ${purchase_amount:.2f}")
print(f"Discount Rate: {discount_rate * 100}%")
print(f"Discounted Price: ${discounted_price:.2f}")


# In[ ]:





# 27. Develop a program to calculate the electricity bill based on different consumption slabs using elif
# statements.

# In[66]:


units=int(input('Enter your Electricity Units :'))
slab1=8
slab2=12
slab3=13
slab4=20
if units<=100 and units>0:
    bill=slab1*units
elif units<=200 and units>100:
    bill=slab2*units
elif units<=300 and units>200:
    bill=slab3*units
elif units>300:
    bill=units*slab4
else:
    print("Invalid input")
    
print(f"Your Electricity bill is {bill}.")


# In[ ]:





# 28. Create a program to determine the type of quadrilateral based on its angles and sides using elif
# statements.

# In[ ]:


side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3: "))
side4 = float(input("Enter the length of side 4: "))

angle1 = float(input("Enter the measure of angle 1 in degrees: "))
angle2 = float(input("Enter the measure of angle 2 in degrees: "))
angle3 = float(input("Enter the measure of angle 3 in degrees: "))
angle4 = float(input("Enter the measure of angle 4 in degrees: "))

sum_of_angles = angle1 + angle2 + angle3 + angle4

if sum_of_angles == 360:
    if side1 == side2 == side3 == side4:
        print("It's a square.")
    elif side1 == side3 and side2 == side4:
        print("It's a rectangle.")
    else:
        print("It's a general quadrilateral.")
else:
    print("It's not a valid quadrilateral.")


# In[ ]:





# 29. Write a Python script to determine the season based on a user-provided month using elif statements.

# In[81]:


month = input("Enter a month (e.g., January, February, etc.): ").lower()

if month in ["december", "january", "february"]:
    season = "Winter"
elif month in ["march", "april", "may"]:
    season = "Spring"
elif month in ["june", "july", "august"]:
    season = "Summer"
elif month in ["september", "october", "november"]:
    season = "Fall"
else:
    season = "Invalid Month"

print(f"The season for {month.capitalize()} is {season}.")



# In[ ]:





# 30. Implement a program to determine the type of a year (leap or common) and month (30 or 31 days) using
# elif statements.

# In[85]:


year=int(input("Enter the Year :"))


if year%4==0:
    print(f"{year} is a Leap year")
else:
    print(f"{year} is Not Leap Year")
    
month=input("Enter the month :").lower()
if month in ["january","march","may","july","september","november"]:
    print(f"{month} has 30 days ")
elif month in ["febraury","april","june","august","octuber","december"]:
    print(f" {month} has 31 days")
else:
    print("invalid month")


# In[ ]:





# Basic Level:

# 1. Write a Python program that checks if a given number is positive, negative, or zero.

# In[11]:


given_number=int(input("Enter the number: "))
if given_number>0:
    print("Positive")
elif given_number<0:
    print("Negative")
elif given_number==0:
    print("Zero")
else:
    print("invalid number")


# In[ ]:





# 2. Create a program to determine if a person is eligible to vote based on their age.

# In[16]:


age=int(input("Enter Your age :"))
if age>=18:
    print("You are eligible to cast your vote")
elif age<18:
    print("You are not eligible not cast your vote")
else:
    print("invalid input")


# In[ ]:





# 3. Write a program to find the maximum of two given numbers using conditional statements.

# In[18]:


num1=int(input("Enter the first number :"))
num2=int(input("Enter the second number :"))
if num1>num2:
    max_num=num1
else:
    max_num=num2
print(f"The maximum number is {max_num}")


# In[ ]:





# 4. Develop a program that calculates the grade of a student based on their exam score.

# In[19]:


score=int(input("Enter the Numbers :"))
if score>=90:
    print(" You Got 'A+' Grades")
elif score>=80:
    print("You Got 'A' Grade")
elif score>=70:
    print("You Got 'B' Grade")
elif score>=60:
    print("You Got 'C' Grade")
elif score>=50:
    print("You Got 'D' Grade")
else:
    print("Fail")


# In[ ]:





# 5. Create a program that checks if a year is a leap year or not.

# In[22]:


year=int(input("Enter the year :"))
if year%4==0:
    print("Leap Year")
else:
    print("Not a leap Year")


# In[ ]:





# 6. Write a program to classify a triangle based on its sides' lengths.

# In[27]:


angle=int(input("Enter the side lenght of a triangle :"))
if angle==90:
    print("Right Angle Triangle")
elif angle>90 and angle<180:
    print("Obtuse Angle Triangle")
elif angle<90 and angle>0:
    print("Acute Angle Triangle")
else:
    print("Invalid input")


# In[ ]:





# 7. Build a program that determines the largest of three given numbers.

# In[28]:


num1=int(input('Enter the First Number :'))
num2=int(input("Enter the Second Number :"))
num3=int(input("Enter the Third Number :"))
if num1>num2 and num1>num3:
    max_num=num1
elif num2>num1 and num2>num3:
    max_num=num2
else:
    max_num=num3
print(f"The maximum number between these numbers is {max_num}.")


# In[ ]:





# 8. Develop a program that checks whether a character is a vowel or a consonant.

# In[48]:


character = input("Enter a character: ").lower()

if len(character) == 1:
    if character.isalpha():
        if character in 'aeiou':
            print(f"{character} is a vowel.")
        else:
            print(f"{character} is a consonant.")
    else:
        print(f"{character} is not an alphabet letter.")
else:
    print("Invalid input. Please enter a single character.")



# In[ ]:





# 9. Create a program to calculate the total cost of a shopping cart based on discounts.

# In[50]:


purchase_amount = float(input("Enter the purchase amount: "))

discount_rate = 0.0

if purchase_amount < 100:
    discount_rate = 0.0  
elif purchase_amount < 500:
    discount_rate = 0.05  
elif purchase_amount < 1000:
    discount_rate = 0.1   
else:
    discount_rate = 0.15  

discounted_price = purchase_amount - (purchase_amount * discount_rate)

print(f"Original Price: ${purchase_amount:.2f}")
print(f"Discount Rate: {discount_rate * 100}%")
print(f"Discounted Price: ${discounted_price:.2f}")


# In[ ]:





# 10. Write a program that checks if a given number is even or odd.

# In[58]:


number=int(input("Enter the number :"))
if number%2!=0:
    print("Odd number")
else:
    print("Even number")


# In[ ]:





# Intermediate Level:

# 11. Write a program that calculates the roots of a quadratic equation .

# In[ ]:


a = int(input("Enter coefficient a: "))
b = int(input("Enter coefficient b: "))
c = int(input("Enter coefficient c: "))

discriminant = b**2 - 4*a*c

if discriminant > 0:
    root1 = (-b + (discriminant)**0.5) / (2*a)
    root2 = (-b - (discriminant)**0.5) / (2*a)
    print(f"Two distinct real roots: {root1} and {root2}")
elif discriminant == 0:
    root1 = -b / (2*a)
    print(f"One real root (repeated): {root1}")
else:
    realPart = -b / (2*a)
    imaginaryPart = ((-discriminant)**0.5) / (2*a)
    print(f"Complex roots: {realPart} + {imaginaryPart}i and {realPart} - {imaginaryPart}i")


# In[ ]:





# 12. Create a program that determines the day of the week based on the day number (1-7).

# In[1]:


number=int(input("Enter the Number :"))

if number==1:
    day="Monday"
elif number==2:
    day="Tuesday"
elif number==3:
    day="Wednesday"
elif number==4:
    day="Thursday"
elif number==5:
    day="Friday"
elif number==6:
    day="Saturday"
elif number==7:
    day="Sunday"
else:
    print("write the number b\w 1--7. ")
print(f"According to {number} today is {day}.")


# In[ ]:





# 13. Develop a program that calculates the factorial of a given number using recursion.

# In[4]:


num=int(input("Enter the Number :"))
factorial=1
if num<0:
    print("The factorial does not work for negative number")
elif num==0:
    print("The factorial for 0 is 1")
else:
    for i in range(1,num+1):
        factorial=factorial*1
print("The factorial of",num,"is",factorial)


# In[ ]:





# 14. Write a program to find the largest among three numbers without using the `max()` function.

# In[3]:


my_list=[23,34,993]
max_number=my_list[0]

for num in my_list[:]:
    max_number>num
    max_number=num
print("The maximum number is",max_number)


# In[ ]:





# 15. Create a program that simulates a basic ATM transaction menu.

# In[8]:


balance=1000
print("Wellcome to MyBank ATM")
print("1.Check Amount :")
print("2.Deposit Amount :")
print("3.Withdraw Amount :")
print("4.Quit.")

choice=int(input("Please! select an option (1,2,3,4):"))

if choice==1:
    print("Your current balance is $",balance)
elif choice==2:
    deposit_amount=int(input("Enter the amount to Deposit $:"))
    if deposit_amount>0:
        balance+=deposit_amount
        print("Deposit Successfully,Your current balance is $",balance)
elif choice==3:
    with_draw=int(input("Enter the amount to withdraw $:"))
    if with_draw<=balance and with_draw>0:
        balance-=with_draw
        print("withdraw Successfully,Your current balance is $",balance)
    else:
        print("invalid input")
elif choice==4:
    print("Quit, thanks for using the MYBank ATM")
else:
    print("invalid choice please select (1,2,3,4)")


# In[ ]:





# 16. Build a program that checks if a given string is a palindrome or not.

# In[11]:


my_string=input("Whats on your mind :")
if my_string==my_string[-1::-1]:
    print("Yes the string is Palindrome :",my_string[-1::-1])
else:
    print("The string is not Palindrome :",my_string[-1::-1])


# In[ ]:





# 17. Write a program that calculates the average of a list of numbers, excluding the smallest and largest values.

# In[12]:


my_numbers=[23,34,23,14,23,13,45,56,99]
max_number=max(my_numbers)
print(my_numbers)
min_number=min(my_numbers)
print(my_numbers)

total=sum(my_numbers)
count=len(my_numbers)
average=total/count
print(average)


# In[ ]:





# In[14]:


numbers=[4,5,3,7,8]
if len(numbers)>=3:
    numbers.remove(max(numbers))
    numbers.remove(min(numbers))
    
    total=sum(numbers)
    count=len(numbers)
    
    average=total/count
    print("The average is",average)
else:
    print("to count the average there should be a list of more than 3 numbers")


# In[ ]:





# 18. Develop a program that converts a given temperature from Celsius to Fahrenheit.

# In[16]:


my_celsius=int(input("Enter the Temperature ="))
if my_celsius>0:
    fahrenheit=my_celsius*(9/5)+32
    print("Fahrenheit=",fahrenheit)
else:
    print("invalid input")


# In[ ]:





# 19. Create a program that simulates a basic calculator for addition, subtraction, multiplication, and division.

# In[1]:


num1=int(input("Enter the first number :"))
signs=input("Enter the calculation sign(/,*-,+,) :")
num2=int(input("Enter the second number :"))

if signs=="/":
    answer=num1/num2
    print("Total =",answer)
elif signs=="*":
    answer=num1*num2
    print("Total =",answer)
elif signs=="-":
    answer=num1-num2
    print("Total =",answer)
elif signs=="+":
    answer=num1+num2
    print("Total =",answer)
else:
    print("invalid input")


# In[ ]:





# In[2]:


20. Write a program that determines the roots of a cubic equation using the Cardano formula.


# In[ ]:


import math

a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))
d = float(input("Enter the coefficient d: "))

p = (3 * a * c - b ** 2) / (3 * a ** 2)
q = (2 * b ** 3 - 9 * a * b * c + 27 * a ** 2 * d) / (27 * a ** 3)
delta = (q ** 2) / 4 + (p ** 3) / 27

if delta > 0:
    root1 = -1 * (q / 2 + math.sqrt(delta)) ** (1 / 3) - (q / 2 - math.sqrt(delta)) ** (1 / 3) - b / (3 * a)
    print("Root 1:", root1)
elif delta == 0:
    root1 = -1 * (q / 2) ** (1 / 3) - (q / 2) ** (1 / 3) - b / (3 * a)
    root2 = (q / a) ** (1 / 3) - b / (3 * a)
    print("Root 1:", root1)
    print("Root 2:", root2)
else:
    r = math.sqrt(-(p ** 3) / 27)
    theta = math.acos(-q / (2 * r))
    root1 = 2 * math.sqrt(-p / 3) * math.cos(theta / 3) - b / (3 * a)
    root2 = 2 * math.sqrt(-p / 3) * math.cos((theta + 2 * math.pi) / 3) - b / (3 * a)
    root3 = 2 * math.sqrt(-p / 3) * math.cos((theta + 4 * math.pi) / 3) - b / (3 * a)
    print("Root 1:", root1)
    print("Root 2:", root2)
    print("Root 3:", root3)


# In[ ]:





# Advanced Level:

# 21. Create a program that calculates the income tax based on the user's income and tax brackets.

# In[4]:


print("""
if income<1000 you not to pay tax,
if income>1000 you have to pay 2.5% tax,
if income>2000 you have to pay 3.5% tax,
if income>3000 you have to pay 5.0% tax""")
income=int(input("Enter your yearly income :$"))
if income>=1000 and income<2000:
    tax=(2.5/100)*income
    print(f"tax=${tax}")
elif income>=2000 and income<3000:
    tax=(3.5/100)*income
    print(f"tax=${tax}")
elif income>=3000 and income<5000:
    tax=(5.0/100)*income
    print(f"tax=${tax}")
elif income<1000 and income>0:
    print("No tax for this price bracket")
else:
    print("invalid number ")


# In[ ]:





# 22. Write a program that simulates a rock-paper-scissors game against the computer.

# In[8]:


import random
computer_chose=["rock","paper","scissor"]
computer_choose=random.choice(computer_chose)

person_chose=input("Enter your choice :")
if  computer_choose==person_chose:
    print(f"Computer choose :{computer_choose}\nTie")
elif computer_choose=="rock" and person_chose=="paper":
    print(f"Computer choose :{computer_choose}\nYou lose")
elif computer_choose=="paper" and person_chose=="rock":
    print(f"Computer choose :{computer_choose}\nYou Win")
elif  computer_choose=="scissor" and person_chose=="rock":
    print(f"Computer choose :{computer_choose}\nYou Win")
elif  computer_choose=="rock" and person_chose=="scissor":
    print(f"Computer choose :{computer_choose}\nYou lose")
elif  computer_choose=="paper" and person_chose=="scissor":
    print(f"Computer choose :{computer_choose}\nYou Win")
elif  computer_choose=="scissor" and person_chose=="paper":
    print(f"Computer choose :{computer_choose}\nYou lose")
else:
    print("invalid input")


# In[ ]:





# 23. Develop a program that generates a random password based on user preferences (length, complexity).

# In[16]:


import random
import string

def generate_password(length, use_uppercase, use_lowercase, use_numbers, use_special_chars):
    characters = ""
    
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_numbers:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    if len(characters) == 0:
        print("Please select at least one character type for the password.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")
    length = int(input("Enter the desired password length: "))

    use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == "yes"
    use_lowercase = input("Include lowercase letters? (yes/no): ").lower() == "yes"
    use_numbers = input("Include numbers? (yes/no): ").lower() == "yes"
    use_special_chars = input("Include special characters? (yes/no): ").lower() == "yes"

    password = generate_password(length, use_uppercase, use_lowercase, use_numbers, use_special_chars)

    if password:
        print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()


# In[ ]:





# 24. Create a program that implements a simple text-based adventure game with branching scenarios.

# In[17]:


import time

print("Welcome to the Simple Adventure Game!")
print("You are standing at the entrance of a cave.")
print("There are two paths in front of you.")
print("Which path will you choose?\n")

print("1. Go left.")
print("2. Go right.")
choice = input("Enter '1' to go left, '2' to go right: ")

if choice == '1':
    print("You follow the left path and find a treasure chest!")
    print("Congratulations! You have won the game.")
else:
    print("You follow the right path and encounter a dead end.")
    print("Unfortunately, you didn't find anything here.")

print("Do you want to play again? (yes/no)")
play_again = input().lower()

if play_again == "yes":
    print("\nWelcome to the Simple Adventure Game!")
    print("You are standing at the entrance of a cave.")
    print("There are two paths in front of you.")
    print("Which path will you choose?\n")

    print("1. Go left.")
    print("2. Go right.")
    choice = input("Enter '1' to go left, '2' to go right: ")

    if choice == '1':
        print("You follow the left path and find a treasure chest!")
        print("Congratulations! You have won the game.")
    else:
        print("You follow the right path and encounter a dead end.")
        print("Unfortunately, you didn't find anything here.")
    
    print("Thanks for playing!")
else:
    print("Thanks for playing!")


# In[ ]:





# 25. Build a program that solves a linear equation for x, considering different cases.

# In[ ]:


def solve_linear_equation(a, b):
    if a == 0:
        if b == 0:
            print("Infinite solutions (all real numbers are solutions).")
        else:
            print("No solution (contradiction).")
    else:
        x = -b / a
        print(f"The solution is x = {x:.2f}")

print("Linear Equation Solver")
print("This program solves equations in the form: ax + b = 0")
a = float(input("Enter the value of 'a': "))
b = float(input("Enter the value of 'b': "))

solve_linear_equation(a, b)


# In[ ]:





# 26. Write a program that simulates a basic quiz game with multiple-choice questions and scoring.

# In[23]:


print("You have 4 Random Questions:")

questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A) London", "B) Berlin", "C) Paris", "D) Madrid"],
        "answer": "C",
    },
    {
        "question": 'Which planet is known as the "Red Planet"?',
        "options": ["A) Venus", "B) Earth", "C) Mars", "D) Jupiter"],
        "answer": "C",
    },
    {
        "question": "What is the chemical symbol for the element oxygen?",
        "options": ["A) O", "B) Ox", "C) O2", "D) Oy"],
        "answer": "A",
    },
    {
        "question": 'Who wrote the play "Romeo and Juliet"?',
        "options": ["A) Charles Dickens", "B) William Shakespeare", "C) Jane Austen", "D) Mark Twain"],
        "answer": "B",
    },
]

total_points = 0

for i, q in enumerate(questions, start=1):
    print(f"Q{i}: {q['question']}")
    for option in q['options']:
        print(option)
    answer = input("Enter your answer: ").strip().upper()
    if answer == q['answer']:
        print("Congratulations! You got 1 point")
        total_points += 1
    else:
        print("You lose")

print(f"You got a total of {total_points} out of 4")
if total_points > 2:
    print("You passed the quiz")
else:
    print("You didn't pass the quiz")

    


# In[ ]:





# 27. Develop a program that determines whether a given year is a prime number or not.

# In[29]:


year=int(input("Enter a Year :"))
if year==2:
    print("Not prime number")
elif year%2!=0:
    print("Prime number")
else:
    print("Not prime number")


# In[ ]:





# 28. Create a program that sorts three numbers in ascending order using conditional statements.

# In[30]:


num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))


if num1 <= num2 and num1 <= num3:
    smallest = num1
    if num2 <= num3:
        middle = num2
        largest = num3
    else:
        middle = num3
        largest = num2
elif num2 <= num1 and num2 <= num3:
    smallest = num2
    if num1 <= num3:
        middle = num1
        largest = num3
    else:
        middle = num3
        largest = num1
else:
    smallest = num3
    if num1 <= num2:
        middle = num1
        largest = num2
    else:
        middle = num2
        largest = num1

print("Numbers in ascending order:", smallest, middle, largest)


# In[ ]:





# 29. Build a program that determines the roots of a quartic equation using numerical methods.

# In[ ]:


import sympy as sp

x = sp.symbols('x')
equation = x**4 - 6*x**3 + 11*x**2 - 6*x


derivative = sp.diff(equation, x)

initial_guesses = [1.0, 2.0, 3.0, 4.0]

max_iterations = 1000
tolerance = 1e-6

roots = []
for guess in initial_guesses:
    root = guess
    for i in range(max_iterations):
        new_root = root - equation.subs(x, root) / derivative.subs(x, root)
        if abs(new_root - root) < tolerance:
            roots.append(new_root)
            break
        root = new_root

print("Roots of the quartic equation:")
for idx, root in enumerate(roots):
    print(f"Root {idx + 1}: {root:.6f}")


# In[ ]:





# In[32]:


height=float(input("Enter Your Height in meters :"))
weight=float(input("Enter Your Weight in kg :"))
bmi=weight / (height ** 2)
if weight / (height ** 2)>=16 and weight / (height ** 2)<18.4:
    print(f"Your BMI is {bmi} and you are Under Weight")
    print("You are week you have to take a healthy meal daily")
elif weight / (height ** 2)>=18.5 and weight / (height ** 2)<24.9:
    print(f" Your BMI is {bmi} and you are Normal")
    print("Your health is good but you have to exercise daily.")
elif weight / (height ** 2)>=25 and weight / (height ** 2)<29.9:
    print(f"Your BMI is {bmi} and you are Over Weight")
    print("You are overweight you have to balance your diet.")
else:
    print("Obese")


# In[ ]:





# 31. Create a program that validates a password based on complexity rules (length, characters, etc.).

# In[ ]:


import re

def is_valid_password(password):
    if len(password) < 8:
        return False

    if not re.search(r'[A-Z]', password) or not re.search(r'[a-z]', password) or not re.search(r'\d', password):
        return False

    if not re.search(r'[!@#$%^&*]', password):
        return False

    return True

password = input("Enter a password: ")
if is_valid_password(password):
    print("Valid password.")
else:
    print("Invalid password.")


# In[ ]:





# 32. Develop a program that performs matrix addition and subtraction based on user input.

# In[ ]:


import numpy as np

rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

matrix1 = np.array([[int(input(f"Enter element at ({i+1},{j+1}) for matrix 1: ")) for j in range(cols)] for i in range(rows)])
matrix2 = np.array([[int(input(f"Enter element at ({i+1},{j+1}) for matrix 2: ")) for j in range(cols)] for i in range(rows)])

sum_matrix = matrix1 + matrix2
diff_matrix = matrix1 - matrix2

print("Matrix Addition:")
print(sum_matrix)

print("Matrix Subtraction:")
print(diff_matrix)


# In[ ]:





# 33. Write a program that calculates the greatest common divisor (GCD) of two numbers using the Euclidean
# algorithm.

# In[ ]:


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = gcd(num1, num2)
print(f"The GCD of {num1} and {num2} is {result}")


# In[ ]:





# 34. Build a program that performs matrix multiplication using nested loops and conditional statements.

# In[ ]:


def matrix_multiply(mat1, mat2):
    result = [[0 for _ in range(len(mat2[0]))] for _ in range(len(mat1))]
    
    for i in range(len(mat1)):
        for j in range(len(mat2[0])):
            for k in range(len(mat2)):
                result[i][j] += mat1[i][k] * mat2[k][j]
    
    return result

rows1 = int(input("Enter the number of rows for matrix 1: "))
cols1 = int(input("Enter the number of columns for matrix 1: "))
rows2 = int(input("Enter the number of rows for matrix 2: "))
cols2 = int(input("Enter the number of columns for matrix 2: "))

matrix1 = [[int(input(f"Enter element at ({i+1},{j+1}) for matrix 1: ")) for j in range(cols1)] for i in range(rows1)]
matrix2 = [[int(input(f"Enter element at ({i+1},{j+1}) for matrix 2: ")) for j in range(cols2)] for i in range(rows2)]

if cols1 != rows2:
    print("Matrix multiplication is not possible. Columns of matrix 1 must equal rows of matrix 2.")
else:
    result_matrix = matrix_multiply(matrix1, matrix2)
    print("Matrix Multiplication Result:")
    for row in result_matrix:
        print(row)


# In[ ]:





# 35. Create a program that simulates a basic text-based tic-tac-toe game against the computer.

# In[ ]:


import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def computer_move(board):
    empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]
    return random.choice(empty_cells)

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"
    computer = "O"

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        row, col = map(int, input("Enter your move (row and column, e.g., 1 2): ").split())
        if board[row - 1][col - 1] != " ":
            print("Invalid move. Try again.")
            continue

        board[row - 1][col - 1] = player
        print_board(board)

        if check_winner(board, player):
            print("Congratulations! You win!")
            break
        elif is_board_full(board):
            print("It's a draw!")
            break

        print("Computer's turn:")
        comp_row, comp_col = computer_move(board)
        board[comp_row][comp_col] = computer
        print_board(board)

        if check_winner(board, computer):
            print("Computer wins. Better luck next time!")
            break
        elif is_board_full(board):
            print("It's a draw!")
            break

play_game()


# In[ ]:





# 36. Write a program that generates Fibonacci numbers up to a specified term using iterative methods.

# In[ ]:


def generate_fibonacci(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib

n = int(input("Enter the number of Fibonacci numbers to generate: "))
fibonacci_sequence = generate_fibonacci(n)
print(f"Fibonacci sequence up to term {n}: {fibonacci_sequence}")


# In[ ]:





# 37. Develop a program that calculates the nth term of the Fibonacci sequence using memoization.

# In[ ]:


def fibonacci_memoization(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memoization(n - 1, memo) + fibonacci_memoization(n - 2, memo)
    return memo[n]

n = int(input("Enter the term of the Fibonacci sequence to calculate: "))
result = fibonacci_memoization(n)
print(f"The {n}-th term of the Fibonacci sequence is {result}")


# In[ ]:





# 38. Create a program that generates a calendar for a given month and year using conditional statements.

# In[35]:


import calendar

year = int(input("Enter year: "))
month = int(input("Enter month (1-12): "))

cal = calendar.month(year, month)
print("Calendar:")
print(cal)


# In[ ]:





# 39. Build a program that simulates a basic text-based blackjack game against the computer.

# In[ ]:


import random

def deal_card():
    return random.randint(1, 11)

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def play_blackjack():
    user_cards = [deal_card(), deal_card()]
    computer_cards = [deal_card()]

    print(f"Your cards: {user_cards}, current score: {calculate_score(user_cards)}")
    print(f"Computer's first card: {computer_cards[0]}")

    while calculate_score(user_cards) != 0 and calculate_score(computer_cards) < 21:
        action = input("Type 'y' to get another card, 'n' to pass: ").lower()
        if action == 'y':
            user_cards.append(deal_card())
            print(f"Your cards: {user_cards}, current score: {calculate_score(user_cards)}")
        else:
            break

    while calculate_score(computer_cards) != 0 and calculate_score(computer_cards) < 17:
        computer_cards.append(deal_card())

    print(f"Your final hand: {user_cards}, final score: {calculate_score(user_cards)}")
    print(f"Computer's final hand: {computer_cards}, final score: {calculate_score(computer_cards)}")

    if calculate_score(user_cards) > 21:
        return "You went over. You lose!"
    elif calculate_score(computer_cards) > 21:
        return "Computer went over. You win!"
    elif calculate_score(user_cards) == calculate_score(computer_cards):
        return "It's a draw!"
    elif calculate_score(user_cards) == 0 or calculate_score(user_cards) > calculate_score(computer_cards):
        return "You win!"
    else:
        return "Computer wins!"

print("Welcome to Blackjack!")
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y":
    print(play_blackjack())


# In[ ]:





# 40. Write a program that generates the prime factors of a given number using trial division.

# In[ ]:


def prime_factors(n):
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    return factors

num = int(input("Enter a number to find its prime factors: "))
result = prime_factors(num)
print(f"Prime factors of {num}: {result}")


# In[ ]:


#hope you like my assignment

