class Data:
    def __init__(self, data):
        self.data = data
    
    #adding two objects.
    def __add__(self, other):
        return self.data + other.data
    
    def __sub__(self, other):
        return self.data - other.data
    
    def __eq__(self, other):
        return self.data == other.data
    
    def __gt__(self, other):
        return self.data > other.data
    
    def __lt__(self, other):
        return self.data < other.data
    

#==================================================================================================================#

num1 = Data(10)
num2 = Data(20)
res1 = num1 + num2 #num1.__add__(num2)
print(res1)

res2 = num1 - num2 #num1.__sub__(num2)
print(res2)

res3 = num1 == num2 #num1.__eq__(num2)
print(res3)


