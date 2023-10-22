class Student:

    def __init__(self, *info):
        if len(info) == 3:
            self.id = info[0]
            self.name = info[1]
            self.cgpa = info[2]
        if len(info) == 2:
            self.id = info[0]
            self.name = info[1]
        if len(info) == 1:
            self.id = info[0]
        print("A student object created successfuly")

#======================================================================================================================#
s1 = Student(1, "Root") #No error, object created successfuly.
s2 = Student(2, "Maxwell", 3.75) #No error, object created successfuly.
s3 = Student() #No error, object created successfuly.