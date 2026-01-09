def factorial(n):
    fact=lambda x:1 if x==0 else x*fact(x-1)
    return fact(n)

num=5
result= factorial(num)
print(result)