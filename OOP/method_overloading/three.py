
from multipledispatch import dispatch
class Calculator:

    @dispatch(int, int)
    def product(self, a, b):
        print(a*b)
    
    @dispatch(int, int, int)
    def product(self, a, b, c):
        print(a*b*c)
    
    @dispatch(int, str)
    def product(self, a, b):
        print(a * int(b))

#======================================================================================================================#

c1 = Calculator()
c1.product(3, 4) #output: 12
c1.product(3, 4, 5) #output: 60
c1.product(3, "4") #output: 12
