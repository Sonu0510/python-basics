# strings in Python are arrays of bytes representing unicode characters

# 3. Python program to check whether the string is Symmetrical or Palindrome




# 2. REMOVING nth CHARACTER FROM A STRING

# Using function to remove nth character
def rem_nth_char(string, index):
    if index == 0:
        return string[1:]

# Method 2 to remove nth character
date_of_birth = "My date of birth is 2000"
removed_date = date_of_birth.translate({ord(i): None for i in '2000'})
print(removed_date)

# Method 1 to remove nth character
char_remove_string = "This is 2324 Yugendra Ray"
new_string_after_removed = char_remove_string.replace(" 2324", "")
print(new_string_after_removed)



# 1. REVERSE SENTENCE IN A STRING
string = "Hello I am here"
print(string[::-1]) #reverse each character from last to first

# Method below reverse each word from last to first means it prints the word from last up until firs word
new_list = list(string.split(" "))
reversed_new_list = new_list[::-1]
reversed_string = " ".join(reversed_new_list)
print(reversed_string)




# *** CLASS WORK ***

# 1. USE len METHOD TO PRINT STRING

str_holder = "Microsoft is one of the Five Big IT companies"
str_holder_len = len(str_holder)
print(str_holder_len)


# Q.2 Print length of String without using len function.
another_string = "Hello"
count = 0
for char in another_string:
    count = count + 1
print(count)
print("\n")


# Q.3 Write python program to print vowel and consonants on the given string
v_c_string = "Yugendra, Here!"
vowel = ""
consonants = ""
for char in v_c_string:
    if char in "aeiouAEIOU":
        vowel = vowel + char
    elif char.isalpha() and char not in "aeiouAEIOU":
        consonants = consonants + char

print(f"Vowels are \"{vowel}\" in \"{v_c_string}\"")
print(f"Consonants are \"{consonants}\" in \"{v_c_string}\"")
print("\n")



"""
Q.4 Write a python program to extract first and last 2 character into new string.
example:
input_string = "my name is xyz"
output_string = "myyz"
"""
given_string = "PD is a MP"
result_string = given_string[:2] + given_string[-2:]
print(result_string)
print("\n")



"""Q.5 Write a python program to get a single string from two given strings, separated by a space and swap the first
two characters of each string.
example:
first_string = "first"
second_string = "second"
output_string = "serst ficond
"""

# One way to achieve task at 5
first_string = "first"
second_string = "second"
single_string = first_string.replace("fi", second_string[:2]) + " " + second_string.replace("se", first_string[:2])
print(single_string)

# another way to achieve task at 5
my_string = "Good morning sir,"
your_string = "How are you sir!"
joint_string = my_string.replace(my_string[:2], your_string[:2]) + " and " + your_string.replace(your_string[:2], my_string[:2])
print(joint_string)
print("\n")



"""Q.6 Write a python program to remove the nth index character from a nonempty string. Ask user to input non-empty
string, and index
example:
non_empty_str = "hello world"
index_to_remove = 3
output_str = "helo world
"""
# One-way to achieve given task at 6
user_given_string = input("String from user is: \n")
given_index_number = input("This index numbered character should be removed: \n")
string_after_removing_given_index = "New string is: " + user_given_string[:int(given_index_number)] + user_given_string[                                                                                                    int(given_index_number) + 1:]
print(string_after_removing_given_index)

# Other way to achieve given task at 6
user_input = input("Enter something: \n")
index_to_remove = int(input("Enter index to remove character: \n"))

output_after_removing_given_index = user_input.replace(user_input[index_to_remove], "")
print(output_after_removing_given_index)

print("\n")
