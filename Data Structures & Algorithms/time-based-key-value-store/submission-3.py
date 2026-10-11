class TimeMap:

    def __init__(self):
        self.timemap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.timemap:
            self.timemap[key].append((value, timestamp))
        else:
            self.timemap[key] = [(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timemap:
            return ""
        
        left = 0
        right = len(self.timemap[key])-1

        values = self.timemap[key]
        res = ("", 0)

        while left <= right:
            mid = (left + right) // 2

            if values[mid][1] == timestamp:
                return values[mid][0]

            if values[mid][1] < timestamp:
                res = values[mid]
                left = mid+1
            else:
                right = mid-1
        
        return res[0]

        
