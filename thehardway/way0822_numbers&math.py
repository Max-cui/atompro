# -*- coding: utf-8 -*-

print "I will now count my chickens"

print "Hens", 25 + 30/6
print "Roosters", 1-- - 25 * 3 % 4

print "now I will count the eggs:"
print 3 + 2 + 1 - 5 + 4 % 2 - 1 /4 + 6

print "Is is true that 3 + 2 < 5 - 7?"

print 3 + 2 < 5 - 7

print "what is 3 + 2?", 3 + 2
print "what is 5 - 7", 5 - 7

print "oh, that's why it's False."

print "How about some more."

print "Is it greater?", 5 > -2
print "Is it greater or equal?", 5 >= -2
print "Is it less or equal?", 5 <= -2

print 7.0/4.0

print 7/4

a = input("please input your first number: ")
b = input("please input your second number: ")
c = input("please input your math operation: 1,'+',2,'-',3,'*',4,'/'")

def my_operation():
  if c == 1:
    print a + b
  elif c == 2:
    print a - b
  elif c == 3:
    print a * b
  elif c == 4:
    print a / b
  else:
    print "you print wrong choices"

my_operation()
