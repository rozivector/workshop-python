class Human:
    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last
 
    def biodata(self):
        print("My mame is " + self.firstname + " " + self.lastname)
 
class Student(Human):
    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last
 
student = Student("Rozi", "Vector")
student.biodata()
