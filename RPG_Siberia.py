# import statements
import random
import time
import math
from tkinter import *
import tkinter.simpledialog as simpledialog
import tkinter.messagebox as messagebox

# Create a window
root = Tk()
w = Label(root, text="Indev")
w.pack()

# initialize variables
HP = 10
speed = 5
XP = 0
total_XP = 0
rifle_ammo = 5
spaces = 1

item1 = "Slice of Bread"
item2 = "Nutella"
item3 = "Empty"

bag1 = "Empty"
bag2 = "Empty"
bag3 = "Empty"

name = "Brad Rukovich"

# Define functions
def Deposit():
    global spaces
    messagebox.showinfo("Deposit","You deposited " + deposit + ".")
    spaces -= 1
def Withdraw():
    global spaces
    messagebox.showinfo("Withdraw","You withdrew " + withdraw + ".")
    spaces += 1

# Intro Text
messagebox.showinfo("Start","You are a hunter in the vast Siberian tundra.")
messagebox.showinfo("Start","Your family raised you to become an independent, self\n"
                    "serving man. Although your family is long gone, you learn to\n"
                    "live on without them.")
messagebox.showinfo("Start","Your primary purpose is to survive.")
time.sleep(1)
messagebox.showinfo("Start","Your current hunting party consists of 3 experienced\n"
                    "poachers. You count on eachother for survival. Living with\n"
                    "these hunters, you realize it's nice to have people that have\n"
                    "your back.")
messagebox.showinfo("Start","However, the struggle to live is not at all non-existent.")
messagebox.showinfo("Hunt","Your party has not had much luck in finding food in the\n"
                    "past week, and as a last resort your group sets out at noon to\n"
                    "search for elk.")
messagebox.showinfo("Hunt","You are hungrier and more food deprived than any of the\n"
                    "other group members. You tag along with the others, slightly\n"
                    "falling behind.")
time.sleep(2)
messagebox.showinfo("Prey","You strut along, being way behind the others. Out of\n"
                    "fatigue, your left leg drags on the snow, making a long trail\n"
                    "behind you.")
messagebox.showinfo("Prey","You hear a piercing roar in the direction you are facing.\n"
                    "You make an effort to hurry forward, although every step feels\n"
                    "like a mile.")
time.sleep(1.5)
messagebox.showinfo("Prey","You finally make out your hunting mates in the distance.\n"
                    "However, you see their shocked expressions on their faces. One\n"
                    "of them opens fire on something you can’t make out yet.")
messagebox.showinfo("Prey","As you observe, you make something out in your field of\n"
                    "vision. Looking to your left, you see a creature making its way\n"
                    "towards you. You see it is alone.")
# Fight Scene 1
while XP == 0:
    choice = simpledialog.askstring("Fight","Enemy: Siberian Tiger\n"
                           "    Hitpoints: 25\n   Damage: 20\n   Speed: 30\n\n"
                           "YOU:\n   Hitpoints: 10\n   Speed: 5\n\n"
                           "What will you do?\nType R to run, and F to Fight.")
    while choice == "F" or choice == "f":
        weapon = simpledialog.askstring("Pick Weapon","Which weapon would you like to use?\n\n"
                                        "(K)nife [Damage:  3]\n"
                                        "(R)ifle [Damage: 10] [Ammunition: " + str(rifle_ammo) + "] [Critical Modifier: 3]")
        if weapon == "R" or weapon == "r":
            time.sleep(.5)
            XP = random.randint(10,25)
            total_XP = total_XP + XP
            rifle_ammo -= 1 
            messagebox.showinfo("Fight","You fumble with the rifle a little, the tiger\n"
                                "covering a large amount of land between itself and your\n"
                                "position. You manage to take aim and fire at the tiger\n"
                                "seconds before it gets to you.")
            messagebox.showinfo("Critical","Luckily, you strike it between the eyes. It's a headshot.\n"
                                "The tiger stops in its tracks and becomes lifeless in moments.")
            messagebox.showinfo("Victory","You gain " + str(XP) + " XP, and you now have a\n"
                                "total of " + str(total_XP) + " XP.")
            break
        else:
            messagebox.showinfo("Select another weapon","The tiger has not caught up to you yet.\n"
                                "Recommend you pull out your rifle...")
    if choice == "R" or choice == "r":
        time.sleep(.5)
        messagebox.showinfo("Death","The tiger catches up to you. It pounces on you and\n"
                            "rips out your jugular. You die in seconds. Advice: ..\n"
                            "Never run from a Siberian tiger...")
        root.destroy()
    if choice != "F" and choice != "f":
        messagebox.showinfo("Error","Please make an appropriate selection.")
