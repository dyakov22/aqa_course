# generator is iterator

list_1 = [1, 2, 3, 4, 5]


# open().readlines() -> list


# list_1 = generator


# def generator():
#     counter = 0
#     while True:
#
#         yield counter
#
#         counter += 1


# gen = generator()

# print(next(gen))
# print(next(gen))
# print(next(gen))



# for index in generator():
#     # print(index)
#     if index == 10000:
#         print(index)
#         break


# def generator():
#
#     # file = open('text.txt', 'r').readlines()
#
#     file = [5, 4, 3, 2, 1]
#
#     counter = 0
#
#     while len(file) != counter:
#
#         yield file[counter]
#
#         counter += 1
#
#
# for line in generator():
#     print(line)


def generator(start: int, stop: int, step: int = 1):
    value = start
    while value < stop:
        yield value

        value += step


# for index in generator(0, 10):
#     print('generator ', index)
#
# for index in range(0, 10):
#     print('range ', index)



def counter(start: int):
    current = start

    while current > 0:

        yield current

        current -= 1


countdown = counter(3)

next(countdown)
next(countdown)


generator_comp = (i * i for i in range(10))

# file = (line for line in open('text.txt', 'r'))


print(list(generator(0, 10)))

