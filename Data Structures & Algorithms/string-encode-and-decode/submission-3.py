class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for i in strs:
            length = len(i)
            encoded_string += f"{length}#{i}"
        return encoded_string

    def decode(self, s: str) -> List[str]:
        res = []
        j = 0
        i = 0
        while i < len(s):
            j = i
            length = ""
            while s[j].isdigit():
                length += s[j]
                j += 1
            start = j + 1
            end = (int(length) if length != '' else 0) + start
            i = end
            res.append(s[start:end])
        return res

            
            
