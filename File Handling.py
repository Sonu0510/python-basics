


# Working with file
#open() function - open(filename_goes_here, mode_goes_here)
#modes are read(r), write(w) and append(a)

filename = "microsoft.txt"
file_obj = open(filename,"r")

# Alternative way to open a file (Recommended method)

with open(filename, "r") as file_obj:
  pass

#READING ALL CONTNENT IN FILES IN PYTHON
with open(filename, "r") as file_obj:
  file_cotnent = file_obj.read()
print(file_cotnent)
print("\n")

# PASSING ARGUMENT IN .read() METHOD
with open(filename, "r") as file_obj:
  file_cotnent = file_obj.read(10)
print(file_cotnent)
print("\n")

#READING SINGLE LINE IN FILES IN PYTHON
with open(filename, "r") as file_obj:
  single_line = file_obj.readline()
print(single_line)
print("\n")


#READING MULTI LINE IN FILES IN PYTHON
with open(filename, "r") as file_obj:
  multi_line = file_obj.readlines()
print(multi_line)


#WRITING IN FILE, WRITE MODE ERASES PREVIOUS CONTENT FROM FILE
file_name = "test.txt"
with open(file_name, "w") as file_obj:
  file_obj.write("Hi, I am writing this new file with Python write() method\n")


# OVERWRITING test.txt
with open(file_name, "w") as file_obj:
  file_obj.write("Previous content is erases with this content\n")

#APPENDIND IN text.text, APPEND MODE ADD CONTENT TO FILE KEEPING PREVIOUS CONTENT
with open(file_name, "a") as file_obj:
  file_obj.write("Adding extra lines in this file with append method")
print("\n")

# CREATING NEW FILE
with open("new.txt" , "x") as file_object:
  pass

# DELETING FILE
import os
# os.remove("newFile.txt")

if os.path.exists("newFile.txt"):
  os.remove("newFile.txt")
else:
  print("File does not exists")



f = open("Sample100.csv","r") #r-read and t-text
#print(f.read()) #return all of the contents in file
#print(f.read(n))- returns first n number of characters of file
#print(f.readline()) - to read one line from given file if you want to read two line call this method twice
#print(f.readline())
for x in f:#You can even loop through file to read its content
    print(x)

pf = open("pdetails.txt", "a")
pf.write("I am going to be a top AI and Data Science Engineer")
pf.close()
pf = open("pdetails.txt", "r")
print(pf.read())

pf = open("microsoft.txt", "w")#microsoft.txt was not there. When I used "w" for this file it created new file for me
pf.write("Microsoft is a top tech giant company.")
pf.close()
pf =open("microsoft.txt", "r")
print(pf.read())

#Short code to create file
with open("newFile.txt", "w") as f:
    f.write("This file is created with shortcut method")

import os
if os.path.exists("pdetails.txt"):#This code removed the file I had created after checking it.
    os.remove("pdetails.txt")
else:
    print("The file does not exit")


# Following code can remove empty folder only
# import os
# os.rmdir("FolderNameHere")
