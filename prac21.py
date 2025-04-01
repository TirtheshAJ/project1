'''
class prac21:
    n=0
    def inp(self):
        self.n=int(input('enter anumber'))
    def output(self):
        print(self.n)

s=prac21()
s.inp()
s.output()
'''       
'''
class prac21:
    n=0
    def __init__(self,x):
        self.n=x
        print(self.n)
s=prac21(10)
'''
'''
class prac21:
    n=0
    def __init__(self,x=20):
        self.n=x
        print(self.n)
s=prac21(10)
'''
'''
class prac22:
    def area(self,l):
        self.s=l*l
        print('area of square',self.s)
    def area(self,l,b):
        self.r=l*b
        print('area of rectangle',self.r)
k=prac22()
k.area(5)
k.area(5,7)

'''
'''
import roman
class roman:
    def convert(self,n):
        return(roman.toRoman(n))
n=int(input('ente a num '))
r=roman()
r.convert(4)
'''

import math
class power:
    def cal(self,x,y):
        ans=(math.pow(x,y))
        print(ans)
p=power()
x=10
y=2
p.cal(x,y)

'''
import math
class power:
    def cal(self,x,y):
        print(math.pow(x,y))
p=power()
p.cal(2,6)
'''






        
