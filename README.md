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
- [Max Circular Subarray Sum](https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/max-circular-subarray-sum-1587115620)
  hint - [Video Reference](https://www.youtube.com/watch?v=Za8V4wkZKkM)
