def fibonacci(max_val):
    a = 0
    b = 1
    while a < max_val:
        print(a)
        a, b = b, a + b

fibonacci(10)
