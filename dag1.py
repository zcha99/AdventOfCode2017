#-*- coding: UTF-8 -*-

tal = raw_input('Captcha? ') #submit the number given
svar = 0 #Sum before start is 0
if tal[:1] == tal[-1:]: #check first and last digit
    global svar
    svar += int(tal[:1]) #add to answer

for i in range(len(tal)): #check rest of the numbers
    global svar
    if tal[i:i+1] == tal[i+1:i+2]:
        svar += int(tal[i:i+1]) #add to answer

print svar #This is the answer to the puzzle
