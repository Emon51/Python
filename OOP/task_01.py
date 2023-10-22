#Task: Design the Vaccine and Person class so that the following expected output is generated.
#[N.B: Students will get vacine on a priority basis, So age for students doesn't matter but others age must be above 24]

class Vaccine:
    def __init__(self, vac_name, made_in, interval):
        self.vac_name = vac_name
        self.made_in = made_in
        self.interval = interval

class Person:
    def __init__(self, pname, age, ptype = "Gneral_citizen"):
        self.pname = pname
        self.age = age
        self.ptype = ptype
        self.vaccine = None
        self.first_dose = False
        self.second_dose = False

    def pushVaccine(self, vac, dose = 1):
        if dose == 1:
            if self.age > 24 or ptype == "student":
                self.vaccine = vac
                self.first_dose = True 
                print("1st dose done for", self.pname)
            else:
                print("Sorry", self.pname, "minimum required age is 25")
        elif dose == 2 and self.first_dose == False:
            print("Sorry", self.pname, "you never can't take 2nd dose before 1st dose.")
        elif dose == 2:
            if self.vaccine.vac_name != vac.vac_name:
                print("Sorry", self.pname, "you can't take two different vaccine.")
            else:
                self.second_dose = True
                print("2nd dose done for", self.pname)
        else:
            print("Something was wrong !!!")
    
    def showDetails(self):
        print("Name: ", self.pname, "Age: ", self.age, "Profession: ", self.ptype)
        print("Vaccine_name: ", self.vaccine.vac_name)
        if self.first_dose and self.second_dose:
            print("1st and 2nd dose Done for you")
        elif self.first_dose:
            print("1st dose done for you", self.pname)
            print("Please come after", self.vaccine.interval, "days.")

#=======================================================================================================================#

#vaccines
pfizer = Vaccine("pfizer", "new_york", 60)
sinopharm = Vaccine("sinpharm", "china", 60)
novavax = Vaccine("novavax", "amarica", 60)
#-----------------------------------------------------------------------------------------------------------------------#
#pushing vaccine to persons
p1 = Person("Gleen", 27, "cricketer")
p1.pushVaccine(pfizer, 1)
p1.showDetails()
p1.pushVaccine(pfizer, 2)
p1.showDetails()


