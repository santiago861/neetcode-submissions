class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ''

        for s in strs:
            encoded_str = encoded_str + f'{len(s)}#{s}'
        return encoded_str

    def decode(self, s: str) -> List[str]:
        l, r = 0, 0
        result = []

        while r < len(s):
            if s[r] == '#':
                result.append(s[r+1:r+1+int(s[l:r])])
                r += 1 + int(s[l:r])
                l = r
            else:
                r += 1
        return result