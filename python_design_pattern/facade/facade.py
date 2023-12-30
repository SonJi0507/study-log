# --- facade ---
class EventManager(object):
    def __init__(self):
        print("Event Manager:: Let me talk to the folks\n")

    def arrange(self):
        self.hotelier = Hotelier()
        self.hotelier.bookHotel()

        self.florist = Florist()
        self.florist.setFlowerRequirements()

        self.caterer = Caterer()
        self.caterer.setCuisine()

        self.musician = Musician()
        self.musician.setMusicType()


# --- subsystem ---
class Hotelier(object):
    def __init__(self):
        print("Arranging the Hotel for Marriage? --")

    def __isAvailable(self):
        print("Is the Hotel free for the event on given day?")
        return True

    def bookHotel(self):
        if self.__isAvailable():
            print("Registered the Booking\n\n")


class Florist(object):
    def __init__(self):
        print("Flower Decorations for the Event? --")

    def setFlowerRequirements(self):
        print("Carnations, Roses and Lilies would be used for Decorations\n")


class Caterer(object):
    def __init__(self):
        print("Food Arrangements for the Event --")

    def setCuisine(self):
        print("Chiness & Continental Cuisine to be served\n")


class Musician(object):
    def __init__(self):
        print("Musical Arrangements for the Marriage --")

    def setMusicType(self):
        print("Jazz and Classical will be played\n")


# --- client ---
class You(object):
    def __init__(self):
        print("You:: Marriage Arrangements??!")

    def askEventManager(self):
        print("You:: Let's Contact the Event Manager\n")
        em = EventManager()
        em.arrange()

    def __del__(self):
        print("You:: Thanks to Event Manager, all preparations done!")


you = You()
you.askEventManager()


"""
You:: Marriage Arrangements??!
You:: Let's Contact the Event Manager

Event Manager:: Let me talk to the folks

Arranging the Hotel for Marriage? --
Is the Hotel free for the event on given day?
Registered the Booking


Flower Decorations for the Event? --
Carnations, Roses and Lilies would be used for Decorations

Food Arrangements for the Event --
Chiness & Continental Cuisine to be served

Musical Arrangements for the Marriage --
Jazz and Classical will be played

You:: Thanks to Event Manager, all preparations done!
"""
