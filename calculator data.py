from colorama import Fore
from datetime import datetime, date

while True:
    try:
        user_year = int(input(f"{Fore.YELLOW}Enetr your year: "))
        user_month = int(input('Enter your month: '))
        user_day = int(input('Enter your day: '))
        break
    except ValueError:
        print(f'\n\n{Fore.RED}Error \n you must enter number only \n Try again \n\n')
        continue

year= datetime.now().year
month= datetime.now().month
day= datetime.now().day

# print(f"\n{Fore.GREEN}your birth year is : {Fore.BLUE}{year-user_year}")
      # f"\n{Fore.GREEN}your birth month is : {Fore.BLUE}{month-user_month}"
      # f"\n{Fore.GREEN}your birth day is : {Fore.BLUE}{day-user_day}")
if day-user_day < 0:
    if month-user_month < 0:
        print(f"\n{Fore.GREEN}your birth year is : {Fore.BLUE}{(year - user_year)-1}")
        print(f"{Fore.GREEN}your birth month is : {Fore.BLUE}{((month-user_month)+12)-1}")
    else:
        print(f"\n{Fore.GREEN}your birth year is : {Fore.BLUE}{(year - user_year)}")
        print(f"{Fore.GREEN}your birth month is : {Fore.BLUE}{(month-user_month)-1}")
    print(f"{Fore.GREEN}your birth day is : {Fore.BLUE}{(day-user_day)+31}")
else:
    if month-user_month < 0:
        print(f"\n{Fore.GREEN}your birth year is : {Fore.BLUE}{(year - user_year)-1}")
        print(f"{Fore.GREEN}your birth month is : {Fore.BLUE}{(month-user_month+12)}")
    else:
        print(f"\n{Fore.GREEN}your birth year is : {Fore.BLUE}{(year - user_year)}")
        print(f"{Fore.GREEN}your birth month is : {Fore.BLUE}{(month-user_month)}")

    print(f"{Fore.GREEN}your birth day is : {Fore.BLUE}{ day -user_day}")