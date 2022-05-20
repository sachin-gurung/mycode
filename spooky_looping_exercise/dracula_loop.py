#!/usr/bin/env python3

count = 0

with open("dracula.txt","r") as draculafile:
    for sentence in draculafile:
        if "vampire" in sentence.lower():
            print(sentence, end="") 
            count += 1
            with open("vampytimes.txt", "a") as vampyfile:
                vampyfile.write(sentence + "\n")
    print(f"The word 'vampire' appreared {count} times!!!")
        