# a, b = 0, 1
#
# while a <= 100:
#     print(a, end=' ')
#     a, b = b, a + b


#verzija 2
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

print([fibonacci(i) for i in range(10)])
