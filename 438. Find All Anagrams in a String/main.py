import string
from typing import List
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ns = len(s)
        np = len(p)
        result = []
        if np > ns: return result
        count = {c: 0 for c in string.ascii_lowercase}
        for c in p:
            count[c] += 1
        for c in s[:np]:
            count[c] -= 1
        if all([c==0 for _,c in count.items()]):
            result.append(0)
        for i in range(np, ns):
            count[s[i-np]] += 1
            count[s[i]] -= 1
            if all([c==0 for _,c in count.items()]):
                result.append(i-np+1)
        return result

s = "baa"
p = "aa"

r = Solution().findAnagrams(s, p)
print(r)