# vowels_init = "aeiou"
# consonants_init = "bcdfghjklmnpqrstvwxyz"
# vowels = ""
# consonants = ""
# string = input("Please enter what you like: ").replace(" ","").lower()
# if string.isalpha() or "," or "." in string:
#   for i in string:
#     if i in vowels_init:
#       vowels+=i
#     elif i in consonants_init:
#       consonants+= i
#     else:
#       pass
#
#   print(f"The total no of vowels is: {len(vowels)}")
#   print(f"Vowels = {''.join(set(vowels))}")
#   print(f"The total number of consonants is: {len(consonants)}")
#   print(f"Consonants = {''.join(set(consonants))}")
#
# else:
#   print("Invalid input, please try again")

string = input("Please enter what you like: ").replace(" ","").lower()
print(string.isalpha())