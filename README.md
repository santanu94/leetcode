# Revisit
### Graph
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
  in order to group `n*n` block in a 2D matrix, divide rows by n and columns by n.
