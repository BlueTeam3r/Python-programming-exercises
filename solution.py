'''
Level 1
'''

'''
Question 1
'''

# First Attempt
'''
for num in range(2_000, 3_200):
    if num % 7 == 0 and num % 5 != 0:
        print(num, end=',')
'''

# Output
# 2002,2009,2016,2023,2037,2044,2051,2058,2072,2079,2086,2093,2107,2114,2121,2128,2142,2149,2156,2163,2177,2184,2191,2198,2212,2219,2226,2233,2247,2254,2261,2268,2282,2289,2296,2303,2317,2324,2331,2338,2352,2359,2366,2373,2387,2394,2401,2408,2422,2429,2436,2443,2457,2464,2471,2478,2492,2499,2506,2513,2527,2534,2541,2548,2562,2569,2576,2583,2597,2604,2611,2618,2632,2639,2646,2653,2667,2674,2681,2688,2702,2709,2716,2723,2737,2744,2751,2758,2772,2779,2786,2793,2807,2814,2821,2828,2842,2849,2856,2863,2877,2884,2891,2898,2912,2919,2926,2933,2947,2954,2961,2968,2982,2989,2996,3003,3017,3024,3031,3038,3052,3059,3066,3073,3087,3094,3101,3108,3122,3129,3136,3143,3157,3164,3171,3178,3192,3199,
# Has comma and not including 3200

# Second Attempt
'''
result = ""
for num in range(2_000, 3_201):
    if num % 7 == 0 and num % 5 != 0:
        if result == "":
            result += f",{num}"
        else:
            result += f"{num}"

# print(result)
'''
# Output
# ,200220092016202320372044205120582072207920862093210721142121212821422149215621632177218421912198221222192226223322472254226122682282228922962303231723242331233823522359236623732387239424012408242224292436244324572464247124782492249925062513252725342541254825622569257625832597260426112618263226392646265326672674268126882702270927162723273727442751275827722779278627932807281428212828284228492856286328772884289128982912291929262933294729542961296829822989299630033017302430313038305230593066307330873094310131083122312931363143315731643171317831923199 
# comma logic in if statment is reversed
'''
Third Attempt, Success
result = ""
for num in range(2_000, 3_201):
    if num % 7 == 0 and num % 5 != 0:
        if result == "":
            result += f"{num}"
        else:
            result += f",{num}"

print(result)
'''
# Source Solution
'''
l=[]
for i in range(2000, 3201):
    if (i%7==0) and (i%5!=0):
        l.append(str(i))

print(','.join(l))
'''

# More Level 1

'''
Question 2
'''
# First Attempt Success
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
# Source Solution
'''
def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)

x=int(input())
print(fact(x))
'''

# More Level 1

'''
Question 3
'''
# First Attempt Success
'''
integral = int(input())
dictionary = {}
for num in range(1, integral + 1):
    dictionary[num] = num * num
print(dictionary)
'''
# Source Solution
'''
n=int(input())
d=dict()
for i in range(1,n+1):
    d[i]=i*i

print(d)
'''

# More Level 1

'''
Question 4
'''
# First Attempt
