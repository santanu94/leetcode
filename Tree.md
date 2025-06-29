# All Tree Concepts

## BASIC TREE TRAVERSALS

1. Preorder Traversal (Root-Left-Right)
2. Inorder Traversal (Left-Root-Right)
3. Postorder Traversal (Left-Right-Root)
4. Level Order / BFS Traversal
5. Zigzag Level Order Traversal
6. Recursive vs Iterative Traversals

| Concept                        | LeetCode Problem                                  | Priority |
| :----------------------------- | :------------------------------------------------ | :------: |
| Inorder Traversal              |   94. Binary Tree Inorder Traversal               |    ✅    |
| Preorder Traversal             |   144. Binary Tree Preorder Traversal             |    ✅    |
| Postorder Traversal            |   145. Binary Tree Postorder Traversal            |    ✅    |
| Level Order Traversal          |   102. Binary Tree Level Order Traversal          |    ✅    |
| Zigzag Level Order Traversal   |   103. Binary Tree Zigzag Level Order Traversal   |    🟡    |
| Iterative Traversals           |   94, 144, 145 (Iterative versions)               |    ✅    |

## TREE BUILDING / CONSTRUCTION

7. Build Tree from Inorder + Preorder
8. Build Tree from Inorder + Postorder
9. Construct Binary Search Tree from Preorder / Postorder
10. Serialize and Deserialize Binary Tree
11. Serialize and Deserialize BST

| Concept                               | LeetCode Problem                                                     | Priority |
| :------------------------------------ | :------------------------------------------------------------------- | :------: |
| Build Tree (Inorder + Preorder)	      |   105. Construct Binary Tree from Preorder and Inorder Traversal	   |    ✅    |
| Build Tree (Inorder + Postorder)	    |   106. Construct Binary Tree from Inorder and Postorder Traversal	   |    ✅    |
| BST from Preorder	                    |   1008. Construct BST from Preorder Traversal	                       |    🟡    |
| Serialize / Deserialize Binary Tree	  |   297. Serialize and Deserialize Binary Tree	                       |    ✅    |
| Serialize / Deserialize BST	          |   449. Serialize and Deserialize BST	                               |    🟡    |

## TREE DEPTH / HEIGHT / DIAMETER

12. Max Depth / Height of Tree
13. Min Depth of Tree
14. Diameter of Binary Tree
15. Balanced Binary Tree
16. Check if Symmetric Tree

| Concept                | LeetCode Problem                        | Priority |
| :--------------------- | :-------------------------------------- | :------: |
| Max Depth	             |   104. Maximum Depth of Binary Tree	   |    ✅    |
| Min Depth	             |   111. Minimum Depth of Binary Tree	   |    ✅    |
| Diameter	             |   543. Diameter of Binary Tree	         |    ✅    |
| Balanced Binary Tree	 |   110. Balanced Binary Tree	           |    ✅    |
| Symmetric Tree	       |   101. Symmetric Tree	                 |    ✅    |

## PATH PROBLEMS

17. Root to Leaf Path Sum
18. All Paths with Target Sum
19. Path with Max Sum (Binary Tree)
20. Longest Zigzag Path
21. Longest Univalue Path
22. Count Good Nodes in Binary Tree

| Concept                    | LeetCode Problem                                | Priority |
| :------------------------- | :---------------------------------------------- | :------: |
| Path Sum	                 |   112. Path Sum	                               |    ✅    |
| Path Sum II (all paths)	   |   113. Path Sum II	                             |    ✅    |
| Path Sum III (any nodes)	 |   437. Path Sum III	                           |    ✅    |
| Max Path Sum	             |   124. Binary Tree Maximum Path Sum	           |    ✅    |
| Longest Zigzag Path	       |   1372. Longest ZigZag Path in a Binary Tree	   |    🟡    |
| Longest Univalue Path	     |   687. Longest Univalue Path	                   |    🟡    |
| Count Good Nodes	         |   1448. Count Good Nodes in Binary Tree	       |    ✅    |

## LOWEST COMMON ANCESTOR (LCA)

23. LCA in Binary Tree
24. LCA in BST
25. Distance Between Nodes Using LCA
26. Kth Ancestor (Advanced)

| Concept                   | LeetCode Problem                                               | Priority |
| :------------------------ | :------------------------------------------------------------- | :------: |
| LCA in Binary Tree	      |   236. Lowest Common Ancestor of a Binary Tree	               |    ✅    |
| LCA in BST	              |   235. Lowest Common Ancestor of a BST	                       |    ✅    |
| Distance Between Nodes	  |   Use LCA (235 or 236) + path length	                         |    🟡    |
| Kth Ancestor	            |   Not in LeetCode; practice on GfG or custom implementation	   |    🟡    |

## BINARY SEARCH TREE (BST) CONCEPTS

27. Validate BST
28. Lowest Common Ancestor in BST
29. Find Kth Smallest / Largest Element
30. Floor and Ceil in BST
31. Delete Node in BST
32. BST to Sorted DLL
33. Recover BST with Swapped Nodes
34. Predecessor and Successor in BST

