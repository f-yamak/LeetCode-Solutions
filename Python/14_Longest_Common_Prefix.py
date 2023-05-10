class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        for x in range(len(strs[0])):
            for y in range(1,len(strs)):
                if (x < len(strs[y]) and strs[y-1][x] == strs[y][x]):
                    continue 
                else:
                    return result
            result += strs[0][x]
        return result