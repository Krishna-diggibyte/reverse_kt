# single inheritance

class Parent:
       def func1(self):
            print("This function is in parent class.")

class Child(Parent):
     def func2(self):
           print("This function is in child class.")

# Driver's code
object = Child()
object.func1()
object.func2()
