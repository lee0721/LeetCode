class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        parts = []
        for s in strs:
            parts.append(str(len(s)))
            parts.append("#")
            parts.append(s)
        return ''.join(parts)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        i = 0
        out = []
        while i < len(s):
            j = i
            while j < len(s) and s[j] != '#':
                j += 1
            num = int(s[i:j]) # not include j
            i = j+1
            out.append(s[i: i + num])
            i += num
        return out