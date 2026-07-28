class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # ans = defaultdict(list)
        # default dict me if key not in d wali line nahi likhni padegi
        d = {}
        for word in strs:
            key = ''.join(sorted(word))

            if key not in d:
                d[key] = []
            d[key].append(word)
        return list(d.values())