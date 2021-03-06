"""
Title: Choose your adventure
Author: Chelsea Chen
Date Created: 2020-06-03
"""
import sys
# --- VARIABLES --- #
coins = 80
lives = 3
red = 0
blue = 0
keyCard = 0
running = True
stage1 = True
stage2 = True
stage3part2 = False
stage3part3 = True
stage4part2 = True
again = True
score = 0
stage3 = False

# --- SUBROUTINES --- #
def intro():
    print("""
Welcome to Escape your Fate! In this choose your adventure game, you will be given various choices, each of them a deciding factor in if you 
will be able to change your fate. You will have three lives and 80 coins to spend on things that will help you on your journey. Every stage
you pass you will be able to gain 5 points for your final score. Choose accordingly and you might be able to survive! 
------------------------------------------------------------------------------------------------------------------------------------------------
STAGE 1
------------------------------------------------------------------------------------------------------------------------------------------------
    """)

# file for stage 4
def file():
    global choice4
    global file
    print(
        "You enter the hall. Beside you see a file. You may see the file for 30 coins. The information in it will help you later on")
    file = str(input("Press y/Y to open file. Press n/N to not open the file"))
    stage3part2 = True
    if file == "y" or file == "Y":
        print("The combination is 3025")
    else:
        if file == "n" or file == "N":
            pass
#Stage 1
def stage1():
    global lives
    global coins
    global stage1
    global score
    print("""
You wake up. You aren't able to remember anything except vaguely the words "Experiment 3025- human brain simulation." As you sit on a 
hospital bed, you see that your head is connected to a machine, its steady beating creates a pattern "thump, thump, thump thump, thump." Around your right
wrists is a metal band that restrict your movement that needs a combination with a four number solution to unlock it. You decide try two different combinations,
What four numbers do you input?  
            """)

    while stage1 and lives > 0:
        # ask for hint (input)
        hint1 = input("Press y/N for a hint. It will cost ten coins.")
        if hint1 == "y" or hint1 == "Y":
            print( "Observe the pattern of the steady beating. Count the beats to find a combination. Remember there are four numbers and four beats."
            )
            coins = coins - 10
        else:
            pass
        # check combination
        combination = int(input("Enter your combination here: "))
        #processing
        if combination == 1121: #input 1121 to move on
            print("Your right hand comes loose")
            print("coins= %s" % coins)
            print("lives = %s" % lives)
            print("score = %s" % score)
            stage1 = False
        else:
            lives = lives - 1
            print("You have lost one life. You have this many left %s" % lives)
            print("coins= %s" % coins)
        if lives == 0:
            print( "The alarm sounds, causing people to rush into the room to restrain you. You have been caught. GAME OVER")
            print("You have been able to score %s points" % score)
            sys.exit()
