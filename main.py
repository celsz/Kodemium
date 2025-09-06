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


task1_1()