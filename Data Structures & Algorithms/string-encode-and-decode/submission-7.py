class Solution:

    def encode(self, strs: List[str]) -> str:
        # encode like this - {len}{word}{#}*
        res = ""
        for s in strs:
            res = f'{res}{len(s)}#{s}'
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        
        i = 0
        while i < len(s):
            j = i
            while j < len(s) and s[j].isdigit():
                j += 1
            num = int(s[i:j])
            i = j+1 
            word = s[i:i+num]
            res.append(word)
            i = i+num
        return res


