import random

def numberGenerator()->int:
    return random.choice(range(1,100))

def hint(num:int):
        if 100>=num>80 :
            print(" hint: the number is too high ")
        elif 80>=num>60 :
            print(" hint: the number is high ")
        elif 60>=num>40 :
            print(" hint: the number is in middle ")
        elif 40>=num>20 :
            print(" hint: the number is low ")
        else:
            print(" hint: the number is too low ")

def main():
    print("Welcome to guess the number game,",
          "you will guess number between 1 and 100,",
          "lets start:",sep="\n")
    while True:
        randNum=numberGenerator()
        hint(randNum)
        break

if __name__=="__main__":
    main()