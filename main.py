# This is a code line to write a leetcode problems :)


# Leetcode problem add  two sums:
# Given the arrays nums1 and nums2, return an array of their sums.
# Example 1:
# Input: nums1 = [1,2,3], nums2 = [4,5,6]
# Output: [5,7,9]


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        result = []
        carry = 0
        while l1 or l2:
            n1 = l1.val if l1 else 0
            n2 = l2.val if l2 else 0
            sum = n1 + n2 + carry
            carry = sum // 10
        result.append(sum % 10)
        l1 = l1.next
        l2 = l2.next
        return result

    # This is a code line to write a leetcode problems :)


Solution.addTwoNumbers([2, 3, 4], [5, 6, 7])  # Output: [7,0,0,0]
