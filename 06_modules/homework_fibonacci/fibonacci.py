def fibonacci(n):

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def seq_fibonacci(n):
    fib = []
    for i in range(0, n):
        fib.append(fibonacci(i))

    return fib
