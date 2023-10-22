
#Task: Create a House class with no. of doors and windows and merge two houses to create a new big house.

class House:
     def __init__(self, door, window):
          self.door = door 
          self.window = window 

     def view(self):
          print("Doors: ", self.door)
          print("Windows: ", self.window)
     
     #merging two objects.
     def __add__(self, other):
          new_door = self.door + other.door
          new_window = self.window + other.window
          new_house = House(new_door, new_window)
          return new_house

#====================================================================================================================#

h1 = House(4, 2)
h2 = House(6, 3)
h3 = h1 + h2 #h1.__add__(h2)
print(h3.view())

