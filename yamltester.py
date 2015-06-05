import yaml

class Person:
    otherPerson = ""
    def __init__(self, name, friend_meetings, kids):
        self.name = name
        self.friend_meetings = friend_meetings
        self.kids = kids

class Kid:
    def __init__(self, name, friends):
        self.name = name
        self.friends = friends


        
billy_friends = {"Goethe": "Classmate", "Pearl": "Mentor"}
jill_friends = {"Amethyst": "Mentor", "Joplin": "Entertainer"}
person1_friend_meetings = {"Jane": "Monday", "Bob": "Tuesday"}
person1_kids = {"Billy": Kid("Billy", billy_friends), "Jill": Kid("Jill", jill_friends)}


person1 = Person("John", person1_friend_meetings, person1_kids)

mylist = [person1]

stream1 = open("yamlsimple.yaml", 'w')

yaml.dump(mylist, stream1)