time.sleep(.25)

# Text
messagebox.showinfo("Prey","Your encounter with the tiger now over, you regain awareness\n"
                    "of your hunting party. However, the condition you see them in is more\n"
                    "than startling.")
messagebox.showinfo("Prey","You see six Siberian Tigers eating away at the carcasses of your\n"
                    "group members. Some tigers lie dead on the ground. You realize the\n"
                    "pack of tigers was more than enough to overwhelm the hunting party.\n"
                    "It would be foolish to resist the tigers now.")
messagebox.showinfo("Prey","You decide to retreat from the scene, being careful to not attract\n"
                    "any attention.")
time.sleep(.5)
messagebox.showinfo("Prey","Luck strikes you twice. The tigers, preoccupied with finishing their\n"
                    "meal, do not face their heads in your direction.")
messagebox.showinfo("Prey","However, you see one tiger smelling the air, like it has picked up a\n"
                    "scent. It lets out a small roar, and returns back to the pack.")
time.sleep(1)
messagebox.showinfo("Descent","You're walking through the forest, finding your way only through\n"
                    "the sun's position. The sun hangs low in the sky.")
messagebox.showinfo("Descent","The trauma of the accident that occured has your brain sending you\n"
                    "off in many directions. You have no idea what to do.")
messagebox.showinfo("Descent","The sun sets. Night falls over the land.")
messagebox.showinfo("Descent","You aimlessly walk through the woods, not knowing what you might\n"
                    "stumble upon.")
time.sleep(.25)
messagebox.showinfo("Descent","You fall on something rock hard. You lift your face off the snow\n"
                    "and wonder what you tripped over.")

