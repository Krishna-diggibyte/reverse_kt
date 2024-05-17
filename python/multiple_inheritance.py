#Multiple Inheritance

class A:
    def func1(self):
        print("A")
class B:
    def func2(self):
        print("B")
class C(A,B):
    def func3(self):
        print("C")
objC=C()
objC.func1()
objC.func2()
objC.func3()
