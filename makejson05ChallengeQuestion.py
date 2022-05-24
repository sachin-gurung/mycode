#!/usr/bin/python3
import json
import yaml

def main():
    # open file with json, convert to python object
    with open("classdata.json","r") as classdatainfo:
        classinformation = json.load(classdatainfo)

    # create new python dictionary to be added
    new = {
        "name": "Sachin",
        "awesome" : False,
        "number": 10,
        "favorites": {"chocolate", "vanilla"}
    }

    # add to data read in from json file
    classinformation.append(new)

    print(classinformation)

    with open("editedClassData.yml","w") as yamlfile:
        yaml.dump(classinformation,yamlfile)



if __name__ == "__main__":
    main()
