"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    # @param airplanes, a list of Interval
    # @return an integer
    def countOfAirplanes(self, airplanes):
        # write your code here
        schedule=[()]*(len(airplanes)*2)

        for i in range(len(airplanes)):
            schedule[i*2-1]=(airplanes[i].start,1) 
            schedule[i*2]=(airplanes[i].end,0)

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
                
            
