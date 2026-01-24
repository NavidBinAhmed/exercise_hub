class Student:

    def __init__ (self, name, gpa, subject, on_probation):
        self.name = name
        self.gpa = gpa
        self.subject = subject
        self.on_probation = on_probation
    
    
    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False
