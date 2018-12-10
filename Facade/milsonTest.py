# coding=utf-8


class Transporter(object):
    def __init__(self, name, destination, typeoftravel):
        self.name = name
        self.destination = destination
        self.typeoftravel = typeoftravel
        print("Reserving Transport! ---")

    def bookTravel(self):
        if self.typeoftravel == 'Car':
            print("No need to reserve! the customer is self-driving!")
        elif self.typeoftravel == 'Plane':
            print("Reserving the plane seats for {} travelling by PLANE to {}!".format(self.name, self.destination))
        elif self.typeoftravel == 'Bus':
            print("Reserving the bus seats for {} travelling by BUS to {}!".format(self.name, self.destination))


class Hotelier(object):
    def __init__(self):
        print("Finding Room and Food! ---")

    def bookRoom(self):
        if self.freeRoomExist():
            print("Your Room is booked!")
        else:
            print("No Room is Vacant at this moment!")

    def arrangeFood(self):
        print("Delicious! food is arranged!")

    def freeRoomExist(self):
        print("One Room is Empty for you!")
        return True


class TravelOrganizer(object):

    def __init__(self):
        print("Talking to the Travel Organizer! ---")

    def arrangeTravel(self, name, destination, typeoftravel):
        self.meansoftransport = Transporter(name, destination, typeoftravel)
        self.meansoftransport.bookTravel()

        self.meansofsleep = Hotelier()
        self.meansofsleep.bookRoom()
        self.meansofsleep.arrangeFood()


class Person(object):
    def __init__(self, name, destination, typeoftravel):
        self.name = name
        self.destination = destination
        self.typeoftravel = typeoftravel
        print("Welcome {}".format(self.name))

    def talkToAgent(self):
        self.travelorganizer = TravelOrganizer()
        self.travelorganizer.arrangeTravel(self.name, self.destination, self.typeoftravel)

if __name__ == '__main__':
    me = Person(name='Milstein', destination='Nepal', typeoftravel='Plane')
    me.talkToAgent()

