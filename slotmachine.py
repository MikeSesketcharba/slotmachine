import random
import time
# termcolor module by vaultboy https://pypi.org/project/termcolor/
from termcolor import colored

# chances:
nothing = 0.0
# between nothing and cherry should be nothing
cherry = 0.125
# between cherry and bell should be cherry
bell = 0.25
# between bell and bar should be bar
bar = 0.375
# between bar and seven is bar
seven = 0.5
# between seven and lemon should be seven
lemon = 0.625
# between lemon and grape should be grape
grape = 0.75
# between grape and orange should be orange
orange = 0.875
# between orange and 1 should be orange

totalchips = 100
insertedchips = "0"
wait = 2

# Inspirational messages:
double = "You win two times your bet!"
fifth = "You win five times your bet!"
tenfold = "You win ten times your bet!"
twenty = "You win twenty times your bet!"
thirty = "You win thirty times your bet!"
forty = "You win forty times your bet!"
sixty = "You win sixty times your bet!"
houndred = "Jackpot! You win a houndred times your bet! Congratulations!"

def insertbets():
    global insertedchips
    global totalchips

    print("You have a a total of " + str(totalchips) + " chips.")
    print("You can bet a maximum of 40 chips.")
    print("\nInsert the number of chips you'd like to bet.")

    insertedchips = input()
    while insertedchips.isnumeric() == False:
            print("Please insert a valid input.")
            insertedchips = input()

    insertedchips = int(insertedchips)
    if insertedchips > totalchips:
        insertedchips = totalchips
    if insertedchips > 40:
        insertedchips = 40

    totalchips = totalchips - insertedchips

def cls():
    for i in range(50):
        print("\n" * i)

def spinthewheel():
    chance = random.random()
    result = ""
    if chance >= nothing and chance < cherry:
        print("A misaligned wheel.")
        result = "nothing"

    if chance >= cherry and chance < bell:
        print("A cherry.")
        result = "cherry"

    if chance >= bell and chance < bar:
        print("A bell.")
        result = "bell"

    if chance >= bar and chance < seven:
        print("A bar.")
        result = "bar"

    if chance >= seven and chance < lemon:
        print("A seven.")
        result = "seven"

    if chance >= lemon and chance < grape:
        print("A lemon.")
        result = "lemon"

    if chance >= grape and chance < orange:
        print("A grape.")
        result = "grape"

    if chance >= orange and chance < 1:
        print("An orange.")
        result = "orange"

    return result

def columnevaluation():
    global totalchips
    global insertedchips

# CHERRIES
    win = False

    if column1 == "cherry" and column2 == "cherry" and column3 == "cherry":
        print(tenfold)
        win = True
        totalchips = totalchips + insertedchips * 10
    elif column1 == "cherry" and column2 == "cherry" or column2 == "cherry" and column3 == "cherry" or column3 == "cherry" and column1 == "cherry":
        print(fifth)
        win = True
        totalchips = totalchips + insertedchips * 5
    else:
        if column1 == "cherry" or column2 == "cherry" or column3 == "cherry":
            print(double)
            win = True
            totalchips = totalchips + insertedchips * 2

# BELLS
    if column1 == "bell" and column2 == "bell" and column3 == "bell":
        print(tenfold)
        win = True
        totalchips = totalchips + insertedchips * 10

# BARS
    if column1 == "bar" and column2 == "bar" and column3 == "bar":
        print(twenty)
        win = True
        totalchips = totalchips + insertedchips * 20

# SEVENS
    if column1 == "seven" and column2 == "seven" and column3 == "seven":
        print(thirty)
        win = True
        totalchips = totalchips + insertedchips * 30

# LEMONS
    if column1 == "lemon" and column2 == "lemon" and column3 == "lemon":
        print(forty)
        win = True
        totalchips = totalchips + insertedchips * 40

# GRAPES
    if column1 == "grape" and column2 == "grape" and column3 == "grape":
        print(sixty)
        win = True
        totalchips = totalchips + insertedchips * 60

# ORANGES
    if column1 == "orange" and column2 == "orange" and column3 == "orange":
        print(houndred)
        win = True
        totalchips = totalchips + insertedchips * 100

# NOTHING
    if win == False:
        print("You win nothing.")

def help():
    print("""The payout goes like this:
        -Any single cherry in any wheel doubles your bet.
        -Two cherries in any wheel quintuples your bet.
        -Three cherries tenfolds your bet.
        -Three bells tenfold your bet.
        -Three bars makes you recieve twenty times your bet.
        -Three sevens makes you recieve thirty times your bet.
        -Three lemons makes you recieve forty times your bet.
        -Three grapes makes you recieve sixty times your bet.
        -Three oranges makes you recieve a houndred times your bet: the ultimate jackopt.

You may also have noticed that the wheel misalignes. You are actually playing a recreation of a vintage slot machine,
and vintage slot machines could have their wheels not fully align with the rest of symbols, making the user
lose a turn in most scenarios. This probable mistake was seen as a feature and a risk in casinos, back in the day!

Continue? Y/N""")

playagain = "yes"
moremoney = "yes"

while playagain.startswith("y") == True:
    cls()
# bet insertion
    insertbets()
    cls()
# spinning
    print("On the first column you've got...")
    time.sleep(wait)
    column1 = spinthewheel()
    print("\nOn the second column you've got...")
    time.sleep(wait)
    column2 = spinthewheel()
    print("\nOn the third column you've got...")
    time.sleep(wait)
    column3 = spinthewheel()
    print()
# display results
    columnevaluation()
# you lost
    if totalchips <= 0:
        print(colored("\nYou lost all your chips! Do you want to try again? Y/N", "red"))
        moremoney = input()
        moremoney = moremoney.lower()
        if moremoney.startswith("y") == False:
            totalchips = 100
        else:
            break
    if moremoney.startswith("y") == False:
        break

    print("\nWanna play again? (Y/N or H for instructions and payout multipliers)")
    playagain = input()
    playagain = playagain.lower()

    if playagain.startswith("h") == True:
        cls()
        help()
        playagain = input()
        playagain = playagain.lower()
