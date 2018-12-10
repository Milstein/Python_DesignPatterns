# coding=utf-8
class Topic:
    def __init__(self):
        self.__clients = []

    def register(self, client):
        print('New Subscriber: {}'.format(client))
        self.__clients.append(client)


    def notifyAll(self, *args, **kwargs):
        for client in self.__clients:
            client.notify(self, *args, **kwargs)


class Observer:
    def __init__(self, topic):
        topic.register(self)

    def notify(self, *args, **kwargs):
        print(type(self).__name__, "--> Got", args, "From", topic)


class AnotherObserver(object):
    def __init__(self, topic):
        topic.register(self)

    def notify(self, *args, **kwargs):
        print(type(self).__name__, "--> Got", args, "From", topic)


topic = Topic()
Subscribers = []
for i in range(100):
    Subscribers.append(Observer(topic))

# obs_1 = Observer(topic)
obs_2 = AnotherObserver(topic)
topic.notifyAll('Thank you for demoing!!')