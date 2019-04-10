import random


# ITEMS ----------------------------------------------------------------------------------------------------------------
class Room(object):
    def __init__(self, name, description, av_dir, long_desc, north=None, north_east=None, north_west=None,
                 south=None, south_east=None, south_west=None, east=None, west=None):
        self.name = name
        self.north = north
        self.north_east = north_east
        self.north_west = north_west
        self.south = south
        self.south_east = south_east
        self.south_west = south_west
        self.east = east
        self.west = west
        self.description = description
        self.av_dir = av_dir
        self.long_desc = long_desc
        self.items = []
        self.characters = []


class Player(object):
    def __init__(self, name, description, health_level, hydration_level, social_level, starting_location):
        self.name = name
        self.description = description
        self.health_level = health_level
        self.hydration_level = hydration_level
        self.social_level = social_level
        self.current_location = starting_location
        self.inventory = []

    def move(self, new_location):
        """This moves the player to a new room
        :param new_location: The room object of which you are going to
        """
        self.current_location = new_location

    def find_next_room(self, direction):
        """This method searches the current room so see if a room
        exists in that direction.
        :param direction: The direction that you want to move to
        :return: The Room object if it exists, or None if it does not
        """
        name_of_room = getattr(self.current_location, direction)
        return globals()[name_of_room]

    def health_gained(self, amount1):
        self.health_level += amount1

    def hydration_gained(self, amount2):
        self.hydration_level += amount2

    def hydration_level_low(self):
        if self.hydration_level() < 5:
            print("You're hydration levels are low! Be sure you are drinking the necessary amount of water.")
            print("this year's summer is hotter than usual. Drink water next time you have the chance.")
            print(self.hydration_level())

    def health_level_low(self):
        if self.health_level() < 5:
            print("You're hydration levels are low! Be sure you are eating well and healthy!!")
            print("We're doing a lot of work than last year! Eat well when you get the chance.")
            print(self.health_level())


# Items ----------

