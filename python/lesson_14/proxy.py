# from abc import ABC, abstractmethod
# import random
#
#
# class BEInterface(ABC):
#
#     @abstractmethod
#     def request(self):
#         pass
#
#
# class RealBEInterface(BEInterface):
#
#     def request(self):
#         print('Request was sent')
#
#
# class Proxy:
#
#     def __init__(self, interface: BEInterface):
#         self._real_be_interface = interface
#
#     def __verify_access_rights(self):
#         ...
#         print('Processing....')
#         return False
#         # return random.choice([False, True])
#
#     def request(self):
#         if self.__verify_access_rights():
#             self.log_msg()
#             self._real_be_interface.request()
#         else:
#             print('Access denied')
#
#     def log_msg(self):
#         print('Access was given')
#
#
#
# _client = RealBEInterface()
#
# client = Proxy(_client)
#
# client.request()
#
