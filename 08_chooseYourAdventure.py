"""
Title: Choose your adventure
Author: Chelsea Chen
Date Created: 2020-06-03
"""
import sys
<<<<<<< HEAD

=======
>>>>>>> origin/master
# --- VARIABLES --- #
coins = 100
lives = 3
red = 0
blue = 0
keyCard = 0
running = True
stage1 = True
stage2 = True
<<<<<<< HEAD
stage4 = False
stage3part2 = True

=======
>>>>>>> origin/master
# --- SUBROUTINES --- #
def intro():
    print("""
Welcome to Escape your Fate! In this choose your adventure game, you will be given various choices, each of them a deciding factor in if you 
will be able to change your fate. You will have three lives and 100 coins to spend on objects that will help you on your journey. Choose 
accordingly and you might be able to survive! 
------------------------------------------------------------------------------------------------------------------------------------------------
STAGE 1
------------------------------------------------------------------------------------------------------------------------------------------------
    """)

<<<<<<< HEAD

=======
>>>>>>> origin/master
def stage2part1():
    global lives
    global keyCard
    global stage2
<<<<<<< HEAD
    print("""
You walk around the room on the furthest right are two doors. You see two doors. You try the handles they don't open. On the left side
of the door you see a scanner. You decide to search in the two most obvious places first: the shelf, the desk, the file cabinet, and
the bookshelf. Which place do you search first? Each time you guess wrong, you loose a life. 
    - Press s/S to search the shelf with the containers. 
    - Press d/D to search the desk.
    - Press f/F to search the file cabinet. 
    - Press b/B to search the bookshelf         
""")
    while lives > 0 and stage2:
        choice2 = str(input("Put choice here:"))
        if choice2 == "s" or choice2 == "S":
            print("""
You move the container over on the shelf and find a key card: 
            ____________________
           |      EMPLOYEE      |
           |      KEY CARD      |
           |                    |          
           |       .xxxx.       | 
           |      |(o)(o)|      |
           |     (  (__)  )     |
           |       | __ |       | 
           |        \__/        | 
           |                    |            
           |                    |
           |____________________|
            """)
            keyCard = 1
            stage2 = False
        else:
            print("It is not there. Try searching in another place")
            lives = lives - 1
            print("You have lost one life. You have this many left %s" % lives)
            print("coins= %s" % coins)
    if lives < 0:
        print("""
        Your heart races, you begin to have a panic attack because nothing you are doing is working. You begin to grow faint. You land on 
        the ground with a thud. People start to rush around you. GAME OVER
              """)
        sys.exit
def stage3part2():
    global stage3part2
    global lives
    global stage4
    print("""
Down the hall you see someone. You inspect the surrondings thinking that it is clear and begin to walk down the hall. Suddenly, you
hear footsteps behind you. You decide to rush into a room to escape them, there are two room numbers. Which one of the rooms do 
you decide to enter: 213 or 215
        """)
    choice4 = int(input("Enter in the number 213 to enter it. Enter in the number 215 to enter the other room. "))
    if choice4 == 213:
        print("""
when you walk into the room, you see people in lab coats, discussing at an table. They see you and grab your arm.
Suddenly, your vision goes black. 
        """)
        lives = lives - 1
        print("You have lost a life. you have this many left %s" %lives)
    if lives < 0:
        print("GAME OVER")
        stage3part2 = False
=======
    print("""
You walk around the room on the furthest right are two doors. You see two doors. You try the handles they don't open. On the left side
of the door you see a scanner. You decide to search in the two most obvious places first: the shelf, the desk, the file cabinet, and
the bookshelf. Which place do you search first? Each time you guess wrong, you loose a life. 
    - Press s/S to search the shelf with the containers. 
    - Press d/D to search the desk.
    - Press f/F to search the file cabinet. 
    - Press b/B to search the bookshelf         
""")
    while lives > 0 and stage2:
        choice2 = str(input("Put choice here:" ))
        if choice2 == "s" or choice2 == "S":
            print("""
You move the container over on the shelf and find a key card: 
            ____________________
           |      EMPLOYEE      |
           |      KEY CARD      |
           |                    |          
           |       .xxxx.       | 
           |      |(o)(o)|      |
           |     (  (__)  )     |
           |       | __ |       | 
           |        \__/        | 
           |                    |            
           |                    |
           |____________________|
            """)
            keyCard = 1
            stage2 = False
        else:
            print("It is not there. Try searching in another place")
            lives = lives - 1
            print("You have lost one life. You have this many left %s" % lives)
            print("coins= %s" % coins)
    if lives < 0:
        print("""
        Your heart races, you begin to have a panic attack because nothing you are doing is working. You begin to grow faint. You land on 
        the ground with a thud. People start to rush around you. GAME OVER
              """)
        sys.exit
