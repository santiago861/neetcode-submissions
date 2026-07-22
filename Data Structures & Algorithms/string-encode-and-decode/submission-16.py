class Solution:

    def encode(self, strs: List[str]) -> str:
        arr = []
        for s in strs:
            arr.append(f'{len(s)}#{s}')
        encoded = ''.join(arr)
        return encoded


    def decode(self, s: str) -> List[str]:
        l, r = 0, 0
        decoded = []

        while r < len(s):
            if s[r] == '#':
                word_length = int(s[l:r])
                decoded.append(s[r+1 : r+1+word_length])
                l = r+1+word_length
                r = l+1
            else:
                r += 1
        return decoded
