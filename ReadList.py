

class ReadList:
    def readlist(path):
        with open(path, 'r', encoding='utf-8-sig')as senf:
            sens = senf.readlines()
            senf.close()
            return sens

    def writelist(lis, path):
        with open(path, 'w', encoding='utf-8') as f:
            for li in lis:
                f.write(li+'、')

    def writestr(str, path):
        with open(path, 'a', encoding='utf-8') as f:
            f.write(str)