from datetime import datetime


def decorator():
    print(datetime.now)

@decorator
def deco():
    return 1

deco()