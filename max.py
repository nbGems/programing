#المكاتب المستخدمه
from colorama import Fore
import random

while True:
    try:
        num1= float(input(Fore.YELLOW+'Enter number: '))
        num2= float(input('Enter number: '))
        num3= float(input('Enter number: '))
        num4= float(input('Enter number: '))
        number_list = [num1, num2, num3, num4]
        break
    except ValueError:
        print(f"{Fore.RED}\n\nError \nYou must enter number \nTry agin \n\n")

# طريقة الراندوم
# while True:
#     x = random.choice(number_list)
#     if x >= num2 and x >= num3 and x >= num4 and x >= num1:
#         print(f"\n{Fore.GREEN}max number is: {Fore.LIGHTBLUE_EX}{x}")
#         break
#     else:
#         continue

# طريقة المقارنه
max_number = number_list[0]

for try_number in number_list[1:]:
    if max_number < try_number:
        max_number= try_number

print(f"\n{Fore.BLUE}{max_number}")
