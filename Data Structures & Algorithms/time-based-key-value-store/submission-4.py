class TimeMap:

    def __init__(self):
        self.store = defaultdict(list) # { name : (timestamp, mood)}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        
        # key is not exist
        if key not in self.store:
            return ""
        # {name: [(1, "sad"), (2, "happy"), (3, "mad")]} 
        values = self.store[key] # [(1, "sad"), (2, "happy"), (3, "mad")]

        left, right = 0, len(values) - 1 # left = 0, right = 2
        res = ""
        
        while left <= right:
            mid = (left + right) // 2 # mid = 1

            if values[mid][0] == timestamp:
                return values[mid][1]

            elif values[mid][0] < timestamp:
                res = values[mid][1]
                left = mid + 1

            else:
                right = mid - 1

        return res
                


        

        


            

    
        
