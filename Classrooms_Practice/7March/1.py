'''
def form(name,mail,ph,age=20,alt_ph=None):
    print(name)
    print(mail)
    print(ph)
    print(age)
    print(alt_ph)
form(mail='Tushar',name='vaishnawtushar@gmail.com',9509494140,alt_ph=89494949410)

def form(**a):
    print('a:',a)
    print(len(a))
form(a='Tushar',b='vaishnawtushar@gmail.com',c=9509494140)

def form(*a):
    print('a:',a)
    print(len(a))
form('Tushar','vaishnawtushar@gmail.com',9509494140)
'''
#Using all four types
#Positional, keyword, default and variable(dict/tuple) argument
def form(name,mail,*ph,age=20,alt_ph=None,**l1):
    print(name)
    print(mail)
    print(ph)
    print(age)
    print(alt_ph)
    print(l1)
form('Tushar','vaishnawtushar@gmail.com',9509494140,2123,123123,alt_ph=89494949410,a=1212,b=2323,c=23)
