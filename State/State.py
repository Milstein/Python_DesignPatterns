# coding=utf-8
from abc import ABCMeta, abstractmethod


class InternalState(metaclass=ABCMeta):
    @abstractmethod
    def changeState(self):
        raise NotImplementedError("Please Implement required method <changeState>")


class TurnedOn(InternalState):
    def changeState(self):
        print("The Radio is Turned ON!")
        return "ON"


class TurnedOff(InternalState):
    def changeState(self):
        print("The Radio is Turned OFF!!!")
        return "OFF"

class VolumeIncrease(InternalState):
    def changeState(self):
        print("The Volume is Increased!")
        return "+10"

class VolumeDecrease(InternalState):
    def changeState(self):
        print("The Volume is Decreased!")
        return "-10"


class RadioStation(InternalState):
    def __init__(self):
        self.state = None

    def setState(self, state):
        self.state = state

    def getState(self):
        return self.state

    def changeState(self):
        self.state = self.state.changeState()


Radio = RadioStation()

ON = TurnedOn()
OFF = TurnedOff()

print("The radio's current state: {}".format(Radio.getState()))

print("Turning ON the Radio:")
Radio.setState(ON)
Radio.changeState()
print("The radio's current state: {}".format(Radio.getState()))

print("Turing OFF the Radio:")
Radio.setState(OFF)
Radio.changeState()
print("The radio's current state: {}".format(Radio.getState()))

Loude = VolumeIncrease()
Quite = VolumeDecrease()

print("Volume Increasing: ")
Radio.setState(Loude)
Radio.changeState()
print("The radio's current state: {}".format(Radio.getState()))

print("Volume Decreasing: ")
Radio.setState(Quite)
Radio.changeState()
print("The radio's current state: {}".format(Radio.getState()))

