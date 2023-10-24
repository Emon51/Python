#Multi class inhertence

class Students: #Base class or Parent class.
    def __init__(self, id, name):
        self.id = id 
        self.name = name

    def info(self):
        print("Name: ", self.name)
        print("ID: ", self.id)

#=======================================================================================================================#

class CSE(Students):
    
    def __init__(self, id, name, labs):
        super().__init__(id, name)
        self.labs = labs

    def coding(self):
        print(self.name, "practicing coding.")

#========================================================================================================================#

class BBA(Students):

    def music(self):
        print(self.name, "practicing music.")

#=======================================================================================================================#

class CSEfresher(CSE):

    def enroll(self):
        print("Enrolled successfuly.")
#=======================================================================================================================#


s1 = CSEfresher(123, "Max", 2)
s1.info() #info() is method of Student class.
s1.coding() #coding() is a method of CSE class.