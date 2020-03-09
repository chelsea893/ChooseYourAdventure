"""
Title: Choose your adventure
Author: Chelsea Chen
Date Created: 2020-06-03
"""
# --- VARIABLES --- #
coins = 100
lives = 3
running = True
# --- SUBROUTINES --- #
def intro():
    print("""
    Welcome to Escape your Fate! In this choose your adventure game, you will be given various choices, each of them a deciding factor in if you 
    will be able to change your fate. You will have three lives and 100 coins to spend on objects that will help you on your journey. Choose 
    accordingly and you might be able to survive! 
    """)
def end():
    again = input("Try Again? (Y/n)")
    if again != "y" and again != "Y" and again != "":
        running = False
def hint():
    coins = coins - 10


def stage1():
    print("""
        You wake up. You aren't able to remember anything except vaguely the words "Experiment 3025- human brain simulation" as you sit on a 
        hospital bed your head wired up to a machine, its steady beating creates a pattern "thump, thump, thump thump, thump." Around your right
        wrists is a metal bands that restrict your movement, a combination key with a four number solution. You decide try two different combinations,
        what four numbers do you input? Press y/N for a hint. It will cost ten coins. 
        """)
    hint1 = input()
    if hint1 == "y" or hint1 == "Y":
        print("Observe the pattern of the steady beating. Count the beats to find a combination. Remember there are four numbers and four beats.")
    else:
        pass
    combination = int(input("Enter your combination here: "))
    if combination == 1121:
        print("Your right hand comes loose")
    else:
        print("The alarm sounds, causing people to rush into the room to restrain you. GAME OVER")




# --- INPUTS --- #
value = input("Press the enter key if you dare!")

# --- Processing --- #
while running:
    intro()
    stage1()



# --- OUTPUTS --- #
