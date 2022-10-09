# The Employee That Worked on the Longest Task

https://leetcode.com/contest/weekly-contest-314/problems/the-employee-that-worked-on-the-longest-task/

There are `n` employees, each with a unique `id` from `0` to `n - 1`.

You are given a 2D integer array logs where `logs[i] = [idi, leaveTimei]` where:

- `id i `is the `id` of the employee that worked on the `ith` task, and
- `leaveTime i` is the time at which the employee finished the `ith` task. All the values `leaveTime i` are unique.

Note that the ith task starts the moment right after the `(i - 1)th` task ends, and the 0th task starts at time 0.

Return the `id` of the employee that worked the task with the longest time. If there is a tie between two or more employees, return the smallest `id` among them.
