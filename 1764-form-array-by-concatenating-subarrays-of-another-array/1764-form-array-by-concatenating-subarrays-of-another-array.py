class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        curr_group = 0
        col_len = len(groups[curr_group])
        row_len = len(groups)
        
        i = 0
        while i < len(nums)-col_len+1:
            sub_nums = nums[i: i+col_len]
            if sub_nums == groups[curr_group]:
                curr_group += 1
                i += col_len - 1
                
                if curr_group == row_len:
                    return True
                col_len = len(groups[curr_group])
            i += 1
        
        return False
        # if curr_groups != row_len:
        #     return False
        # else:
        #     return True