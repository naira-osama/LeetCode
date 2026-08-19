class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_set = set(nums)
        print(nums_set)
    
        return len(nums) != len(nums_set) 