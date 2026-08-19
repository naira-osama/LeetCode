class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        nums_dic = Counter(nums)

        for ele in nums_dic:
            if nums_dic[ele] > 1:
                return True
        

        return False