class Person:
    def __init__(self, name, gender):
        self.name   = name
        self.gender = gender

    def getDetails(self):
        self.details = {
            "name" : self.name,
            "gender" : self.gender
        }
        return self.details

class Cricketer(Person):
    def __init__(self, name, gender, batting_average, bowling_average):
        super().__init__(name, gender)
        self.batting_average = batting_average
        self.bowling_average = bowling_average
    
    def getDetails(self):
        self.details = {
            "name" : self.name,
            "gender" : self.gender,
            "batting_average" : self.batting_average,
            "bowling_average" : self.bowling_average
        }
        return self.details


class Footballer(Person):
    def __init__(self, name, gender):
        super().__init__(name, gender)

cricketer_obj = Cricketer('Cricketer One', 'Male', 40, 90)
print(cricketer_obj.getDetails())
cricketer_obj = Footballer('Footballer One', 'Male')
print(cricketer_obj.getDetails())
