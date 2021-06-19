

class MyHash:
    def __init__(self, bucketSize) -> None:
        self.BUCKET = bucketSize
        self.table = [[] for x in range(bucketSize)]

    def findIdx(self, ele):
        return ele % self.BUCKET

    def insert(self, ele):
        idx = self.findIdx(ele)
        self.table[idx].append(ele)

    def remove(self, ele):
        idx = self.findIdx(ele)
        try:
            self.table[idx].remove(ele)
        except ValueError:
            pass

    def search(self, ele):
        idx = self.findIdx(ele)
        return ele in self.table[idx]
