

# class Car:
#
#     def purchase(self):  # going to be changed
#         pass
#
#     def clean_up(self):  # probably will be changed
#         print('Clean up lights')
#
#
# class BMW(Car):
#
#     pass
#
# bmw = BMW()
# bmw.start()


from abc import ABC, abstractmethod


class Car(ABC):

    @abstractmethod
    def start(self):
        pass

    def stop(self):
        print('Stop engine')

class BMW(Car):

    def start(self):
        print('Start engine with fuel')

    def check_engine(self):
        pass


class Tesla(Car):

    def start(self):
        print('Start engine with electricity')


car = BMW()
car.start()
car.stop()

tesla = Tesla()
tesla.start()
tesla.stop()
