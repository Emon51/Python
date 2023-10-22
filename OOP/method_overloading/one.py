class Calculator:

    def product(self, a, b):
        print(a*b)
    
    def product(self, a, b, c):
        print(a*b*c)

#======================================================================================================================#

#Method_overloading: In one class there are multiple methods with same name and with different parameters and latest method will get priority to execute.
c1 = Calculator()
#c1.product(2, 3) #TypeError: Calculator.product() missing 1 required positional argument:
c1.product(2, 3, 4) #output: 24