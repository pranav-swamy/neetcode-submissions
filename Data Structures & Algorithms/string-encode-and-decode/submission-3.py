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
            
            # move past #
            i += 1

            # extract string
            size_int = int(size)
            string = ''
            k = 0
            while k < size_int:
                string = f'{string}{s[i]}'
                i += 1
                k += 1
            res.append(string)
        return res
            
        
