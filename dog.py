"""

Vincente Prata
CS 100 2020F Section 019
HW 11, November 18, 2020
"""


class Dog:
    """Represents information about dog names and breeds"""

    species = "Canis familiaris"

    def __init__(self,name,breed):
        self.name = name
        self.breed = breed
        self.tricks = []

    def teach(self,trick):
        self.tricks.append(trick)
        print(self.name + ' knows ' + trick)

    def knows(self,trick):
        if trick in self.tricks:
            print('Yes, ' + self.name + ' knows ' + trick)
            return True
        else:
            print('No, ' + self.name + " doesn't know " + trick)
            return False

    


