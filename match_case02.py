import random
def matching(guess, x):
    flag = False
        # check = guess>=x
    match guess:
        case g if g < x:
            print("You are low")
        case g if g > x:
            print("You are high")
        case _:
            print(f"You got it!")
            flag = True
    if abs(guess - x) < 5:
                print("You are close!!")
    return flag

if __name__ == "__main__":
    x = random.randint(0,100)
    tries = int(input("How many attempts you want: "))
    total = tries
    while tries!=0:
        guess = int(input("Enter your guess: "))
        check = matching(guess,x)
        tries = tries - 1
        if check == True:
            print(f"It was {x} and you got it in {total-tries} tries")
            break
    else:
        print("Out of tries! Better luck next time")
    