>>>>>>> origin/master



# --- INPUTS --- #
value = input("Press the enter key if you dare!")

# --- Processing --- #
intro()
print("""
You wake up. You aren't able to remember anything except vaguely the words "Experiment 3025- human brain simulation" as you sit on a 
hospital bed your head wired up to a machine, its steady beating creates a pattern "thump, thump, thump thump, thump." Around your right
wrists is a metal bands that restrict your movement, a combination key with a four number solution. You decide try two different combinations,
what four numbers do you input?  
        """)

while stage1 and lives > 0:
    hint1 = input("Press y/N for a hint. It will cost ten coins.")
    if hint1 == "y" or hint1 == "Y":
        print(
            "Observe the pattern of the steady beating. Count the beats to find a combination. Remember there are four numbers and four beats."
        )
        coins = coins - 10
    else:
        pass
    combination = int(input("Enter your combination here: "))
    if combination == 1121:
        print("Your right hand comes loose")
        print("coins= %s" % coins)
        print("lives = %s" % lives)
        stage1 = False
    else:
        lives = lives - 1
        print("You have lost one life. You have this many left %s" % lives)
        print("coins= %s" % coins)
    if lives == 0:
        print("The alarm sounds, causing people to rush into the room to restrain you. You have been caught. GAME OVER")
        sys.exit
<<<<<<< HEAD

print("""
------------------------------------------------------------------------------------------------------------------------------------------------
STAGE 2
----------------------------------------------------------------------------------------------------------------------------------------
As you get up, you rip the wires from your head. All of sudden you feel dizzy and have a terriable headache. Everything around you is
blurry the only thing you can make out are two containers, on the shelf. The red one says that it will get rid of your headache
but lead to side effects of confusion. The other one doesn't have a label; however, it is still on the shelf labelled pain-killers. 
Which one do you take? 
              _________                       _________
             {_________}                     {_________}       
              )=======(                       )=======(
             /         \                     /         |
            | _________ |                   | _________ |
            ||   RED   ||                   ||  BLUE   ||
            ||  side   ||                   ||         ||
            || effects ||                   ||         ||        
      __    ||         ||                   ||         ||
 __  (_|)   |'---------'|                   |'---------'| 
(_|)        `-.........-'                   `-.........-'
=======
>>>>>>> origin/master

print("""
------------------------------------------------------------------------------------------------------------------------------------------------
STAGE 2
----------------------------------------------------------------------------------------------------------------------------------------
As you get up, you rip the wires from your head. All of sudden you feel dizzy and have a terriable headache. Everything around you is
blurry the only thing you can make out are two containers, on the shelf. The red one says that it will get rid of your headache
but lead to side effects of confusion. The other one doesn't have a label; however, it is still on the shelf labelled pain-killers. 
Which one do you take? 
              _________                       _________
             {_________}                     {_________}       
              )=======(                       )=======(
             /         \                     /         |
            | _________ |                   | _________ |
            ||   RED   ||                   ||  BLUE   ||
            ||  side   ||                   ||         ||
            || effects ||                   ||         ||        
      __    ||         ||                   ||         ||
 __  (_|)   |'---------'|                   |'---------'| 
(_|)        `-.........-'                   `-.........-'

    

""")
choice = str(input("Press r/R to choose the red container. Press b/B to choose the red"))
if choice == "r" or choice == "R":
    red = 1
    print("Your headache is alleviated. BUT remember this may later influence your choices or EVEN YOUR FATE. ")
    stage2part1()
elif choice == "b" or choice == "B":
    blue = 1
    print("""
Your headache is completely alleviated. Behind the container, you find a key card:
     ____________________
    |      EMPLOYEE      |
    |      KEY CARD      |
    |                    |          
    |       .xxxx.       | 
    |      |(o)(o)|      |
    |     (  (__)  )     |
    |       | __ |       | 
    |        \__/        | 
    |                    |            
    |                    |
    |____________________|
    """)
    keyCard = 1

if keyCard == 1:
    print("""
----------------------------------------------------------------------------------------------------------------------------------------
STAGE 3
------------------------------------------------------------------------------------------------------------------------------------------
There are two doors that can be accessed by the key card: 
  ______________           ______________
|\ ___________ /|        |\ ___________ /|       
| |  _ _ _ _  | |        | |  _ _ _ _  | |
| | | | | | | | |        | | | | | | | | |
| | |-+-+-+-| | |        | | |-+-+-+-| | |
| | |-+-+=+%| | |        | | |-+-+=+%| | |                
| | |_|_|_|_| | |        | | |_|_|_|_| | |
| |    ___    | |   __   | |    ___    | |   __
| |   [___] ()| |  |  |  | |   [___] ()| |  |  |
                    --                       --
| |         ||| |        | |         ||| |
| |         ()| |        | |         ()| |
| |           | |        | |           | |
| |           | |        | |           | |
| |           | |        | |           | |
|_|___________|_|        |_|___________|_|
<<<<<<< HEAD

    """)
choice3 = str(input("Press l/L to go through the door to the left. Press r/R to go through the door to the right"))
while lives > 0 and stage3part2:
    if choice3 == "l" or choice3 == "L":
        stage3part2()
        file = str(input())
    if choice3 == "r" or choice3 =="R":
        print("You enter the hall. Beside you see a file. You may see the file for 30 coins. The information may help you later on")
        file = str(input("Choose y/N to see the file"))
    if file == "y" or file == "Y":
        print("combo for exit is 445")
        stage3part2()
        coins = coins - 30
        print("You have this many coins %s" %coins)
    else:
        if file == "n" or file == "N":
            stage3part2()
            pass
=======
 
    """)
