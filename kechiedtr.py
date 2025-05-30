import os
from time import sleep

a = list(input('Yazı: '))
k = len(a) - 1  # Kursor sondan başlıyor
buff = ''
help_text = '''
KechiEdtr
Backspace -> back   a -> one symbol left
Delete -----> del   d -> one symbol right
Add word/s -> +word   copy-> copy,1to3
Paste -> paste
Exit  -------> exit
____________________________________
'''

def welcome():
    anim = ''
    spinner = ['|', '/', '-', '\\']
    msg = list(' Welcome to KechiEdtr <3')
    for ch in msg:
        os.system('clear')
        anim += ch
        print(anim)
        sleep(0.15)
    for i in spinner * 2:
        os.system('clear')
        print(' ', i)
        sleep(0.1)
    sleep(0.6)

welcome()

while True:
    display = a[:]
    display.insert(k + 1, '|')
    os.system('clear')
    print(help_text)
    print(' ', ''.join(display))
    print(' Kursor:', k)

    prompt = input(' Prompt: ').lower()

    if prompt == 'del':
        if 0 <= k + 1 < len(a):
            del a[k + 1]

    elif prompt == 'back':
        if 0 <= k < len(a):
            del a[k]
            k -= 1
            if k < -1:
                k = -1

    elif prompt.startswith('+'):
        for ch in prompt[1:]:
            k += 1
            if k >= len(a):
                a.append(ch)
            else:
                a.insert(k, ch)

    elif prompt == 'a':
        if k >= 0:
            k -= 1

    elif prompt == 'd':
        if k < len(a) - 1:
            k += 1

    elif prompt == '':
        continue

    elif prompt.startswith('copy'):
        try:
            _, range_str = prompt.split(',')
            st, ed = map(int, range_str.split('to'))
            if 0 <= st < ed <= len(a):
                buff = a[st:ed]
        except:
            pass

    elif prompt == 'paste':
        for ch in buff:
            k += 1
            if k >= len(a):
                a.append(ch)
            else:
                a.insert(k, ch)

    elif prompt == 'exit':
        break
