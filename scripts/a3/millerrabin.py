import random

def miller_rabin(n, a):
    """Performs the Miller-Rabin primality test on n with base a, with debug statements."""

    print(f"Testing n = {n} with base a = {a}")

    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    # Find values for d and s: n - 1 = 2^s * d, with d odd
    s = 0
    d = n - 1
    while d % 2 == 0:
        s += 1
        d //= 2
    print(f"n - 1 = 2^s * d, where s = {s} and d = {d}")

    # Compute x = a^d (mod n)
    x = pow(a, d, n)
    print(f"x = a^d (mod n) = {a}^{d} (mod {n}) = {x}")

    if x == 1 or x == n - 1:
        return True

    # Test for composite through the s iterations
    for r in range(s - 1):
        print(f"Iteration {r}:")
        old_x = x
        x = pow(x, 2, n)
        print(f"  x = x^2 (mod n) = {old_x}^2 (mod {n}) = {x}")
        if x == 1:
            return False
        if x == n - 1:
            return True

    return False  # If none of the above conditions, n is composite

# Get input 
n = int(input("Enter a number to test: "))
a = int(input("Enter a base value: "))

if miller_rabin(n, a):
    print(n, "is probably prime")
else:
    print(n, "is composite")
