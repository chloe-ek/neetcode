class TimeMap:

    def __init__(self):
        # { key: [(timestamp1, value1), (timestamp2, value2), ...] }
        self.store = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        # if key exists
        values = self.store[key]

        left, right = 0, len(values) - 1
        res = ""
        
        while left <= right:
            mid = (left + right) // 2

            if values[mid][0] == timestamp:
                return values[mid][1]

            elif values[mid][0] < timestamp:
                res = values[mid][1]
                left = mid + 1

            else:
                right = mid - 1

        return res
        
