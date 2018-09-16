# CREATION OF DATA
######################### DO NOT MODIFY THIS CODE ###########################
from components import Person, Club
steve = Person("Steve", "average joe", 27)
michelle = Person("Michelle", "average jane", 12)
john = Person("John", "a blond guy", 32)
ron = Person("Ron", "a red guy", 23)
maha = Person("Maha", "a shy girl", 22)
fatma = Person("Fatma", "a fruit", 24)
dude = Person("Dude", "a college 'dude'", 25)
dudette = Person("Dudette", "a meme", 7)
forever_alone = Person("Forever Alone", "a more popular meme", 9)
confession_bear = Person("Confession Bear", "an even more popular meme", 10)
jack = Person("Jack", "an american", 43)
audrey = Person("Audrey", "just some woman", 31)
asis = Person("Asis", "a joke we have at Coded", 1)
caesar = Person("Julius Caesar", "Google me.", 56)
marcus_aurelius = Person("Marcus Aurelius", "Roman Emperor, philosopher. 'Nuff said.", 61)

people = [
	steve,
	michelle,
	john,
	ron,
	maha,
	fatma,
	dude,
	dudette,
	forever_alone,
	confession_bear,
	jack,
	audrey,
	asis,
	caesar,
	marcus_aurelius
]

population = []
for person in people:
	population.append(person)

book = Club("The KPOP Dome", "Your average secret kpopies")
book.recruit_member(steve)
book.recruit_member(ron)
book.recruit_member(maha)
book.recruit_member(confession_bear)
book.recruit_member(audrey)
book.assign_president(ron)

sports = Club("Anime Weebs", "Anime for LIFE!")
sports.recruit_member(michelle)
sports.recruit_member(john)
sports.recruit_member(jack)
sports.recruit_member(caesar)
sports.recruit_member(marcus_aurelius)
sports.assign_president(jack)

coding = Club("Coding Club", "A coding club")
coding.recruit_member(dude)
coding.recruit_member(dudette)
coding.recruit_member(forever_alone)
coding.recruit_member(confession_bear)
coding.recruit_member(asis)
coding.assign_president(dudette)

glub = Club("Go Home Club", "We like to go home. ¯\\_(ツ)_/¯")
glub.recruit_member(steve)
glub.recruit_member(john)
glub.recruit_member(maha)
glub.recruit_member(fatma)
glub.recruit_member(caesar)
glub.assign_president(fatma)


clubs = [book, sports, coding, glub]


