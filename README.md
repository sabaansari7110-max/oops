# OOPs
This repository is designed for beginners and intermediate Python developers who want to deeply understand Object-Oriented Programming. It covers core OOP concepts with simple, well-commented code examples, real-world analogies, and mini-projects.

**Topics Covered:**
- Classes and Objects
- Class Attributes vs Instance Attributes
- The `self` parameter
- `__init__` Constructor
- Instance Methods, Class Methods, and Static Methods
- And more (Inheritance, Encapsulation, Polymorphism, etc. — coming soon)

Perfect for students, self-learners, and anyone preparing for Python interviews or building robust applications.

## 🗂️ Table of Contents

- [What is a Class?](#what-is-a-class)
- [Class Attributes vs Instance Attributes](#class-attributes-vs-instance-attributes)
- [The `self` Parameter](#the-self-parameter)
- [The `__init__` Constructor](#the-init-constructor)
- [Static Methods](#static-methods)
- [How to Run](#how-to-run)
- [Contributing](#contributing)

## What is a Class?

A **class** is a blueprint for creating objects. It defines the properties (attributes) and behaviors (methods) that the objects will have.

```python
class Dog:
    # Class attribute (shared by all instances)
    species = "Canis familiaris"
    
    def __init__(self, name, age):
        # Instance attributes
        self.name = name
        self.age = age
```

    # Instance method
    def bark(self):
        return f"{self.name} says Woof!"
# Class Attributes vs Instance Attributes
Class Attributes: Defined directly in the class body. Shared among all instances.
<br>
Instance Attributes: Defined inside __init__ (or other methods) using self. Unique to each object.
<br>
```python
class Car:
    # Class attribute
    wheels = 4
    
    def __init__(self, brand, model):
        # Instance attributes
        self.brand = brand
        self.model = model

# Usage
car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")

print(car1.wheels)   # 4 (shared)
print(car2.wheels)   # 4

Car.wheels = 6       # Changes for all instances
print(car1.wheels)   # 6
```
# The self Parameter
self represents the instance of the class. It allows you to access attributes and methods within the class.
<br>
It is the first parameter of every instance method.
<br>
You don't pass it manually — Python does it automatically when you call the method on an object.
```python
class Person:
    def __init__(self, name):
        self.name = name   # self.name is instance attribute
    
    def introduce(self):
        print(f"Hi, I'm {self.name}!")   # Accessing via self
```
# The __init__ Constructor
The __init__ method is a special method (constructor) that gets called automatically when you create a new object.
<br>
It is used to initialize the object's attributes.
```python
class Student:
    def __init__(self, name, roll_no, marks=0):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
    
    def display(self):
        print(f"Name: {self.name}, Roll No: {self.roll_no}, Marks: {self.marks}")

s1 = Student("Alice", 101, 95)
s1.display()
```
# Static Methods
Defined using the @staticmethod decorator.
<br>
Do not receive self or cls as the first argument.
<br>
Behave like regular functions but logically belong to the class.
<br>
Cannot access or modify instance or class attributes.
<br>
Use case: Utility functions related to the class.
```python
class MathUtils:
    @staticmethod
    def add(x, y):
        return x + y
    
    @staticmethod
    def is_even(num):
        return num % 2 == 0

print(MathUtils.add(5, 7))        # 12
print(MathUtils.is_even(10))      # True
```
# How to Run
<br>
Clone the repository:
<br>
https://github.com/sabaansari7110-max/oops.git
<br>

<br>
Run any example file:
<br>
    ```    python examples/ 01_class.py
<br>
All examples are in the examples/ folder with clear filenames.

## Who this is for
This repo is built for beginners learning python who want to understand OOPs from the ground up with clear, practical examples.
<br>

## Author
Created as part of Python learning journey to strengthen programming fundamentals and logical thinking.

## License
This project is licensed under the MIT License. You are free to use, modify, and distribute this project with proper attribution.
## Contributing
1.Feel free to contribute!
<br>
2.Add more examples
<br>
3.Improve explanations
<br>
4.Fix bugs or add new OOP topics (Inheritance, Polymorphism, etc.)
<br>
5.Fork the repo
<br>
6.Create a feature branch
<br>
7.Commit your changes
<br>
8.Open a Pull Request
<br>
⭐ Star this repo if you found it helpful!
