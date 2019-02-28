class Teacher(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.dialogue = []

    def talk_to(self):
        greetings = ["cheerful", "tired", "neutral"]
        print("There's the director!")
        print("How do you greet him? cheerful? tired? Or neutral?")
        answer = input(">_")
        if answer.lower() is "cheerful":
            print("You cheerfully greeted the director!")
            print("DIRECTOR:")
            print("Morning! Hope you're ready for a productive day today! Do your best on the field today!")
        elif answer.lower() is "tired":
            print("You greeted the director in a tired manner.")
            print("DIRECTOR:")
            print("Not enough rest? Make sure to step out of practice if you're not feeling well. Get some water too"
                  " when you need it.")
        elif answer.lower() is "neutral":
            print("You greeted the director with little to no visible emotion.")
            print("DIRECTOR")
            print("")


Director = Teacher("Band Director", "It's the band director. A very nice, funny, and welcoming man. "
                                    "Very talented when it comes to music and knowledge on how to care for cats too.")

playing = True

while playing:
    Director.talk_to()