choice3 = str(input("Press l/L to go through the door to the left. Press r/R to go through the door to the right"))
if choice3 == "l" or "L":
    print("You enter the hall. Beside you see a file. You may see the file for 30 coins. The information in it will help you later on")
if choice3 == "r" or "R":

    print("""
    Down the hall you see someone. You inspect the surrondings thinking that it is clear and begin to walk down the hall. Suddenly, you
    hear footsteps behind you. You decide to rush into a room to escape them
        """)
>>>>>>> origin/master

print("""
----------------------------------------------------------------------------------------------------------------------------------------
STAGE 4
------------------------------------------------------------------------------------------------------------------------------------------
    """)
print("""
You enter the room and see people all around you 
    """)


"""
Title: Choose your adventure
Author: Chelsea Chen
Date Created: 2020-06-03
"""
import sys
# --- VARIABLES --- #
coins = 100
lives = 3
red = 0
blue = 0
keyCard = 0
running = True
stage1 = True
stage2 = True
# --- SUBROUTINES --- #
def intro():
    print("""
Welcome to Escape your Fate! In this choose your adventure game, you will be given various choices, each of them a deciding factor in if you 
will be able to change your fate. You will have three lives and 100 coins to spend on objects that will help you on your journey. Choose 
accordingly and you might be able to survive! 
------------------------------------------------------------------------------------------------------------------------------------------------
STAGE 1
------------------------------------------------------------------------------------------------------------------------------------------------
    """)

def stage2part1():
    global lives
    global keyCard
    global stage2
    print("""
You walk around the room on the furthest right are two doors. You see two doors. You try the handles they don't open. On the left side
of the door you see a scanner. You decide to search in the two most obvious places first: the shelf, the desk, the file cabinet, and
the bookshelf. Which place do you search first? Each time you guess wrong, you loose a life. 
    - Press s/S to search the shelf with the containers. 
    - Press d/D to search the desk.
    - Press f/F to search the file cabinet. 
    - Press b/B to search the bookshelf         
""")
    while lives > 0 and stage2:
        choice2 = str(input("Put choice here:" ))
        if choice2 == "s" or choice2 == "S":
            print("""
You move the container over on the shelf and find a key card: 
            ____________________
           |      EMPLOYEE      |
           |      KEY CARD      |
           |                    |          
           |       .xxxx.       | 
           |      |(o)(o)|      |
           |     (  (__)  )     |
           |       | __ |       | 
           |        \__/        | 
           |                    |            
           |                    |
           |____________________|
            """)
            keyCard = 1
            stage2 = False
        else:
            print("It is not there. Try searching in another place")
            lives = lives - 1
            print("You have lost one life. You have this many left %s" % lives)
            print("coins= %s" % coins)
    if lives < 0:
        print("""
        Your heart races, you begin to have a panic attack because nothing you are doing is working. You begin to grow faint. You land on 
        the ground with a thud. People start to rush around you. GAME OVER
              """)
        sys.exit



