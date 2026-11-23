#                                                                       Object Oriented Programming - II in Python
---

# Instance Variables vs. Class Variables

**Instance variables** are the attributes attached to a specific object of a class. Each object can store different values in its instance variables.

We usually create instance variables using `self` inside the `__init__()` method. We can also create them inside other instance methods.

```python
#example

class Student:

	def __init__(self, name, marks):
	
		self.name = name
		self.marks = marks
		
	def update_marks(self, marks):
	
		self.marks = marks
		
	def add_grade(self, grade):
	
		self.grade = grade

student1 = Student("Yash", 90)
student2 = Student("Aman", 75)

student1.update_marks(95)
student1.add_grade("A")

print(student1.name, student1.marks, student1.grade) # Yash 95 A
print(student2.name, student2.marks) # Aman 75
```

Here, `student1` and `student2` are different objects. Changing the marks of one object does not change the marks of the other object.

The `grade` attribute is created only for `student1` when we call `add_grade()`. It does not automatically exist in `student2`.

**Class variables** are the attributes defined directly inside a class rather than inside its methods. They are stored on the class and can be accessed using the class name or an object.

```python
#example

class Car:

	wheels = 4
	
	def __init__(self, brand, colour):
	
		self.brand = brand
		self.colour = colour

car1 = Car("Toyota", "Black")
car2 = Car("Honda", "White")

print(car1.brand) # Toyota
print(car2.brand) # Honda
print(Car.wheels) # 4
print(car1.wheels) # 4
print(car2.wheels) # 4

Car.wheels = 6

print(car1.wheels) # 6
print(car2.wheels) # 6
```

Here, `brand` and `colour` are instance variables while `wheels` is a class variable. The class variable is not copied into each object. When we access `car1.wheels`, Python checks the object and then finds `wheels` in the class.

Changing `Car.wheels` changes the value found by both objects as long as they do not have their own `wheels` attribute.

**Attribute shadowing** happens when an object has an instance variable with the same name as a class variable. Python uses the instance variable when accessing that attribute through the object.

```python
#example

class Car:

	wheels = 4

car1 = Car()
car2 = Car()

car1.wheels = 3

print(car1.wheels) # 3
print(car2.wheels) # 4
print(Car.wheels) # 4

Car.wheels = 6

print(car1.wheels) # 3
print(car2.wheels) # 6
```

Here, `car1.wheels = 3` creates an instance attribute for `car1`. It does not modify `Car.wheels`. The instance attribute hides the class variable only for `car1`.

`self.variable` refers to an attribute through the current object. When we assign a value to it, we normally create or update the object's instance attribute. `ClassName.variable` refers to the attribute through the class.

Class variables can be used to store shared settings or to count the number of objects created.

```python
#example

class Employee:

	company = "ABC"
	count = 0
	
	def __init__(self, name):
	
		self.name = name
		Employee.count += 1

employee1 = Employee("Yash")
employee2 = Employee("Aman")

print(Employee.company) # ABC
print(Employee.count) # 2
```

**Mutable class variables** are class attributes that store mutable objects such as lists and dictionaries. Changes made to these objects in place can be visible through different instances.

```python
#example

class Classroom:

	students = []

class1 = Classroom()
class2 = Classroom()

class1.students.append("Yash")

print(class2.students) # ['Yash']
print(Classroom.students) # ['Yash']
```

Here, both objects access the same list stored on the class. `append()` modifies that list rather than creating a new instance attribute.

If each object needs its own list, we should create it using `self` inside `__init__()`.

```python
#example

class Classroom:

	def __init__(self):
	
		self.students = []

class1 = Classroom()
class2 = Classroom()

class1.students.append("Yash")

print(class1.students) # ['Yash']
print(class2.students) # []
```

We should not use `self.count += 1` to update a shared class counter when `count` is a class variable. This can create a separate instance attribute instead of updating the class variable.

---

# Instance Methods, Class Methods, and Static Methods

**Instance methods** are functions defined inside a class that receive the current object as their first argument, usually named `self`. They are used to access or modify the attributes of an object.

