# Created by Vincente Prata
"""
This program represents a user defined class. The init method for the class Dog
is designed to give each dog its own name and breed. The method "teach" adds a passed
string parameter to tricks (a list) and prints a message that the dog knows the trick.
Finally, the method "knows" checks whether a passed string parameter is in the dog's list of tricks
and prints an appropriate message and returns True or False.
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

    


