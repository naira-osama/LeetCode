class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        result_dic  = defaultdict(list)

        for str in strs:
            new_key = [0] * 26

            for c in str:
                new_key[ord(c) - 97] += 1
                
            key = tuple(new_key)
            result_dic[key].append(str)

        result = []

        for val in result_dic.values():
            result.append(val)        


        return result