#!/usr/bin/env python3
"""Adventure Eater - My mini project"""
import pyfiglet
pyfiglet.print_figlet("Adventure   Eater")
 
def main():
    count = 0
    answer = ""

    print("Let's adventure some weird food")
    print("Press 'q' anytime to quit")
    print("Have you tried this food or would love to try it soon?")

    food= ["snake","alligator","fish eggs","beef tongue", "blood sausage","brain", "goat intestines", "chicken feet", "frog legs", "heart (chicken, cow or lamb)", "jelly fish", "kangaroo", "pigeon", "pigs tail", "rats", "scorpion", "octopus", "snake whiskey", "turtle soup", "tuna eyeballs"]

    for question in food:
        answer = input(f"{question} (yes/no)").upper().strip() 
        if answer == "YES":
            count += 1

    print("Adventurous foods chosen:", count)

    if count >15:
        print("You are super duper adventurous. Now go EAT!!!")
    elif count >10 and count <= 15:
        print("You are adventurous eater.")
    elif count >5 and count <= 10:
        print("You are semi-adventurous eater. You need to eat more weird food my friend.")
    else:
        print("You are not an adventurous eater. Sorry!!!")


main()