#Stage 2
def stage2part1():
    global keyCard
    global stage3
    print("""
------------------------------------------------------------------------------------------------------------------------------------------------
STAGE 2
----------------------------------------------------------------------------------------------------------------------------------------
As you get up, you rip the wires from your head. All of sudden you feel dizzy and have a terriable headache. Everything around you is
blurry. The only thing you can make out are two containers on the shelf. The red one says that it will get rid of your headache
but will lead to side effects of confusion. The other one doesn't have a label; however, it is still on the shelf labelled pain-killers. 
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
    #choose container
    choice = str(input("Press r/R to choose the red container. Press b/B to choose the blue"))
    if choice == "r" or choice == "R":
        red = 1
        print("Your headache is alleviated. BUT remember this may later influence your choices or EVEN YOUR FATE. ")
        stage2part2()
    elif choice == "b" or choice == "B":
        blue = 1
        stage3 = True
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
def stage2part2():
    global lives
    global keyCard
    global stage2
    global stage3
    # finding key card
# if chose the red container
    print("""
You walk around the room and on the furthest right are two doors. You try the handles. They don't open. On the left side
of the door you see a scanner. You decide to search in the two most obvious places first: the shelf, the desk, the file cabinet, and
the bookshelf. Which place do you search first? Each time you guess wrong, you loose a life. 
    - Press s/S to search the shelf with the containers. 
    - Press d/D to search the desk.
    - Press f/F to search the file cabinet. 
    - Press b/B to search the bookshelf         
""")
    # shelf is chosen and key card is found
    while lives > 0 and stage2:
        choice2 = str(input("Put choice here:" ))
    #input s to move on
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
            stage3 = True
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
        sys.exit()
#Stage 3
def stage3part1():
    global stage2
    if stage3:
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
    #here is where extra information and subroutines for stage 3 start
def stage3part2():
    global choice4
    global stage3part3
    global lives
    global score
    print("""
Down the hall you see someone. You inspect the surroundings thinking that it is clear and begin to walk down the hall. Suddenly, you
hear footsteps behind you. You decide to rush into a room to escape them. You can either enter room 213 or 215:

     ______________                  ______________
    |\ ___________ /|               |\ ___________ /|
    | |  _ _ _ _  | |               | |  _ _ _ _  | |
    | | | | | | | | |               | | | | | | | | |
    | | |-+-+-+-| | |               | | |-+-+-+-| | |
    | | |-+-+=+%| | |   213         | | |-+-+=+%| | |    215
    | | |_|_|_|_| | |               | | |_|_|_|_| | |
    | |    ___    | |               | |    ___    | |
    | |   [___] ()| |               | |   [___] ()| |
    | |         ||| |               | |         ||| |
    | |         ()| |               | |         ()| |
    | |           | |               | |           | |
    | |           | |               | |           | |
    | |           | |               | |           | |
    |_|___________|_|               |_|___________|_| 
        """)
    # choosing rooms
    #choosing 213
    choice4 = int(input("To enter room 213, press 213. To enter room 215, press 215"))
    if choice4 == 213:
        print("""
When you walk into the room you see people in lab coats discussing at an table. They see you and grab your arm. Suddenly, your vision
goes black 
        """)
        lives = lives - 1
        print("You have lost a life. This is how many you have left %s" % lives)
#Stage 4
def stage4part1():
    global stage3part3
    global choice5
    print("""
------------------------------------------------------------------------------------------------------------------------------------------
STAGE 4
------------------------------------------------------------------------------------------------------------------------------------------
            """)
    stage3part3 = False
    print(""" 
You enter a room and around you are people on beds hooked up to the same machines you were connected to. 
Again you see the words "Experiment 3025 -human brain simulator". In the corner, you see a small child on a bed who is 
trembling in fear as their eyes search the celling as though disconnected from reality. Suddenly, you resonate
with that hopelessness as you remember how scared you felt when you woke up. You begin to debate whether or not to wake up the child. 
You walk closer and they look pale. Around their wrist is a metal band with a combination:

          ()- _ `._.--.
        ((0_. (  )  )  \_    _.-.-._
     -- ((0   .' /  (\   \`--'  _)--=' ------ .
   '       -' _ - ._)_\   \.-.-._.             .
  '    ''`````\        \  .  _)--='             .
 '-----------\/'-. ---- `--"'-------------------.
|             |\\                                |
|                                                |
 `----------------------------------------a:f---'
        [_]                               [_]
            """)
    choice5 = str(input( "Press y/Y to release them from the machine and save them from their nightmare. Press n/N to leave them as you fear they might scream or alert the officials: "))
#stage 4 and 5 version 1
def stage4part2():
    global score
    global coins
    global lives
    global again
    global stage4part2
    print("Around their wrist is a metal band needing a 4 number combination")
    # input combo
    while lives > 0 and stage4part2:
        print("Enter the combo you found earlier in the map. If you did not find this combo, you may purchase a hint for 30 coins.")
        hint = str(input("Press y/N to buy the hint"))
        if hint == "y" or hint == "Y":
            print("Remember the experiment name")
            coins = coins - 30
            print("You have this many coins left: %s" % coins)
        else:
            pass
        combo = int(input("Enter Combo here: "))
    # combo is 3025
        if combo == 3025:
            print("""
The child is released. You pull the equipment from their head. Their eyes slowly gain consciousness of reality.
A shocked expression spreads across their face and it soon shifts to worry. They tell you have to leave right now, explaining how
if they find you it will lead to a fate worse than death. All of a sudden, you hear a sound.
                        """)
            stage4part2 = False
            print("lives = %s" % lives)
            print("coins = %s" % coins)
            print("score = %s" % score)
        else:
            lives = lives - 1
            print("You have lost a life. This is how many you have left %s"%lives)
    print("""
---------------------------------------------------------------------------------------------------------------------------------------
STAGE 5 
---------------------------------------------------------------------------------------------------------------------------------------
        """)
    while lives > 0 and again:
        #finding place to hide
        print("""
You search for a place to hide. You spot 2 different places. Under one of the beds or behind the shelf.
                                        _____________
                                       /____________/|
_____ /|________/| ____________________|     o     | |_______________________________________________
     // /      //|                     |___________| |
    |/_/______|//!                     |           | |
    |_________|/                       |     o     | |
    !         !                        |___________|/
    
_______________________________________________________________________________________________________
""")

        choice10 = str(input("Press b/B to hide under the bed. Press s/S to hide behind the shelf"))
        if choice10 == "b" or choice10 == "B":
            print("You run under the bed. Someone enters the room. You wait under the bed until you hear their footsteps subside. ")
            again = False
        else:
            #shelf
            if choice10 == "s" or choice10 == "S":
                print("""
