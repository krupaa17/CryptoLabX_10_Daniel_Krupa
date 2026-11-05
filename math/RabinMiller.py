import secrets
import time
from Crypto.Util.number import isPrime

BITS = 512
ROUNDS = 20

BASES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
         31, 37, 41, 43, 47, 53, 59, 61, 67, 71]

def miller_rabin(n, bases):
    if n < 2:
        return False

    if n in (2, 3):
        return True

    if n % 2 == 0:
        return False

    d = n - 1
    s = 0

    while d % 2 == 0:
        d //= 2
        s += 1

    for a in bases:
        a %= n

        if a in (0, 1):
            continue

        x = pow(a, d, n)

        if x == 1 or x == n - 1:
            continue

        for _ in range(s - 1):
            x = pow(x, 2, n)

            if x == n - 1:
                break
        else:
            return False

    return True


def generate_prime(bits, bases):
    candidates_tested = 0
    start = time.perf_counter()

    while True:
        candidate = secrets.randbits(bits)
        candidate |= (1 << (bits - 1)) | 1

        candidates_tested += 1

        if miller_rabin(candidate, bases):
            elapsed = time.perf_counter() - start
            return candidate, candidates_tested, elapsed


prime, count, elapsed = generate_prime(BITS, BASES)

print("Generated prime candidate:", prime)
print("Actual bit length:", prime.bit_length())
print("Candidates tested:", count)
print("Miller-Rabin rounds:", len(BASES))
print("Execution time:", round(elapsed, 6), "seconds")

print("Miller-Rabin verification:",
      miller_rabin(prime, BASES))

print("Independent library verification:",
      isPrime(prime))
