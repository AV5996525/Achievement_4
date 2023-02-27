#Name:          achieve_4.py
#Author:        AJ Varatharajan
#Date Created:  February 22, 2023
#Date Last Modified: February 23, 2023
#Purpose: User is able to input a value as either a temperature or speed and convert to and from it's interchangeable state.
#
#This program will output the requested conversion.
def celToFah (cel) : #celsius to fahrenheit function
    conv = (cel * 1.8) + 32
    return conv
def fahToCel (fah) : #fahrenheit to celsius function
    conv = (5/9) * (fah-32)
    return conv
def mphToKm (mph) : #Miles to kilometers function
    conv = (mph * 1.609344)
    return conv
def kmToMph (km) : #Kilometers to miles function
    conv = (km / 1.609344)
    return conv
choice = input("Welcome to the conversion calculator! Would you like to convert: \n1. Temperature \n2. Speed\n").strip() #Prompting user input and stripping spaces and saving it to a variable
if choice == "1": #Temperature conversion selection
    choiceT = input("Would you like to convert from Celcicus (C, c) or Fahernite (F, f):\n").strip().lower() #Prompting user input and stripping spaces, converting to lower case and saving it to a variable
    if choiceT == "c" :
        celinput = celToFah(float(input("Enter your celcius temperature:"))) #Prompting user input casting float on the input and saving to variable
        print("The temperature is {} fahernite".format(celinput))    
    elif choiceT == "f" :
        fahinput = fahToCel(float(input("Enter your fahernite:"))) #Prompting user input casting float on the input and saving to variable
        print("The temperature is {} degrees celcius".format(fahinput))
    else:
        print("Incorrect input!")
elif choice == "2":
    choiceS = input("Would you like to convert from Kilometers Per Hour (KMH, kmh) or Miles Per Hour (MPH, mph):\n").strip().lower()  #Prompting user input and stripping spaces, converting to lower case and saving it to a variable
    if choiceS == "kmh" :
        kmhInput = kmToMph(float(input("Enter your speed in kilometers per hour:\n"))) #Prompting user input casting float on the input and saving to variable
        print("The speed is {} miles per hour".format(kmhInput))
    elif choiceS == "mph" :
        mphInput = mphToKm(float(input("Enter your speed in miles per hour:\n"))) #Prompting user input casting float on the input and saving to variable
        print("The speed is {} kilometers per hour".format(mphInput))             
else:
    print("Incorrect entry")    