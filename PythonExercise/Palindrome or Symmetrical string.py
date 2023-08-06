#PROGRAMS TO RETURN SYMMETRIC WORD ONLY FROM ANY STRING
def is_palindrome(word):
    return word == word[::-1]

def find_symmetric_words(string):
    words = string.split()  # Split the input string into individual words
    symmetric_words = [word for word in words if is_palindrome(word)]
    return symmetric_words

input_string = "level radar hello madam kayak world civic noon stats repaper"
symmetric_words = find_symmetric_words(input_string)
print("Symmetric words:", symmetric_words)

#PROGRAM TO RETURN SYMMETRIC WORDS
def is_symmetrical(string):
    length = len(string)
    for i in range(length // 2):
        if string[i] != string[length - i - 1]:
            return False
    return True

print(is_symmetrical("amaama"))

#ANOTHER PROGRAM TO RETURN SYMMETRIC OR PALINDROMIC WORDS
def palindrome(string):
    start = 0
    last = len(string) - 1
    while start < last:
        if string[start] != string[last]:
            print("The string \'" + string + "\' is not palindrome")
            return False
        start += 1
        last -= 1
    print("The string \'" + string + "\' is palindrome")
    return True


while True:
    string_to_be_checked = input("check palindrome or not: \n")
    if string_to_be_checked.lower() == "q":
        break
    print(palindrome(string_to_be_checked.lower()))
    print("-----------\n")

