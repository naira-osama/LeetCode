class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        
        for i in range(len(nums)):
            y = target - nums[i]

            if y in hashmap and hashmap[y] != i:
                return [i, hashmap[y]]