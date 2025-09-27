#DAY 1
name=input("Enter name : ")
age=int(input("Enter age: "))
print(f"Hello {name}, you are {age} years old!") 

#DAY2
print("Table using for loop")
number=int(input("Enter number "))
for i in range(1,11):
    print(i*number)


print("Table using while loop")
n=1
while(n!=11):
   print(n*number)
   n=n+1

#DAY3
students = {
    "Amit": 85,
    "Pooja": 92,
    "Rahul": 78,
    "Sneha": 95,
    "Vikram": 88
}

topper = max(students, key=students.get)

print("Student with highest marks:", topper, "with", students[topper], "marks")

#DAY4

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):  
        if n % i == 0:
            return False
    return True

primes = [num for num in range(1, 101) if is_prime(num)]

with open("primes.txt", "w") as f:
    for p in primes:
        f.write(str(p) + "\n")

print("Prime numbers between 1 and 100 are saved in primes.txt")

# DAY5
class Student:
    def _init_(self, name: str, marks: list):
        self.name = name
        self.marks = marks

    def average(self) -> float:
        if len(self.marks) == 0:
            return 0
        return sum(self.marks) / len(self.marks)

s1 = Student("Krishna", [85, 90, 78, 92, 88])
print("Name:", s1.name)
print("Marks:", s1.marks)
print("Average Marks:", s1.average())


#DAY6

import math

class Shape:
    def _init_(self, length=None, width=None, radius=None):
        self.length = length
        self.width = width
        self.radius = radius

    def area(self):
        return 0

class Rectangle(Shape):
    def _init_(self, length, width):
        super()._init_(length=length, width=width)  

    def area(self):
        return self.length * self.width

class Circle(Shape):
    def _init_(self, radius):
        super()._init_(radius=radius)  

    def area(self):
        return math.pi * self.radius ** 2

rect = Rectangle(10, 5)
circle = Circle(7)

print("Rectangle Area:", rect.area())
print("Circle Area:", circle.area())
      

# DAY 7
import numpy as np

matrix = np.arange(9).reshape(3, 3)
print("Matrix:\n", matrix)
print("Shape:", matrix.shape)        # rows, columns
print("Size:", matrix.size)          # total number of elements
print("Dimension:", matrix.ndim)     # number of dimensions

# 2. Generate 100 random numbers from normal distribution
data = np.random.normal(loc=0, scale=1, size=100)  # mean=0, std=1
print("\nMean of data:", np.mean(data))
print("Standard Deviation of data:", np.std(data))





