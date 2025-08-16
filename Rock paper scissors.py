from colorama import Fore
import random
import sys

print(f"{Fore.YELLOW}Hello, I am the game programmer. \n"
      f"I want to play with you rock, paper, scissors.\n"
      )

while True:
    first_q= input(f"{Fore.GREEN}And you to? \ny/n: ").lower().strip()
    print('')
    if first_q in ['n','no']:
        print(f'{Fore.YELLOW}Ok good bye.')
        sys.exit()
    elif first_q in ['yes','y']:
        print(f"{Fore.YELLOW}Ok let's go \n"
              f"{Fore.MAGENTA}\ngo Game rules: \n"
              f'rock > scissors\n'
              f'paper > rock\n'
              f'scissors > paper'
              )

        while True:
            try:
                high_score= int(input(f'\n{Fore.GREEN}How many points to win? \n{Fore.MAGENTA}>>>'))
                user_score= 0
                ai_score = 0
                if high_score <= 0:
                    print(f"{Fore.RED}You can't enter 0 or negative number \nTry again")
                    continue
                else:
                    while user_score < high_score or ai_score < high_score:
                        if user_score == high_score or ai_score == high_score:
                            break
                        else:
                            items= ['1','2','3']
                            user= input(f'\n{Fore.GREEN}Choose: \n1.rock \n2.paper \n3.scissors\n{Fore.MAGENTA}>>>').lower().strip()
                            ai= random.choice(items)
                            if user in items:
                                print(f"{Fore.YELLOW}I choice {Fore.CYAN}{ai}")
                                rules= {'2':2,
                                        '1':1,
                                        '3':-3
                                        }
                                if (user == 'paper' and ai == 'scissors') or (ai == 'paper' and user == 'scissors'):
                                    rules['3']= 3

                                if rules[user] > rules[ai]:
                                    user_score += 1
                                    print(f'\n{Fore.LIGHTGREEN_EX}You get point\n'
                                          f'{Fore.CYAN}You  :  me\n'
                                          f'----------\n'
                                          f'  {user_score}  :  {ai_score}\n')
                                elif rules[user] < rules[ai]:
                                    ai_score += 1
                                    print(f'\n{Fore.LIGHTRED_EX}I get point\n')
                                    print(f'{Fore.CYAN}You  :  me\n'
                                          f'----------\n'
                                          f'  {user_score}  :  {ai_score}\n')
                                elif rules[user] == rules[ai]:
                                    print(f'\n{Fore.LIGHTBLACK_EX}   Draw\n'
                                          f'{Fore.CYAN}You  :  me\n'
                                          f'----------\n'
                                          f'  {user_score}  :  {ai_score}\n')
                            else:
                                print(f'\n\n{Fore.RED}ERROR \nYou must choice paper ,rock and scissors \nTry again\n\n')
                                continue
                    if user_score == high_score:
                        print(f'{Fore.LIGHTGREEN_EX}You win \n'
                              f'{Fore.YELLOW}I enjoyed playing with you\n'
                              f'Thank you')
                        sys.exit()
                    elif ai_score == high_score:
                        print(f'{Fore.LIGHTRED_EX}You lose \n'
                              f'{Fore.YELLOW}You can win next time\n'
                              f'I enjoyed playing with you\n'
                              f'Thank you')
                        sys.exit()
            except ValueError:
                print(f"{Fore.RED}\n\nERROR \nYou must enter number \ntry agin\n\n")
                continue
    else:
        print(f"{Fore.RED}\n\nERROR \nYou must enter yes or n \nTry again \n\n")
        continue
