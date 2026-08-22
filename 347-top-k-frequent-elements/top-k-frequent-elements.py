from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        h = Counter(nums)

        n = len(nums)

        buckets = [0] * (n + 1)

        for key, val in h.items():
            if buckets[val] == 0:
                buckets[val] = [key]
            else:
                buckets[val].append(key)

        result = []

        for i in range(n, -1, -1):
            if buckets[i]:
                result.extend(buckets[i])
            if len(result) == k:
                break

        return result

