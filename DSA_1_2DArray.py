#2D array - Matrix computation

mat = [[1,2,3], 
       [4,5,6],
       [7,8,9]]

mem1 = mat[0][0]
print("member at 0x0 index is", mem1)

mem2 = mat[1][2]
print("member at 1x2 index is", mem2)

mem3 = mat[2][2]
print("member at 3x3 index is", mem3)


#application of array 1# insertion and deletion
'''linked list is preferable instead of array due to its
constant space complexity instead of O(n)'''
#application of array 2# sorting- ascending and descending
'''concept of sorting algorithm
1. in-place sorting- no extra space/ no external data structure is used
2. out-place sorting- extra space/ external data structure is used (merge sort)'''


#leetcode 75 - sort colors
from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        p0 = 0
        curr = 0
        p3 = 0
        #p4 = 0
        p2 = n - 1

        while curr <= p2:
            if nums[curr] == 0:
                nums[curr], nums[p0] = nums[p0], nums[curr]
                p0 += 1
                curr += 1
            elif nums[curr] == 2:
                nums[curr], nums[p2] = nums[p2], nums[curr]
                p2 -= 1
            elif nums[curr] == 3:
                nums[curr], nums[p3] = nums[p3], nums[curr]
                p3 -= 1
            #elif nums[curr] == 4:
            #    nums[curr], nums[p4] = nums[p4], nums[curr]
            #    p4 += 1
            else:
                curr += 1

# Example Usage:
nums = [2, 3, 0, 2, 1, 3, 1, 0, 3]
solution = Solution()
solution.sortColors(nums)
print(nums)  # Output should be [0, 0, 1, 1, 2, 2]
