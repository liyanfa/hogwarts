# -*- coding: utf-8 -*-
# @Time    : 2023/5/4 18:09
# @Author  : yanfa
# @user   : yanfa 
# @File    : hj6.py
# @remark:
"""
质数（Prime Number）是指
大于 1 的正整数中，除了 1 和它本身以外没有其他因数的数。换句话说，一个大于 1 的正整数 n 如果只能被 1 和 n 整除，那么 n 就是一个质数。
例如，2、3、5、7、11、13、17、19 等数都是质数，因为它们除了 1 和它本身以外没有其他因数可以整除它们。
质数在数学和计算机科学中都有广泛的应用。例如，RSA 公钥加密算法就是基于质数的分解难题设计的，其中质数的性质被用来保证加密和解密的安全性。在计算机科学中，质数也被用于生成哈希函数，构造一些随机数生成器等。

# 判断一个数是否为质数
def is_prime(n):

    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

质因子是指
质因子是指一个正整数能够被整除的所有质数因子的集合。换句话说，如果一个正整数 n 可以被质数 p 整除，那么 p 就是 n 的一个质因子。例如，24 的质因子包括 2、2 和 3，因为 24 可以被 2 和 3 整除，而 2 和 3 都是质数。
正整数的质因子分解是将该数表示为一系列质数的乘积的过程。例如，24 的质因子分解可以表示为 2 × 2 × 2 × 3，其中 2 和 3 是质数，且没有其他的质数可以整除 24。
质因子在数论、代数、计算机科学等领域中都有广泛的应用。例如，在密码学中，可以使用大质数的质因子来实现安全的公钥加密。在计算机科学中，可以使用质因子分解来对整数进行快速的因数分解，这在许多算法和数据结构中都有应用。"""
"""
描述
功能:输入一个正整数，按照从小到大的顺序输出它的所有质因子（重复的也要列举）（如180的质因子为2 2 3 3 5 ）

数据范围：
1≤n≤2×10e9+14

输入描述：
输入一个整数

输出描述：
按照从小到大的顺序输出它的所有质数的因子，以空格隔开。

示例1
输入：
180
复制
输出：
2 2 3 3 5
"""
# def is_prime(n):
#
#     if n < 2:
#         return False
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return True
# input_str = int(input())  # 输入一行字符串
# input_str_list=[i for i in range(1,input_str) if input_str%i==0]
# for i in range(2,input_str):

# for i in sorted(input_str_list):
#     print(i)
#     if is_prime(i)==True:
#         print(i)
#     else:
#         continue
import math
num = int(input())
s = ''
prime = 2
while prime < math.sqrt(num)+1:
    if num%prime != 0:
        prime += 1
    else:
        num = num //prime
        s += str(prime)+' '
        prime = 2
if num>=2:
    s += str(num)+' '
print(s)