| Concept                   | LeetCode Problem                                           | Priority |
| :------------------------ | :--------------------------------------------------------- | :------: |
| Validate BST	            | 98. Validate Binary Search Tree	                           |    ✅    |
| LCA in BST	              | 235. Lowest Common Ancestor of a BST	                     |    ✅    |
| Kth Smallest Element	    | 230. Kth Smallest Element in a BST	                       |    ✅    |
| Kth Largest Element	      | Variant of above or use Max Heap	                         |    🟡    |
| Delete Node in BST	      | 450. Delete Node in a BST	                                 |    ✅    |
| BST to DLL	              | 426. Convert BST to Sorted Doubly Linked List (Premium)	   |    🟡    |
| Recover Swapped Nodes	    | 99. Recover Binary Search Tree	                           |    🟡    |
| Predecessor & Successor	  | 285. Inorder Successor in BST (Premium) / Custom	         |    🟡    |

## TREE MODIFICATION & TRANSFORM

35. Invert / Mirror Binary Tree
36. Flatten Binary Tree to Linked List
37. Convert Sorted Array to BST
38. Convert Sorted Linked List to BST
39. Populating Next Right Pointers

| Concept                               | LeetCode Problem                                      | Priority |
| :------------------------------------ | :---------------------------------------------------- | :------: |
| Invert Binary Tree	                  | 226. Invert Binary Tree	                              |    ✅    |
| Flatten Binary Tree	                  | 114. Flatten Binary Tree to Linked List	              |    ✅    |
| Sorted Array to BST	                  | 108. Convert Sorted Array to BST	                    |    ✅    |
| Sorted List to BST	                  | 109. Convert Sorted List to BST	                      |    🟡    |
| Next Right Pointers (Perfect Tree)	  | 116. Populating Next Right Pointers in Each Node	    |    ✅    |
| Next Right Pointers (General Tree)	  | 117. Populating Next Right Pointers in Each Node II	  |    🟡    |

## TREE TRAVERSAL WITH MEMORY / CACHING

40. Tree DFS with Memoization (e.g. Robber on Tree)
41. DP on Trees (Tree DP / Tree-based DP)

| Concept                 | LeetCode Problem                              | Priority |
| :---------------------- | :-------------------------------------------- | :------: |
| Robber on Tree	        | 337. House Robber III	                        |    ✅    |
| Longest Path in Tree	  | Custom or adaptation of Path Sum III or 124	  |    🟡    |

## ADVANCED / HARD PATTERNS

42. Tree Isomorphism
43. Burning Tree / Time to Burn Tree
44. Delete Nodes and Return Forest
45. Tree Diameter in N-ary Tree
46. Vertical Order Traversal
47. Boundary Traversal
48. Morris Inorder Traversal (O(1) Space)

| Concept                           | LeetCode Problem                                     | Priority |
| :-------------------------------- | :--------------------------------------------------- | :------: |
| Tree Isomorphism	                | No exact match; GfG / system design / Google mock	   |    🟡    |
| Time to Burn Tree	                | Custom or GeeksForGeeks	                             |    🟡    |
| Delete Nodes and Return Forest	  | 1110. Delete Nodes and Return Forest	               |    ✅    |
| Diameter of N-ary Tree	          | 1522. Diameter of N-ary Tree	                       |    🟡    |
| Vertical Order Traversal	        | 987. Vertical Order Traversal of a Binary Tree	     |    ✅    |
| Boundary Traversal	              | Custom; often asked in service-based companies	     |    🟡    |
| Morris Inorder Traversal	        | No direct problem; asked in Meta / Google rounds	   |    🟡    |

## TRIE (Prefix Tree)

49. Basic Trie Insert/Search
50. Word Search II (Backtracking + Trie)
51. Replace Words using Trie
52. Longest Common Prefix
53. Count of Distinct Substrings using Trie

| Concept                      | LeetCode Problem                                  | Priority |
| :--------------------------- | :------------------------------------------------ | :------: |
| Basic Insert/Search	         | 208. Implement Trie (Prefix Tree)	               |    ✅    |
| Word Search II	             | 212. Word Search II	                             |    ✅    |
| Replace Words	               | 648. Replace Words	                               |    ✅    |
| Longest Common Prefix	       | 14. Longest Common Prefix	                       |    ✅    |
| Count Distinct Substrings	   | Not in LeetCode, common in GfG / coding rounds	   |    🟡    |

## N-ARY TREE

54. Preorder/Postorder Traversal in N-ary Tree
55. Serialize / Deserialize N-ary Tree
56. Level Order for N-ary Tree

| Concept                            | LeetCode Problem                                      | Priority |
| :--------------------------------- | :---------------------------------------------------- | :------: |
| N-ary Preorder Traversal           | 589. N-ary Tree Preorder Traversal                    |    ✅    |
| N-ary Postorder Traversal          | 590. N-ary Tree Postorder Traversal                   |    ✅    |
| N-ary Level Order Traversal        | 429. N-ary Tree Level Order Traversal                 |    ✅    |
| Serialize/Deserialize N-ary Tree   | 428. Serialize and Deserialize N-ary Tree (Premium)   |    🟡    |

---

⭐ Bonus: Techniques to Master

- Recursive Backtracking on Trees
- DFS vs BFS on Trees
- Recursion Stack vs Explicit Stack
- State Representation for DP on Trees
- Hashing for Tree Structure Matching



