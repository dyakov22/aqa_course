import time


def null_decorator(func):
    return func


def decorator(func):  # func - function as argument

    def wraps():
        result = func()
        modified_result = result.lower()
        return modified_result

    return wraps


@decorator
def print_hi():
    return 'Hi' + 'There'


# print(print_hi())


# result = decorator(print_hi)

# print(result())


def print_hi(name: str):
    print(name)

    return 'Hi' + name


def print_hello(name: str):
    print(name)

    return 'Hi' + name


# def print_nihao(name: str):
#     print(name)
#
#     return 'Hi' + name


def decorator_time(func):  # func - function as argument

    def wraps(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()

        print(f'Func was executed in {end_time - start_time}, func was {func.__name__}')

        return result

    return wraps


@decorator_time
def print_nihao(name: str):
    print(name)

    return 'Hi' + name


# print_nihao('Kate')


@decorator_time
def sum_range():
    return sum(range(100000))


# print(sum_range())


@decorator_time
def sleep_for_while():
    time.sleep(5)


# sleep_for_while()


# @decorator_time(1)
# def sleep_for_while():
#     time.sleep(5)

# result = decorator_time(sleep_for_while)
# result = decorator_time(1)


def main_decorator(times: int):

    def decorator_time_with_arg(func):  # func - function as argument

        def wraps(*args, **kwargs):
            result_list = []
            for _ in range(times):
                start_time = time.time()
                result_list.append(func(*args, **kwargs))
                end_time = time.time()

                print(f'Func was executed in {end_time - start_time}, func was {func.__name__}')

            return result_list

        return wraps

    return decorator_time_with_arg



@main_decorator(2)
def find_number(target: int, source: list) -> tuple:
    for index, item in enumerate(source):
        # time.sleep(0.3)
        if target == item:
            return index, item


# find_number(10000, range(100000000))


result = main_decorator(2)
result_inner = result(find_number)
print(result_inner(10000, range(100000000)))