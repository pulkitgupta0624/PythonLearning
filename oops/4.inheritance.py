'''
Inheritance in python:
One class (child) can use the propertirs/methods of another class (parent)

'''

## Single inheritance
class A:
    def showA(self):
        print("From class A")

class B(A):
    def showB(self):
        print("From class B")

obj = B()
obj.showA()
obj.showB()

## Multiple inheritance
class Father:
    def skill1(self):
        print("Father : Driving 🚗")

class Mother: 
    def skill2(self):
        print("Mother : cooking 🍲")

class Child(Father, Mother):
    pass

c = Child()
c.skill1()
c.skill2()

## Multilevel inheritance
class GrandParent:
    def gp(self):
        print("Grandparent property")

class Parent(GrandParent):
    def p(self):
        print("Parent property")

class Bachha(Parent):
    def b(self):
        print("Baccha property")

obj = Bachha()
obj.gp()
obj.p()
obj.b()

## Hierarchial inheritance
class X:
    def home(self):
        print("X class")

class Child1(X):
    pass

class Child2(X):
    pass

c1 = Child1()
c2 = Child2()

c1.home()
c2.home()

