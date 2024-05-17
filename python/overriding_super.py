# by super()
class A:
    def func1(self):
        print('feature_1 of class A')


class B(A):
    # already exist in class A
    def func1(self):
        print('Modified feature_1 of class A by class B')
        super().func1()


# Create instance
obj = B()

obj.func1()
