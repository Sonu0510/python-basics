#Loop through each items of List using for loop
techGiant = ["Amazon", "Apple", "Facebook", "Google", "Netflix", "OpenAI"]
for x in techGiant:
    print(x)

aiTools = ["ChatGPT", "Bard", "Siri", "Alexa"]
i = 0
while i < len(aiTools):
    print(aiTools[i])
    i = i + 1

bike = ["Hero", "Yamaha", "Royal Enfield", "TVS", "Honda"]
[print(x) for x in bike]

#List Comprehension
techGiant = ["Amazon", "Apple", "Facebook", "Google", "Netflix", "OpenAI"]
startingWithA = []
for x in techGiant:
    if 'A' in x:
        startingWithA.append(x)
print(startingWithA)


names = ["Yugendra Ray", "Siya Kishor Sah", "Susmita Ray", "Bill Gates", "Ray Charles", "Napoleon Bonaparte Sah"]
surnameRay = []
for x in names:
    if "Ray" in x:
        surnameRay.append(x)
print(surnameRay)

#Single-line code for above lines of code
surnameSah = [x for x in names if "Sah" in x]
print(surnameSah)


nameAndAges = ["Yugendra Ray - 23", "Suresh Ray - 48", "Devendra Ray - 53", "Bimlendra Ray - 25", "Sabita Ray - 44"]
#This line of code is not totally correct to print ages in 20s because it will print age if it conatins 2 in 10s place.
ageIn20s = [x for x in nameAndAges if "2" in x]
print(ageIn20s)

# Using range() function to create iterable
numberTill9 = [x for x in range(10)]
print(numberTill9)

numberBelow6 = [x for x in range(10) if x < 6]
print(numberBelow6)

#Expression: - Manipulating current item in iteration before ending up in a list
grains = ["Rice", "Gram", "Peas", "Maize", "Wheat", "Buckwheat"]
grainswithi = [x.upper() for x in grains if "i" in x]
print(grainswithi)

grainswithe = [x.lower() for x in grains if "e" in x]
print(grainswithe)

newGrainsList = [x if x != "Rice" else "Paddy" for x in grains]
print(newGrainsList)

grainsWithoutRice = [x for x in grains if x != "Rice"]
print(grainsWithoutRice)

