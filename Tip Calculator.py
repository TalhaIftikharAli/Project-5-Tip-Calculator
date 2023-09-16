# -*- coding: utf-8 -*-
# """
# Created on Sun Sep 17 02:15:40 2023

# @author: talha.i
# """

# Tip Calculator

print('Welcome to the tip calculator.')

# Input 1:
bill = float(input('What was the total bill? $'))

# Input 2:
tip = int(input('What percentage tip would you like to give? 10, 12 or 15? '))

# Input 3:
bill_split = int(input('How many people to split the bill? '))

# Calculation 1:
bill_and_tip = bill * (1 + (tip / 100))

# Calculation 2:
divided_bill = round(bill_and_tip / bill_split, 2)

# Final Output
print(f'Each person should pay: ${divided_bill}')