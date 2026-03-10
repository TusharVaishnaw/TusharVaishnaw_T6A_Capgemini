class circle:
    def __init__(self):
        self.r=int(input('Enter radius: '))
    def area(self):
        a=self.r
        print('area is : ',a*a*22/7)
    def para(self):
        a=self.r
        print('paramter is: ', a*2*22/7)

c1=circle()
c1.area()
c1.para()
