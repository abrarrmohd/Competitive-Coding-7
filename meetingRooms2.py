"""
Approach: to see what's the max conflicts- we can use a minHeap with end times which will have all the 
meetings in the heap that do not end by current time
t.c. => O(nlogn)
s.c. => O(n)
"""
from heapq import heappop, heappush
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        minHeap = [] #will have end times
        minRooms = 0 
        
        for start, end in intervals:
            while minHeap and minHeap[0] <= start:
                heappop(minHeap)
            heappush(minHeap, end)
            minRooms = max(minRooms, len(minHeap)) 
        return minRooms