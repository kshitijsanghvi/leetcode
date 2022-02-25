class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals = [[i[0],1] for i in intervals] + [[i[1],-1] for i in intervals]
        intervals.sort()
        
        room_count = 0
        max_room = -math.inf
        for i in intervals:
            room_count += i[1]
            max_room = max(max_room, room_count)
        return max_room
        
                
            