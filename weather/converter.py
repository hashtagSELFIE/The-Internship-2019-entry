"""

XML to JSON converter
Created by Chetsadaporn Traivinidsreesuk
For The Internship 2019 Application

Credits: MicroPyramid
https://medium.com/@MicroPyramid/how-to-convert-xml-content-into-json-using-xmltodict-3ab92bff913e

xmltodict package by xmltodict package by martinblech
https://pypi.org/project/xmltodict/

"""


import json
import os
import xmltodict


def newformat():
    """
MAKE SURE TO INSTALL XMLTODICT LIBARY FIRST, you can do so by type the following in your terminal


>> pip3 install xmltodict


Read the 'weather.xml' file then convert it using xmltodict libary, then export it
in to readable JSON file
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Welcome to XML to JSON parser.\n\nEnter for demo mode(Read the preset example file).\n\n\
Enter 'SUDO' for your custom xml context file.\nMake sure you put your custom file in THIS exact same\
 folder as this Python file directory!\n")
    # default file to be parse in this program (also the example file in Bitbucket)
    filename = 'weather.xml'
    response = input()
    realfilename = ''
    os.system('cls' if os.name == 'nt' else 'clear')
    # In case of user not understanding how to properly type in SUDO as of vague instruction.
    if response in ("SUDO", "'SUDO'", "sudo", "'sudo'"):
        while 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Please enter EXACT file name down below (Example: export.xml).\n")
            filename = input()
            print("\nPress ENTER to confirm\nType in 'EDIT' to re-enter file name.\n")
            answer = input()
            if answer in ("EDIT", "'EDIT'"):
                continue
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Custom file accepted!")
                break
    # previously did not work since open function need to be read as binaries
    with open(filename, 'rb') as xml_file:
        raw_json = json.loads(json.dumps(xmltodict.parse(xml_file)))
    print("Conversion done!")
    for i in filename:  # removes filename extension
        if i == ".":
            break
        realfilename += i
    with open(realfilename + '_parsed.json', 'w') as export:
        if realfilename == 'weather':
            # To achieve same result as in Bitbucket example
            json.dump(raw_json["current"], export, indent=2)
        else:
            json.dump(raw_json, export, indent=2)
    print("File created as", realfilename + '_parsed.json')
    print("Export done!\n\nPress Enter to exit this program.\n")
    input()


newformat()
