# LINK: https://leetcode.com/problems/insert-interval/description/

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        [newStart, newEnd] = newInterval
        for i in range(len(intervals)):
            # if the current interval's start is after the newInterval's end,
            # we have reached the position to add newInterval to our result (AKA goal state)
            if newEnd < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            # if the current interval's end is before the newInterval's start,
            # add the current interval to the result 
            elif newStart > intervals[i][1]:
                res.append(intervals[i])
            # otherwise, if we have conflicting intervals, merge them
            # by updating newInterval
            else:
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1])
                ]
        # if intervals is an empty list, it will not enter the for loop (or exit)
        # thus, we need to append the newInterval to res in this scenario
        res.append(newInterval)
        return res