# Experimenting an Intelligence System
choice = simpledialog.askstring("Descent","Observe the object? (Y or N)")
if choice == "Y" or choice == "y":
    messagebox.showinfo("Lock","You scrape off the snow and dirt off the object. It looks rough\n"
                        "at first, but as you make progress uncovering it, it starts to take a\n"
                        "rectangular shape.")
    time.sleep(.5)
    messagebox.showinfo("Lock","You discover that the object you found was a locked container.\n"
                        "It requires a number combination to open up.")
    number = random.randint(20,50)
    combo = 1995 + number
    while combo == 1995 + number:
        choice = simpledialog.askstring("Lock","(E)xamine the object closer\n"
                               "(U)nlock the combination")
        if choice == "U" or choice == "u":
            messagebox.showinfo("Lock","Starting up interface...")
            messagebox.showinfo("Lock","1995 Wesley Security System\n"
                                "Copyright Wesley Inc. 1993")
            user_combo = simpledialog.askstring("Lock","Enter number:\n[ ][ ][ ][ ]")
            
            digit1 = user_combo[0]
            digit2 = user_combo[1]
            digit3 = user_combo[2]
            digit4 = user_combo[3]
            
            messagebox.showinfo("Lock","Confirm\n  [ " + digit1 + " ] [ " + digit2 + " ] [ " + digit3 + " ] [ " + digit4 + " ]")
            if int(user_combo) == int(combo):
                choice2 = "W"
                while choice2 != "E":
                    choice2 = simpledialog.askstring("Open","=== Welcome, " + name + " ===\n"
                                        "   (W)ithdraw Item\n"
                                        "   (D)eposit Item\n"
                                        "   (C)hange Name\n"
                                        "   (Ch)eck your Bag\n"
                                        "   (E)xit System")
                    if choice2 == "W":
                        withdraw = simpledialog.askstring("Withdraw","List of things you can withdraw:\n\n" + item1 + "\n" + item2 + "\n" + item3 + "\nWhat would you like to take?")
                        if withdraw == "Empty":
                            messagebox.showinfo("Error","You can't withdraw from an empty slot.")
                            withdraw = ""
                        if withdraw == item1:
                            Withdraw()
                            item1 = "Empty"
                            bag1 = withdraw
                        elif withdraw == item2:
                            Withdraw()
                            item2 = "Empty"
                            bag2 = withdraw
                        elif withdraw == item3:
                            Withdraw()
                            item3 = "Empty"
                            bag3 = withdraw
                        else:
                            messagebox.showinfo("Withdraw","You didn't withdraw anything.")
                    elif choice2 == "D":
                        if spaces > 0:
                            deposit = simpledialog.askstring("Deposit","There are " + str(spaces) + " spaces in the\n"
                                                   "container to store items. What would you like to deposit?")
                            if deposit == bag1:
                                Deposit()
                                bag1 = "Empty"
                                item1 = deposit
                            elif deposit == bag2:
                                Deposit()
                                bag2 = "Empty"
                                item2 = deposit
                            elif deposit == bag3:
                                Deposit()
                                bag3 = "Empty"
                                item3 = deposit
                            else:
                                messagebox.showinfo("Withdraw","You dont have a " + deposit + "...")
                        else:
                            messagebox.showinfo("Error","The container is full.")
                    elif choice2 == "C":
                        messagebox.showinfo("Name","Name change request sent... ... ...")
                        time.sleep(2)
                        messagebox.showinfo("Name","Unable to connect to network. Temporary name change activated.")
                        name = simpledialog.askstring("Name","What would you like to change your name to?")
                        messagebox.showinfo("Name","Your name has been changed to " + name + ".")
                    elif choice2 == "E":
                        messagebox.showinfo("Shutdown","Goodbye, " + name + "!\nShutting off system...")
                    elif choice2 == "Ch":
                        messagebox.showinfo("Bag","Items in your Bag:\n\n" + bag1 + "\n" + bag2 + "\n" + bag3 + "")       
                    else:
                        messagebox.showinfo("Error","Please make an appropriate selection.")
                break
            else:
                messagebox.showinfo("Lock","Incorrect combination. Shutting off system...")
                time.sleep(.5)
        elif choice == "E" or choice == "e":
            messagebox.showinfo("Lock","You see something written in Russian,\n"
                                "barely legible, but you can make out the broken\n"
                                "text:")
            messagebox.showinfo("Lock","Сочетание равна год производство плюс " + str(number) + "")
    messagebox.showinfo("Progress","You store the container in your bag.")
    bag3 = "Security Container"

# Eat up
if bag1 == "Slice of Bread" and bag2 == "Nutella":
    messagebox.showinfo("Eat","You feel the strongest urge to satisfy your appetite.\n"
                        "With both a " + bag1 + " and " + bag2 + ", you decide to\n"
                        "eat in fashion, and make a Nutella sandwich. You finish it in seconds.")
    bag1 = "Empty"
    bag2 = "Nutella Container"
    speed += 10
    messagebox.showinfo("Speed","Your speed increases by 10.")
elif bag1 == "Slice of Bread":
    messagebox.showinfo("Eat","You feel the strongest urge to satisfy your appetite.\n"
                        "You pull out the " + bag1 + " and finish it in seconds.")
    bag1 = "Empty"
    speed += 5
    messagebox.showinfo("Speed","Your speed increases by 5.")
elif bag2 == "Nutella":
    messagebox.showinfo("Eat","You feel the strongest urge to satisfy your appetite.\n"
                        "You pull out the " + bag2 + " and finish it in seconds.")
    speed += 7
    messagebox.showinfo("Speed","Your speed increases by 7.")
    bag2 = "Nutella Container"
messagebox.showinfo("End","Demo version over. Insert 50 coins to continue...")

# Destroy Window
root.destroy()
                                       
#WORK IN PROGRESS
