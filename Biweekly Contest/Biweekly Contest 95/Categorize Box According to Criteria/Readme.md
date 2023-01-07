# Categorize Box According to Criteria

https://leetcode.com/contest/biweekly-contest-95/problems/categorize-box-according-to-criteria/

Given four integers `length`, `width`, `height`, and `mass`, representing the dimensions and mass of a box, respectively, return a string representing the category of the box.

The box is `"Bulky"` if:
- Any of the dimensions of the box is greater or equal to `1e4`.
- Or, the volume of the box is greater or equal to `1e9`.

- If the mass of the box is greater or equal to `100`, it is `"Heavy"`.
- If the box is both `"Bulky"` and `"Heavy"`, then its category is `"Both"`.
- If the box is neither `"Bulky"` nor `"Heavy"`, then its category is `"Neither"`.
- If the box is `"Bulky"` but not `"Heavy"`, then its category is `"Bulky"`.
- If the box is `"Heavy"` but not `"Bulky"`, then its category is `"Heavy"`.

Note that the volume of the box is the product of its length, width and height.
