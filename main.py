def task1_1():
    num = input("Enter a number: ")

    try:
        num = int(num)
        if num % 2 == 0:
            print("Четное")
        else:
            print("Нечетное")
    except ValueError:
        print("Invalid input")

def task1_2():
    temperature = input("Enter a temperature: ")

    try:
        temperature = int(temperature)
        if temperature <= 0:
            print("VERY COLD!")
        elif 0 < temperature <= 20:
            print("COLD!")
        else:
            print("WARM")


    except ValueError:
        print("Invalid input")

def task1_3():
    time = input("Enter a time: ")
    try:
        time = int(time)
        if 6 <= time <= 11:
            print("Утро")
        elif 12 <= time <= 17:
            print("День")
        elif 18 <= time <= 22:
            print("Вечер")
        elif time == 23 or time <= 5:
            print("Ночь")
    except ValueError:
        print("Invalid input")

