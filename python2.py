bil = int(input("Masukan bilangan bulat: "))

if(bil%2 == 0):
    print("genap")
else:
    print("ganjil")

print("Masukan nilai koordinat")
x = int(input("Nilai x: "))
y = int(input("Nilai y: "))

if x>0 and y>0:
    print("Koordinat ("+ str(x) + ","+ str(y) +") berada pada Kuadran I" )
elif x<0 and y>0:
    print("Koordinat ("+ str(x) + ","+ str(y) +") berada pada Kuadran II" )    
elif x<0 and y<0:
    print("Koordinat ("+ str(x) + ","+ str(y) +") berada pada Kuadran III" )
elif x>0 and y<0:
    print("Koordinat ("+ str(x) + ","+ str(y) +") berada pada Kuadran IV" )
else:
    pass

num1 = int(input("First Number : "))
num2 = int(input("Second Number : "))
num3 = int(input("Third Number : "))

#set number1 sebagai yang terbesar
largestNum = num1

#deteksi apakah num2 > num1
if num2 > largestNum:
    largestNum = num2

#deteksi apakah num3 > num2
if num3 > largestNum:
    largestNum = num3

print("The largest number is: ", largestNum)

plant = input("Please input a best plant = ")

if plant == "Spathiphyllum":
    print("Yes - Spathiphyllum is the best plant ever!")
elif plant == "spathiphyllum":
    print("No, I want a big Spathiphyllum!")
else:
    print("Spathiphyllum! Not "+ plant +"!")

income = float(input("Enter the annual income: "))
tax = 0

if income<85528:
    tax = 0.18 * income - 556.2
else:
    tax = 14839 + 0.2 + 0.32 * (income - 85528)

tax = round(tax, 0)

if tax<0:
    tax = 0

print("The tax is:", tax, "thalers")

year = int(input("Enter a year: "))

if year < 1582:
    print("Not within the Gregorian calender period")
else :
    if year % 4 !=0 :
        print("common year")
    elif year % 100 !=0:
        print ("leap year")
    elif year % 400 !=0:
        print("common year")
    else : 
        print("leap year")

x = 5
y = 10
z = 8

print(x > y)
print(y > z)

x, y, z = 5, 10, 8

print(x > z)
print((y - 5) == x)

x, y, z = 5, 10, 8
x, y, z = z, y, x

print(x > z)
print((y - 5) == x)

x = 10

if x == 10:
    print(x == 10)

if x > 5:
    print(x > 5)

if x < 10:
    print(x < 10)
else:
    print("else")

x = "1"

if x == 1:
    print("one")
elif x == "1":
    if int(x) > 1:
        print("two")
    elif int(x) < 1:
        print("three")
    else:
        print("four")
        
if int(x) == 1:
    print("five")
else:
    print("six")

x = 1
y = 1.0
z = "1"

if x == y:
    print("one")
if y == z:
    print("two")
    print(x)
    print(y)
elif x == y:
    print("three")
else:
    print("four")

secretNum = 777

guessNum = 0

while guessNum != secretNum:
    guessNum = int(input("Input angka rahasia untuk berhenti : "))
    if guessNum != secretNum:
        print("Perulangan akan terus lanjut...")

print("Well done, Congrats...")

import time

for i in range(5):
    print(i," Missisipi")
    time.sleep(1)

while True:
    word = input("Masukkan Sebuah Kata untuk keluar dari perulangan = ")
    if(word=="chupacabra"):
        break
        
print("You've successfully left the loop")

# Prompt the user to enter a word
# and assign it to the userWord variable.
userWord = input("Masukkan sebuah kata = ")

for letter in userWord:
    if letter.upper() in ['A','I','U','E','O']:
        continue
    
    print(letter.upper())

blocks = int(input("Enter the number of blocks: "))
current_block = 0
height = 0
i=0

while i<blocks:
    height += 1
    current_block += height
    # print(i,current_block)
    if current_block> blocks:
        break

height -= 1

print("The height of the pyramid:", height)

for i in range(1, 11):
    if i % 2 !=0:
        print(i,end=' ')

x=1
while x<11:
    if x % 2 !=0:
        print(x,end=' ')
    x +=1

for ch in "ratna.lestari@ugm.ac.id":
    if ch == "@":
        break
    print(ch,end=' ')

for digit in "0165031806510":
    if digit == "0": 
        print ("x")
        continue
    print(digit)

n = 3

while n > 0:
    print(n + 1)
    n -= 1
else:
    print(n)  

n = range(4)

for num in n:
    print(num - 1)
else:
    print(num)

for i in range(0, 6, 3):
    print(i)

# step 1
beatles = []
print("Step 1:", beatles)

# step 2
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Step 2:", beatles)

# step 3
for i in range(2):
    nama = input("Masukkan anggota baru = ")
    beatles.append(nama)
print("Step 3:", beatles)

# step 4
del beatles[-2:]
print("Step 4:", beatles)

# step 5
beatles.insert(0,"Ringo Starr")
print("Step 5:", beatles)


# testing list legth
print("The Fab", len(beatles))

lst = [5, 1, 3, 2, 10]
print(lst)
lst.sort()
print(lst)
lst.reverse()
print(lst)

vehiclesOne = ['car', 'bicycle', 'motor']
print(vehiclesOne) # outputs: ['car', 'bicycle', 'motor']

vehiclesTwo = vehiclesOne
del vehiclesOne[0] # deletes 'car'
print(vehiclesTwo) # outputs: ['bicycle', 'motor']
print(vehiclesOne)

vehiclesOne = ['car', 'bicycle', 'motor']
print(vehiclesOne) # outputs: ['car', 'bicycle', 'motor']

vehiclesTwo = vehiclesOne[:]
del vehiclesOne[0] # deletes 'car'
print(vehiclesTwo) # outputs: ['bicycle', 'motor']
print(vehiclesOne)

nama = ["Ana","Budi","Citra"]
kata_kunci = "Budi"

print(kata_kunci not in nama)

if kata_kunci in nama:
    print("Nama "+kata_kunci+" ada di list")

for i in range(10):
    print(i, end=" ")
    
print()
for i in range(1,7):
    print(i, end=" ")
    
print()
for i in range(1,10,2):
    print(i, end=" ")
    
print()
for i in range(10,-10,-2):
    print(i, end=" ")

x = 1
while x < 11:
    if x%2!=0:
        print(x, end=" ")
    x += 1

for ch in "john.smith@pythoninstitute.org":
    if ch == "@":
        break
    print(ch,end="")

for digit in "0165031806510":
    if digit == "0":
        print("x",end="")
        continue
    print(digit,end="")