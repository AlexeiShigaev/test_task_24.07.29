import math
import time


def start_test():
    time_start = time.time()

    numbers = [i for i in range(1, 1000001)]
    squares = []
    for number in numbers:
        squares.append(number ** 2)

    print(squares[4])
    time_end = time.time()
    print("Elapsed time: {}".format(time_end - time_start))


def my_test_1():
    time_start = time.time()

    # numbers = [i for i in range(0, 1000001)]
    squares = []
    for number in range(0, 1000001):
        squares.append(number ** 2)

    print(squares[5])
    time_end = time.time()
    print("Elapsed time: {}".format(time_end - time_start))


def my_test_2():
    # индекс в списке squares соответствует числу квадрат которого исчисляем.
    time_start = time.time()

    # numbers = [i for i in range(0, 1000001)]
    squares = [math.pow(num, 2) for num in range(0, 1000001)]

    print(squares[5])
    time_end = time.time()
    print("Elapsed time: {}".format(time_end - time_start))


def my_test_3():
    # наилучший результат по скорости выполнения. в пять раз быстрее.
    # индекс в списке squares соответствует числу, квадрат которого исчисляем.
    time_start = time.time()

    # numbers = [i for i in range(0, 1000001)]
    squares = [num * num for num in range(0, 1000001)]

    print(squares[5])
    time_end = time.time()
    print("Elapsed time: {}".format(time_end - time_start))


def my_test_4():
    time_start = time.time()

    numbers = [i for i in range(0, 1000001)]
    squares = []
    for number in numbers:
        squares.append(number * number)

    print(squares[5])
    time_end = time.time()
    print("Elapsed time: {}".format(time_end - time_start))


if __name__ == "__main__":
    # Original test
    # 25
    # Elapsed time: 0.7560434341430664
    #
    # my_test_1
    # 25
    # Elapsed time: 0.79604172706604
    #
    # my_test_2
    # 25.0
    # Elapsed time: 0.5210299491882324
    #
    # my_test_3
    # 25
    # Elapsed time: 0.1500084400177002
    #
    # my_test_4
    # 25
    # Elapsed time: 0.3090176582336426

    print("\nOriginal test")
    start_test()
    print("\nmy_test_1")
    my_test_1()
    print("\nmy_test_2")
    my_test_2()
    print("\nmy_test_3")
    my_test_3()
    print("\nmy_test_4")
    my_test_4()
