# استيراد المكتبات المطلوبة

import math  # مكتبة العمليات الرياضية
import sys   # مكتبة للتحكم بإنهاء البرنامج
from colorama import Fore  # مكتبة لتلوين النصوص

# طباعة قائمة العمليات المتاحة للمستخدم
print(Fore.GREEN + "operations: \n+ \n- \n* \n/ \n% \n** \n// \n3// \nsin \ncos \ntan \n")

# بدء حلقة لا نهائية حتى يتم كسرها
while True:
    try:
        # إدخال الرقم الأول من المستخدم
        num1 = float(input((Fore.RESET+"Enter number: ")))

        # إدخال العملية المراد تنفيذها
        op = input("Enter operations: ")

        # التحقق من صحة العملية المدخلة
        if op.lower().strip() not in ['+', '-', '*', '**', '/', '//3', '//', '\\','\\\\','\\\\3','3\\\\','3//' 'sin', 'cos', 'tan','%']:
            print(Fore.RED+"")
            print("\n\nERROR  \nYou must enter operations \nTry again \n\n")

        # إذا كانت العملية مثلثية نطلب الزاوية من المستخدم
        elif op.lower().strip() in ['sin', 'cos', 'tan']:
            num2 = float(input("Enter the angle of the triangle: "))

        # إذا كانت العملية جذر تربيعي
        elif op.lower().strip() in ['//','\\']:
            print(f'//{num1:10g}')
            print(Fore.BLUE)
            print(f'={(math.sqrt(num1)):10g}')
            sys.exit()  # إنهاء البرنامج

        #إذا كانت العملية جذر تكعيبي
        elif op.lower().strip() in ['3//','//3','3\\\\','\\\\3']:
            print(f'3//{num1:10g}')
            print(Fore.BLUE)
            print(f'={(num1 ** 3 / 1):10g}')  # هذا الحساب غير صحيح للجذر التكعيبي
            sys.exit()  # إنهاء البرنامج

        #االنسبه المئويه
        elif op.strip() in '%':
            print(f'%{num1}= {Fore.BLUE}{num1/100}')
            break

        # نطلب الرقم الثاني
        else:
            num2 = float(input("Enter number: "))
    # في حال أدخل المستخدم قيمة غير رقمية
    except ValueError:
        print(Fore.RED+"")
        print("\n\n ERROR \n You must enter number \n Try again \n\n")
        continue  # إعادة المحاولة

    try:
        # جمع
        if op.lower().strip() == '+':
            print(f'{num1:10g}')
            print(f'+{num2:10g}')
            print(Fore.BLUE+'-------------')
            print(f'={(num1 + num2):10g}')
            break  # إنهاء الحلقة

        # طرح
        elif op.lower().strip() == '-':
            print(f'{num1:10g}')
            print(f'-{num2:10g}')
            print(Fore.BLUE+"-------------")
            print(f'={(num1 - num2):10g}')
            break

        # ضرب
        elif op.lower().strip() == '*':
            print(f'{num1:10g}')
            print(f'*{num2:10g}')
            print(Fore.BLUE+'-------------')
            print(f"={(num1 * num2):10g}")
            break

        # القوى والأسس
        elif op.lower().strip() == '**':
            print(Fore.LIGHTBLACK_EX+f"  {num2:10g}")
            print(Fore.RESET+f"{num1:10g}\n"+Fore.BLUE+f"={(num1**num2):10g}")
            break

        # قسمة
        elif op.lower().strip() in ['/', '\\']:
            print(f"{num1:10g}")
            print('------------')
            print(f"{num2:10g}\n"+Fore.BLUE+f'={(num1 / num2):10g}')
            break

        # جيب (sin)
        elif op.lower().strip() == 'sin':
            # إذا كان المعامل 1 لا تكتبه
            if num1 == '1':
                print(f'sin({num2:10g})\n'+Fore.BLUE+f'={(math.sin(num2)):10g}')
                break
            else:
                print(f"{num1:10g} sin({num2:10g})\n"+Fore.BLUE+f'={(num1 * math.sin(num2)):10g}')
                break

        # جيب تمام (cos)
        elif op.lower().strip() == 'cos':
            if num1 == '1':
                print(f'cos({num2:10g})\n'+Fore.BLUE+f'={(math.cos(num2)):10g}')
                break
            else:
                print(f"{num1:10g} cos({num2:10g})\n"+Fore.BLUE+f'={(num1 * math.cos(num2)):10g}')
                break

        # ظل (tan)
        elif op.lower().strip() == 'tan':
            if num1 == '1':
                print(f'tan({num2:10g})\n'+Fore.BLUE+f'={(math.tan(num2)):10g}')
                break
            else:
                print (f"{num1:10g} tan({num2:10g})\n"+Fore.BLUE+ f'={(num1 * math.tan(num2)):10g}')
                break
    # في حال تم استخدام متغير غير معرف
    except NameError:
        print("")
    except ZeroDivisionError:
        print(f'\n\n{Fore.RED}ERROR\nZero division apologizes\nTry again \n\n')
        continue