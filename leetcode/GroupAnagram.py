from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        anamap = defaultdict(list)
        for s in strs:
            anamap[''.join(sorted(s))].append(s)
        for v in anamap.values():
            res.append(v)
        return res
