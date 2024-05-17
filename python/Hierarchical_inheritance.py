# Hierarchical inheritance

class A:
    def func1(self):
        print("A")
class B(A):
    def func2(self):
        print("B")
class C(A):
    def func3(self):
        print("C")

objB=B()
objB.func1()
objB.func2()

objC=C()
objC.func1()
objC.func3()
