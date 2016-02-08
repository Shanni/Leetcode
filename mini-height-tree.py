class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        nodes=dict(zip(range(n),[set()]*n))
        degree=[0]*n
       
        for v1,v2 in edges:
            print v1,v2
            print nodes[v1]
            s1=nodes[v1]
            s2=nodes[v2]

            nodes[v1]=set(s1).add(v2)
            nodes[v2]=set(s2).add(v1)
            degree[v1]+=1
            degree[v2]+=1
            print nodes, degree
        while len(nodes) > 3:
            print degree
            for i in range(n):
               
                if degree[i]==1:
                    
                    for node in nodes[i]:
                        degree[node]-=1
                    print i
                    del nodes[i]
            print degree
        print nodes
        return nodes.keys()
s=Solution()
s.findMinHeightTrees(8,[[0,1],[1,2],[2,3],[0,4],[4,5],[4,6],[6,7]])