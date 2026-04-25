class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramsMap = defaultdict(list)
        for s in strs:
            alphas = [0]*26
            for c in s:
                alphas[ord(c)-ord('a')] += 1
            anagramsMap[tuple(alphas)].append(s)

        print(anagramsMap)

        return list(anagramsMap.values())