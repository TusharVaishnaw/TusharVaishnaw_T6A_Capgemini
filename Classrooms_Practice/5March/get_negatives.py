def func(a) :
    ans=[]
    for i in a:
        if i < 0:
            ans.append(i)
    print(ans)

a = eval(input("Enter list: "))
func(a)
