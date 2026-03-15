
 # Output: [[1,5],[6,9]]

#  trick is to take min of start intervals and max of end intervals we do this check when end of 
# interval is merging or greater thatn next upcoming interval
def inter(intervals,newInterval):
    res = []
    for i in range(len(intervals)):
        if newInterval[1] < intervals[i][0]:
            res.append(newInterval)
            return res + intervals[i:]
        elif newInterval[0] > intervals[i][1]:
            res.append(intervals[i])
        else:
            newInterval = [min(newInterval[0],intervals[i][0]),max(newInterval[1],intervals[i][1])]
    res.append(newInterval)

intervals = [[1,3],[6,9]]
newInterval = [2,5]
inter(intervals,newInterval)