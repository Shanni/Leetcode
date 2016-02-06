class Solution:
    # @param n a integer
    # @return ans a integer
    def trailingZeros(self, n):
        five=[5]
        while n>five[-1]:
            five.append(five[-1]*5)
        ret=sum([n/x for x in five])
        return ret
