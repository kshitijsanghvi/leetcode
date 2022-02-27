class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        """
        Approach: 
        1. Key obseravation: We see that the range of nodes is [1,12] which hints we can use bitmasks [Fancy name for a bit array storing some information encoded in bits]
        2. The starting point and ending points are floating. This gives us a hint that we nevertheless will have to try all nodes as starting points
        
        3. The problem seems a flavor of Graph traversal Problem
        
        4. This gives an intuition of DFS and BFS
        
        5. We know BFS is quivalent of Dijkstras when all edges have equal weight 
        
        6. One constraint of BFS is that we never visited the nodes more than once. Additionally when we backtrack we add the distance by 1. In other words in any transisiton we add the distance by 1
        
        7. Here we have to backtrack due to lack of edges connecting all nodes
        
        8. We can solve this by expanding the visited key from just the node number to the node number and the state of all the visited nodes.
        9. Storing this value will help us not to traverse a given edge if we already explored and returned from it
        
        10. We put all the nodes as starting point in the queue and select the one giving the minimum distance
        
        11. Runtime Analysis, two variable numberOfNodes * Number of Possible states = N * 2^N Space and time both
        
        """
        
        # The number of nodes
        n = len(graph)
        
        # Edge case
        if n <= 1:
            return 0
        
        # Termiantion styate [n-1,..,0] bits are set to 1
        termination_state = 2 ** n - 1
        
        # Using deque so poping from head is O(1)
        queue = deque()
        
        # Visited set to keep track of the (currentNode,visitedNodeState) 
        v = set()
        
        # Adding all the sources
        for i in range(n):
            # appending the nth node and the state of ith bit set
            queue.append([i,1<<i,0])
            # Marking the currentNode,currentState visited
            v.add((i,1<<i))
            
        # Variable to keep track of the minimum distance, no trace needed
        min_ans = math.inf
        
        # While there are elements left to be explored
        while queue:
            # Take the head of the queue
            cn,cs,cd = queue.popleft()
            
            # if all the nodes are visited record the answer
            if cs == termination_state:
                # Taking the minimum of all valid traveresals
                min_ans = min(min_ans,cd)
                continue
            
            #Exploring next nodes
            for nn in graph[cn]:
                # What the new state is when we visit the next node too
                ns = cs | 1 << nn
                # Make sure we already havent explored this path before
                if (nn,ns) not in v:
                    # Visiting this path
                    v.add((nn,ns))
                    # Add the node to be explored
                    queue.append([nn,ns,cd+1])
        
        
        return min_ans