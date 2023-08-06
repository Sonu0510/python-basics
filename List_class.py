# LIST FROM CLASSES
list1 = [1, 2, 3, 4, 5, 6, 7]
list1.pop()
print(list1)

list1.reverse()
print(list1)

list1.sort()  # to sort lists in ascending order
print(list1)

list1.sort(reverse=True)
print(list1)

given_list = ["Hello", "World"]
join_item_in_list = " ".join(given_list)
print(join_item_in_list)

# print(" ".join([1, 2, 3]) # will give error because .join method expects each items in list to be string


# create list
sample_list = [1, 2, 3, 4, 5]
new_list = []
# loop through list items

for item in sample_list:
    print(item)
    item_str = str(item)
    new_list.append(item_str)
    # print('------------')

another_list = ["item1", "item2", "item3", "item4"]

for item in enumerate(sample_list):
    print(item)
    print('------')

for idx, item in enumerate(sample_list):
    print(idx)
    print(item)
    print('-------')

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
new_fruit_list = [item.upper() for item in fruits]
print(new_fruit_list)

vegetables = ["bitter gourd", "spinach", "onion", "tomato", "tea"]
new_vegetable_list = [item for item in vegetables if item != "tea"]
print(new_vegetable_list)

country_list = ["Nepal", "India", "China", "Kathmandu"]
new_country_check_list = ["I am city" if item =="Kathmandu" else "I am Country" for item in country_list]
print(new_country_check_list)
print('----------*------------*--------\n')

voter_list = ["Bill Gates", "Gautam Buddha", "Marcus Aurelius", "Socrates"]
enumerated_voter_list = [item for item in enumerate(voter_list)]
print(enumerated_voter_list)
print(len(enumerated_voter_list))
print(type(enumerated_voter_list))
print(type(enumerated_voter_list[1]))

