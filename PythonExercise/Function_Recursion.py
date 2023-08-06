

# Calculate sum of numbers in list
def add_num_in_list(num):
    if not num:
        return 0
    else:
        return num[0] + add_num_in_list(num[1:])


num = list(range(11))
print(add_num_in_list(num))
print("*____________________*______________________*____________________*\n")


# Calculate factorial using function
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print("The factorial of 3 is:", factorial(3))
print("The factorial of 5 is:", factorial(5))


# Recursion simple example
def tri_recursion(k):
    if k > 0:
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result


print("\n\nRecursion Example Results")

print("The result for tri-recursion(3): -")
tri_recursion(2)
print("*____________________*______________________*____________________*")
print("The result for tri-recursion(4): -")
tri_recursion(4)
