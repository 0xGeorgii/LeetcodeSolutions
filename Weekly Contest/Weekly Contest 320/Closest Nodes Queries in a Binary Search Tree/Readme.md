# Closest Nodes Queries in a Binary Search Tree

https://leetcode.com/contest/weekly-contest-320/problems/closest-nodes-queries-in-a-binary-search-tree/

You are given the `root` of a binary search tree and an array queries of size `n` consisting of positive integers.

Find a 2D array answer of size `n` where `answer[i] = [min i, max i]`:

- `min i` is the largest value in the tree that is smaller than or equal to `queries[i]`. If a such value does not exist, add `-1` instead.
- `max i` is the smallest value in the tree that is greater than or equal to `queries[i]`. If a such value does not exist, add `-1` instead.

Return the array `answer`.
