import math
class Circle:
    def __init__(self, radius, color):
        self.__radius = radius
        self.__color = color
        
    def getRadius(self):
        return self.__radius
    
    def setRadius(self,radius):
        self.__radius = radius
    
    def getColor(self):
        return self.__color
    
    def setColor(self,color):
        self.__color = color
    
    def getArea(self):
        return math.pi * self.__radius ** 2
    

# radius = 2, color = blue
c1 = Circle(2,"blue")
# c1.setRadius(2)
# c1.setColor("blue")
print(c1.getArea())

# radius = 2, color = red
c2 = Circle(2,"red")
# c2.setRadius(2)
# c2.setColor("red")
print(c2.getArea())

# radius = 1, color = red
c3 = Circle(1,"red")
# c3.setRadius(1)
# c3.setColor("red")
print(c3.getArea())

class Student:
    def __init__(self,name,address):
        self.__name = name
        self.__address = address
        self.__numCourses = 0
        self.__courses = []
        self.__grades = []
        
    def getName(self):
        return self.__name
    
    def getAddress(self):
        return self.__address
    
    def setAddress(self,address):
        self.__address = address
        
    def addCourseGrade(self,course,grade):
        self.__courses.append(course)
        self.__grades.append(grade)
        self.__numCourses += 1
        
    def printGrades(self):
        for i in range(len(self.__courses)):
            print(self.__courses[i] +" : "+ str(self.__grades[i]))
            
    def getAverageGrade(self):
        sum = 0
        for n in self.__grades:
            sum += n
        return sum / len(self.__grades)
            

n_siswa = int(input("Masukkan Jumlah Siswa = "))
n_course = int(input("Masukkkan Jumlah Course = "))

siswa = []
for i in range(n_siswa):
    nama = input("Masukkan Nama Siswa = ")
    alamat = input("Masukkan Alamat Siswa = ")
    siswa.append(Student(nama,alamat))
    for j in range(n_course):
        mapel = input("Masukkan Nama Mapel Siswa "+nama+" = ")
        nilai = int(input("Masukkan Nilai Mapel Siswa "+nama+" = "))
        siswa[i].addCourseGrade(mapel,nilai)

print("Hasil")
for i in range(n_siswa):
    print(s1.getName(),s1.getAddress())
    siswa[i].printGrades()
    print("Rata-Rata : ", siswa[i].getAverageGrade())

# s1 = Student("Ani","Yogyakarta")
# print(s1.getName(),s1.getAddress())
# s1.addCourseGrade("Matematika",95)
# s1.addCourseGrade("IPA",90)
# s1.addCourseGrade("Bahasa Indonesia",85)
# s1.printGrades()
# print("Rata-Rata : ", s1.getAverageGrade())

# print()
# s2 = Student("Budi","Jakarta")
# print(s2.getName(),s2.getAddress())
# s2.addCourseGrade("Matematika",60)
# s2.addCourseGrade("IPA",70)
# s2.addCourseGrade("Bahasa Indonesia",100)
# s2.printGrades()
# print("Rata-Rata : ", s2.getAverageGrade())

class Employee:
    def __init__(self,idEmp,firstName,lastName,salary):
        self.__idEmp = idEmp
        self.__firstName = firstName
        self.__lastName = lastName
        self.__salary = salary
    
    def getID(self):
        return self.__idEmp
    
    def getFirstName(self):
        return self.__firstName
    
    def getLastName(self):
        return self.__lastName
    
    def getName(self):
        return self.__firstName + " " + self.__lastName
    
    def getSalary(self):
        return self.__salary
    
    def setSalary(self,salary):
        self.__salary = salary
        
    def getAnnualSalary(self):
        return self.__salary * 12
    
    def raiseSalary(self,percent):
        self.__salary += self.__salary * (percent/100)
        return self.__salary
    
    def __str__(self):
        return self.getName() + " " + str(self.getSalary())
        

class Manager(Employee):
    def __init__(self,idEmp,firstName,lastName,salary,bonus):
        super().__init__(idEmp,firstName,lastName,salary)
        self.__bonus = bonus
        
    def setBranch(self, branch):
        self.__branch = branch
    
    def getBranch(self, branch):
        return self.__branch
    
    def getBonus(self, bonus):
        return self.__bonus
    
    def setBonus(self, bonus):
        self.__bonus = bonus
        
    def getAnnualSalary(self):
        return super().getSalary() * 12 + self.__bonus
        

m1 = Manager(1234,"Guntur","Budi",5000,9000)
print(m1.getName())
print(m1.getAnnualSalary())

# e1 = Employee(1234,"Guntur","Budi",5000)
# print(e1.getSalary())
# print(e1.getAnnualSalary())
# print(e1.raiseSalary(50))
# print(e1.getAnnualSalary())
# print(e1)

class Person:
    def __init__(self,name,address):
        self.__name = name
        self.__address = address
    
    def getName(self):
        return self.__name
    
    def getAddress(self):
        return self.__address
    
    # Tambahan 'self' di sini agar tidak error saat dipanggil
    def setName(self, name): 
        self.__name = name
        
    def __str__(self):
        return self.__name+" "+self.__address
    

# Posisikan sejajar paling kiri (di luar class Person)
class Student(Person):
    # Menjorok ke dalam (di dalam class Student)
    def __init__(self,name,address):
        super().__init__(name,address)
        self.__numCourses = 0
        self.__courses = []
        self.__grades = []        
    
    def addCourseGrade(self,course,grade):
        self.__courses.append(course)
        self.__grades.append(grade)
        self.__numCourses += 1
        
    def printGrades(self):
        for i in range(len(self.__courses)):
            print(self.__courses[i] +" : "+ str(self.__grades[i]))
            
    def getAverageGrade(self):
        sum = 0
        for n in self.__grades:
            sum += n
        return sum / len(self.__grades)
    
    def __str__(self):
        return "Student: " + super().getName() + " " +super().getAddress()


# Posisikan sejajar paling kiri
class Teacher(Person):
    def __init__(self,name,address):
        super().__init__(name,address)
        self.__numCourses = 0
        self.__courses = []
        
    def addCourse(self, course):
        if course not in self.__courses:
            self.__courses.append(course)
            return True
        else:
            return False
        
    def removeCourse(self, course):
        if course in self.__courses:
            i = self.__courses.index(course)
            del self.__courses[i]
            return True
        else:
            return False
        
    def printCourse(self):
        print(self.__courses)
        
    def __str__(self):
        return "Teacher: " + super().getName() + " " +super().getAddress()

# --- BLOK TESTING ---
t1 = Teacher("Pak Budi","Jakarta")
print(t1)

t1.addCourse("Matematika")
t1.addCourse("Fisika")

t1.printCourse()
if(t1.removeCourse("Biologi")):
    print("Berhasil Dihapus")
else:
    print("Gagal Dihapus")
t1.printCourse()