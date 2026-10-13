class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for i in strs:
            if tuple(sorted(i)) in d:
                d[tuple(sorted(i))].append(i)
            else:
                d[tuple(sorted(i))] = [i]
        return (list(d.values()))

# can be more optimal

    #     class Solution:
    # def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    #     res = defaultdict(list)
    #     for s in strs:
    #         count = [0] * 26
    # example = ord('e') - ord('a') = 101 - 97 = 4
    #         for c in s:
    #             count[ord(c) - ord('a')] += 1
    #         res[tuple(count)].append(s)
    #     return list(res.values())