# coding=utf-8
from abc import ABCMeta, abstractmethod
import time


class Platform(metaclass=ABCMeta):
    @abstractmethod
    def stop_systems(self):
        raise NotImplementedError("Please implement the method <stop_systems>!")

    @abstractmethod
    def start_systems(self):
        raise NotImplementedError("Please implement the method <start_systems>!")

    @abstractmethod
    def health_check_systems(self):
        raise NotImplementedError("Please implement the method <health_check_systems>!")


class WebServer(Platform):
    __nodes = ['web_node_a', 'web_node_b', 'web_node_c']

    def stop_systems(self):
        for system in self.__nodes:
            print("Stopping system: {}".format(system))
            time.sleep(0.5)

    def start_systems(self):
        for system in self.__nodes:
            print("Starting system: {}".format(system))
            time.sleep(0.5)

    def health_check_systems(self):
        for system in self.__nodes:
            print("Health Checking system: {}".format(system))
            time.sleep(0.5)


class FireWall(Platform):
    __nodes = ['fw_node_a', 'fw_node_b', 'fw_node_c']

    def stop_systems(self):
        for system in self.__nodes:
            print("Stopping system: {}".format(system))
            time.sleep(0.5)

    def start_systems(self):
        for system in self.__nodes:
            print("Starting system: {}".format(system))
            time.sleep(0.5)

    def health_check_systems(self):
        for system in self.__nodes:
            print("Health Checking system: {}".format(system))
            time.sleep(0.5)


class Database(Platform):
    __nodes = ['db_node_a', 'db_node_b', 'db_node_c']

    def stop_systems(self):
        for system in self.__nodes:
            print("Stopping system: {}".format(system))
            time.sleep(0.5)

    def start_systems(self):
        for system in self.__nodes:
            print("Starting system: {}".format(system))
            time.sleep(0.5)

    def health_check_systems(self):
        for system in self.__nodes:
            print("Health Checking system: {}".format(system))
            time.sleep(0.5)


class PatchingFactory(object):
    def stop_all(self, platform_object):
        print("Stopping platform: {}".format(platform_object))
        return eval(platform_object)().stop_systems()

    def start_all(self, platform_object):
        print("Starting platform: {}".format(platform_object))
        return eval(platform_object)().start_systems()

    def hc_all(self, platform_object):
        print("Health Checking platform: {}".format(platform_object))
        return eval(platform_object)().health_check_systems()

    def make_magic_happens(self, platform_object):
        self.hc_all(platform_object)
        self.stop_all(platform_object)
        self.start_all(platform_object)
        self.hc_all(platform_object)


PF = PatchingFactory()
PFORMS = ['WebServer', 'FireWall', 'Database']
for platform in PFORMS:
    PF.make_magic_happens(platform)
# platform = input("Which platform?")
# PF.stop_all(platform)
# PF.start_all(platform)
# PF.hc_all(platform)
# PF.make_magic_happens(platform)
