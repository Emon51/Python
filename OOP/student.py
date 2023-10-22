class Student:
    def __init__(self, name, id) -> None: #constructor
        self.id = id      #instance variable
        self.name = name  #instance variable

    def details(self): #instance method and self received object's reference or address.
        #print(self)
        print("Name: ", self.name, "ID: ", self.id)

    def update_name(self, new_name) -> None:
        self.name = new_name

    def compare(self, stud)  -> None:
        #self received 1st compareable student's reference and stud received 2nd compareable student's reference.
        if self.name == stud.name:
            print("They are same")
        else:
            print("They are different")
    
    def display(self, x, arr):
        x = x + 5
        arr[0] = 7
        print("In inside_method:")
        print("x", x)
        print('arr', arr)

#==========================================================================================================#

s1 = Student("Bob", 1)
s2 = Student("Carol", 2)
#show the name of the student s1
#print(s1.name)
#change the id of the student s2
#s2.id = 3
#print(s2.id)
#s1.details()

#update name of student s1 using update_name method
#s1.update_name("Max")
#s1.details()

#show object's attributes value as a dictionary
#print(s1.__dict__)

#show object's all the built in method and created methods
#print(dir(s1))
#print(s1.__dir__)

#compare 
# s1.compare(s2)

#Note: string and integer are passed by value and list is passed by reference.
#val = 10
#nums = [1, 2, 3, 4, 5]
#s1.display(val, nums)

#print("In outside_method:")
#print("val", val)
#print("nums", nums)
#observations: nums is changed in both inside and outside method but val is changed in inside not in  outside method.

#Method_overloading: In one class there are multiple methode with same name and with different parameters and latest method will get priority to execute.

