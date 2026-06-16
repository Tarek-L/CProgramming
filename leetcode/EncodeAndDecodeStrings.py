class Solution:

    def encode(self, strs: List[str]) -> str:
        res = '["' + '","'.join(strs) + '"]'
        return res

    def decode(self, s: str) -> List[str]:
        append = False
        tmp  = ""
        res = []
        for i in s:
            if i == '"' and not append:
                append = True
                continue
            elif i == '"' and append:
                append = False
                res.append(tmp)
                tmp = ""
            if append:
                tmp += i
        return res

a = Solution()
print(type(a.encode(["hello","world"])))
print(type(a.decode(a.encode(["hello","world"]))))
print(a.encode(["hello","world"]))
print(a.decode(a.encode(["hello","world"])))

# this is wrong actual problem wants us to distinguish between strings ie strings can contain , [] '' "" so we will use a special charectere as a seperator and put length next to it
