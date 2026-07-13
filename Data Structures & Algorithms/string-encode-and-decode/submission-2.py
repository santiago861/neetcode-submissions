class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ''
        for s in strs:
            encoded_string += f'{len(s)}#{s}'
        return encoded_string

    def decode(self, s: str) -> List[str]:
        start, end = 0, 1
        result = []

        while start < len(s):
            if s[end] == '#':
                result.append(s[end+1 : end+1+(int(s[start : end]))])
                start = end+1+(int(s[start : end]))
                end = start + 1
            else:
                end += 1
        return result
 