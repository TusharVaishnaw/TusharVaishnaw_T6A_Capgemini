#wap to 2 to 5 numbs sum


def func(*s1):
    return sum(s1)

nums = list(map(int, input("enter 2 to 5 nums: ").split()))
print(func(*nums))


def func(*a):
    if(len(a)>=2 and len(a)<=5):
        return sum(a)
    else:
        return 'limit exceeded'
func(*eval(input('enter nums 2 to 5: ')))
