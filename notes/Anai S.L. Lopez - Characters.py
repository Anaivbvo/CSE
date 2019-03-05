class Teacher(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def talk_to(self):
        greetings = ['CHEERFUL', 'TIRED', 'NEUTRAL']
        print("There's the director!")
        print(Director.name)
        print(Director.description)
        print("How do you greet him? cheerful? tired? Or neutral?")
        answer = input(">_")
        if answer.upper() == greetings[0]:
            print("You cheerfully greeted the director!")
            print("DIRECTOR:")
            print("Morning! Hope you're ready for a productive day today! Do your best on the field today!")
        elif answer.upper() == greetings[1]:
            print("You greeted the director in a tired manner.")
            print("DIRECTOR:")
            print("Not enough rest? Make sure to step out of practice if you're not feeling well. Get some water too"
                  " when you need it.")
        elif answer.upper() == greetings[2]:
            print("You greeted the director with little to no visible emotion.")
            print("DIRECTOR")
            print("Oh? Where's that enthusiasm? C'mon get some water and get ready for practice like you've never done"
                  " before!")
        else:
            print("That's not a greeting!")


class SectionLeader(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def talk_to(self):
        greetings2 = ['HAPPY', 'SAD', 'AVOID']
        print("There's your section leader!")
        print(Sax_Section_Leader.name)
        print(Sax_Section_Leader.description)
        print("How do you greet him?")
        answer = input(">_")
        print("You greeted your section leader in a", answer, "manner.")
        print("SECTION LEADER: ")
        if answer == greetings2[0]:
            print("'Oh hi there. Good to see you're doing well. Get your stuff ready we're heading out to the field "
                  "soon'")
            print("...")
            print("Hm.. That's probably the nicest they'll be to you for now.")
        elif answer == greetings2[1]:
            print("'Uh, is something wrong? I'm bad at talking to newbies so if something is wrong step out of practice"
                  "when you need to.")
            print("...")
            print("How nice of them!")
        elif answer == greetings2[2]:
            print("'...'")
            print("...")
            print("Hm,, you made it a bit too obvious..")


Director = Teacher("Band Director", "A very nice, funny, and welcoming man. Very talented when it comes to music and "
                                    "knowledge on how to care for cats too.")
Sax_Section_Leader = SectionLeader("Sax Section Leader", "You are part of the saxes, therefore under the lead of The "
                                   "Sax Section leader! Incredibly talented, you don't see them often but they always "
                                   "get work done.")
Director.talk_to()
print("You walked away from your director..")
print("Oh who's that?")
Sax_Section_Leader.talk_to()

"""
if answer == greetings2[0]:
    print("You happily greeted your section leader!")
    print("SECTION LEADER:")
    print("'Oh hi there. Good to see you're doing well. Get your stuff ready we're heading out to the field "
          "soon'")
    print("...")
    print("Hm.. That's probably the nicest they'll be to you for now.")
elif answer == greetings2[1]:
    print("You greeted your section leader in a sad manner..")
    print("SECTION LEADER")
"""