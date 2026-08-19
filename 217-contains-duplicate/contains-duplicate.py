class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        nums_dic = Counter(nums)
        
        return len(nums) != len(nums_dic)