import os
from time import sleep

a = list(input('Yazı: '))
k = int(input('Kursorun indexi: '))
buff=''
help_text = '''
KechiEdtr
Backspace -> back   a -> one symbol left
Delete -----> del   d -> one symbol right
Add word/s -> +word   copy-> copy,1to3
Paste -> paste
____________________________________
'''
def welcome():
    a = ''
    l = ['|', '/', '-', '\\', '|', '/', '-', '\\']
    w = list(' Welcome to KechiEdtr <3')
    for i in range(len(w)):
        os.system('clear')
        a += w[i]
        print(a)
        sleep(0.15)
    for i in l * 2:
        os.system('clear')
        print(' ', i)
        sleep(0.1)
    sleep(0.6)

welcome()

while True:
    c = a[:]
    c.insert(k + 1, '|')
    c = ''.join(c)
    os.system('clear')
    print(help_text)
    print(' ', c)
    print(' Kursor:', k)

    prompt = input(' Prompt: ').lower()

    if prompt == 'del':
        if k + 1 < len(a):
            del a[k + 1]

    elif prompt == 'back':
        if k >= 0:
            del a[k]
            k -= 1
            if k < -1:
                k = -1

    elif prompt[0]==('+'):
        for i in prompt[1:]:
            k += 1
            a.insert(k, i)

    elif prompt == 'a':
        if k >= 0:
            k -= 1

    elif prompt == 'd':
        if k < len(a) - 1:
            k += 1

    elif prompt == '':
        pass
        
    elif prompt.split(',')[0] =='copy':
    	st=int((prompt.split(',')[1]).split('to')[0])
    	ed=int((prompt.split(',')[1]).split('to')[1])
    	buff=a[st:ed]
    	print(buff)
    elif prompt=='paste':
    	for i in buff:
            k += 1
            a.insert(k, i)
    elif prompt == 'exit':
        break