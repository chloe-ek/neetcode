class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        # Sort the position, speed by descending order 
        pairs = sorted(zip(position, speed), reverse=True)

        stack = [] 
        # Get each time to be at destination 
        for pos, spd in pairs:
            time = (target - pos) / spd

            if not stack:
                stack.append(time)

            if stack[-1] >= time:
                continue
                
            else:
                stack.append(time)


        return len(stack)