# CLASSES AND METHODS
class Person():
    def __init__(self, name, bio, age):
        # your code goes here!
        self.name = name
        self.bio = bio
        self.age = age


class Club():
    def __init__(self, name, description):
        # your code goes here!
        self.name = name
        self.description = description
        self.members = []


    def assign_president(self, person):
        # your code goes here!
        self.president = person
        if not (person in self.members) :
            self.members.append(person)



    def recruit_member(self, person):
        # your code goes here!
        self.members.append(person)



    def print_member_list(self):
        # your code goes here!
        print("Members:")
        for person in self.members:
            if person.name == self.president.name :
                print("- %s (%s years old, President) - %s\n"% (person.name, person.age, person.bio))
            else :
                print("- %s (%s years old) - %s \n"% (person.name, person.age, person.bio))

