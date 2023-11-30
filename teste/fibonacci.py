# 0 1 1 2 3 5 8 13 21 34

def fibo(n):
    if n <= 1:
        return 0
    elif n == 2 or n == 3:
        return 1
    else:
        return fibo(n - 2) + fibo(n - 1)
    

print(fibo(1))
print(fibo(5))
print(fibo(10))
print(fibo(15))
print(fibo(20))
print(fibo(25))
print(fibo(30))
print(fibo(35))
print(fibo(40))
print(fibo(45))