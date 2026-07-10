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
        
        arr = self.timemap[key]
        left = 0
        right = len(arr) - 1
        res = ""

        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid][1] == timestamp:
                return arr[mid][0]
            elif arr[mid][1] < timestamp:
                res = arr[mid][0] # track current best answer
                left = mid + 1
            else:
                right = mid - 1
        return res # return best answer

        
