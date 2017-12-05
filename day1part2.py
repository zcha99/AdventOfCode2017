#-*- coding: UTF-8 -*-

tal = raw_input('Captcha? ') #submit the number given
talc = len(tal)/2
q = len(tal) - 1
svar = 0

for i in range(len(tal)):
    global svar
    if (i + talc) <= q:
        if tal[i] == tal[i+talc]:
            print "if", i
            svar += int(tal[i])
    else:
        if tal[i] == tal[i-talc]:
            print "else", i
            svar += int(tal[i])

print svar
