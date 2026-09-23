class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        needs = defaultdict(list)
        # {course: [prerequisites]}
        for course, pre in prerequisites:
            needs[course].append(pre)

        visiting = set() # checking 
        done = set() # no cycle 

        def has_cycle(course):
            if course in visiting:
                return True
            if course in done:
                return False

            visiting.add(course)
            for pre in needs[course]:
                if has_cycle(pre):
                    return True
            visiting.remove(course)
            done.add(course)
            return False

        for course in range(numCourses):
            if has_cycle(course):
                return False
        return True 

