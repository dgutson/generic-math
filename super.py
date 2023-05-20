
def n(x: int) -> int:
    return x + 1

def p(x: int) -> int:
    return x - 1

def positive_op(a: int, op: int, b: int) -> int:
    """
    4 + 3 = 4 +1+1+1
    4 * 3 = 4 +4+4
    4 ^ 3 = 4 *4*4
    a opi b = a opi-1 (a opi b-1)

    a + b = next(a) + (b-1)

    a + b = next(a)... b veces

    3 + 2 = next(3) + 1
    next(3) + 1 = next(next(3)) + 0

    4 * 3 = 4 + (4*2)
    """
    if op == 0:
        return n(a)

    if b == 0:
        return a

    x = a
    for i in range(b-1 if op > 1 else b):
        x = positive_op(x, p(op), a)
    return x

def negative_op(a: int, op: int, b: int) -> int:
    if op == 0:
        return p(a)
    
    if b == 0:
        return a
    
    times = 1
    while positive_op(times, op, b) < a:
        times = times + 1
    
    return times if positive_op(times, op, b) == a else times - 1

def operation(a: int, op: int, b: int) -> int:
    if op >= 0:
        return positive_op(a, op, b)
    return negative_op(a, -op, b)

def factorial(n: int) -> int:
    if n == 0:
        return 1
    return operation(n, 2, factorial(n-1))

def main() -> int:
    print(operation(125, -3, 3))    # 125^(1/3)
    print(operation(16, -3, 2))     # square root: 16^(1/2)
    print(operation(8, -3, 2))      # log2(8)
    print(factorial(5))
    return 0

if __name__ == "__main__":
    main()