```python
#example

class Car:

	wheels = 4
	
	def __init__(self, brand):
	
		self.brand = brand
		self.speed = 0
		
	def accelerate(self, acceleration):
	
		self.speed += acceleration
		print(f"{self.brand} accelerated to {self.speed} km/h")
		
	def show_wheels(self):
	
		print(self.wheels)

car1 = Car("Toyota")

car1.accelerate(30) # Toyota accelerated to 30 km/h
car1.show_wheels() # 4
```

Here, `self` represents `car1` when we call `car1.accelerate(30)`. Python automatically passes the object to the instance method.

An instance method can access instance variables using `self.brand` and class variables using `self.wheels`. We use instance methods when the operation needs to work with a specific object's data.

**Class methods** are methods that receive the class as their first argument, usually named `cls`. We use the `@classmethod` decorator to define them.

```python
#example

class Employee:

	company = "ABC"
	
	def __init__(self, name):
	
		self.name = name
		
	@classmethod
	def change_company(cls, company):
	
		cls.company = company

employee1 = Employee("Yash")

Employee.change_company("XYZ")

print(Employee.company) # XYZ
print(employee1.company) # XYZ

employee1.change_company("PQR")

print(Employee.company) # PQR
```

Here, `cls` represents the `Employee` class. We can call a class method using the class name or an object. Both calls change the class variable in this example.

`self` refers to the instance passed to an instance method, while `cls` refers to the class passed to a class method. Both are commonly used names, not reserved Python keywords.

A class method cannot directly access the instance attributes of an arbitrary object without receiving that object.

Class methods can also be used as **alternative constructors** to create objects using a different form of input.

```python
#example

class Student:

	def __init__(self, name, marks):
	
		self.name = name
		self.marks = marks
		
	@classmethod
	def from_text(cls, data):
	
		name, marks = data.split(",")
		return cls(name, int(marks))

student1 = Student.from_text("Yash,90")

print(student1.name) # Yash
print(student1.marks) # 90
```

Here, `from_text()` creates and returns a new `Student` object using the string provided to it.

**Static methods** are methods defined inside a class that do not automatically receive `self` or `cls`. We use the `@staticmethod` decorator to define them.

```python
#example

class Calculator:

	@staticmethod
	def add(a, b):
	
		return a + b

print(Calculator.add(5, 3)) # 8

calculator1 = Calculator()

print(calculator1.add(10, 2)) # 12
```

Here, `add()` does not need any instance or class attributes. We can call it using the class name or an object.

Static methods are useful for utility operations related to a class. They can still access instance or class data if we explicitly pass an object or class to them.

```python
#example

class Student:

	school = "ABC School"
	
	def __init__(self, marks):
	
		self.marks = marks
		
	@staticmethod
	def show_details(student):
	
		print(student.marks)
		print(Student.school)

student1 = Student(90)

Student.show_details(student1) # 90
                               # ABC School
```

Here, the object is passed explicitly to the static method. Python does not pass it automatically.

We can use all three method types in the same class depending on what the method needs to do.

```python
#example

class Employee:

	company = "ABC"
	
	def __init__(self, name, salary):
	
		self.name = name
		self.salary = salary
		
	def update_salary(self, salary):
	
		self.salary = salary
		
	@classmethod
	def change_company(cls, company):
	
		cls.company = company
		
	@staticmethod
	def annual_salary(monthly_salary):
	
		return monthly_salary * 12

employee1 = Employee("Yash", 20000)

employee1.update_salary(25000)
Employee.change_company("XYZ")

print(employee1.salary) # 25000
print(Employee.company) # XYZ
print(Employee.annual_salary(employee1.salary)) # 300000
```

**Instance methods** use `self` when we need to access or modify an object's data.

**Class methods** use `cls` when we need to access or modify class-level data or create objects through alternative constructors.

**Static methods** do not receive `self` or `cls` automatically. We use them when a function belongs logically to a class but does not need an implicit object or class argument.

Do not forget `self` while defining instance methods. Do not forget `@classmethod` or `@staticmethod` when defining the other method types, as this changes how Python passes arguments during a method call.
