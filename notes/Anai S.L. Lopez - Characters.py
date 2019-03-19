class Player(object):
    def __init__(self, name, social):
        self.name = name
        self.social = social


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
            print("'Morning! Hope you're ready for a productive day today! Do your best on the field today!'")
            print("You walked away feeling even happier than before! You're determined to do your best!")
        elif answer.upper() == greetings[1]:
            print("'Not enough rest? Make sure to step out of practice if you're not feeling well. Get some water too"
                  " when you need it.'")
            print("Hmm, that gave you enough motivation fot the day, how nice.")
        elif answer.upper() == greetings[2]:
            print("'Oh? Where's that enthusiasm? C'mon get some water and get ready for practice like you've never done"
                  " before!'")
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
            Player.social = + 5
            print("you gained +5 in your social level")
            print("social level ::", Player.social)
        elif answer.upper() == greetings2[1]:
            print("'Uh, is something wrong? I'm bad at talking to newbies so if something is wrong step out of practice"
                  " when you need to.")
            print("...")
            print("How nice of them!")
            Player.social = + 5
            print("you gained +5 in your social level")
            print("social level ::", Player.social)
        elif answer.upper() == greetings2[2]:
            print("'...'")
            print("...")
            print("Hm,, you made it a bit too obvious..")
            Player.social = - 3
            print("you gained -3 in your social level")
            print("social level ::", Player.social)
        else:
            print("'...?'")
            print("I don't know what you were trying to say and nor either did your section leader...")


class Student(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def talk_to(self):
        greetings3 = ['HAPPY', 'SAD', 'AVOID']
        print("It's another student!")
        print(Andrea.name)
        print(Andrea.description)
        print("How do you greet her? happy? sad? or avoid?")
        answer = input(">_")
        print("You greeted your them in a", answer, "manner.")
        print("ANDREA:")
        if answer.upper() == greetings3[0]:
            print("'Oh hey there! Hope you're ready for today! Do your best!'")
            print("Huh.. You seem hyped, she's great at cheering someone up! Well don't fail her, do your best!")
            Player.social = + 5
            print("you gained +5 in your social level")
            print("social level ::", Player.social)
        elif answer.upper() == greetings3[1]:
            print("'Is something wrong? Put yourself first! If you step out i'll play 2x as loud for you!'")
            print(".. Stepping out won't be needed, seems her words cheered you up right off the bat!")
            Player.social = + 5
            print("you gained +5 in your social level")
            print("social level ::", Player.social)
        elif answer.upper() == greetings3[2]:
            print("'...'")
            print("...")
            print("Hm,, that was rude,, Say hi to her next time >:-(")
            Player.social = - 3
            print("you gained -3 in your social level")
            print("social level ::", Player.social)
        else:
            print("'...?'")
            print("huh.. she's in your section, don't be shy! oh she left.. Say hi to her next time.")


me = Player("me", 10)
Director = Teacher("Band Director", "A very nice, funny, and welcoming man. Very talented when it comes to music and "
                                    "knowledge on how to care for cats too.")
Sax_Section_Leader = SectionLeader("Sax Section Leader", "You are part of the saxes, therefore under the lead of The "
                                   "Sax Section leader! Incredibly talented, you don't see them often but they always "
                                   "get work done.")
Andrea = Student("Andrea", "A really nice freshmen. She's a first year too, but her confidence and optimism cheers "
                           "you to do your best as well!")
Director.talk_to()
print("You walked away from your director..")
print("Oh who's that?")
Sax_Section_Leader.talk_to()
print("Oh hey there's a student..  who is it..?")
print("Oh it's a sax member!!")
Andrea.talk_to()
