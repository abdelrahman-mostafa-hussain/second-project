import random

def numberGenerator()->int:
    return random.choice(range(1,20))

def hint(num:int):
        if 20>=num>15 :
            print("hint: the number is too high ")
        elif 15>=num>10 :
            print("hint: the number is high ")
        elif 10>=num>5 :
            print("hint: the number is low ")
        else:
            print("hint: the number is too low ")

def main():
    print("Welcome to guess the number game, you will guess number between 1 and 20, lets start:")
    while True:
        randNum=numberGenerator()
        hint(randNum)
        chance=2
        while True:
            numberguessed=int(input("please enter the number you guessed: "))
            if randNum==numberguessed:
                print("your guess is correct")
                break
            else:
                if chance==0:
                    print("your guess was wrong and consume your chances")
                    break
                print('your guess was wrong try again')
                chance-=1
        quit=input("(if you want to quit the game press q or press enter to continue):")
        if quit.lower()=="q":
            print('thank to play our game')
            break
        print("let's try another round")

if __name__=="__main__":
    main()