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
if choice == 1:
    choiceT = input("Would you like to convert from Celcicus (C, c) or Fahernite (F, f):\n").strip().lower()
    if choiceT == "c" :
        celinput = celToFah(float(input("Enter your celcius temperature:")))
    elif choiceT == "f" :
        fahinput = fahToCel(float(input("Enter your fahernite:")))
    else:
        print("Incorrect input!")
elif choice == 2:
    choiceT = input("Would you like to convert from Kilometers Per Hour (KMH, kmh) or Miles Per Hour (MPH, mph):\n")
else:
    print("Incorrect entry")    