You run to hide behind the shelf. A person enters the room checking on the people on the beds. They begin to near the shelf you
hide behind. They spot you and you try to get away, but it is useless as they grab you and drag you away.
                    """)
                lives = lives - 1
                print("You have lost a life. You have this many left %s" %lives)
    if (choice10 == "s" or choice10 == "S") and again and lives < 0:
            print("GAMEOVER")
            sys.exit()
#ending of stage 5 version 2
    if lives > 0:
        print("""
When they finally leave, you get up and ask the child to leave with you. They reluctantly agree. You guys wait 20 seconds
before exiting the room. When you guys walk down the hallway, you guys are able to find a stairway. You walk down the stairway and 
find a door: 
     ______________
    |\ ___________ /|
    | |  _ _ _ _  | |
    | | | | | | | | |
    | | |-+-+-+-| | |
    | | |-+-+=+%| | |
    | | |_|_|_|_| | |
    | |    ___    | |
    | |   [___] ()| |
    
    | |         ||| |
    | |         ()| |
    | |           | |
    | |           | |
    | |           | |
    |_|___________|_| 
        """)
        enter = input("Press enter to open the door:")
        if enter == "":
            print("Behind the door, you find a button. ")
            print("""
               __-------------------__
             _/                        \_
            /                            |
           /        PRESS TO RETURN       |
           |          TO REALITY          |
           |                              |
             \_                         /
               \______________________/
               
            """)
            choice12 = str(input("Press Y/y to return to reality"))
            if choice12 == "Y" or choice12 == "y":
                print("""
You press the button and suddenly everything goes black. When you open your eyes, you see you are surrounded by people
in white lab coats. Beside you is a lady writing information down on a clipboard, her mouth forms the words:
        
        "Congratulations, you have successfully completed the experiment and helped out others even if there was a risk" 
        
                """)

#Stage 5 version 2
def stage5part1():
    global lives
    global coins
    global score
    print("lives = %s" % lives)
    print("coins = %s" % coins)
    print("score = %s" % score)
    print("""
---------------------------------------------------------------------------------------------------------------------------------------
STAGE 5
---------------------------------------------------------------------------------------------------------------------------------------
    """)
    print("""
Quickly you walk around the room searching around for an exit out of the room. In the corner, you see a box of surgical tools. 
You walk towards it and decide to open it in case you might need anything from it later. You open open the box and you see a scalpel
and a syringe full of some sort of substance. Which one will you choose.
    """)
    #choose tool
    choice6 = int(input("Press 1 to choose the scalpel and 2 to choose the syringe"))
    if choice6 == 1:
        print("you pick up the scalpel and all of a sudden hear a sound")
    elif choice6 == 2:
        print("you pick up the syringe and all of sudden you hear a sound")
    print("""
A person walks into the room heading towards the computer. They pull up an image of a map on the screen:
     _______________________________________________
    |                          |                    |
    |                 |        |            216     |
    |       215       |        |_________           |
    |          _______|                  |          |  
    |         |     ______________       |          |
    |_________|    |              |      |__________|
    | window       |      214     |                 |      
    | -------|------              |                 |             
    | 213    |                    |      stairs     |          
    |________|____________________|_________________|
    """)
    print("""
They leave the room. You decide wait 20 seconds. When you can hear no sounds, you sneak out. You look around remember the exits you saw
on the map. Which exit do you take press W for window and press S for stairs.
          """)
def stage5part2():
    global score
    global lives
    print("""
You walk to the window and look down seeing nothing but darkness below. Behind you you hear foot steps, you have your item in your hand.
Do you jump or do you take your chances and turn around and try to fight with the person behind you? 
                              """)
    #choose action
    while lives > 0:
        choice8 = int(input("Press 1 to jump and 2 to fight: "))
        #Stage 5 version 2 ending (winning)
        if choice8 == 1:
            print("""
You wake up. You hear beeping all around you as you wake up a deep chilling feeling in your belly. You see people
writing on clipboards around you. A person in a white coat smiles her mouth forming the words:

     "Welcome Back, you have successful completed the expirement. You have shown a sense of fearlessness into entering the unknown " """)

            print("Congratulations you have finished the game! ")
            score = score + 5
            break
        # Stage 5 version 2 ending- attack (loosing)
        if choice8 == 2:
            print("""
You grab the scalpel and swing it in front of you. It punctures the person approaching in a white lab coat
however it doesn't keep them grabbing you and injecting something in your neck. You vision goes black.
            """)
            lives = lives - 1
        if lives > 0:
            print("You have lost a life. You have this many lives %s" % lives)
        else:
            print("GAME OVER")


def stage5part3():
    global coins
    global lives
    global score
    print("""
