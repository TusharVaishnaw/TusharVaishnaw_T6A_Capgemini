#wap to find the sum of individual digits
def digsum(a):

    ans=0;
    while a>0:
        ans+=a%10
        a//=10
    return ans
print(digsum(int(input('enter a num: '))))
