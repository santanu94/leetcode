# Revisit
### Graph
```
Tips: Use BFS/DFS from sorce to destination if question is:
- Can I go from cell A to cell B?
- How far can I reach from this point?
- What is the shortest/longest path from A to B?

  Use BFS/DFS from destination(s) (i.e. reverse) when:
- From which cell can water/air/people reach X?
- What are all possible startig points that can eventually reach this end conditioon?
```
```
Tips: When to use disjoint set union:
- Problems revolve around groups, components or connectivity.
- Problem says: check if there is cycle in undirected graph
- Problem says: These things are similar/belong together/can be merged based on some condition
- Problem says: detect whether adding an edge would create a cycle or while sorting edges whether to include them
- There are repeated online queries about connectedness over time (maybe if two nodes are connected after K updates)

Don't use Union Find when:
- Directed graph with cycles
- You need shortest path or distances
- Order matters (e.g., topological sorting)
- You need to explore actual paths
```
```
Use BFS when you want the shortest number of steps in an unweighted graph
Typical Scenarios:
- All eedges have same cost (unit cost)
- Grid traversal problems (minimum steps)
- Finding shortest path in maze using only directions (↑↓←→)
- First occurance/closest solution needed
- Tree order level traversal

Use DFS when you want to explore all paths or components deeply
Typical use case:
- Find all paths/combinations (backtracking)
- Cycle detection in a graph
- Topological sort
- Connected components/island counting
- Reachability/path existance

Use Dijkstra's Algorithm when you want to find the minimum total cost/time/distance in a weighted graph with positive weighths
Typical use cases:
- Weighted graph (positive weights only)
- Find shorted path from source to all nodes (positive weights only)
- Optimize delivery/network/signal time
- Cost vary and must be minimized

Quick Decision Table
--------------------

Graph Type                                         Goal                        Use
__________                                         ____                        ___
Unweighted                                     Shortest path                   BFS
Weighted (poositive)                           Shortest path                 Dijkstra
Weighted (0/1 edges)                           Shortest path                 0-1 BFS
Weighted (may include negatives)               Shortest path               Bellman-Ford
Unweighted                            No path required, just explore         BFS/DFS
Unweighted                            All paths or full tree explore           DFS
Unweighted                                Early solution needed                BFS
```
`Tip: If we can update a grid during BFS (e.g., Rotting Oranges) then we don't need visited set, but if we can't then we do need visited.`
- [Detect cycle in undirected graph](https://www.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=practice_card)
- [42. Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water)
- [15. 3Sum](https://leetcode.com/problems/3sum/description)
- [31. Next Permutation](https://leetcode.com/problems/next-permutation/description)
- [48. Rotate Image](https://leetcode.com/problems/rotate-image/submissions/1439548326)
  hint: transpose + reverse
- [49. Group Anagrams](https://leetcode.com/problems/group-anagrams/submissions/1440056199)
  hint: without sorting -> take `arr = [0] * 26`, for every character, `arr[ord(ch) - ord('a')] += 1`. This will sort each woord. Use `str(arr)` as key.
- [1329. Sort the Matrix Diagonally](https://leetcode.com/problems/sort-the-matrix-diagonally/description)
  hint: ![diagonal movement](hint/img/diagonal.png)
- [724. Find Pivot Index](https://leetcode.com/problems/find-pivot-index/description/)
  hint: although this looks like a two pointer, but we should use two pointer primarily when we intend to reduct the range or we can find definite answe with the two pointers. In this case use cumulitive/prefix sum.
- [36. Valid Sudoku](https://leetcode.com/problems/valid-sudoku/description/)
  hint: ![selecting quare block in matrix](hint/img/select_square_block.png)
  in order to group `n*n` block in a 2D matrix, divide rows by n and columns by n. [Full Video Solution](https://www.youtube.com/watch?v=TjFXEUCMqI8)
- [976. Largest Perimeter Triangle](https://leetcode.com/problems/largest-perimeter-triangle/description/)
  hint: in oorder to find largest perimeter of a triangle, we can sort it and start from last. if the last (greatest) 3 number don't follow `side1 + side2 > side3`, `side2 + side3 > side1` and `side3 + side1 > side2` then omit greatest and check next 3 greatest numbers. Because if side[n], side[n-1] and side[n-2] can't form tringle then it means `side[n-1] + side[n-2] < side[n]`. So ideally we can only check if `side[n-1] + side[n-2] > side[n]` we can return their sum.
- [645. Set Mismatch](https://leetcode.com/problems/set-mismatch/description)
  hint: whenever input is an array with elements 1-n where n is size of array, this is a hint that we can use element value to go to an index by doing `arr[arr[i] - 1]`. Here we can first traverse the array and for each i set `arr[arr[i] - 1] = - arr[arr[i] - 1]` if `arr[arr[i] - 1] > 0`, but if the value is negative then we have already visited this index, and arr[i] is the duplicate. We can traverse the array one last time to find the only postive number in the array. the missing number is index of the only positive number + 1. 
- [523. Continuous Subarray Sum](https://leetcode.com/problems/continuous-subarray-sum/description/)
  hint: we cannnot use sliding window here because we don't know how to reduce the window size. So we will use a math property if num % k = x, the (num + multiple of k) % k = x, e.g., 31 % 4 = 3, (31 + 12) = 43, 43 % 4 = 3.
  ![continuous_subarray_sum](hint/img/continuous_subarray_sum.png) 
- [Stock Buy and Sell – Multiple Transaction Allowed](https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/stock-buy-and-sell2615)
  hint: because there is a dependency such that we can buy after we sell, i.e., when we loop through the loop, after we see a small number, we cannot pair it with a large number that has come before, we can only pair it with a large number in the future. So what we should do is, as soon as we encounter a small number, we should reset the large number as well. This ensures that we only look forward and not behind.
  ![stock_buy_sell_multiple](hint/img/stock_buy_sell_multiple.png)
- [Stock Buy and Sell – Max one Transaction Allowed](https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/buy-stock-2)
  hint: becuse we can only look forward, instead of using a window (we cannot use a window because we have no way of reducing it), we can use double pointers that move from left to right, one pointer to mark sell and one to mark buy. Since we cannot sell before buy, i.e., we cannot pair current low value with any large value previously seen, we have to reset the sell pointer everytime we move the buy pointer.
  ![stock_buy_sell_singel](hint/img/stock_buy_sell_single.png)
- [Kadane's Algorithm](https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/kadanes-algorithm-1587115620)
  hint: for max subarray we are more interested in max sum produced by +ve numbers.
  [Video Reference](https://www.youtube.com/watch?v=AHZpyENo7k4)
- [Maximum Product Subarray](https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/maximum-product-subarray3604)
  hint: this can be solved with slight modification to kadane's algorithm. All we need to do is do a forward pass and the a backward pass. This helps eliminate odd number of -ve numbers.
  ![maximum_product_subarray_my_kadane](hint/img/maximum_product_subarray_my_kadane.png)
  [Video Reference](https://www.youtube.com/watch?v=hnswaLJvr6g)
- [990. Satisfiability of Equality Equations](https://leetcode.com/problems/satisfiability-of-equality-equations/description/)
  hint: create graph by connecting all nodes with "==". Then, for each "a!=b", check if we can reach "b" from "a" by graph traversal. If we can then there is contradiction.
- [Max Circular Subarray Sum](https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/max-circular-subarray-sum-1587115620)
  hint - [Video Reference](https://www.youtube.com/watch?v=Za8V4wkZKkM)
- [210. Course Schedule II](https://leetcode.com/problems/course-schedule-ii/description/)
- [207. Course Schedule](https://leetcode.com/problems/course-schedule/)
- [1129. Shortest Path with Alternating Colors](https://leetcode.com/problems/shortest-path-with-alternating-colors/description/)
  hint: with bfs, if path count is needed, most of the time path count should be added to queue along with neighbour nodes. Plus if graph is bi-directional with different weights along different directions, then for visited set, we also need to add in this format `f"{nei}_{nei_edge}"` because if we just chech `if nei in visited: continue` then we don't take into account this neighbor revisiting through a different edge. Check submitted solution.
- [1319. Number of Operations to Make Network Connected](https://leetcode.com/problems/number-of-operations-to-make-network-connected/description/)
  hint: if this case we are not just checking cycle, we are counting the number of edges we have that makes a cycle (i.e., number of cycles), e.g., A<->B<->C<->A, here C<->A edge can be removed. To do this we need to cache C<->A edge as well, or else we can go through ths edge twice, once via A<->B<->C<->A and once via A<->C. So even if a node is already visited, we need to check if the same edge was used to form a previous cycle.
- [417. Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/description/)
  hint: the question says, we have to go from a cell to both ocean, so we have one source and two destinations. Hence it is better to do dfs/bfs in reverse. [DFS Code](https://leetcode.com/problems/pacific-atlantic-water-flow/submissions/1677660719/) [BFS Code](https://leetcode.com/problems/pacific-atlantic-water-flow/submissions/1677673026/)
- [Graph Valid Tree](https://neetcode.io/problems/valid-tree)
  hint: we can solve this with 2 approaches.
- []()
  hint: we obviously need to use dijkstra algo, but there is a twist. Unlike dijkstra, we cannot use a visited set or distance dictionary, because in dijkstra we visit each node only once with the cheapest cost, but in this case it is possible that the cheapest path takes up too many intermediate steps and doesn't each the destination, but a more expensive but direct path reaches the destination within the given number of steps. Hence we should explore all paths. [Solution](https://leetcode.com/problems/cheapest-flights-within-k-stops/submissions/1699447383/). This solution has a catch, it takes up too much time for large graphs. In order to optimize the time we can fall back to visited set idea, but instead of removing all paths that lead to node n after the shortest, we cache (node, steps). [Optimized Solution](https://leetcode.com/problems/cheapest-flights-within-k-stops/submissions/1699455697/)
DFS Traversal Code:
```
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {i: [] for i in range(n)}
        
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = set()

        def dfs(node, parent):
            # if we are able to reach a node in multiple ways, then it cannot be a tree
            if node in visited:
                return False
            
            visited.add(node)
            for nei in adj[node]:
                if nei == parent:
                    continue
                
                if not dfs(nei, node):
                    return False
            
            return True
        
        # We should call this function only once, otherwise it will always return False
        if not dfs(0, -1):
            return False
        
        # in a graph there should not be any unreachable node
        if n == len(visited):
            return True
        else:
            return False
```
Union Find Code:
```
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {i: [] for i in range(n)}
        
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = set()

        def dfs(node, parent):
            # if we are able to reach a node in multiple ways, then it cannot be a tree
            if node in visited:
                return False
            
            visited.add(node)
            for nei in adj[node]:
                if nei == parent:
                    continue
                
                if not dfs(nei, node):
                    return False
            
            return True
        
        # We should call this function only once, otherwise it will always return False
        if not dfs(0, -1):
            return False
        
        # in a graph there should not be any unreachable node
        if n == len(visited):
            return True
        else:
            return False
```
Time Complexity: O(V) [because we are always updating parent[x] find function time complexity is very close to 1]
Space Complexity: O(V) [to store parent array]
- [994. Rotting Oranges](https://leetcode.com/problems/rotting-oranges/description/)
  hint: multi point BFS. [Solution](https://leetcode.com/problems/rotting-oranges/submissions/1680221570/)
### Linked List
`Tip: if we need to maintain order like a list, but also be able to change order of elements inside the list in time O(1), instead of O(n), we should use linked list.`

```
Tip: If we are frequently inserting or deleting nodes at both ends (head/tail) or in the middle, it is almost always better to use dummy head and tail nodes. This will remove edge case checks like:
if node.next is not None and node.prev is not None:
  node.next.prev = node.prev.Next
```
- [237. Delete Node in a Linked List](https://leetcode.com/problems/delete-node-in-a-linked-list/description/)
  hint: in order to remove node we need prev node, but here there is no way of accessing prev node. So we will instead traverse the linked list till the end and replace current node value with next value and finally drop the last node.
- [142. Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/description/)
  hint: [Video Reference](https://www.youtube.com/watch?v=vlrxs-LPni4&list=PLpIkg8OmuX-LH398-_ZcuHiRueOdsJbXU&index=5)
- [382. Linked List Random Node](https://leetcode.com/problems/linked-list-random-node/description)
  hint: consider linked list `[a, b, c, d, e, f]`. Prob of selecting a is 1. Then looking at prob of not changing (i.e., selecting) `a` between `a` and `b` is 1/2, then prob of not changing `a` between `a`, `b` and `c` is 2/3, next 3/4, .... n-2/n-1, n-1/n. So if we multiply all of them, the final prob of selecting is 1/n. Check submission.
- [109. Convert Sorted List to Binary Search Tree](https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/description/)
  hint: time complexity nlogn. Recursive divide and conquere (binary search). Recurssively find mid point, attach left and right. Check solution.
- [23. Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/description/)
  hint: [Video Reference](https://www.youtube.com/watch?v=Q64u-W3l3mA&list=PLpIkg8OmuX-LH398-_ZcuHiRueOdsJbXU&index=8) time complexity klogn. My solution time complexity kn.
- [1171. Remove Zero Sum Consecutive Nodes from Linked List](https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/description/)
  hint: if we have to remove consecutive nodes which sum up to 0, then cumulative sum before and after the consecutive nodes should be the same. We can save the cumulative sum in a dict as key and corresponding node as value. While traversing through the linked list, if a cumulative sum is already present in our dict, then we found a consecutive section of nodes summing to 0. We can set the next of the node value of the dict entry to current node->next. We need to iterate through these consecutive nodes and remove their entries from the dict. Finally add a dummy head to the linked list to handle original head being part of the consecutive nodes summing up to 0. At the end we can return dummy node->next as output. [Video Reference](https://www.youtube.com/watch?v=5UWEVMg10rY&list=PLpIkg8OmuX-LH398-_ZcuHiRueOdsJbXU&index=9)
- [1721. Swapping Nodes in a Linked List](https://www.youtube.com/watch?v=TxryJMerDwE&list=PLpIkg8OmuX-LH398-_ZcuHiRueOdsJbXU&index=10)
  hint: If we need to find nth node from the last, in a single pass, we can move to nth item from the front, then immediately put a second pointer at head position and increment both of them till current pointer becomes null. Then the second pointer will point to nth node from the end. [Video Reference](https://www.youtube.com/watch?v=TxryJMerDwE&list=PLpIkg8OmuX-LH398-_ZcuHiRueOdsJbXU&index=10)
- [24. Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs/description/)
  hint: use recurssion for problems like this, flattening of linked list, flattening of doubly linked list. [Video Reference](https://www.youtube.com/watch?v=8yLiGS4ntHw&list=PLpIkg8OmuX-LH398-_ZcuHiRueOdsJbXU&index=11)
- [138. Copy List with Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/description/)
  hint: approach 1 is to use two loops and a hashmap or array. first create new nodes with values of given linked list and store each node in an array or hashmap. In the second loop set value of next and randon pointer. [Reference Code](https://leetcode.com/problems/copy-list-with-random-pointer/solutions/6280241/video-solution-with-hashmap-python-javascript-java-c/). Approach 2 uses no extra space. [Video Reference](https://www.youtube.com/watch?v=q570bKdrnlw)
- [2. Add Two Numbers](https://leetcode.com/problems/add-two-numbers/description/)
  hint: at the end, do not forget to check if carry is greater than 0. If yes, then create another node with carry.
### String
- [567. Permutation in String](https://leetcode.com/problems/permutation-in-string/description/)
  hint: Approach 1 is to generate all permutations. Here is the code for that: ![permutation_of_strings](hint/img/permutation_of_strings.png)
But the better approach is to identify that permutations of all strings will have the same characters. So we can sort the string and all its permutations and the output should be the exact same. Say string s1 has length `n1` and s2 has length `n2`. So we can take string s2 and loop through all chunks of length [i, i+n1]. If this chunk is sorted and the output is the same as the sorted output of s1, then we can say that a permutation of s1 is present in s2. But sorting takes n1log(n1) time complexity. A better solution can be that we take a 26 length array and fill it with count of characters. E.g., let s1 = `"aab"`, we can represent it in as an array like this `[2, 1, 0, 0, .... ]` and if the chunk produces the same array, we can say that a permutation exists. [Leetcode Editorial Solution](https://leetcode.com/problems/permutation-in-string/editorial/)
- [290. Word Pattern](https://leetcode.com/problems/word-pattern/description/)
  hint: a very easy problem with a very easy trap to fall into. Lets take pattern `"abba"` and string `"dog dog dog dog"`, this should throw error. Check submission for solution. [Submission](https://leetcode.com/problems/word-pattern/submissions/1514890238/)
- [1071. Greatest Common Divisor of Strings](https://leetcode.com/problems/greatest-common-divisor-of-strings/description/)
  hint: [Solution](https://leetcode.com/problems/greatest-common-divisor-of-strings/solutions/3024822/greatest-common-divisor-of-strings/)
- [32. Longest Valid Parentheses](https://leetcode.com/problems/longest-valid-parentheses/description/)
  hint: [Two pointer solution](https://www.youtube.com/watch?v=D5b_JWlkXxw), [Stack solution](https://leetcode.com/problems/longest-valid-parentheses/submissions/1696537712/)
### Array
`Tip: If array has both +ve and -ve numbers, we cannot use sliding windoow. In such cases we need prefix sum with hash map`

`Tip: If order is important, we cannot use sorting`

`Note: sub-array is contiguous, sub sequence is non contiguous`

`Tip: A different way of doing sliding window is, hashing the prefix sum along with index as key-value in dict. Here, if we need to find sub-array that sum to value k, we can check if k - current_sum in dict. If yes, then dict[k-current_sum] to curren_index is the sub array. Check video: [Video Reference](https://www.youtube.com/watch?v=frf7qxiN2qU)`

`Tip: If sub array problem with sum, check prefix or prefix + hashing`

```
Tip: For prefix sum hash map problems, if array contains +ve and -ve numbers then:

1) Store {prefix_sum: count} in hash
2) Initialize the hash with {0: 1}
```

`Tip: If order is not important, ask yourself this question: If I sort this array, will it make my job easier?`
`Tip: If we want to left rotate a n array by D steps, we do 1) reverse array[:d] 2) reverse array[d+1:] 3) reverse arr`
`Tip: A xor A = 0; 0 xor A = A`
`Tip: if we need to rearrange elements of an array such that the sequence should be +, -, +, -, ... while maintaining order of +ve and - sequences, we can notice that +ve numbers take up odd places and -ve numbers take up even places. (Assumption: no. of +ve = no. of -ve). we can take two variables; pos = 0, neg = 1; for num in nums: if num < 0: result[neg] = num; neg += 2 else result[pos] = num; pos += 2. The two pointers will move independently and eventually fill up the array. If no. of +ve != no. of -ve, then we cannot use this, we should take two arrays: pos_arr, neg_arr and fill them with O(n) and then enter data in another O(n).`
- [560. Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/description/)
  hint: [video reference](https://www.youtube.com/watch?v=xvNwoz-ufXA)
- [56. Merge Intervals](https://leetcode.com/problems/merge-intervals/description/)
  hint: if we sort the array, then it becomes easier to merge the groups. Sort, then loop over all entries and check if current start <= prev end current end > previous end. If yes then merge. [Solution code](https://leetcode.com/problems/merge-intervals/submissions/1655509120/)
- [169. Majority Element](https://leetcode.com/problems/majority-element/description/)
  hint: [Video Solution](https://www.youtube.com/watch?v=nP_ns3uSh80&list=PLgUwDviBIf0rENwdL0nEH0uGom9no0nyB&index=7)
- [268. Missing Number](https://leetcode.com/problems/missing-number/description/)
  hint: sum of numbers 0-N is N*(N+1)/2. [Solution](https://leetcode.com/problems/missing-number/submissions/1687783195/). [XOR Solution](https://leetcode.com/problems/missing-number/submissions/1687785076/)
- [75. Sort Colors](https://leetcode.com/problems/sort-colors/description/)
  hint: [Video Solution](https://www.youtube.com/watch?v=tp8JIuCXBaU&list=PLgUwDviBIf0rENwdL0nEH0uGom9no0nyB&index=6)
- [229. Majority Element II](https://leetcode.com/problems/majority-element-ii/description/)
  hint: [Solution](https://leetcode.com/problems/majority-element-ii/solutions/4131226/99-7-hashmap-boyer-moore-majority-voting-explained-intuition/)
- [4. Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/description/)
  hint: [Video Solution](https://www.youtube.com/watch?v=q6IEA26hvXc)
- [678. Valid Parenthesis String](https://leetcode.com/problems/valid-parenthesis-string/description/)
  hint: [Video Solution](https://www.youtube.com/watch?v=cHT6sG_hUZI)
- [135. Candy](https://leetcode.com/problems/candy/description/)
  hint: [My Solution](https://leetcode.com/problems/candy/submissions/1696880271/) Explanation: We start with the smallest rating and add a candy to it's neighbor if the neighbor has a greater rating. Not all neighbors will be greater, as we move from small rating to large rating, so may have one neighbor greater and one neighbor smaller, so we will only add candy to the greater rating neighbor by current_rating + 1. [Efficient Solution](https://www.youtube.com/watch?v=1IzCRCcK17A)
- [K-th element of two Arrays](
### Binary Tree
- [114. Flatten Binary Tree to Linked List](https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/)
  hint: [Solution](https://www.youtube.com/watch?v=sWf7k1x9XR4)
- [236. Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/)
  hint: [My Submission - easy to understand](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/submissions/1656998875/), [Elegant Solution](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/submissions/1657107800/)
### DP and Backtracking
`Tip: if we are computing count, max, min, True/False -> it is likely DP. If we are computing all combinations/answers -> likely backtracking.`
- [139. Word Break](https://leetcode.com/problems/word-break/description/)
  hint: we can think about splitting a word in to `word = A, B, C, D`. Now we can explore different paths like `word = AB, C, D` or `word = ABC, D` or `word = A, BC, D`. If we memoize D, then we can reuse D multiple times. Lets say combination `A, BC, D` is valid and D is cached. Then we will return True the moment we get to this combination, but memoization helped us reduce computation for combination, `ABC, D` and `A, BC, D` as it was already calculated during `A, B, C, D`.
- [39. Combination Sum](https://leetcode.com/problems/combination-sum/description/)
  hint: [Solution 1](https://leetcode.com/problems/combination-sum/submissions/1704155904/) pick or don't pick an item. time complexiy: 2^T * k where T is target and k is avg. leng of valid combinations, we need k to add combination to result. If we couldn't reuse each item, then time complexity would be 2^n (P/NP, P/NP, P/NP, .... n items -> 2 * 2 * 2 ... n times). Space complexity: T * k *x, where x is number of valid combinations. [Solution 2](https://leetcode.com/problems/combination-sum/submissions/1704157057/) for each item, loop though each remaining items including the current item. time complexity: n^t
### Tree
`Tip: if tree values are not unique, reconstruction from Inorder + Preorder/Postorder is not possible. If Preorder/Postorder array has "null" in the list, We can reconstruct the tree easily with just Preorder/Postorder array.`
`Tip: if we are finding level of a tree and we are not doing 'level = max(level, node_level)' and instead using the last value of node_level, then actual level is 'node_level - 1' because the last level will be all None entries.`
```
Tip: Find height of tree:
class Solution:
    def findHeight(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return 0

            left_height = dfs(node.left)
            right_height = dfs(node.right)

            return 1 + max(left_height, right_height)

        return dfs(root)
```
- [105. Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/)
  hint: from the preorder we learn the first item is parent, but we are not sure that the second item belongs to left or right (left may be null). We use the inorder to find if the second item is left or roght, if the second item appears before the intext of root in inorder, the second item is left, else right. [Solution](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/submissions/1680842042/)
- [297. Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/)
  hint: [Solution](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/submissions/1681575925/)
- [110. Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/description/)
  hint: [Solution](https://leetcode.com/problems/balanced-binary-tree/submissions/1683371069/)
### TODO LIST
- [Kadane's Algorithm | Maximum Subarray Sum | Finding and Printing](https://www.youtube.com/watch?v=AHZpyENo7k4)
- [Top 5 Most Common Graph Algorithms for Coding Interviews](https://www.youtube.com/watch?v=utDu3Q7Flrw&t=405s)
- [House Robber - Leetcode 198 - Python Dynamic Programming](https://www.youtube.com/watch?v=73r3KWiEvyk)
- [L15. Sudoko Solver | Backtracking](https://www.youtube.com/watch?v=FWAIf_EVUKE)
- [213. House Robber II](https://leetcode.com/problems/house-robber-ii/)

# 🧠 Backtracking Strategy Cheat Sheet

| | Constraint Summary	                               | Problem Scenario	| Strategy / Thought Process	| Notes / Edge Handling |
|-|----------------------------------------------------|------------------|------------------------------|----------------------|
|1 |	✅ Reuse allowed, ❌ Duplicates allowed in result	| Use each number unlimited times (e.g., Combination Sum) |	Pick / Not Pick |	Stay at i when picking, move to i + 1 when not picking |
|2 | ❌ Reuse allowed, ❌ Duplicates allowed in result	| Each number used at most once (e.g., Subsets, Combination Sum II)	| For-loop from i to n with visited check	Use i + 1 in recursive call |
|3 | ❌ Reuse allowed, ✅ Duplicates in input, ❌ Duplicates allowed in result	| Each number once, input has duplicates (e.g., Combination Sum II)	| Sort input + skip duplicates in loop | Check: if i > start and candidates[i] == candidates[i-1]: continue |
|4 | ✅ Reuse allowed, ✅ Duplicates in input, ❌ Duplicates allowed in result	| Use same number multiple times, but input has duplicates (e.g., infinite supply) | Sort + Skip duplicates only when exploring new branches | Still Pick/Not Pick style, but with duplicate skipping |
|5 | ✅ Reuse allowed, ✅ Duplicates in result allowed | Permutations with repetition (e.g., coin change with order) | Classic backtrack over full range | Do not skip duplicates, order matters |
|6 | ❌ Reuse allowed, ✅ Duplicates in input, ❌ Duplicates allowed in result | Permutations without repetition (e.g., Permutations II) | Backtrack with used[] or boolean visited[] | Also sort + skip same value if used[i - 1] is False |
|7 | Subset generation | All combinations regardless of sum (e.g., power set) | Pick / Not Pick | No need to track sum; just include/exclude each |
|8 | Fixed size k-subsets | Choose k items only (e.g., Combinations) | Backtrack with count | Stop recursion when len(cur) == k |
|9 | Target sum combinations, values > 0 | Subset sum problems with pruning | Sort + break early when candidates[i] > target | Optimizes time significantly |
|10	| Order matters (e.g., permutations) | Every number can go to every position | For-loop with visited[] | Track used[] to avoid reusing same index |



---
