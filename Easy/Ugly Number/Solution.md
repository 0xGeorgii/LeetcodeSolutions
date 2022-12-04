# 💡Python log(n) simple solution

# Intuition
- **Factorization** is a process of calculating prime factors for a given number.
- **Prime numbers** are numbers that can be divided on themselves and 1 with `mod=0`.
- **Factors** are multiplicators of a given number.

There is an algorithm to find prime factors for not big numbers and small prime factors – https://en.wikipedia.org/wiki/Quadratic_sieve

# Approach

- In our case the sieve is known – `(2, 3, 5)`
- Until `n == 1` (see the definition of prime numbers)
  - Try to divide `n` on numbers in `sieve` with `mod=0`
  - If can, then divide `n` on this number and continue
  - If cannot, return `false`

# Complexity
- Time complexity: log(n)
- Space complexity: O(1)

# Code
```
class Solution:
    def isUgly(self, n: int) -> bool:
        
        if n == 0: return False

        sieve = (2, 3, 5)

        while n != 1:
            for f in sieve:
               if n % f == 0:
                   n = n // f
                   break
            else:
                return False

        return True

```
