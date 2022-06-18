class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        len_nums = len(nums)
        left_sum = [0] * len_nums
        right_sum = [0] * len_nums
        
        running_left_sum = 0
        running_right_sum = 0
        for i in range(len_nums):
            left_sum[i] = running_left_sum
            right_sum[len_nums-1-i] = running_right_sum
            
            running_left_sum += nums[i]
            running_right_sum += nums[len_nums-1-i]
        
        # print(left_sum)
        # print(right_sum)
        for i in range(len_nums):
            if left_sum[i] == right_sum[i]:
                return i
        
        return -1