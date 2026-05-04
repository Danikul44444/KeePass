def hash(passwd: str, key: int) -> str:
    if len(passwd) > 0:
        elem: list = list()
        for x in passwd:
            elem.append(str(ord(x) + key))
        return " ".join(elem)
    return ""

def decode(code: str, key: int) -> str:
    if len(code) > 0:
        string: list = code.split(" ")
        for x in range(0, len(string)):
            string[x] = chr(int(string[x]) - key)
        return "".join(string)
    return ""

