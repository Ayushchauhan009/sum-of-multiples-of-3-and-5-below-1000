# num=int(input("Enter the number:"))
# sum = 0
# for i in range(3, 10000):
#     if(i % 3 == 0 or i % 5 == 0):
#         sum += i
# print(sum)
import math


def multiples_of_3_5(n):
    p = math.floor(999/n)
    return math.floor(n*(p*(p+1)/2))


print(multiples_of_3_5(3)+multiples_of_3_5(5)-multiples_of_3_5(15))


# import math
# p = math.floor(1000/15)
# print(p)
