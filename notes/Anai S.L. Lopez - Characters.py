class Teacher(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.dialogue = []

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
            return


Director = Teacher("Band Director", "A very nice, funny, and welcoming man. Very talented when it comes to music and "
                                    "knowledge on how to care for cats too.")
Director.talk_to()
