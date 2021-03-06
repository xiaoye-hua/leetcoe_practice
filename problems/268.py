#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/19 7:45 下午
# @Author  : guohua08
# @File    : playground.py
from typing import List
import copy
import collections
import string

from src.linked_list.ListNode import ListNode
from src.linked_list.LinkedList import LinkedList


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        Similar solution as problem 41 (first missing positive)
        """
        for idx, value in enumerate(nums):
            while value <= len(nums) and value < len(nums):
                tmp = nums[value]
                nums[value] = float('inf')
                value = tmp
        # print(nums)
        for idx, value in enumerate(nums):
            if value != float("inf"):
                return idx
        return len(nums)


# Input: nums = [3,0,1]
# Output: 2
# Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
nums = [3, 0, 1]
res = Solution().missingNumber(nums)
print(res)