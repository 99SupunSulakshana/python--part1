# Basic Operators

# Addition
print(6+5)

# subtraction
print(7-3)

# multiplication
print(4*5)

# division
print(4/3)

# flow division
print(4//3)

# modulus
print(6%2)
print(6%4)

# exponent
print(2**4)

# variables handling in python
name = 'Supun'
_name = 'Sulakshana'
print(name)
print(_name)

# data types

a = 12
type(a)  # Building function

f = 3+4j
type(f)

myInt = 10
myFloat = 7.5

myFloat = myInt
print(myFloat)

myFloat = float(myInt)
print(myFloat)

# print function and input function in python

print('Supun Sulakshana')

name = 'Supun'
print('New Software Engineer is '+name)

age = 23
print('His age is '+str(age))

# create format
# %s - string value & %d - decimal value & %f - float value
print('New Software Engineer is %s and His age is %d' %(name,age))

x = 4.2312
print('price is %f' %x)

# change the .mark
print('price is %.3f' %x)

# input function
x = input()
print(x)

z = int(input('Enter the your age = '))
print(z)

s = float(input('Enter the your weight = '))
print(s)


# built in functions

print(pow(5,4))

help(pow)


print(max(4,6,5,8))

print(min(4,5,9,8))

import math
math.sqrt(100)

# python String handling

x = "Supun Sulakshana"
print(x.capitalize())
print(x.upper())
print(x.lower())
print(x[2:6])
print(x.replace('S','K'))
print(x.split('u'))

y = x.split(' ')
print(y)

z = 'and'.join(y)
print(z)


# python comparison operators

# Equal Operators
x = 12
y = 13
print(x == y)

# Not equal operators
print(x != y)
# Greater than operators
print(x > y)
# Less Than Operators
print(x < y)
# Greater than or equal operators
print(x >= y)
# Less than or equal operators
print(x <= y)

# check the lower letters or not
x = 'supun sulakshana'
print(x.islower())
# check the upper letters or not
print(x.isupper())

# Logical operators
print(3 > 1 and 6 > 5)
# OR operators
print(3 > 1 or 3 > 5)
# NOT operators
print(not 3 > 5)

# If else statement
x = 15
if x > 50:
    print('pass')
else:
    print('fail')

# Python collection - list

x = [5,2,7,2]
y = ['s','u','p','u','n']
z = [5,3,1,'c','supun',True,[1,2,3]]

# List access
print(z[0])
print(z[1])
print(z)

# change the element
x[1] = 12
print(x)

# check the length

print(len(x))
print(len(y))
print(len(z))

# insert the value
x.insert(2,12)
print(x)

# add the last element
x.append(11)

# remove the values
x.remove(7)
print(x)

# remove the last value
x.pop()
print(x)

# completely clear the elements
x.clear()
print(x)

# sort the list ( assending order )
x.sort()
print(x)

# sort the list ( dissending order )
x.sort(reverse=True)
print(x)

a,b,c,d = [5,2,1,3]
print(a)
print(b)
print(c)
print(d)

a,b,*c = [5,1,2,4]
print(a)
print(b)
print(c)

# completely delete list
del x
print(x)

# Tuple in the python - cannot change the elements in the tuple
x = (1,2,3,4)
z = (4,2,7,True,'g','python')


print(x)
print(len(x))

# create the tuple (join two tuple)
x = y+z

x = ()
y = ('java',)
z = ('python', 'spring')

print(x)
print(y)
print(z)

# create new tuple
x = (5,2,1,1)
# find the max value in tuple
print(max(x))
# find the min value in tuple
print(min(x))

# delete the tuple
del x
print(x)
# tuple cannot add the elements, cannot remove the elements,but tuple has high security, speed

# check the tuple and list speed
import timeit
list_time = timeit.timeit(stmt="[1,2,3,4]")
tuple_time = timeit.timeit(stmt="(1,2,3,4)")

print(list_time)
print(tuple_time)

# Set - python collection

x = {5,2,3,1}
print(x)

# set cannot identify the index number and cannot print the sort order
# set remove the all duplicate values and its can print the uniq values

# length check the set
print(len(x))

# add elements in set
x.add(12)
print(x)

# how to add multiple elements in set
x.update([12,13])
print(x)

# how to remove the elements in set
x.remove(12)
print(x)

# clear the set elements
x.clear()

# completely delete the set
del x
print(x)

# how to tuple convert the set
x = (1,2,3,4)
y = set(x)
print(y)
print(type(y))

# how to list convert the set
x = [1,2,3,4]
y = set(x)
print(y)
print(type(y))

# how to check common elements in set
x = {1,2,3,4}
y = {2,3,4,5,6}

# 1st method
print(x & y)
# 2nd method
print(x.intersection(y))

# how to check all of set elements
x = {1,2,3,5,6}
y = {2,3,4}

# 1st method
print(x | y)
# 2nd method
print(x.union(y))

# Dictionary - python Collections
# It has include key - value pairs
# We can include the all data types in this dictionary collections


x = {"physics": 65,
     "maths": 43,
     "chemistry": 62}
print(x)

# check the key values
print(x["maths"])

# add the elements
x["english"] = 67
print(x)

# remove the elements
x.pop("english")
print(x)

# clear the dictionary
x.clear()
print(x)

# delete dictionary
del x
print(x)

# Update the elements
x['maths'] = 76
print(x)

# If we want to view the keys
print(x.keys())
# If we want to view the values
print(x.values())
# If we want to view the all items
print(x.items())


# Slicing and Negative Indexing
# Slicing format = list[start:end+1]
lst = [1,4,5,3,4]
print(lst[2:4])
# It we want to print selected value to end elements
print(lst[2:])
# It we want to print last value to start values
print(lst[:3])
# If we want to view the all list elements
print(lst[:])
print(lst)
# If we want to print the step by step elements
print(lst[1::2])

# Negative Indexing
lst = [5,7,4,11,8]
print(lst[-3])

# If we want print the negative values in the step by step
print(lst[-3:-1])
# It we want print the step by step negative indexing
print(lst[-4:-1:2])
# Ir we want print the step by step negative indexing
print(lst[::-1])

# Loops - while Loop
# example -1
i = 1;
while(i < 11):

    print(i)
    i = i+1

# example -2
sum = 0
i = 1;
while(i<=5):
    number = int(input("Enter number : "))
    sum = sum+number
    i = i+1
    print("Sum of Numbers =",sum)

# For loop
# example -1

x = (1,2,3,4,5)
for num in x:
    print(num)

# example -2 with dictionary

x = {'name':'Supun Sulakshana',
     'age':22,
     'Gender':'Male'}

for i,j in x.items():
    print(i)

# Range function -1
for i in range(5):
    print(i)

# Range function -2
for i in range(2,11,2):
    print(i)

# Break Statement and Continue statement

for x in range(1,6):
    if(x == 3):
        break
        print(x)

print("__________________________________________")
i=0
while(i<5):
    i+=1
    if(i == 3):
        break
        print(i)

print("__________________________________________")
for x in range(1,6):
    if(x == 3):
        continue
        print(x)

i =0
while(i<5):
    i+=1
    if(i == 3):
        continue
        print(i)


# User define functions
# example-1
def sum(num1,num2):
    print(num1+num2)
    sum(6,8)

# example-2
def sum1(num1, num2):
    return num1+num2
print(sum(4,5))

# example-3
def func(length, width):
    perimeter = 2*(length+width)
    area = length*width
    print("Perimeter =",perimeter)
    print("Area = ",area)

    func(10,12)

# default arguments in python
def student(subject,marks):
    print("Subject = ",subject)
    print("Marks = ",marks)

    student("Maths",69)

def student(subject,marks,*friends):
    print("Subject = ",subject)
    print("Marks = ",marks)

    for key,values in friends.items():
        print(key,"=",values)

    student("Maths",67,Kasun=76,Pasintha=67,Pamal=90)

# Object Oriented Programming in Python

# create class
class Phone:
    # create method
    def say(self,name):
        self.x=name
        print("Hello "+name)
# what is the self parameter mean? -> Its can help the class attributes define in the another objects
# How to call the class
phone1 = Phone()
phone1.say("Apple")
print(phone1.x)
phone1.x = "Nokia"
print(phone1.x)

phone2 = Phone()
phone2.say("Samsung")


# init_method
# when we create the objects, init methods are run in this all time
class Student:
    def __init__(self,name,age):
        print("hello")

st1 = Student("Kamal",22)
st2 = Student("Supun",22)
print(st1.name)
print(st1.age)

# Encapsulation in python
# We can restrict access to methods and variables
class myClass:
    # public variable
    x = 10
    # private variable
    __y = 20;
    def disp(self):
        return self.__y

myObj = myClass()
print(myObj.__y)

# private methods create

class myClass:
    def meth1(self):
        print("Hello")
        self.__meth2()

    def __meth2(self):
        print("Welcome")

myObj = myClass()
myObj.meth1()

# Inheritance in python

# Single Inheritance
class Phone1:
    def feature1(self):
        print('camera')

class Phone2(Phone1):
    def feature2(self):
        print('blutooth')

myObj = Phone2()
myObj.feature2()

# Multiple Inheritance
class Phone1:
    def feature1(self):
        print('camera')

class Phone3:
    def feature3(self):
        print('blutooth')

class Phone2(Phone1,Phone3):
    def feature2(self):
        print('Internet')

myObj = Phone2()
myObj.feature1()

# Multi level Inheritance
class Phone1:
    def feature1(self):
        print('camera')

class Phone3(Phone1):
    def feature3(self):
        print('blutooth')

class Phone2(Phone3):
    def feature2(self):
        print('Internet')

myObj = Phone2()
myObj.feature1()

# Super function

class Parent:
    def function1(self):
        print('hello')

class Child(Parent):
    def function2(self):
        super().function1()
        print('Welcome')

myObj = Child()
myObj.function2()

# Method Overriding

class Parent:
    def function1(self):
        print('hello')

class Child(Parent):
    def function2(self):
        print('Welcome')
    def function1(self):
        print('Suppa')

myObj = Child()
myObj.function1()

# example of inheritance

class Fruit:
    number_of_items = None
    unit_price = None

    def set_value(self,x,y):
        self.number_of_items = x
        self.unit_price = y

class Apple(Fruit):
    def price(self):
        print('For Apple ',self.number_of_items*self.unit_price)

class Orange(Fruit):
    def price(self):
        print('For Orange ',self.number_of_items*self.unit_price)

class Graphs(Fruit):
    def price(self):
        print('For Graphs ',self.number_of_items*self.unit_price)

myObj1 = Apple()
myObj2 = Orange()
myObj3 = Graphs()

myObj1.set_value(7,100)
myObj2.set_value(5,75)
myObj3.set_value(7,40)

myObj1.price()
myObj2.price()
myObj3.price()

# Create Modules

import cal

i = 10
j = 20

print(cal.add(i,j))
print(cal.sub(i,j))
print(cal.mul(i,j))
print(cal.div(i,j))

# Date and time Module

import datetime

b_dy = datetime.date(1999,9,22)
print(b_dy)

# today

today = datetime.date.today()
print(today)

age = today - b_dy
print(age)

print(today.weekday())

t = datetime.time(9,21,32,10000)
print(t)


# Turtle Module

import turtle

x = turtle.Turtle()

x.forward(100)
x.shape('turtle')
x.color('red')
x.pencolor('blue')
x.forward(100)
x.left(120)
x.forward(200)

# Create square with turtle

x = turtle.Turtle()

x.forward(100)
x.left(90)
x.forward(100)
x.left(90)
x.forward(100)
x.left(90)
x.forward(100)

# create circle with turtle

x.circle(50)

# factorials ex: 4! = 4*3*2*1

result = 1
for i in range(1,5):
    result = result*i

print(result)

# With user input

x = int(input('Enter the number :'))

result = 1
for i in range(1,x+1):
    result = result*1

print(result)

# Factorial using recursion- its only use for positive numbers

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

print(fact(4))






































