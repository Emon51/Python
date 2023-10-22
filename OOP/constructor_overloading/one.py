class Student:

    def __init__(self, id, name, cgpa):
        self.id = id 
        self.name = name
        self.cgpa = cgpa

    def __init__(self, id, name, cgpa):
        self.id = id 
        self.name = name
        self.cgpa = cgpa

#======================================================================================================================#
s1 = Student(1, "Root") #TypeError: Student.__init__() missing 1 required positional argument: 'cgpa'
s1 = Student(2, "Maxwell", 3.75) #No error, object created successfuly.
    