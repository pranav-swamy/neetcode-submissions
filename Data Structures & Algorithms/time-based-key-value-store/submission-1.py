class TimeMap:

    def __init__(self):
        self.timemap = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.timemap:
            self.timemap[key].append((value, timestamp))
        else:
            self.timemap[key] = [(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timemap:
            return ""
        
        values = self.timemap[key]
        l = 0
        r = len(values) - 1
        res = ""

        while l <= r:
            mid = l + (r-l) // 2
            if values[mid][1] == timestamp:
                return values[mid][0]
            elif values[mid][1] < timestamp:
                res = values[mid][0] # track currect best answer
                l = mid + 1
            else:
                r = mid - 1
        return res

        
