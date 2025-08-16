from colorama import Fore
import random
import sys

print(Fore.YELLOW+'Hello \nI want to test your athletic skills.\n')

while True:
    frist_q = input(Fore.GREEN+f'are you ready? \ny/n: ').lower().strip()
    if frist_q in ['n','no']:
        print(Fore.BLUE+'\nOk fine we can test that next time')
        sys.exit()
    elif frist_q in ['y','yes']:
        while True:
            try:
                print(Fore.LIGHTWHITE_EX)
                num1 = int(random.randint(1,10))
                op_list= ['+','-','*','/']
                op= random.choice(op_list)
                num2= random.randint(1,10)
                if op == '+':
                    q = int(input(f'\n{num1}+{num2} '+Fore.BLUE+'\n='))
                    if q == (num1+num2):
                        print(Fore.LIGHTGREEN_EX)
                        print("The answer is correct\n\n")
                    elif q != (num1+num2):
                        print(Fore.LIGHTRED_EX)
                        print(f"The answer isn't correct \nAnswer is {num1+num2} \n\n")

                elif op == '-':
                    max_num= max([num1,num2])
                    min_num= min([num1,num2])
                    q= int(input(f'\n{max_num}-{min_num} '+Fore.BLUE+'\n\n='))
                    if q == (max_num-min_num):
                        print(Fore.LIGHTGREEN_EX)
                        print("The answer is correct")
                    elif q != (max_num-min_num):
                        print(Fore.LIGHTRED_EX)
                        print(f"The answer isn't correct \nAnswer is {max_num - min_num} \n\n")
                elif op == '*':
                    q= int(input(f'\n{num1}*{num2} '+Fore.BLUE+'\n\n='))
                    if q == (num1*num2):
                        print(Fore.LIGHTGREEN_EX)
                        print("The answer is correct")
                    elif q != (num1*num2):
                        print(Fore.LIGHTRED_EX)
                        print(f"The answer isn't correct \nAnswer is {num1*num2} \n\n")
                elif op == '/':
                    max_num = max([num1, num2])
                    min_num = min([num1, num2])
                    if min_num == 1:
                        continue
                    q= input(Fore.LIGHTWHITE_EX+f'\n   {max_num}\n------------\n     {min_num}\n\n= ').strip().replace(' ','')
                    user_num= float(q)
                    if str(user_num) in str(max_num/min_num).strip().replace(' ','') or str(user_num) in str(round(max_num/min_num,0)):
                        print(Fore.LIGHTGREEN_EX)
                        print("The answer is correct")
                    elif str(user_num) not in str(max_num/min_num).strip().replace(' ','' ) or str(user_num) not in str(round(max_num/min_num,0)):
                        print(Fore.LIGHTRED_EX)
                        print(f"The answer isn't correct \nAnswer is {round(max_num/min_num,2)} \n\n")
            except ValueError:
                        print(Fore.RED+"\n\nERROR \nYou must enter number\n\n")

    else:
        print(Fore.LIGHTRED_EX+f'\n\nERROR \n You must enter y or n \n Try again\n\n')