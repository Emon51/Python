class Student:

    def __init__(self, **info): #keywords argument(dictionary)
        if len(info) == 3:
            self.id = info["id"]
            self.name = info["name"]
            self.cgpa = info["cgpa"]
        if len(info) == 2:
            self.id = info["id"]
            self.name = info["name"]
        if len(info) == 1:
            self.id = info["id"]
        print("A student object created successfuly")

#======================================================================================================================#
s1 = Student(id = 1, name = "Root") #No error, object created successfuly.
s2 = Student(id = 2, name = "Maxwell", cgpa = 3.75) #No error, object created successfuly.
s3 = Student() #No error, object created successfuly.