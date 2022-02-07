class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x:x[1])
        curr = 1
        ans = 0
        # print(courses)
        h = []
        for c in courses:
            if curr + c[0] -1 <= c[1]:
                heapq.heappush(h,-c[0])
                curr+=c[0]
                ans+=1
            else:
                if h and c[0] < abs(h[0]):
                    curr+=h[0]+c[0]
                    heapq.heappop(h)
                    heapq.heappush(h,-c[0])
        return ans                    