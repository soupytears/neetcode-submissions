class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anas = dict()
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word in anas:
                anas[sorted_word].append(word)
            else:
                anas[sorted_word] = [word]
        return anas.values()