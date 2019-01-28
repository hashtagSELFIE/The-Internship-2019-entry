"""

XML to JSON converter
Created by Chetsadaporn Traivinidsreesuk

Credits: MicroPyramid
https://medium.com/@MicroPyramid/how-to-convert-xml-content-into-json-using-xmltodict-3ab92bff913e

"""


import json
import os
import xmltodict


def newformat():
    """
Read the 'weather.xml' file then convert it using xmltodict libary, then export it
in to readable JSON file
    """
    print("Welcome to XML to JSON parser.\n\n Enter for demo mode(Read the preset example file)\n\n\
Enter 'SUDO' for your custom xml context file\nMake sure you put custom file in THIS exact same\
folder as this Python file directory!\n\n")
    filename = 'import.xml'
    response = input()
    os.system('cls' if os.name == 'nt' else 'clear')
    if response in ("SUDO", "'SUDO'"):
        while 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Please enter EXACT file name down below (Example: export.xml)\n")
            filename = input()

    with open(filename, 'rb') as xml_file:
        raw_json = json.loads(json.dumps(xmltodict.parse(xml_file)))
    print("Conversion done!")
    with open('export.json', 'w') as export:
        json.dump(raw_json, export, indent=4)
    print("Export done!\n\nPress Enter to exit this program")
    input()


newformat()
