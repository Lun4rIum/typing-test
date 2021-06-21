import random
import time
import os
if os.name == 'nt': # Only if we are running on Windows
    from ctypes import windll
    k = windll.kernel32
    k.SetConsoleMode(k.GetStdHandle(-11), 7)
i=1



word_list_file = open("liste_francais.txt", "r")
word_list = word_list_file.read().lower().replace(' ','\n').split('\n')

word_list_file.close()

timeout = time.time() + 60*1

WPM = 0
Error = 0
Frappe = 0
while True:
    x = True


    word_select = random.randint(1,22740)
    word = word_list[word_select]



    print('     ' + word + '     ' + '                    ', "00 :",int(timeout-time.time()))


    user_input = input(f'\u001b[32m{"> "}\x1b[0m').replace(' ','')
    Frappe += len(user_input)

    if user_input == word:
        WPM += 1
    else:
        Error += 1

        while x:
            user_input = input(f"\x1b[31m{'> '}\x1b[0m").replace(' ','')
            Frappe += len(user_input)
            if user_input == word:
                WPM += 1
                x = False
            elif user_input != word:
                Error += 1

    if time.time() > timeout:
        break

WPM = Frappe - Error*6
WPM = WPM / 6
WPM = int(WPM)
print('Vous écrivez',WPM,'mots par minutes !')
