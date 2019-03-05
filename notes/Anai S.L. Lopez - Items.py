class Instrument(object):
    def __init__(self, name):
        self.name = name


class Wind(Instrument):
    def __init__(self, name):
        super(Wind, self).__init__(name)


class Flute(Wind):
    def __init__(self, name):
        super(Flute, self).__init__(name)
