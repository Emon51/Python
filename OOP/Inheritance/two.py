
#Single class inheritence
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
        print("CSE students practicing coding.")

#========================================================================================================================#

class BBA(Students):

    def music(self):
        print("BBA students practicing music.")

#=======================================================================================================================#

s1 = CSE(111, "Mike", 4)
s2 = BBA(2222, "Gleen")

s1.info()
s2.info()

s1.coding()

s2.music()