#!/usr/bin/python3
# _*_ coding: UTF-8 _*_

#les polynomes sont du type
# p= a**2 -2*a*b +b**2

a = 4
b = -3

p1 = a**2 - 2*a*b + b**2
p2 = a**2 + 2*a*b + b**2

print(p1)
print(p2)

if p1 == p2:
    print ("sont egaux")
