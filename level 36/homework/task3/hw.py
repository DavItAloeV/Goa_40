def zero_or_no():
    num1 = input(int("please enter a number more than 0:"))
    if num1 > 0:
        return("its more than zero")
    elif num1 < 0:
        return("its below zero")
    else:
        return("its zero")
zero_or_no