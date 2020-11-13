
"""

This program will determine which payment option, out of two, is better in terms of higher pay.
The first option pays 100 dollars a day for 10 days. The second option pays 1 dollar on the first
day with the amount paid then doubling each day after that for 10 days. There will be two fuctions,
one for each pay option.

Function 1 will calculate the pay total for option 1, and fuction 2 will calculate the pay for option 2.
Function 1 will output 100 * 10.
Function 2 will loop 10 times, each time doubling the previous amount and adding it to the total. 

If amounts for option 1 and option 2 are equal, program will display "Option 1 and Option 2
pay the same."
If option 1 pays more, program will output to user "Option 1 is better."
If option 2 pays more, program will output to user "option 2 is better." 

"""

"""
#option1
 return 100 * 10

#option2
 amount = 1
 list1 = []
 loop 10 times
   add amount to list1
   amount *= 2
 sum = sum of all items in loop
 return sum

#main
 var1 = option1
 var2 = option2

 if var1 = var 2
   "Option 1 and Option 2 pay the same" 
 if var1 > var2
   "Option 1 is better."
 else
   "Option 2 is better."  

Main
""" 




def option1():
    return 100 * 10

def option2():
    amount = 1
    list1 = []
    for i in range(0, 10):
        list1.append(amount)
        amount *= 2
    total = sum(list1) 
    return total

def main(): 
    answer = ""
    var1 = option1()
    var2 = option2()
    if var1 == var2:
        answer = "Option 1 and Option 2 pay the same." 
    elif var1 > var2:
        answer = "Option 1 is better."
    else:
        answer = "Option 2 is better."  
    print(answer)

main() 
