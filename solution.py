# Level 1
# Question 1

'''
result = ""
for num in range(2_000, 3_201):
    if num % 7 == 0 and num % 5 != 0:
        if result == "":
            result += f"{num}"
        else:
            result += f",{num}"

print(result)
'''

# Level 1
# Question 2

''' 
import pyinputplus as pyip
def factorial(num, mode="Default"):
    verbose_list = []
    result = 1
    
    for num in range(1, num+1):
        verbose_list.append(str(num))
        result *= num

    verbose_str = " * ".join(verbose_list)

    if mode == "Default":
        return result
    elif mode == "Verbose":    
        return f"{verbose_str} = {result}"
    else:
        return "**INVALID MODE**"

def main():
    num = pyip.inputInt("Enter a number to calculate its factorial: ")
    print(f"{num}! = {factorial(num)}")
if __name__ == "__main__":
    main()
'''

# Level 1
# Question 3

'''
integral = int(input())
dictionary = {}
for num in range(1, integral + 1):
    dictionary[num] = num * num
print(dictionary)
'''

# Level 1
# Question 4

'''
comma_seperated_numbers = input()
as_a_list = comma_seperated_numbers.split(",")
print(as_a_list)
as_a_tuple = tuple(as_a_list)
print(as_a_tuple)
'''

# More Level 1
# Question 5
