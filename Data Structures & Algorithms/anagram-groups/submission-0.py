from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupby = defaultdict(list)
        for s in strs: 
            key = "".join(sorted(s))
            groupby[key].append(s)
        return list(groupby.values())

        