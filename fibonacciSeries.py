# Fibonacci Series
n  =int(input("Enter end point for fibonacci series:\t"))
fib = lambda n: n if n < 2 else fib(n-1) + fib(n-2)
print("Fibonacci Result:\t", fib(n))