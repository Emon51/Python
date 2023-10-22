class Calculator:

    def product(self, *nums): #*nums store data as a tuple.
        res = 1
        for num in nums:
            res *= num
        print(res)
    

#======================================================================================================================#

c1 = Calculator()
c1.product(2) #output: 2
c1.product(2, 3) #output: 6
c1.product(2, 3, 4) #output: 24