# Substring XOR Queries

https://leetcode.com/contest/weekly-contest-332/problems/substring-xor-queries/

You are given a binary string `s`, and a 2D integer array `queries` where `queries[i] = [first i, second i]`.

For the `ith` query, find the shortest substring of `s` whose decimal value, `val`, yields `second i` when bitwise XORed with `first i`. In other words, `val ^ first i == second i`.

The answer to the ith query is the endpoints (0-indexed) of the substring `[left i, right i]` or `[-1, -1]` if no such substring exists. If there are multiple answers, choose the one with the minimum `left i`.

Return an array ans where `ans[i] = [left i, right i]` is the answer to the ith query.

A substring is a contiguous non-empty sequence of characters within a string.
