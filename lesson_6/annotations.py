from typing import Union, Optional



# def say_hi(name: str) -> str:
#     if isinstance(name, int):
#         print('This int')
#     print('This smth else')
#     return 'from return'
#
#
# say_hi(10)

# my_string = 'my string Failed'
#
# test_list = ['Failed: msg error', 'Success: success msg', 'Failed: error msg']
#
#
# def count_words(data: Union[str, list], target_word: str = 'Failed') -> int:
#     if isinstance(data, str):
#         return data.count(target_word)
#     elif isinstance(data, list):
#         return len([word for word in data if word.count(target_word) >= 1])
#     else:
#         raise Exception(f'This type does not support {type(data)}')
#
#
# print(count_words(test_list))


my_string = 'my string Failed'

test_list = ['Failed: msg error', 'Success: success msg', 'Failed: error msg']


# class MyClass:
#
#     age: int = 20
#     name: str = 'Nikita'
#
#     def get_last_50_requests(self):
#         return []


def count_words(data: Union[str, list], target_word: str = 'Failed') -> Optional[int]:
    if isinstance(data, str):
        return data.count(target_word)
    elif isinstance(data, list):
        return len([word for word in data if word.count(target_word) >= 1])
    else:
        return None

# print(__name__, 'From annotations')


if __name__ == '__main__':
    print(count_words(test_list))
    print('From annotations')

