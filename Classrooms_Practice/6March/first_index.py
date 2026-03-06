#wap to print the inital index of a char
#present in a given string
def func(s,ch):
    cnt=0
    for i in s:
        if i==ch:
            return cnt
        cnt+=1

s=input('enter the string: ')
ch=input('enter the char to be searched: ')
print('first index is: ',func(s,ch))