class Items(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def pickup(self):
        print("Would you like to pick up this item?")
        answer = input(">_")
        if answer.upper() in ['YES']:
            me.inventory.append(self)
            print("you picked up:", self.name)
            print(me.inventory)
        if answer.upper() in ['NO']:
            print("you did not pick up:", self.name)
            print(me.inventory)


class ConsumableLiquid(Items):
    def __init__(self, name, description, hydration_plus, social_plus):
        super(ConsumableLiquid, self).__init__(name, description)
        self.name = name
        self.description = description
        self.hydration_plus = hydration_plus
        self.social_plus = social_plus

    def drink(self):
        print("Would you like to drink:", self.name, "?")
        answer = input(">_")
        if answer.lower() in ['yes']:
            print("You drank: ", self.name)
            me.hydration_level += self.hydration_plus
            print("You've gained: ", self.hydration_plus, "on hydration level!")
        elif answer.lower() in ['no']:
            print("You save", self.name, "for later.")
        else:
            self.drink()


class ConsumableSolid(Items):
    def __init__(self, name, description, health_plus, social_plus):
        super(ConsumableSolid, self).__init__(name, description)
        self.name = name
        self.description = description
        self.health_plus = health_plus
        self.social_plus = social_plus

    def eat(self):
        print("Would you like to eat: ", self.name, "?")
        answer = input(">_")
        if answer.lower() in ['yes']:
            print("You ate:", self.name)
            me.health_level += self.health_plus
            print("You've gained: ", self.health_plus, "on health level!")
        elif answer.lower() in ['no']:
            print("You save", self.name, "for later.")
        else:
            self.eat()


class HealthItems(Items):
    def __init__(self, name, description, health_plus):
        super(HealthItems, self).__init__(name, description)
        self.name = name
        self.description = description
        self.health_plus = health_plus

    def use(self):
        print("Would you like to use the item?")
        answer = input(">_")
        if answer in ['yes']:
            print("you used the item: ", self.name)
            me.health_level += self.health_plus
            print("you've gained:", self.health_plus, "in your health level!")


class Wearable(HealthItems):
    def __init__(self, name):
        super(Wearable, self).__init__(name, description, health_plus)
        self.name = name
        self.description = description
        self.health_plus = health_plus


class Music(Items):
    def __init__(self, name, description, section, chair, social_plus):
        super(Music, self).__init__(name, description)
        self.name = name
        self.description = description
        self.section = section
        self.section = section
        self.chair = chair
        self.social_plus = social_plus


# CHARACTERS -----------------------------------------------------------------------------------------------------------

class Characters(object):
    def __init__(self, name, description, check, rank, grade, group, sorry, alright, them, last_year, this_year,
                 section):
        self.name = name
        self.description = description
        self.check = check
        self.rank = rank
        self.grade = grade
        self.group = group
        self.sorry = sorry
        self.alright = alright
        self.them = them
        self.last_year = last_year
        self.this_year = this_year
        self.section = section
        self.inventory = []

    def trade(self):
        print("((What would like from ", self.name, "?))")
        for num, item in enumerate(self.inventory):
            print(str(num + 1) + ": " + item.name)
        wanted_item = input(">_")
        if wanted_item.upper() in [self.inventory]:
            character_want = random.choice(Plyer.inventory)
            print("'Alright I see, well in return I would like ", character_want, ".'")
            print("((Do you have the item?))")
            if character_want in Player.inventory:
                print(Player.inventory)
                print("((You do have the item, trade?))")
                answer = input(">_")
                if answer.upper() in ['YES']:
                    print(self.name, ":")
                    print(self.alright, "looks like you got a deal!'")
                    Player.inventory.remove(character_want)
                    self.inventory.append(character_want)
                    Player.inventory.append(wanted_item)
                    self.inventory.remove(wanted_item)
                    print("((Awesome! You know have ", wanted_item, " but lost ", character_want, ".")
                    print("((You gained plus 5 on your social level!")
                elif answer.upper() in ['NO']:
                    print(self.name, ":")
                    print(self.sorry, ", well maybe someone else might have", wanted_item, "for a different price.")
            elif character_want not in Player.inventory:
                print(Player.inventory)
                print("((Hmm.. Seems like you don't have the item...))")
                print(self.name, ":")
                print("'Oh well... I'm sure someone else might be able to trade ", wanted_item, "for something ya got.")
        elif wanted_item.upper() not in self.inventory:
            print(self.name, ":")
            print(self.sorry, "don't have that on me right now. You can try asking others.")
            print("is there anything else you want?")
            answer = input(">_")
            if answer.upper() in ['YES']:
                return self.trade()
            elif answer.upper() in ['NO']:
                print(self.sorry, "you're better off asking someone else..")

    def talk_to(self):
        print("You've approached: ", self.name)
        print("What would you like to talk about?")
        print("'1. Them', '2. Band last year', '3. Band this year', '4. Their section'")
        answer = input(">_")
        if answer.lower() in ['Them', 'them', '1']:
            print(self.them)
            print("-"*5)
            print("You've learned more about:", self.name)
        elif answer.lower() in ['Band last year', 'Band Last Year', 'band last year', '2']:
            print(self.last_year)
            print("-" * 5)
            print("You know now more about the band and about", self.name, "!")
        elif answer.lower() in ['Band this year', 'Band This Year', 'band this year', '3']:
            print(self.this_year)
            print("-" * 5)
            print("You now know how", self.name, "really thinks of your year, whether its a good or bad thing..")
        elif answer.lower() in ['Their section', 'their section', 'Their Section', '4']:
            print(self.section)
            print("-" * 5)
            print("You now know now more about", self.name, "and the", self.group)
        else:
            print("??? Do you wan't to repeat that again?")
            self.talk_to()

    def check(self):
        print("This is:", self.name)
        print("-"*3)
        print(self.name)
        print("-" * 1)
        print(self.description)
        print("-" * 1)
        print(self.rank)
        print("-" * 1)
        print(self.grade)
        print("-" * 1)
        print(self.group)
        print("-" * 1)


# ITEMS ----------------------------------------------------------------------------------------------------------------
# Liquids -----
WATER = ConsumableLiquid("Water", "Fresh and cold water you brought from home! It even has ice!", 15, 5)
MILK = ConsumableLiquid("Milk", "Cold school plain milk. Nothing special about it.", 7, 2)
SPORTS_DRINK = ConsumableLiquid("Sports Drink", "This is the usual brand of sports drink everyone brings to camp. "
                                "Refreshing, fruity, and energy giving!", 10, 15)
ARIZONA = ConsumableLiquid("Arizona", "This is most everyone's favorite juice. This can most definitely bring up your "
                                      "social level, though how sweet it is, it may not be as nice with your health "
                                      "level.", 4, 8)
REBEL = ConsumableLiquid("Rebel Energy Drink", "Every one loves this energy drink! Though it's not as healthy as water,"
                                               " everyone craves for this after practice.", 2, 15)
# Solids -----
APPLE = ConsumableSolid("Apple", "A nice red apple! Sweet but solid! Though everyone likes junk food, no one could "
                                 "decline a nice apple!", 10, 5)
FRIES = ConsumableSolid("Mac's Fries", "Everyone loves fried! Though it'snot the healthiest item, but that doesnt stop"
                                       " anyone from eating them!", 10, 15)
BURGER = ConsumableSolid("Mac's Burger", "A cheese burger! If you'd compare this to Mac's Fries, you'd think the "
                                         "burger was the side option. Though this is a whole meal for anyone after "
                                         "practice!", 8, 12)
SANDWICH = ConsumableSolid("School Sandwich", "Since this is a school food, you never know if this sandwich is any "
                                              "good or bad...", random.randint(-20, 20), random.randint(-5, 5))
SALAD = ConsumableSolid("Salad", "School's salad. This is a surprise whether you feel better or worse after eating "
                                 "this...", random.randint(-10, 10), random.randint(-5, 5))
# Health -----
SUN_SCREEN = HealthItems("Sun Screen", "Sun screen helps you stay protected! This is the type the band provides to "
                         "every student. Safe for every student and very protective!", 25,)
ENERGY_SHOT = HealthItems("Energy", "A mini energy drink! Has the necessary proteins and energy giving for incoming"
                          " activities.", 10)
# Music -----
ALTO1A = Music("First chair Alto", "Alto Section Leader's music. A rare item to get a hold of since they are always"
                                   " organized with their music!", "Saxes", "1st", 20)
ALTO1B = Music("2nd First chair Alto", "Music for the next in command! although this is 1st chair music, it seems to "
                                       "be just a tad different from the Section leader's music.", "Saxes", "1st", 15)
ALTO2A = Music("Second Chair Alto", "Music for the second chairs.. Which seems to be majority of the section. Not too"
                                    "different from the 1st chair.. except everything.", "Saxes", "2nd", 5)

# CHARACTERS -----------------------------------------------------------------------------------------------------------
# EXAMPLE -----
MAX = Characters("Max", "Senior High brass section leader", "Max is the high brass section leader. Not as energetic as"
                 " the sophomores but very energetic for a senior section leader. Vey talkative as he is proud of his"
                 " section. Has also been dating the 2nd guard captain for 3 years.", "Section Leader", "Senior/12th",
                 "High brass/Horns", "ah sorry,", "cool then,", "I'm Max! The high brass section leader! I've done "
                 "marching band all four years! Thanks to that i have the best girl by my side and the most talented "
                 "section!", "Last year was great!.. That's a lie.. We won "
                 "sweeps the year before, but for what ever reason we've all gone downhill.. Do your best this year! "
                 "Who knows! We might win something above 1st!", "This year seems to be starting really off.. Don't "
                 "let that bother you though, just do your best!", "High brass? They're the best! We're the best!",)
# DIRECTOR -----
DIRECTOR = Characters("Director", "Band Director", "The band director is one of the nicest people you'll ever meet. "
                      "He's always ready to help you when you need it. He's also the type of person to wear converse "
                      "to a formal concert.", "Director", "Adult", "Director", "Director", "Cool, awesome,",
                      "Whoops, sorry", "Last year we had a few up and down moments. But it's alright! We'll do better "
                      "this year and put in twice as much hard work than the last!", "This year I plan to have twice "
                      "as many fundraisers I as well plan to have as many competitions. So be prepared.", "I'm the "
                      "director of the band. Haha, not much of a section.")
# DRUM MAJORS ------
DML = Characters("Drum Major L", "Parade Drum Major", "Incredibly talented Tenor player. Known for being an incredible"
                 " player with knowledge in multiple instruments.", "Drum Major", "Junior/11th", "DM, Saxes", "Sorry,",
                 "Okay then,", "I'm L. The Parade Drum Major. I've been an alumni from the school's feeder. I've been "
                 "playing Tenor Sax since i was in 3rd grade and i've been getting better since then.", "Last year was "
                 "my first year as parade drum major. I started off roughly but we all do, and we all improve.", "This"
                 " year seems to be off to a good start. I can't make much assumptions about it yet.", "You can "
                 "consider the Drum majors as their own section, but i came from the saxes. They're a good section. "
                 "There's not much I can say about it.")

DMJ = Characters("Drum Major J", "Head Field Drum Major", "Incredibly talented player of multiple instruments. Has been"
                 " head drum major since freshmen year. Rumors say he had made it to the top ranks due to an upper "
                 "class men being related to him. Though records show no one with the same last name as him in the past"
                 "8 years.", "Drum Major", "Junior/11th", "DM, Saxes", "Hm,", "Well,", "I'm J, the Head Drum major of "
                 "the band.", "Last year we had won sweeps. I expect the band to win again, if the first years don't"
                 " mess it up..", "I expect the first years to put their all into the band. If not, there's no reason"
                 " for them being here.", "Section..? Thee's only 3 drum majors, you can consider that a section.")

DMC = Characters("Drum Major C", "Event Drum Major", "He's incredibly nice and chill. Despite being drum major, he is"
                 "more known for being very chill and a friend to most everyone. Plays multiple low instruments rather"
                 " than high ones.", "Drum Major", "Junior/11th", "DM, Saxes, Brass", "Sorry bud,", "Cool!", "Hey, i'm"
                 "C! I'm a brass player and sax player! Oh drum major too. I take control and lead during school and"
                 "football game events! Lead bari player in most events when the other drum majors are the ones"
                 " conducting too.", "Last year was my first year as drum major! A great time and i look forward to "
                 "the rest of my years coming!", "This year i know it's going to be great! Do you're best!", "I was "
                 "part of the Saxes my middle school years. I started brass such as trombone and tuba my first two "
                 "years of high school! Both sections are great and i know both will keep up the good work!")

# MAP ------------------------------------------------------------------------------------------------------------------
TREE1 = Room("Band_Tree", "This is the nearest tree to the band room. Nothing too special about it.", "west: "
             "Hang_Out_Tree, north_east: Outside_Band_room", "This is the nearest tree to the band room. A lot of "
             "upperclassmen like to hang around here before school starts. You can often find junior to senior "
             "upperclassmen here.")
TREE2 = Room("Hangout_Tree", "It's the usual tree we hang out at. It has the best shade range, not too big and "
             "definitely not to small. ", "WEST: Lunch_Table, EAST: Band_Tree", "You'de expect there to be a lot of "
             "members hanging here.. Though rarely anyone tends to show up here. That's why it's our hang out tree. ")
TABLE = Room("Lunch_Table", "This is the usual lunch table we hang out at. Enough for our circle to hang out at. "
             "Great shade as well.", "WEST: Amp, EAST: Hang_Out_Tree.", "A small lunch table next to the hangout tree."
             " It's a nice spot for lunch, near the band room as well as the cafeteria.")
OUTER_STAGE = Room("Amp", "The amp. It's stairs and wide stage is the best place to have fun and rest at.", "NORTH: "
                   "Back_Stage, EAST: Lunch_Table.", "Jazz tends to perform for school afternoon events here. Sometimes"
                   " marching band gets to perform songs here as well. We have our visual square practices here. best "
                   "hope no teachers come walking around.. The visuals are awkward to do around others.")
BACK_STAGE = Room("Back_Stage", "It's the back of the stage. There's really no need to be here. ", "NORTH_WEST: "
                  "Stage, NORTH_EAST: Stage.", "Occasionally you can find theatre kids hanging around here.. Something"
                  " had happened between band and theatre kids 2 years ago. Though uperclassmen won't mention what this"
                  " event was about, it seems to have seperated these two groups into almost purely enemies.. You'd "
                  "best hurry out of here..")
STAGE = Room("Stage", "The school's main stage. Band performances, mainly concert happen here! When the lights shine "
             "on you, it's the best feeling! Oh, and theatre kids do their plays here to. ", "NORTH_WEST: Cafeteria, "
             "NORTH_EAST: Cafeteria.", "Saxes  tends to have sectionals here.. They tend to be the only ones close to "
             "theatre kids compared to the rest of the band sections, that's why they get to have sectionals here "
             "peacfully while theatre kids rehaearse and work on the stage.")
CAFETERIA = Room("Cafeteria", "It's the school's cafeteria. The tables and chairs are put away most times.", "TH_WEST:"
                 " Water_Fountains, NORTH: Janitor_Storage_Room, SOUTH_EAST: Band_Hall, NORTH_EAST: Band_Hall.", "A lot"
                 " of sections tend to have practice here. It can get awkward with theatre kids appearing on stage. "
                 "Only groups to show up here are horns and saxes. Tends to be fights on who gets to practice here.")
JANITOR_ROOM = Room("Janitor's_Room", "It's the janitor's storage room. Nothing special about it since it's always "
                    "closed.. ", "NORTH: Food_Booths.", "This room tends to be closed majority of the time. It's "
                    "rumored the lower brass have the key to the room.. Though that hasn'e been confirmed yet.")
WATER_FOUNTAIN = Room("Water_Fountains", " This room has no actual walls but it does have around 5 water fountains!",
                      "SOUTH: Cafeteria.", "This is the best place to get water at. It has the coldest water in the "
                      "school. Though it is really far from the field, it's worth it for a cold drink.")
FOOD_BOOTHS = Room("Food_Booths", " This is where you receive the food from the lunch ladies. ",
                   "EAST: Cafeteria_Kitchen, SOUTH: Cafeteria.", "They have posters of how to eat healthy and "
                   "nutritious. Sometime's the food seems to be a lot healthier than the food itself.. ")
KITCHEN = Room("Cafeteria_Kitchen", "The cafeteria's kitchen. They never actually cook anything, but there is always "
               "a lot of ingredients here.. ", "WEST: Food_Booths.", " There tends to be boxes of fruit snacks. A lot "
               "of milk cartons and juice boxes here too.. Or at least tends to be. As for now.. It's quite empty.")
BAND_ROOM = Room("Band_Room_Entrance", "It's the band room! There is a fridge and a lost and found box.", "NORTH: "
                 "Director_Office, SOUTH: Drum-Line_Lockers, WEST: Main_Band_Room", "Once entering the band room, you "
                 "feel at home. This is where you'll make all your best memories!")
OFFICE = Room("Director's_Office", "It's the director's office. ", "NORTH: Orchestra_Room, SOUTH: Band_Room entrance.",
              "There is music, trophies, awards, photos and... dvd cases? There's a lot of stuff personal to the "
              "director here you can find too. No ones allowed in the office except Section Leaders and Drum Majors.")
DRUMLINE = Room("Drumline_Lockers", "It's the drum line locker rooms!", "NORTH: Band_Room, SOUTH_WEST: "
                "Percussion_Lockers", "They are what really hold the band into their top level. Being in their locker "
                "room is an honor! The drum captain and his crew tend to hang here any chance they get. But unless "
                "you're a member or a god tier level junior/senior player, you best leave now...")
PERCUSSION = Room("Percussion_Lockers", "This isn't a room necessarily but more of a section of the room. There are "
                  "marimbas and drum sets.", "WEST: Wood-Wind_Lockers, NORTH_EAST: Drum-Line_Lockers, NORTH: "
                  "Main_Band_Room", "Never stay here for too long though, pit members aren't fond of having non "
                  "percussion kids near the instruments. If you have no reason for being here, leave asap.")
WOODWIND = Room("Woodwind_Lockers", "It's the woodwind lockers!", "EAST: Percussion_Lockers, NORTH: Main_Band_room.",
                "Most everyone hangs around here since there is rarely anyone that takes their instrument from their "
                "lockers. Flutes and clarinets always take theirs home.. Saxes though... They always go back and forth "
                "from here from lockers to stands.")
MAIN_BAND_ROOM = Room("Main_Band_Room", "This is the main band room.", "SOUTH_WEST: Wood-Wind_Lockers, SOUTH: "
                      "Percussion_Lockers, SOUTH_EAST: Drum-Line_Lockers, NORTH: Uniform_Storage_Room, WEST: Band_Hall",
                      "This is where most classes and practice takes place. No matter if you're a part of orchestra, "
                      "choir, jazz, concert, etc, this is the main used room.")
UNIFORM = Room("Uniform_Room", "This is where we keep the band uniforms as well as any extra snacks, water bottles, "
               "and other stuff. A storage room of course.", "NORTH: Orchestra_Room, SOUTH: Main_Band_Room", "The room "
               "has carts full of uniforms. There's also drinks and snacks for upcoming trips, so they're not "
               "available yet.")
ORCHESTRA = Room("Orchestra_Room", "The orchestra room isn't always used. There's a piano and lockers here as well.",
                 "NORTH_WEST: Brass_Lockers, NORTH_EAST: Color_Guard_Lockers, WEST: Band_Hall, SOUTH_WEST: "
                 "Uniform_Room, SOUTH_EAST: Director_Office, EAST: Outer_Orchestra", "The room tends to be used by "
                 "half the members for colo practice. This room is mainly used by orchestra and guard members.")
BRASS = Room("Brass_Lockers", "The brass lockers.", "SOUTH: Orchestra_Room, EAST: Color_Guard_Lockers", "You see the "
             "members always hanging around here having a good time talking or practicing. The lockers are very neat "
             "compared to the woodwinds actually! This may be because how organized the brass section leaders are!")
GUARD = Room("Color_Guard_Lockers", "It's the color guard's locker room.", "WEST: Brass_Lockers, SOUTH: Orchestra_Room",
             "The color guard change into their outfits here. As well as have their props such as flags and rifles "
             "here. The guard don't like waiting, you best hurry and leave before they catch you in here!")
BAND_HALL = Room("Band_Hall", "This is thr band hall.", "SOUTH_WEST: "
                 "Cafeteria, NORTH_WEST: Cafeteria, SOUTH_EAST: Main_Band_room, NORTH_EAST: Orchestra_Room, "
                 "NORTH: Lounge_Hall", "Students have sectionals and solo practices here when ever the director lets "
                 "us. Well, sometimes we just play video games here in groups too.")
LOUNGE_HALL = Room("Lounge_Hall", "Hall leading to the band hall, cafeteria, and lounge room.", "SOUTH: Band_Hall, "
                   "NORTH: Storage_Room, EAST: Outer_Orchestra_Room, NORTH_EAST: Teacher_Lounge_Room", "Band members "
                   "practice here too. But majority of the space is occupied by old broken stands and unused carts.")
STORAGE = Room("Storage_Room", "Storage room for the school, very small.", "SOUTH: Lounge_Hall", "This room has tables "
               "and chairs. A lot of them seem to be broken. It's not very bright in here, lights are very dim..")
TEACHER_LOUNGE = Room("Teacher's_Lounge", "It's the teacher's lounge room.", "SOUTH_EAST: Lounge_Hall, EAST: "
                      "Lounge_Table", " A lot of teachers spent there time here during lunch. Though why the lounge "
                      "room is so far from other classes as well as near the band room, is a weird placement..")
LOUNGE_TABLE = Room("Lounge_Table", "This is an area outside the teacher's lounge table.", "WEST: Teacher_Lounge, "
                    "SOUTH: Outside_Orchestra_Room", "Sometimes students hang here "
                    "during lunch. Sometimes sectionals happen here too. Well.. it tends to be a battle between low "
                    "brass and saxes for this spot too.")
OUTER_BAND = Room("Outer_Band", "This is outside the band room. ", "SOUTH_EAST: Band_Tree, NORTH: Outside_"
                  "Orchestra_Room, WEST: Band_Room", "A lot of band member hang out here during "
                  "lunch and Break.")
OUTER_ORCHESTRA = Room("Outer_Orchestra", "This is outside the orchestra room.", "SOUTH: Outside_Band_Room, WEST: "
                       "Orchestra_Room, NORTH: Lounge_Table, NORTH_WEST: Lounge_Hall", "Members don;t hang here as "
                       "often except during lunch.")


TREE1.north_east = OUTER_BAND
TREE1.west = TREE2
TREE2.east = TREE1
TREE2.west = OUTER_STAGE
OUTER_STAGE.east = TREE2
OUTER_STAGE.north = BACK_STAGE
BACK_STAGE.south = OUTER_STAGE
BACK_STAGE.north = STAGE
STAGE.south = BACK_STAGE
STAGE.north_east = CAFETERIA
STAGE.north_west = CAFETERIA
CAFETERIA.south_east = STAGE
CAFETERIA.south_west = STAGE
CAFETERIA.north_west = WATER_FOUNTAIN
CAFETERIA.north = JANITOR_ROOM
CAFETERIA.south_east = BAND_HALL
CAFETERIA.north_east = LOUNGE_HALL
JANITOR_ROOM.north = FOOD_BOOTHS
JANITOR_ROOM.south = CAFETERIA
WATER_FOUNTAIN.south = CAFETERIA
FOOD_BOOTHS.south = CAFETERIA
FOOD_BOOTHS.east = KITCHEN
KITCHEN.west = FOOD_BOOTHS
BAND_ROOM.north = OFFICE
BAND_ROOM.south = DRUMLINE
BAND_ROOM.west = MAIN_BAND_ROOM
OFFICE.north = ORCHESTRA
OFFICE.south = BAND_ROOM
DRUMLINE.south_west = PERCUSSION
DRUMLINE.north = BAND_ROOM
PERCUSSION.west = WOODWIND
PERCUSSION.north = MAIN_BAND_ROOM
PERCUSSION.north_east = DRUMLINE
WOODWIND.east = PERCUSSION
WOODWIND.north = MAIN_BAND_ROOM
MAIN_BAND_ROOM.south_west = WOODWIND
MAIN_BAND_ROOM.south_east = DRUMLINE
MAIN_BAND_ROOM.south = PERCUSSION
MAIN_BAND_ROOM.north = UNIFORM
MAIN_BAND_ROOM.west = BAND_HALL
UNIFORM.north = ORCHESTRA
UNIFORM.south = MAIN_BAND_ROOM
ORCHESTRA.north_east = GUARD
ORCHESTRA.north_west = BRASS
ORCHESTRA.south_east = OFFICE
ORCHESTRA.south_west = UNIFORM
ORCHESTRA.west = BAND_HALL
ORCHESTRA.east = OUTER_ORCHESTRA
BRASS.south = ORCHESTRA
BRASS.east = GUARD
GUARD.west = BRASS
GUARD.south = ORCHESTRA
BAND_HALL.south_west = CAFETERIA
BAND_HALL.south_east = MAIN_BAND_ROOM
BAND_HALL.north_east = ORCHESTRA
BAND_HALL.north = LOUNGE_HALL
LOUNGE_HALL.north = STORAGE
LOUNGE_HALL.south = BAND_HALL
LOUNGE_TABLE.north_east = TEACHER_LOUNGE
LOUNGE_HALL.east = OUTER_ORCHESTRA
LOUNGE_HALL.west = CAFETERIA
STORAGE.south = LOUNGE_HALL
TEACHER_LOUNGE.south_east = LOUNGE_HALL
TEACHER_LOUNGE.east = LOUNGE_TABLE
LOUNGE_TABLE.west = TEACHER_LOUNGE
LOUNGE_TABLE.south = OUTER_ORCHESTRA
OUTER_BAND.north = OUTER_ORCHESTRA
OUTER_BAND.south_east = TREE1
OUTER_BAND.west = BAND_ROOM
OUTER_ORCHESTRA.north = LOUNGE_TABLE
OUTER_ORCHESTRA.south = OUTER_BAND
OUTER_ORCHESTRA.west = ORCHESTRA
OUTER_ORCHESTRA.north_west = LOUNGE_HALL


# PLAYING CONTROL ------------------------------------------------------------------------------------------------------

playing = True
directions = ['north', 'south', 'east', 'west', 'north_east', 'north_west', 'south_east', 'south_west']

Player = Player("me", "it's me", 10, 10, 10, TREE1)

print("===***************************************")
print("COMMANDS::                               *")
print("PRESS:                                   *")
print(" 'q', 'quit', 'ee', or 'exit':           *")
print("To exit and end game.                    *")
print("===                                      *")
print("'i' or 'inventory':                      *")
print("To check inventory.                      *")
print("===                                      *")
print("'c', or 'check':                         *")
print("To check the room's longer description.  *")
print("===                                      *")
print("'t', or 'talk':                          *")
print("To talk to the room's characters.        *")
print("===                                      *")
print("'commands':                              *")
print("To see the commands again.               *")
print("===***************************************")


    while playing:
    print("-", Player.current_location.name)
    print("-", Player.current_location.description)
    print("-", Player.current_location.av_dir)
    command = input(">_")
    if command.lower() in ['q', 'quit', 'exit', 'ee']:
        playing = False
    if command.lower() in ['i', 'inventory']:
        print(Player.inventory)
    if command.lower() in ['check', 'c']:
        print("*****")
        print(Player.current_location.long_desc)
        print("*****")
    if command.lower() in ['t', 'talk']:
        Room.Characters.talk()
    if command.lower() in ['commands']:
        print("===***************************************")
        print("COMMANDS::                               *")
        print("PRESS:                                   *")
        print(" 'q', 'quit', 'ee', or 'exit':           *")
        print("To exit and end game.                    *")
        print("===                                      *")
        print("'i' or 'inventory':                      *")
        print("To check inventory.                      *")
        print("===                                      *")
        print("'c', or 'check':                         *")
        print("To check the room's longer description.  *")
        print("===                                      *")
        print("'t', or 'talk':                          *")
        print("To talk to the room's characters.        *")
        print("===                                      *")
        print("'commands':                              *")
        print("To see the commands again.               *")
        print("===***************************************")
    if command.lower() in directions:
        try:
            room_name = getattr(Player.current_location, command.lower())
            Player.move(room_name)
        except KeyError:
            print("Error: Can't go that way")
        if command.lower() in short_directions:
            pos = short_directions.index.(command.lower())
            command = directions[pos]