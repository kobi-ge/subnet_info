def input_size() -> tuple:
    print("please choose your preferred board size")
    while True:
        x = input("enter the first number \n").strip()
        y = input("enter the second number \n").strip()
        if x.isdigit() and y.isdigit():
            return int(x), int(y)
        print("invalid input try again. ")



