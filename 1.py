# a = input()

# dic = {}

# for i in a:
#     if dic.get(i):
#         dic[i] += 1
#     else:
#         dic[i] = 1

# l = []

# for k, v in dic.items():
#     l.append((v, k))

# print(dic)
# print(l)

# n = input()
# n = int(n)
# a, b = 0, 1
# for i in range(n):
#     a, b = b, a+b
# print(a)

# def isprime(n):
#     i = 2
#     while i <= n:
#         if n % i == 0:
#             break
#         i += 1
#     if i == n:
#         return True
#     else:
#         return False

# B = input()
# B = int(B)

# if B % 2 == 0:
#     i = 1
#     while i <= B:
#         j = B - i
#         if isprime(i):
#             if isprime(j) and i <= j:
#                 print('%d + %d = %d' %(i, j, B))
#         i += 1
# else:
#     print('不是偶数')

# import numpy as np
# mass = [ 50*i for i in range(1,12)] #这里偷懒用的列表推导式，python初学者可以百度一下，一看就懂
# length = [1.000,1.875,2.750,3.250,4.375,4.875,5.675,6.500,7.250,8.000,8.750]
# F = np.polyfit(mass,length,2) #按一次多项式拟合
# print(F) #输出各项系数
# P = np.poly1d(F)
# print(P) #输出方程式