#!/usr/bin/env python3

def main():

    data = {1:["Rooster","hardworking, resourceful, courageous, and talented"],
    2:["Dog","loyal, honest, cautious, and kind"],
    3:["Pig","a symbol of wealth, honesty, and practicality"],
    4:["Rat","artistic, sociable, industrious, charming, and intelligent"],
    5:["Ox","strong, thorough, determined, loyal, and reliable"],
    6:["Tiger","courageous, enthusiastic, confident, charismatic, and a leader"],
    7:["Rabbit","vigilant, witty, quick-minded, and ingenious"],
    8:["Dragon","talented, powerful, lucky, and successfull"],
    9:["Snake","wise, like to work alone, and determined"],
    10:["Horse","animated, active, and energetic"],
    11:["Sheep","creative, resilient, gentle, mild-mannered, and shy"],
    0:["Monkey","sharp, smart, curious, and mischievious"]}    


    usr_name = input("Please enter your name:\n>") 
              
    usr_name = usr_name.title()    
    usr_date = int(input("Please enter your birth year in YYYY format, e.g 2010:\n>"))
    year = int(usr_date)%12
    print(f"{usr_name} your zodiac sign is {data[year][0]}, you are {data[year][1]}.")


if __name__ == "__main__":
    main()

