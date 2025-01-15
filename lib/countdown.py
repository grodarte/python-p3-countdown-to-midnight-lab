import time

# your code goes here!
def countdown(number):
    i = number
    while i > 0:
        print(f"{i} SECOND(S)!")
        i -= 1
    else:
        print("HAPPY NEW YEAR!")

def countdown_with_sleep(number):
    while number > 0:
        print(f"{number} SECOND(S)!")
        number -=1
        time.sleep(1)
    print("HAPPY NEW YEAR!")