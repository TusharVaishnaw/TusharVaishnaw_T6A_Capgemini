def prodl(l1):
    prod=1
    for i in l1:
        prod*=i
    return prod
l1=eval(input('enter the list: '))
print('product is: ', prodl(l1))
