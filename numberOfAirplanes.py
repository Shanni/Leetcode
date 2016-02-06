
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    # @param airplanes, a list of Interval
    # @return an integer
    def countOfAirplanes(self, airplanes):
        # write your code here
        schedule=[()]*(len(airplanes)*2)
        i=0
        for start,end in airplanes:
            schedule[i]=(start,1) 
            schedule[i+1]=(end,0)
            i+=2
        schedule.sort()
        count=0
        record_max=count
        for airplane,flag in schedule:
            if flag==1:
                count+=1
            else:
                count-=1
            record_max=max(record_max,count)
        return record_max

s=Solution()
print s.countOfAirplanes([[1,10],[2,3],[5,8],[4,7]])