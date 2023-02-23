#Name:          achieve_4.py
#Author:        AJ Varatharajan
#Date Created:  February 22, 2023
#Date Last Modified: February 23, 2023
#Purpose: User is able to input a value as either a temperature or speed and convert to and from it's interchangeable state.
#
#This program will output the requested conversion.
def celToFah (cel) :
    conv = (cel * 1.8) + 32
    return conv
def fahToCel (fah) :
    conv = (5/9) * (fah-32)
    return conv
def mphToKm (mph) :
    conv = (mph * 1.609344)
    return conv
def kmToMph (km) :
    conv = (km / 1.609344)
    return conv
choice = input("Welcome to the conversion calculator! Would you like to convert: \n1. Temperature \n2. Speed\n").strip()
if choice == "1":
    choiceT = input("Would you like to convert from Celcicus (C, c) or Fahernite (F, f):\n").strip().lower()
    if choiceT == "c" :
        celinput = celToFah(float(input("Enter your celcius temperature:")))
        print("The temperature is {} fahernite".format(celinput))    
    elif choiceT == "f" :
        fahinput = fahToCel(float(input("Enter your fahernite:")))
        print("The temperature is {} degrees celcius".format(fahinput))
    else:
        print("Incorrect input!")
elif choice == "2":
    choiceS = input("Would you like to convert from Kilometers Per Hour (KMH, kmh) or Miles Per Hour (MPH, mph):\n").strip().lower()
    if choiceS == "kmh" :
        kmhInput = kmToMph(float(input("Enter your speed in kilometers per hour:\n")))
        print("The speed is {} miles per hour".format(kmhInput))
    elif choiceS == "mph" :
        mphInput = mphToKm(float(input("Enter your speed in miles per hour:\n")))
        print("The speed is {} kilometers per hour".format(mphInput))             
else:
    print("Incorrect entry")    