def findSep(self):
    text = self.text
    data = list(text)
    found="-1"
    for x in data:
        found=type(x)
        if (found != "-1"):
            break
    return found

def type(i):
    switcher={
                ' ':'space',
                ',':'comma',
                ';':'semi-colon',
                ':':'colon',
                '|':'ampersand',
                '.':'period',
             }
    return switcher.get(i,"-1")

