import random

def numberGenerator():
    return random.choice(range(1,100))

def main():
    print("Guess number game")

if __name__=="__main__":
    main()