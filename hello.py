def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
        if n == 3:
            return 'done'
    return 'done'

f = fib(6)
for n in f:
    print(n)