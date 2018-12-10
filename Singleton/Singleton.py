# coding=utf-8
class Singleton_Lazy(object):
    __instance = None

    def __init__(self):
        if not Singleton_Lazy.__instance:
            print("I have already got an instance!")
        else:
            print("I don't have got an instance!")

    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = Singleton_Lazy()
        return cls.__instance


class Singleton_Strict(object):

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton_Strict, cls).__new__(cls)
        return cls.instance


sl = Singleton_Lazy()
sl2 = Singleton_Lazy()

print("sl: %s, sl2: %s" % (sl.getInstance(), sl2.getInstance()))

ss = Singleton_Strict()
ss2 = Singleton_Strict()

print('ss: %s, ss2: %s' % (ss, ss2))
