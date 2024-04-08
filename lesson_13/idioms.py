


# Делегирование
#
# class Character:
#
#     def __init__(self, race: str):
#         self.race = race
#
#     def make_sound(self):
#         print(f'Sound of {self.race}')
#
#
# class Shield:
#
#     def pair_hit(self):
#         print('Hit was paired')
#
#
# class Hero:   # class Hero(Character, Shield):
#
#     def __init__(self, race: str):
#         self.__character = Character(race=race)
#         self.__shield = Shield()
#
#     @property
#     def character(self):
#         return self.__character
#
#     @property
#     def shield(self):
#         return self.__shield
#
#
# hero = Hero('hero')
# hero.character.make_sound()


# Composition
#
# class Engine:
#
#     def __init__(self):
#         self.type = 'v6'
#
#     def start(self):
#         print(f'{self.type} engine was started')
#
#     def stop(self):
#         print(f'{self.type} engine was stopped')
#
#
# class Lights:
#
#     def lights_on(self):
#         print('Lights on')
#
# class Car:
#
#     def __init__(self):
#         self.__engine = Engine()
#         self.__lights = Lights()
#
#     def start(self):
#         self.__engine.start()
#
#     def stop(self):
#         self.__engine.stop()
#
#     def lights_on(self):
#         self.__lights.lights_on()
#
#
# car = Car()
# car.start()
# car.lights_on()


# Facade

#
# class Engine:
#
#     def __init__(self):
#         self.type = 'v12'
#
#     def start_engine(self):
#         print(f'{self.type} engine was started')
#
#
# class Lights:
#
#     def __init__(self):
#         self.type = 'led'
#
#     def lights_on(self):
#         print('Lights on')
#
# class ClimateControl:
#
#     def __init__(self):
#         self.type = '0.0.1'
#         self.availability = True
#
#     def set_temp(self, temperature: float):
#         if self.availability:
#             print(f'Temp was set {temperature}')
#
#
# class Car:
#
#     def __init__(self):
#         self.__engine = Engine()
#         self.__lights = Lights()
#         self.__climate_control = ClimateControl()
#
#     @property
#     def engine(self):
#         return self.__engine
#
#     @property
#     def lights(self):
#         return self.__lights
#
#     @property
#     def climate_control(self):
#         return self.__climate_control
#
#     def start_car(self, temperature: float):
#         self.engine.start_engine()
#         self.lights.lights_on()
#         self.climate_control.set_temp(temperature=temperature)
#
#
# car = Car()
# car.start_car(10.1)
