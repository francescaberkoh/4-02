'''
Created on Apr 22, 2019

@author: Francesca
'''
def rounding(num,spaces):
    ans = int(num* (10**spaces)+ 0.5)/(10**spaces)
    return ans

user_num = float(input("Enter a number with decimals:"))

dec_space = float(input("Enter the number of space you'd like to round to:"))

print ("Your final answer is:" + str(rounding(user_num, dec_space))) 
