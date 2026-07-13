class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_list = []

        for s in strs:
            encoded_list.append(f'{len(s)}#{s}')
        return ''.join(encoded_list)

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