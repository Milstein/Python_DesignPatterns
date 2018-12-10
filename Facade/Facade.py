# coding=utf-8
class Transporter(object):
    def __init__(self, destination, typeoftravel):
        print("Arranging transport to destination: {} by means: {} ---".format(destination, typeoftravel))
        self.destination = destination
        self.typeoftravel = typeoftravel

    def bookTravel(self):
        if self.typeoftravel == 'owncar':
            print("Nothing to book, the customer uses his/her own CAR!")
        elif self.typeoftravel == 'plane':
            print("Booking seats for travelling to: {} by PLANE!".format(self.destination))
        elif self.typeoftravel == 'bus':
            print("Booking seats for travelling to: {} by BUS!".format(self.destination))

class Hotelier(object):
    def __init__(self):
        print("Arranging room for customer, ---")

    def roomFree(self):
        print("Checking if there are any rooms left free?")
        return True

    def bookRoom(self):
        if self.roomFree():
            print("Booking room for the customer")

    def arrangeFood(self):
        print("Arranging food for the customer")



class TravelOrganizer(object):
    def __init__(self):
        print("Travelorganizer:: let me arrange the travel for you!")

    def arrangeTravel(self, destination, typeoftravel):
        print("The destination is {}".format(destination))

        self.meansoftransport = Transporter(destination = destination, typeoftravel = typeoftravel)
        self.meansoftransport.bookTravel()

        self.meansofsleeping = Hotelier()
        self.meansofsleeping.bookRoom()
        self.meansofsleeping.arrangeFood()

class RoadTripping(object):
    def __init__(self):
        print("Arranging some sightseeing for the customers. ---")

    def arrangeTour(self):
        print("Arranging some fancy places to visit!")

class You(object):
    def __init__(self, name):
        print("Me:: Whohoo we are travelling: {}".format(name))

    def talkToAgent(self):
        print("Me:: Asking to arrange this weekend!")
        manager = TravelOrganizer()
        manager.arrangeTravel(destination='Greece', typeoftravel='plane')

    def __del__(self):
        print("Me:: Thank you mister manager for arranging us this beautiful weekend!")


Me = You('Milson')
Me.talkToAgent()