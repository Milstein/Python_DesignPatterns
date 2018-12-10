# coding=utf-8
from random import randint


class Player(object):
    def __init__(self, name):
        self.name = name
        self.price = randint(1000, 9000)
        self.training = False
        self.vacation = False

    def onTraining(self):
        self.training = True
        return self.training

    def onVacation(self):
        self.vacation = True
        return self.vacation

    def getPrice(self):
        return self.price

    def status(self):
        return (self.vacation or self.training)


class Manager(object):
    def __init__(self, player):
        self.managed_player = player
        print('Managing Player: {}'.format(self.managed_player.name))

    def send_player_on(self, typee):
        if typee in ['vacation', 'training']:
            if typee == 'vacation':
                print('Sending player: {} on vacation'.format(self.managed_player.name))
                self.managed_player.onVacation()
            else:
                print('Sending player: {} on training'.format(self.managed_player.name))
                self.managed_player.onTraining()
        else:
            print('Can\'t send player on: {}, it\'s not a valid option!'.format(typee))

    def sell_player(self, offer):
        print('The price of the player is: {}'.format(self.managed_player.getPrice()))
        if offer > self.managed_player.getPrice():
            print('Saying goodbye to {}'.format(self.managed_player.name))
        else:
            print('Saying No to the offer, as the player {} is more valuable!'.format(self.managed_player.name))

if __name__ == '__main__':
    fballer = Player('Daniel')
    mgr = Manager(fballer)

    # mgr.send_player_on('vacation')
    mgr.send_player_on('training')

    mgr.sell_player(1000)
