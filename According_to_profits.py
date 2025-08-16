from colorama import Fore
import sys
import math
from typing import List
while True:
    try:
        profit_percentage= float(input(f'{Fore.GREEN}Enter the profit_percentage:{Fore.CYAN} '))
        break
    except ValueError:
        print(f'\n\n{Fore.RED}ERROR \nYou must enter number \nTry again \n\n')
        continue

def calculateSacrificeProfit(buy_price):
    buy_price= sum(buy_price)
    return buy_price*(profit_percentage/100)

while True:
    try:
        cost_price= float(input(f'\n{Fore.GREEN}Enter cost_price:{Fore.CYAN} '))
        administrative_expenses= float(input(f'{Fore.GREEN}Enter administrative_expenses:{Fore.CYAN} '))
        sling_and_packaging_expenses = float(input(f'{Fore.GREEN}Enter sling_and_packaging_expenses:{Fore.CYAN} '))
        marketing_expenses = float(input(f'{Fore.GREEN}Enter marketing_expenses:{Fore.CYAN} '))
        break
    except ValueError:
        print(f'\n\n{Fore.RED}ERROR \nYou must enter number \nTry again \n\n')
        continue
        
value_buy_price= [cost_price,administrative_expenses,sling_and_packaging_expenses,marketing_expenses]

print(f"\n{Fore.YELLOW}Total cost is: {Fore.BLUE}{sum(value_buy_price)}")

print(f"\n{Fore.YELLOW}Selling price with {profit_percentage} profit excluding tax: {Fore.BLUE}{round((calculateSacrificeProfit(value_buy_price)),2)}")

print(f"\n{Fore.YELLOW}Selling price with {profit_percentage} profit plus tax: {Fore.BLUE}{round((calculateSacrificeProfit(value_buy_price)*115/100),2)}")
print(Fore.RESET)

input()