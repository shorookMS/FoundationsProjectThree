# UTILS AND FUNCTIONALITY
from data import  population, clubs
from components import Club, Person

my_name = "Stitch"
my_age = 51
my_bio = "I have no idea what I am doing most of the time."
myself = Person(my_name, my_bio, my_age)

def introduction():
    print("Hello, %s. Welcome to our portal." % my_name)

def options():
    # your code goes here!
    print("="*20)
    
    while True:
        print("Would you like to: \n1) Create a new club. \n2) Brows and join clubs."+
        "\n3) View existing clubs. \n4) Display members of a club. \n-1) Close Application.")
        choice = input("> ")
        try :
            if int(choice) == 1 :
                create_club()
            elif int(choice) == 2 :
                join_clubs()
            elif int(choice) == 3 :
                view_clubs()
            elif int(choice) == 4 :
                view_club_members()
            elif int(choice) == -1 :
                break
            else :
                print("Invalid input, please try again.")
                continue
        except ValueError:
            print("Invalid input, please try again.")
            continue




def create_club():
    # your code goes here!
    title = input("Give a name to your club, go wild: ")
    desc = input("What is it gonna be about? ")
    newClub = Club(title,desc)
    print("Enter the numbers of the people you like to recruit to your club (-1 to stop):")
    print("="*20)
    newClub.assign_president(myself)

    i = 1
    for person in population:
        print("[%s] %s"%(i,person.name))
        i+=1
    while True:
        num = input(">> ")
        try:

            if int(num) in range(1,16):
                newClub.recruit_member(population[int(num)-1])
                print("Member added!")
            elif int(num) == -1 :
                break
            else :
                print("value not part of the list, try again :d")
                continue
                
        except ValueError:
            print("value not part of the list, try again :d")
            continue


    clubs.append(newClub)
    print("Here is your club!!")
    print("="*20)
    print("Name: %s \nDescription: %s" % (newClub.name, newClub.description))
    newClub.print_member_list()
    total = 0
    for x in newClub.members:
        total += x.age

    avrg = total*1.0/len(newClub.members)
    print("Avrage age in the club: %syr"% avrg)
    print("-"*20)
    
  

def view_clubs():
    # your code goes here!
    for club in clubs:
        print("\tNAME: %s\n\tDESCRIPTION: %s\n\tMEMBERS: %s\n" % 
            (club.name, club.description, len(club.members)))
    print("-"*20)





def view_club_members():
    # your code goes here!
    for club in clubs:
        print("\tNAME: %s\n\tDESCRIPTION: %s\n\tMEMBERS: %s\n" % 
            (club.name, club.description, len(club.members)))

    print("Enter the name of the club you want to view the members list for, \"cancel\" to go back.")
    while True:
        loc = len(clubs)
        title = input(">> ")
        if "cancel" == title.lower() :
                break

        for x in clubs :
            if x.name.lower() == title.lower() :
                loc = clubs.index(x)
                break

        if loc in range(0, len(clubs)) :
            x.print_member_list()
            print("="*20)
            
        else :
            print("Invalid input, try again.")
        

    print("-"*20)
    

def join_clubs():
    # your code goes here!
    for club in clubs:
        print("\tNAME: %s\n\tDESCRIPTION: %s\n\tMEMBERS: %s\n" % 
            (club.name, club.description, len(club.members)))

    print("Enter the name of the club you want to join, \"cancel\" to go back. ")
    while True:
        loc = len(clubs)
        title = input(">> ")
        if "cancel" == title.lower() :
                break
        for x in clubs :
            if x.name.lower() == title.lower() :
                loc = clubs.index(x)
                break

        if loc in range(0, len(clubs)) :
            if [True for x in clubs[loc].members if x.name.lower() == my_name.lower()]:
                print("You are already a member D: ??")
            else :
                clubs[loc].members.append(myself)
                print("%s, congrats on joining %s!"%(my_name, clubs[loc].name))
        else :
            print("Invalid input, try again.")
    print("-"*20)



    

def application():
    introduction()
    # your code goes here!
    options()

    
