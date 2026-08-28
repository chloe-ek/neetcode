class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        task_counter = Counter(tasks)

        max_freq = max(task_counter.values()) 

        count = 0 
        for v in task_counter.values():
            if v == max_freq:
                count += 1

        max_count = count

        frame = (max_freq - 1) * (n + 1) + max_count


        return max(frame, len(tasks))


            
        