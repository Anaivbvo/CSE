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
        print("You greeted the Director in a ", answer, "manner.")
        print("DIRECTOR:")
        if answer.upper() == greetings[0]:
            print("Morning! Hope you're ready for a productive day today! Do your best on the field today!")
        elif answer.upper() == greetings[1]:
            print("Not enough rest? Make sure to step out of practice if you're not feeling well. Get some water too"
                  " when you need it.")
        elif answer.upper() == greetings[2]:
            print("Oh? Where's that enthusiasm? C'mon get some water and get ready for practice like you've never done"
                  " before!")
        else:
            print("That's not a greeting!")
            print("Well... the director is gone now..")


class SectionLeader(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def talk_to(self):
        greetings2 = ['HAPPY', 'SAD', 'AVOID']
        print("There's your section leader!")
        print(Sax_Section_Leader.name)
        print(Sax_Section_Leader.description)
        print("How do you greet him? happy? sad? or avoid?")
        answer = input(">_")
        print("You greeted your section leader in a", answer, "manner.")
        print("SECTION LEADER: ")
        if answer.upper() == greetings2[0]:
            print("'Oh hi there. Good to see you're doing well. Get your stuff ready we're heading out to the field "
                  "soon'")
            print("...")
            print("Hm.. That's probably the nicest they'll be to you for now.")
        elif answer.upper() == greetings2[1]:
            print("'Uh, is something wrong? I'm bad at talking to newbies so if something is wrong step out of practice"
                  "when you need to.")
            print("...")
            print("How nice of them!")
        elif answer.upper() == greetings2[2]:
            print("'...'")
            print("...")
            print("Hm,, you made it a bit too obvious..")
        else:
            print("'...?'")
            print("I don't know what you were trying to say and nor either did your section leader...")


Director = Teacher("Band Director", "A very nice, funny, and welcoming man. Very talented when it comes to music and "
                                    "knowledge on how to care for cats too.")
Sax_Section_Leader = SectionLeader("Sax Section Leader", "You are part of the saxes, therefore under the lead of The "
                                   "Sax Section leader! Incredibly talented, you don't see them often but they always "
                                   "get work done.")
Director.talk_to()
print("You walked away from your director..")
print("Oh who's that?")
Sax_Section_Leader.talk_to()
