class Solution:

    def encode(self, strs: List[str]) -> str:
        for i in range(0, len(strs)):
            strs[i] = f'{len(strs[i])}#{strs[i]}'
        
        one_liner = ''.join(strs)
        print(one_liner)
        return one_liner


        
    def decode(self, s: str) -> List[str]:
        res = []

        i = 0
        while i < len(s):
            # extract size
            size = ''
            while s[i] != '#':
                size = f'{size}{s[i]}'
                i += 1
            
            size_int = int(size)

            # move past # 
            i += 1

            # extract string
            res.append(s[i:i+size_int])
            i += size_int
            
        return res
            
        
