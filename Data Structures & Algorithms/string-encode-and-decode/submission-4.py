class Solution:
    def encode(self, strs: List[str]) -> str:
        for i in range(len(strs)):
            strs[i] = str(len(strs[i])) + ':' + strs[i]
        return ''.join(strs)

    def decode(self, s: str) -> List[str]:
        strs = list()
        if (s == None or len(s) == 0):
            return []
        while s.find(':') != -1:
            l = int(s[:s.index(':')])
            start = s.index(':') + 1
            strs.append(s[start : start + l])
            s = s[start + l:]
        return strs

