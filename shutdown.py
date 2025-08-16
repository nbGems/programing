import sys
import os

print('1.shutdown \n2.restart')



while True:
    q = input('1/2: \n').lower().strip()
    if q == '1':
        os.system('shutdown /s /t 1')
    elif q == '2':
        os.system('shutdown /r /t 0')
    elif q in ['exit','exit()']:
        sys.exit()
    else:
        continue
