class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        mapping = {' ': ' '}
        i = 0
        res = ''
        letters = 'abcdefghijklmnopqrstuvwxyz'     
        for char in key:
            if char not in mapping:
                mapping[char] = letters[i]
                i += 1    
        for char in message:
            res += mapping[char]            
        return res
    

solution_instance = Solution()

result = solution_instance.decodeMessage(key = "the quick brown fox jumps over the lazy dog", message = "vkbs bs t suepuv")
print(result)

result = solution_instance.decodeMessage(key = "eljuxhpwnyrdgtqkviszcfmabo", message = "zwx hnfx lqantp mnoeius ycgk vcnjrdb")
print(result)

