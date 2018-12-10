# coding=utf-8
class Topic(object):

    def __init__(self):
        self.__clients = []

    def register(self, client):
        print('New Subscriber: {}'.format(client))
        self.__clients.append(client)

    def notifyAll(self, *args, **kwargs):
        for client in self.__clients:
            # if isinstance(client, MenAbove40):
            #     print('These are the men!')
            # elif isinstance(client, LadiesAbove30):
            #     print('Ladies go First!')
            if kwargs.get('menOnly') and isinstance(client, MenAbove40):
                client.notify(self, *args, **kwargs)
            elif kwargs.get('ladiesOnly') and isinstance(client, LadiesAbove30):
                client.notify(self, *args, **kwargs)


class LadiesAbove30:
    def __init__(self, topic):
        topic.register(self)

    def notify(self, *args, **kwargs):
        print(type(self).__name__, "--> Got", args, "From", topic)

class MenAbove40:
    def __init__(self, topic):
        topic.register(self)

    def notify(self, *args, **kwargs):
        print(type(self).__name__, "--> Got", args, "From", topic)

topic = Topic()
Subsribers = []

for i in range(10):
    Subsribers.append(LadiesAbove30(topic))

for i in range(5):
    Subsribers.append(MenAbove40(topic))

topic.notifyAll('Hello World Men!', menOnly=True)
topic.notifyAll('Welcome Ladies!', ladiesOnly=True)