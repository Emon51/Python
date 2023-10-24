class Students: #Base class or Parent class.
    def __init__(self, id, name, dept):
        self.id = id 
        self.name = name
        self.dept = dept 

    def info(self):
        print("Name: ", self.name)
        print("ID: ", self.id)
        print("Dept.: ", self.dept)

#=======================================================================================================================#

class CSE(Students):
    dept = "CSE" #class variable 
    def __init__(self, id, name, labs):
        super().__init__(id, name, CSE.dept)
        self.labs = labs

    def coding(self):
        print("CSE students practicing coding.")

#========================================================================================================================#

class BBA(Students):
    dept = "BBA" #class variable
    def __init__(self, id, name):
        super().__init__(id, name, BBA.dept)
    def music(self):
        print("BBA students practicing music.")

#=======================================================================================================================#

s1 = CSE(111, "Mike", 4)
s2 = BBA(2222, "Gleen")

s1.info()
s2.info()

#print(help(s1))

