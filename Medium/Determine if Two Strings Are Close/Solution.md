# 💡Python O(n) simple solution

# Intuition
To solve this problem we need to figure out whether we can derive one string from another. To do that according to the rules (swap and substitution) there are two pieces requred:
1. the same set of letters (we cannot introduce new letters)
2. the same number of appearance among all charaters (so we can swap them)

# Approach
1. build a has map to count characters `char:num_of_occurrences`
2. compare the keys (characters are the same in both strings)
3. compare the values (the same numbers are presented in both strings)

**see the example:**

`word1 = "cabbba", word2 = "abbccc"`

| character (word1)  | number of occurrences (word1) | character (word2)  | number of occurrences (word2) |
|---|---|---|---|
| c | 1 | a | 1 |
| a | 2 | b | 2 |
| b | 3 | c | 3 |


# Complexity
- Time complexity: O(n)
- Space complexity: O(n)

# Code
```
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:

        cnt1 = Counter(word1)
        cnt2 = Counter(word2)

        v1 = list(cnt1.values())
        v1.sort()
        v2 = list(cnt2.values())
        v2.sort()

        if v1 != v2:
            return False

        v1 = list(cnt1.keys())
        v1.sort()
        v2 = list(cnt2.keys())
        v2.sort()

        return  v1 == v2

```
