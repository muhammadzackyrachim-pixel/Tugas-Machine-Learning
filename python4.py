## override nilai sin dan pi
from math import sin, pi

print(sin(pi/2))

print("=====")

pi = 3.14

def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return None

print(sin(pi/2))

from math import *
print(tan(0))

from math import pi, radians, degrees, sin, cos, tan, asin

ad = 90

ar = radians(ad)
print(ar)
ad = degrees(ar)
print(ad)

print(ad == 90.)
print(ar == pi / 2.)
print(sin(ar) / cos(ar) == tan(ar))
print(asin(sin(ar)) == ar)

# aritmatika.py

def tambah(a,b):
    return a+b

def kurang(a,b):
    return a-b

def kali(a,b):
    return a*b

def bagi(a,b):
    return a/b

import aritmatika

a=aritmatika.tambah(3,4)
b=aritmatika.kurang(3,4)
c=aritmatika.kali(3,4)
d=aritmatika.bagi(3,4)

print(a)
print(b)
print(c)
print(d)

from aritmatika import tambah

a=tambah(10,3)
print(a)