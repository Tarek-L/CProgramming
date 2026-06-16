#from collections import defaultdict
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#        ctr = defaultdict(int)
#        invctr = defaultdict(list)
#        for i in nums:
#            ctr[str(i)] += 1
#        for key, value in ctr.items():
#            invctr[str(value)].append(int(key))
#        pres = sorted(set(ctr.values()),reverse=True) 
#        maxi = pres[:k]
#        res = []
#        for i in maxi:
#            l = invctr[str(i)]
#            for i in l:
#                res.append(i)
#                if len(res) == k: break
#            if len(res) == k: break
#        return res
        ctr = Counter(nums)

        bucket = [[] for _ in range(len(nums)+1)]

        for num, freq in ctr.items():
            bucket[freq].append(num)

        res = []

        for freq in range(len(nums), 0, -1):
            for num in bucket[freq]:
                res.append(num)
                if len(res) == k:
                    return res

        return res
