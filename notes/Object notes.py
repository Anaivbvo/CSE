class Phone(object):
    def __init__(self, carrier, charge_left):
        # These are attributes that a phone has.
        # These should all be relevant to our program
        self.screen = True
        self.camera = 2
        self.microphone = True
        self.carrier = carrier
        self.battery_left = charge_left

    def charge(self, time):
        self.battery_left += time
        if self.battery_left > 100:
            self.battery_left = 100

        def make_call(self, duration):
            if not self.screen:
                print("You can't make a phone call.")
                print("Your screen is broken.")
                return
            battery_loss_per_minute = 5
            if self.batter_left <= 0:
                print("You can't the phone is dead.")
                return
            self.batter_left -= duration * battery_loss_per_minute
            if self.batter_left < 0:
                self.batter_left = 0
                print("Your phone dies during the conversation.")
            elif self.batter_left ==0:
                print("Your phone dies at the end of this conversation.")
            else:
                print("You sincerely make the phone call!")