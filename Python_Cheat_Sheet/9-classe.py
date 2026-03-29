"""
DocStrings --> Classes:
A class defines the behavior of en object and the king of information an object can store.
The information a class is stored in attributes, and functions that belong to class are
called methods. A child class inherits the attributes and methods from it's perents class.
"""

"""Exemple from class"""

"""Defining"""


class MyNewClass:
    pass


# Class Instantiation
my = MyNewClass()

"""----------------------------------------------------------------"""
"""Constructors"""


class Animal:  # type: ignore
    def __init__(self, voice):
        self.voice = voice


cat = Animal("Meow")
print(Animal(cat.voice))  # => Meow

dog = Animal("Woof")
print(dog.voice)  # => Woof


"""----------------------------------------------------------------"""
"""Methods"""


class Dog1:
    # Methods of the class
    def bark(self):
        print("Ham")


charlie = Dog1()
charlie.bark()

"""----------------------------------------------------------------"""
"""Class Variables"""


class MyClass:  # type: ignore
    class_variable = "A class variable!"


# ==> A class variable!
print(MyClass.class_variable)

x = MyClass()

print(x.class_variable)


"""----------------------------------------------------------------"""
"""Super() Function"""


class ParentClass:  # type: ignore
    def print_test(self):
        print("Parent Method")


class ChildClass(ParentClass):  # type: ignore
    def print_test(self):
        print("Child Method")
        # Calls the parent's print_test()
        super().print_test()


"""----------------------------------------------------------------"""
"""repr() method"""


class Employee:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


john = Employee("John")
print(john)  # => John

"""----------------------------------------------------------------"""
"""Polymorphism"""


class ParentClass:  # type: ignore
    def print_self(self):
        print("A")


class ChildClass(ParentClass):  # type: ignore  # noqa: F811
    def print_self(self):
        print("B")


obj_A = ParentClass()
obj_B = ChildClass()

obj_A.print_self()  # => A
obj_B.print_self()  # => B

"""----------------------------------------------------------------"""
"""Overriding"""


class ParentClass:
    def print_self(self):
        print("Parent")


class ChildClass(ParentClass):
    def print_self(self):
        print("Child")


child_instance = ChildClass()
child_instance.print_self()  # => Child

"""----------------------------------------------------------------"""
"""Inheritance"""


class Animal:
    def __init__(self, name, legs):
        self.name = name
        self.legs = legs


class Dog(Animal):  # type: ignore
    def sound(self):
        print("Woof!")


Yoki = Dog("Yoki", 4)
print(Yoki.name)  # => YOKI
print(Yoki.legs)  # => 4
Yoki.sound()  # => Woof!

"""----------------------------------------------------------------"""


class MyClass:
    @staticmethod
    def greet(name):
        return f"Hello, {name}!"


# No instantiation nedded

# Call via class
print(MyClass.greet("Alice"))  # => Hello, Alice!

# Can still call via instance
obj = MyClass()
print(obj.greet("Bob"))  # => Hello, Bob!

"""----------------------------------------------------------------"""
"""Creating a dog class"""


class Dog:
    """Represent a dog"""

    def __init__(self, name):
        self.name = name

    def sit(self):
        """Simulate sitting"""
        print(f"{self.name} is setting.")


my_dog = Dog("Peso")
print(f"{my_dog.name} is great dog!")
my_dog.sit()

"""----------------------------------------------------------------"""
"""Inheritance"""


class SARDog(Dog):
    """Represent a search dog"""

    def __int__(self, name):
        super().__init__(name)

    def search(self):
        """Simulate searching"""
        print(f"{self.name} is searching")


my_dog = SARDog("Wille")

print(f"{my_dog.name} is a search dog.")
my_dog.sit()
my_dog.search()
