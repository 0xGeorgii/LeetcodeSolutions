# 💡Python log(n) simple solution

# Intuition

It is a very basic `binary search` case. The only trick we need to do in order to eliminate redundant search is check whether or not initial borders (i.e. `1` and `n`) are not an answer.

# Approach

1. Check left border
2. Check right border
3. Do binary search

# Complexity

- Time complexity: log(n)
- Space complexity: O(n)

# Code
```
    def guessNumber(self, n: int) -> int:

        l = 1
        res = guess(l)
        if res == 0: return l
        
        r = n
        res = guess(r)
        if res == 0: return r

        for _ in range(int(math.sqrt(n))):
            rn = (r+l) // 2
            res = guess(rn)
            if res == 0:
                return rn
            elif res < 0:
                r = rn
            else:
                l = rn

```
