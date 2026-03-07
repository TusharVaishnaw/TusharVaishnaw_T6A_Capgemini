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
'''

def form(*a):
    print('a:',a)
    print(len(a))
form('Tushar','vaishnawtushar@gmail.com',9509494140)
