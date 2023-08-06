
#Sorting name alphabetically
cities = ["Kathmandu", "New Delhi", "Bangalore", "San Francisco", "London", "Hobart", "Amsterdam", "Zurich"]
cities.sort()
print(cities)

#To sort from higher letter use reverse = True
cities.sort(reverse=True)
print(cities)

#Sorting numbers numerically
randomNum = [22, 32, 11, 333, 121, 423, 823, 222, 1]
randomNum.sort()
print(randomNum)

#Sorting in descending order
randomNum.sort(reverse=True)
print(randomNum)

#Customize Sort Function key=function
def myfunc(n):
    return abs(n-50)
randomNum.sort(key=myfunc)
print(randomNum)

# sort() function is case senstive i.e. it arranges capital letter first before arranging lower case letters
fruits = ["Orange", "banana", "watermelon", "Apple", "guava", "apple"]
fruits.sort()
print(fruits)

#use key=sort.lower to sort in alphabetically in spite of lower case or upper case letters
fruits.sort(key=str.lower)
fruits.reverse()# To reverse items in a list alphabetically
print(fruits)

#TO COPY LIST
# nameOfNewList = oldList.copy() or
# nameOfNewList = list(oldList)

#TO JOIN LIST
# can use + operator to join list
# use extend or append method to join list as well

