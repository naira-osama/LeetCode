from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        h = Counter(nums)
        topfreq = h.most_common(k)

        result = []

        for ele in topfreq:
            result.append(ele[0])
        
        return result
  