def find_primitive_roots(n):
  """
  Finds all primitive roots of a positive integer n.

  Args:
    n: A positive integer.

  Returns:
    A list of all primitive roots of n.
  """
  roots = []
  for a in range(2, n):
    if is_primitive_root(n, a):
      roots.append(a)
  return roots

def is_primitive_root(n, a):
  """
  Checks if a is a primitive root of n.

  Args:
    n: A positive integer.
    a: A positive integer.

  Returns:
    True if a is a primitive root of n, False otherwise.
  """
  if a < 1 or a >= n:
    return False
  if gcd(a, n) != 1:
    return False

  phi_n = euler_totient(n)
  for i in range(1, phi_n + 1):
    if pow(a, i, n) == 1 and i != phi_n:
      return False
  return True

def gcd(a, b):
  """
  Calculates the greatest common divisor of two non-negative integers.

  Args:
    a: A non-negative integer.
    b: A non-negative integer.

  Returns:
    The greatest common divisor of a and b.
  """
  while b:
    a, b = b, a % b
  return a

def euler_totient(n):
  """
  Calculates Euler's totient function for a positive integer n.

  Args:
    n: A positive integer.

  Returns:
    The number of positive integers less than n that are coprime to n.
  """
  phi = n
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      phi -= phi // i
      while n % i == 0:
        n //= i
        phi -= phi // i
  if n > 1:
      phi -= phi // n

  return phi

primes_under_100 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

for i in primes_under_100:
    roots = find_primitive_roots(i)
    if 2 in roots:
        print(i)