num=50;
while(num>40):
    print(num)
    num-=1

n=0
while(n<=20):
    if(n%2==0):
        print(n)
        n+=1
    else:
        n+=1


numd=int(input('enter the number: '))
ans=0;
while numd>0:
    p=numd%10
    ans*=10
    ans+=p
    numd//=10
print(ans)

s1=input('enter any string: ')
l=len(s1)
s2=''
while(l>0):
    s2+=s1[l-1]
    l-=1
print(s2)