You walk down the hallway and reach the stairs. You may buy a life for 30 coins at this point.
    """)
    # buying a life
    getlives = str(input("Do you want to buy a life? y/N"))
    if (getlives == "y" or getlives == "Y") and coins > 30:
        lives = lives + 1
        print("You have this many coins %s"%coins)
        print("You have this many lives %s" % lives)
    else:
        print("You did not purchase a life or have enough coins to purchase a life")
    print("You walk down the stairs and reach a long corridor at the end of the corridor is a door:")
    print("""
  ______________
|\ ___________ /|
| |  _ _ _ _  | |
| | | | | | | | |
| | |-+-+-+-| | |
| | |-+-+=+%| | |
| | |_|_|_|_| | |
| |    ___    | |
| |   [___] ()| |

| |         ||| |
| |         ()| |
| |           | |
| |           | |
| |           | |
|_|___________|_| 
    """)
    print("""Y
You open the door. In front of you is the same child you left behind in the other room. Behind you is a screen:
    _______________________________________________________
    |                                                     |
    |                                                     |
    |                                                     |
    |          FINAL STAGE OF EXPERIMENT 3025             |
    |  You have a choice sacrifice yourself or the child  |
    |                  Choose Wisely                      |
    |                                                     |
    |                                                     |
    |                                                     |
    |                                                     |
    |_____________________________________________________|
          """)
    print("In your hands, you have the item you picked up earlier. Do you sacrifice yourself or the child? Your lives here no longer apply")
    while lives > 0:
        choice9 = int(input("Press 1 to sacrifice yourself. Press 2 to sacrifice the child"))
        #Stage 5 version 2 ending (winning)
        if choice9 == 1:
            print("""
You pierce your skin. Suddenly everything goes black. When you open your eyes, you see that you are on a bed. Around you are people
dressed in white coats taking notes. Beside you, you see a women smiling as her mouth forms the words.

            "Congratulations you have successful completed the experiment. You have been able to demonstrate virtues of selflessness
            and intelligence" 
            
You have finished the game 
            """)
            score = score + 5
            break
        # Stage 5 version 2 ending-sacrifice (losing)
        elif choice9 == 2:
            print("""
You decide to sacrifice the child. Suddenly your vision goes black. When you open your eyes, you see that you are in bed. Around you 
are people dressed in white coats with disapproving looks on their faces. Beside you, you see a women with tight lipped frown as she 
sighs. She grabs a syringe from beside her and injects it into you. Before you can process, it has entered your system. You feel faint
as your eyes close once again. You have failed the experiment 
            """)
            break
            sys.exit
        if lives < 0:
            print("GAME OVER. You have been unsucessful")
            sys.exit


# --- INPUTS --- #
value = input("Press the enter key if you dare!")
#more inputs within subroutines

# --- PROCESSING / OUTPUTS --- #
"""
solution: to get past stage 1 the combination is 1121
solution: to get past stage 2 if you chose the red container choose to search the shelf
solution: to get past stage 3 enter the room 215
solution: to get past stage 4 if you chose yes, the combination is 3025
solution: to get past stage 5 if you chose no and went threw the window, jump to finish
solution: to get past stage 5 if you chose no and went down the stairs, chose to sacrfice yourself to finish 
solution: to get past stage 5 if you chose yes to freeing the child, hide under the bed

"""
intro()
#Press enter to initiate stages

# Stage 1
start1 = input("Press Enter to start stage 1:")
if start1 == "":
    score = score + 5
    stage1()
else:
    sys.exit()

# Stage 2
start2 = input("Press Enter to start stage 2:")
if start2 == "":
    score = score + 5
    stage2part1()
    print("lives = %s" % lives)
    print("coins = %s" % coins)
    print("score = %s" % score)
else:
    sys.exit()

# Stage 3
if stage3 == True:
    stage3part1()
    score = score + 5

#stage3 use of specific subroutine * put a comment where this would fit in
if keyCard == 1:
    choice3 = str(input("Press l/L to go through the door to the left. Press r/R to go through the door to the right"))
    if choice3 == "l" or choice3 == "L":
        file()
        stage3part3 = True
    else:
        pass
# STAGE 3, STAGE 4, and STAGE 5 use of specific subroutines
while stage3part3 and lives > 0:
    stage3part2()
    # Enter 215 to move on
    if choice4 == 215:
        print("lives = %s" % lives)
        print("coins = %s" % coins)
        print("score = %s" % score)
        score = score + 5
    #Stage 4
        stage4part1()
        if choice5 == "y" or choice5 == "Y":
            stage4part2()
            score = score + 5
            print("lives = %s" % lives)
            print("coins = %s" % coins)
            print("score = %s" % score)
        else:
    #Stage5
            stage5part1()
            choice7 = str(input())
            if choice7 == "W" or choice7 == "w":
                stage5part2()
            elif choice7 =="S" or choice7 =="s":
                stage5part3()



print("You have been able to score %s points" %score)
#more outputs and processing within subroutine