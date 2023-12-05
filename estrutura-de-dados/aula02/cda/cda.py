def fibonacci(n):
    if n > 1:
        return fibonacci(n-1) + fibonacci(n-2)
    else:
        return n
    
print(fibonacci(20))