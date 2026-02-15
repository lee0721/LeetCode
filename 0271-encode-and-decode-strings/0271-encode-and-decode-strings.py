class Codec:
    """NeetCode uses Codec class; LeetCode variants may call methods directly."""

    def encode(self, strs: List[str]) -> str:
        parts: List[str] = []
        for s in strs:
            parts.append(str(len(s)))
            parts.append('#')
            parts.append(s)
        return ''.join(parts)

    def decode(self, s: str) -> List[str]:
        res: List[str] = []
        i = 0
        n = len(s)

        while i < n:
            # find the delimiter '#' that ends the length field
            j = i
            while j < n and s[j] != '#':
                j += 1

            # Safety: if no '#', input is malformed
            if j == n:
                raise ValueError("Malformed encoded string: missing length delimiter")

            length = int(s[i:j])  # length can be 0
            i = j + 1

            # slice out the next `length` characters
            res.append(s[i:i + length])
            i += length

        return res