# --- INPUTS --- #
value = input("Press the enter key if you dare!")

# --- Processing --- #
intro()
print("""
You wake up. You aren't able to remember anything except vaguely the words "Experiment 3025- human brain simulation" as you sit on a 
hospital bed your head wired up to a machine, its steady beating creates a pattern "thump, thump, thump thump, thump." Around your right
wrists is a metal bands that restrict your movement, a combination key with a four number solution. You decide try two different combinations,
what four numbers do you input?  
        """)

while stage1 and lives > 0:
    hint1 = input("Press y/N for a hint. It will cost ten coins.")
    if hint1 == "y" or hint1 == "Y":
        print(
            "Observe the pattern of the steady beating. Count the beats to find a combination. Remember there are four numbers and four beats."
        )
        coins = coins - 10
    else:
        pass
    combination = int(input("Enter your combination here: "))
    if combination == 1121:
        print("Your right hand comes loose")
        print("coins= %s" % coins)
        print("lives = %s" % lives)
        stage1 = False
    else:
        lives = lives - 1
        print("You have lost one life. You have this many left %s" % lives)
        print("coins= %s" % coins)
    if lives == 0:
        print("The alarm sounds, causing people to rush into the room to restrain you. You have been caught. GAME OVER")
        sys.exit

print("""
------------------------------------------------------------------------------------------------------------------------------------------------
STAGE 2
----------------------------------------------------------------------------------------------------------------------------------------
As you get up, you rip the wires from your head. All of sudden you feel dizzy and have a terriable headache. Everything around you is
blurry the only thing you can make out are two containers, on the shelf. The red one says that it will get rid of your headache
but lead to side effects of confusion. The other one doesn't have a label; however, it is still on the shelf labelled pain-killers. 
Which one do you take? 
              _________                       _________
             {_________}                     {_________}       
              )=======(                       )=======(
             /         \                     /         |
            | _________ |                   | _________ |
            ||   RED   ||                   ||  BLUE   ||
            ||  side   ||                   ||         ||
            || effects ||                   ||         ||        
      __    ||         ||                   ||         ||
 __  (_|)   |'---------'|                   |'---------'| 
(_|)        `-.........-'                   `-.........-'

    

""")
choice = str(input("Press r/R to choose the red container. Press b/B to choose the red"))
if choice == "r" or choice == "R":
    red = 1
    print("Your headache is alleviated. BUT remember this may later influence your choices or EVEN YOUR FATE. ")
    stage2part1()
elif choice == "b" or choice == "B":
    blue = 1
    print("""
Your headache is completely alleviated. Behind the container, you find a key card:
     ____________________
    |      EMPLOYEE      |
    |      KEY CARD      |
    |                    |          
    |       .xxxx.       | 
    |      |(o)(o)|      |
    |     (  (__)  )     |
    |       | __ |       | 
    |        \__/        | 
    |                    |            
    |                    |
    |____________________|
    """)
    keyCard = 1

if keyCard == 1:
    print("""
----------------------------------------------------------------------------------------------------------------------------------------
STAGE 3
------------------------------------------------------------------------------------------------------------------------------------------
There are two doors that can be accessed by the key card: 
  ______________           ______________
|\ ___________ /|        |\ ___________ /|       
| |  _ _ _ _  | |        | |  _ _ _ _  | |
| | | | | | | | |        | | | | | | | | |
| | |-+-+-+-| | |        | | |-+-+-+-| | |
| | |-+-+=+%| | |        | | |-+-+=+%| | |                
| | |_|_|_|_| | |        | | |_|_|_|_| | |
| |    ___    | |   __   | |    ___    | |   __
| |   [___] ()| |  |  |  | |   [___] ()| |  |  |
                    --                       --
| |         ||| |        | |         ||| |
| |         ()| |        | |         ()| |
| |           | |        | |           | |
| |           | |        | |           | |
| |           | |        | |           | |
|_|___________|_|        |_|___________|_|
 
    """)
choice3 = str(input("Press l/L to go through the door to the left. Press r/R to go through the door to the right"))
if choice3 == "l" or "L":
    print("You enter the hall. Beside you see a file. You may see the file for 30 coins. The information in it will help you later on")
if choice3 == "r" or "R":

    print("""
    Down the hall you see someone. You inspect the surrondings thinking that it is clear and begin to walk down the hall. Suddenly, you
    hear footsteps behind you. You decide to rush into a room to escape them
        """)


# --- OUTPUTS --- #
