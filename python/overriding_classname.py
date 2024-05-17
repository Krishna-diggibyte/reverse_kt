# Using Classname:
class A:
    def func1(self):
        print('feature_1 of class A')


class B(A):
    # already exist in class A
    def func1(self):
        print('Modified feature_1 of class A by class B')
        A.func1(self)


# Create instance
obj = B()

obj.func1()
