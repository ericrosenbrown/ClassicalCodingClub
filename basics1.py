import math

#Data Types
4
-2
50121

1/3
-2/8

'a'
'G'
'z'

'!'
'@'
'?'

"I like computer Science!"
"Classical is a great highschool"

True
False
1 == 1
1 > 5
2 < 1

#Printing

print "hi"
print 50
print 1==1
print "True"

#Variables
x=2
y=6

z=x+y
print x
print y
print z

name = "eric"
age = 21
legal_driving_age = 16
can_drive = age > legal_driving_age
print legal_driving_age
print age
print can_drive

#Data operations
a = (((10*5)-20)/6) + 9
print a
print math.pi

fname = "Eric"
lname = "Rosen"
space = " "

name1 = fname + lname
print name1
name2 = fname + space + lname
print name2

j = 5 > 2
print j
k = (5 > 2 ) and (6 > 2)
print k
l = (1 > 2 ) and (6 > 2)
print l

#Functions
def f(x):
    return x + 1

print f(5)

def g(a,b,c):
    return ((a+b)/c)

print g(2,4,1)

def gpa_calculator(grades):
    return sum(grades)/len(grades)

print gpa_calculator([4,3.33,3.33])

#if statements
if (2 < 3):
    print "2 is less than 3"
if (2 > 3):
    print "2 is greater than 3"
if (2 == 3):
    print "2 is equal to 3"

#for loops/increments
for i in range(3):
    print "dog"
    
x = 2
print x
x = x + 1
print x
x = x + 1
print x

x = 0
print x

for i in range(3):
    x = x + 1

print x
    

