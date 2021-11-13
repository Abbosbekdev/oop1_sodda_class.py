# 1 - masala

# class Amal :
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#     def kopaytirish(self):
#         a = self.a
#         b = self.b
#         return a*b
#     def bolish(self):
#         a = self.a
#         b = self.b
#         return a/b
#     def qoshish(self):
#         a = self.a
#         b = self.b
#         return a+b
#     def ayirish(self):
#         a = self.a
#         b = self.b
#         return a - b
# x,y = int(input()),int(input())
# son = Amal(x,y)
# print(son.qoshish(),' ',son.bolish())
# print(son.kopaytirish(),' ',son.ayirish())

# 2 - masala

# class Uchburchak :
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#     def peremetr(self):
#         a = self.a
#         b = self.b
#         c = (a*a+b*b)**0.5
#         return a+b+c
#     def yuzasi(self):
#         return (self.a*self.b)/2
# a,b = int(input()),int(input())
# uchburchak = Uchburchak(a,b)
# print(uchburchak.yuzasi(),' ',uchburchak.peremetr())

# 3 - masala

import math


# class Aylana :
#     def __init__(self,r):
#         self.r = r
#     def peremetri(self):
#         return 2*math.pi*self.r
#     def yuzasi(self):
#         r = self.r
#         return math.pi*r*r
# r = int(input())
# aylana = Aylana(r)
# print('yuzasi : ',aylana.yuzasi())
# print('peremetri : ',aylana.peremetri())

# 4 - masala

# class Doira :
#     def __init__(self,s):
#         self.s = s
#     def radius(self):
#         return (self.s/math.pi)**0.5
# s = float(input())
# doira = Doira(s)
# print('radius : ',doira.radius())

# 5 - masala

# class Nuqta :
#     def __init__(self,x1,y1,x2,y2):
#         self.x1 = x1
#         self.x2 = x2
#         self.y1 = y1
#         self.y2 = y2
#     def masofa(self):
#         return ((self.x2-self.x1)**2+(self.y2-self.y2)**2)**0.5
# x1,x2 = float(input()),float(input())
# y1,y2 = float(input()),float(input())
# nuqta = Nuqta(x1,x2,y1,y2)
# print(nuqta.masofa())

# 6 - masala

# class Uchburchak :
#     def __init__(self,x1,x2,x3,y1,y2,y3):
#         self.x1 = x1
#         self.x2 = x2
#         self.x3 = x3
#         self.y1 = y1
#         self.y2 = y2
#         self.y3 = y3
#     def a(self):
#         return ((self.x2-self.x1)**2+(self.y2-self.y1)**2)**0,5
#     def b(self):
#         return ((self.x3-self.x2)**2+(self.y3-self.y2)**2)**0,5
#     def c(self):
#         return ((self.x3-self.x1)**2+(self.y3-self.y1)**2)**0,5
#     def yuzasi(self):
#         a = self.a()
#         b = self.b()
#         c = self.c()
#         p = (a+b+c)/2
#         return (p* (p-a)*(p-b)*(p-c))**0.5
# x1,x2,x3 = float(input()),float(input()),float(input())
# y1,y2,y3 = float(input()),float(input()),float(input())
# uchburchak = Uchburchak(x1,x2,x3,y1,y2,y3)
# print(uchburchak.yuzasi())

# 7 - masala

# class Son :
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#     def arifmetik(self):
#         return self.a/2+self.b/2
#     def geometrik(self):
#         return (self.a*self.b)**0.5
# a,b = int(input()),int(input())
# son = Son(a,b)
# print('arifmetik : ',son.arifmetik())
# print('geometrik : ',son.geometrik())

# 8 - masala

# class Tortburchak:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#     def yuzasi(self):
#         return self.a*self.b
# a,b = int(input()),int(input())
# tortburchak = Tortburchak(a,b)
# print(tortburchak.yuzasi())

# 9 - masala

# class Raqam :
#     def __init__(self,a):
#         self.a = a
#     def yigindisi(self):
#         a = self.a
#         s = 0
#         while a >0 :
#             s+=a%10
#             a//=10
#         return s
#     def kopaytmasi(self):
#         a = self.a
#         s =1
#         while a>0 :
#             s *= a%10
#             a //= 10
#         return s
# a = int(input())
# raqam = Raqam(a)
# print(raqam.yigindisi())

"""metodli classlarga doir masalalar"""

# 1 - masala

# class Son :
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#     def max(self):
#         a = self.a
#         b = self.b
#         if a>b :
#             return a
#         else:
#             return b
#     def min(self):
#         a = self.a
#         b = self.b
#         if a<b :
#             return a
#         else:
#             return b
# a,b = int(input()),int(input())
# son = Son(a,b)
# print(son.max(),' ',son.min())

# 2 - masala

# class Uchburchak :
#     def __init__(self,a,b,c):
#         self.a = a
#         self.b = b
#         self.c = c
#     def peremetri(self):
#         return self.a + self.b +self.c
#     def yuzasi(self):
#         p = self.peremetri()/2
#         a = self.a
#         b = self.b
#         c = self.c
#         return (p*(p-a)*(p-b)*(p-c))**0.5
# a,b,c =int(input()),int(input()),int(input())
# uchburchak = Uchburchak(a,b,c)
# print(uchburchak.yuzasi())

# 3 - masala

# class KattaKichik :
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#     def katta(self):
#         return max(self.a,self.b)
#     def kichik(self):
#         return min(self.a,self.b)
# a,b,c = int(input()),int(input()),int(input())
# katta_kichik = KattaKichik(a,b)
# print(max((c,katta_kichik.katta())))
# print(min(c,katta_kichik.kichik()))

# 5 - masala

# class Amal :
#     def __init__(self,n):
#         self.n = n
#     def yigindi(self):
#         s = 0
#         for i in range(1,self.n+1) :
#             s+=i
#         return s
#     def kopaytma(self):
#         s = 1
#         for i in range(1,self.n+1) :
#             s *= i
#         return s
# n = int(input())
# amal = Amal(n)
# print(amal.kopaytma())

# 6 - masala

# class Yigindi :
#     def __init__(self,n):
#         self.n = n
#     def yigindi(self):
#         s = 0
#         for i in range(self.n+1) :
#             s += i*i
#         return s
# n = int(input())
# yigindi = Yigindi(n)
# print(yigindi.yigindi())

# 7 - masala

# class Yigindi :
#     def __init__(self,n):
#         self.n = n
#     def yigindi(self):
#         a = list(range(1,self.n+1))
#         s = 0
#         j = 1
#         for i in range(len(a)) :
#             s+= a[i]*a[-j]
#             j+=1
#         return s
# n = int(input())
# ketma_ketlik = Yigindi(n)
# print(ketma_ketlik.yigindi())

# 8 - masala

# class Fibonachi :
#     def __init__(self,n):
#         self.n = n
#     def fib_yigindi(self):
#         a1,a2 = 1,1
#         s = 0
#         for i in range(self.n-2) :
#             c = a1+a2
#             a1 = a2
#             a2 = c
#             s +=c
#         s+= 2
#         return s
# n = int(input())
# fib = Fibonachi(n)
# print(fib.fib_yigindi())

# 9 - masala

# class Karrali :
#     def __init__(self,k,n):
#         self.n = n
#         self.k = k
#     def karrali(self):
#         n = self.n
#         k = self.k
#         a =[]
#         for i in range(1,n+1) :
#             a.append(k*i)
#         return a
# n,k =int(input()),int(input())
# karrali = Karrali(k,n)
# print(karrali.karrali())
