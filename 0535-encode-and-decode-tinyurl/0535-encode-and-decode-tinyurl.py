BASE62 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
class Codec:
    def __init__(self):
        self.code_to_url = {}
        self.counter = 0
        self.prefix = "http://tinyurl.com/"

    def _base62_encode(self, num: int) -> str:
        out = []
        base = len(BASE62)
        while num > 0:
            num, r = divmod(num, base)
            out.append(BASE62[r])
        return "".join(reversed(out))

    def encode(self, longUrl: str) -> str:
        self.counter += 1
        code = self._base62_encode(self.counter)
        self.code_to_url[code] = longUrl
        return self.prefix+code

    def decode(self, shortUrl: str) -> str:
        code = shortUrl.split("/")[-1]
        return self.code_to_url[code]