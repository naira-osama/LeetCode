class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        sorted_list = []
        for str in strs:
            l = list(str)
            slist = sorted(l)
            new_str = "".join(slist)
            sorted_list.append(new_str)



        h = defaultdict(list)
        for i in range(len(sorted_list)):
            h[sorted_list[i]].append(i)


        result = []

        for val in h.values():
            inner_list = []
            for i in val:
                inner_list.append(strs[i])
            result.append(inner_list)
        


        return result
