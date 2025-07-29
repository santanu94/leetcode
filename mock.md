# 10 Google-Style DSA Questions


---

Q1. “Data Detox”<br>

In Google Photos, users want to clean up duplicate memories.<br>
You are given a string s and an integer k.<br>

You must find the length of the longest subsequence of s such that no character appears more than k times.<br>

🧪 Input:<br>

s: a string of lowercase letters (length ≤ 10⁵)<br>

k: an integer (1 ≤ k ≤ 26)<br>


🎯 Output:<br>
Return the length of the longest valid subsequence.<br>

<details>

<summary>Expand to view concept information</summary>

### Concept and Twist

📦 Concepts: Greedy + Frequency Counting + Subsequence + Priority Queue (if optimizing)<br>
🌀 Twist: Subsequence (not substring), and frequency is global, not local.<br>

</details>

---

Q2. “Teleporting Islands”

You are building teleportation pads on n islands, connected by roads.<br>

Each road can be activated or deactivated at will.<br>
You must process a list of operations:<br>

"connect u v" — add a road between u and v<br>

"disconnect u v" — remove the road<br>

"query u v" — return True if u and v are currently connected via any path<br>


🧪 Input: n and list of operations (≤ 10⁴ operations)<br>
🎯 Output: Boolean results for each query.<br>

<details>

<summary>Expand to view concept information</summary>

### Concept and Twist

📦 Concepts: Union-Find (DSU) + Offline Query + Path Compression<br>
🌀 Twist: Union-Find doesn’t handle deletions → requires rollback DSU or segment tree of sets.<br>

</details>

---

Q3. “Data Packet Maze”

You’re given a grid of 0s (open) and 1s (walls).<br>
You must send a data packet from (0, 0) to (n-1, m-1).<br>

Rules:<br>

You can break at most one wall on your way.<br>

Find the shortest path, considering you can break at most one wall.<br>


🧪 Input: 2D grid of size ≤ 1000x1000<br>
🎯 Output: Minimum number of steps to reach the destination, or -1 if not possible.<br>

<details>

<summary>Expand to view concept information</summary>

### Concept and Twist

📦 Concepts: BFS + State Tracking + Grid Traversal<br>
🌀 Twist: Each node state is (x, y, broken) → classic BFS fails without tracking that state.<br>

</details>

---

Q4. “Hidden Palindromes”

In a secret Google Docs document, some substrings are palindromes in disguise.<br>

You’re given a list of strings words.<br>
Count how many unique pairs (i, j) exist such that:<br>

i ≠ j, and<br>

words[i] + words[j] is a palindrome<br>


🧪 Input: List of ≤ 10⁴ strings (length ≤ 100)<br>
🎯 Output: Number of valid pairs<br>

<details>

<summary>Expand to view concept information</summary>

### Concept and Twist

📦 Concepts: Trie + Palindrome Partitioning + HashMap<br>
🌀 Twist: You need efficient prefix-suffix matching with palindrome checks.<br>

</details>

---

Q5. “Virus Quarantine”

You’re asked to partition n machines into two groups. Some machines are incompatible (edges), and you may skip at most k incompatibilities (edges can be ignored).<br>

Return True if such a partition exists.<br>

🧪 Input: n, list of edges, and k<br>
🎯 Output: True or False<br>

<details>

<summary>Expand to view concept information</summary>

### Concept and Twist

📦 Concepts: Graph Bipartition + Backtracking + Bitmask Pruning<br>
🌀 Twist: Standard bipartition fails → needs bounded backtracking on removed edges.<br>

</details>

---

Q6. “Binary Sandstorm”

You are given an array arr of integers ≤ 10⁵.<br>

Find the number of subarrays where the XOR of elements is equal to the AND of elements.<br>

🧪 Input: Integer array<br>
🎯 Output: Count of subarrays<br>

<details>

<summary>Expand to view concept information</summary>

### Concept and Twist

📦 Concepts: Bitmask + XOR Properties + Sliding Window<br>
🌀 Twist: XOR and AND match rarely → pruning + bitwise logic required.<br>

</details>

---

Q7. “Autocomplete with Edge-Costs”

A search engine suggests query completions.<br>

Each character typed is a node in a Trie.<br>
Typing each character has a cost depending on the edge weight (stored in the Trie).<br>
You can accept a suggestion anytime, paying a flat completion cost c.<br>

Find the minimum cost to complete a search string using the system.<br>

🧪 Input: root of Trie with edge weights + flat c + target word<br>
🎯 Output: Minimum cost to type or accept auto-complete<br>

<details>

<summary>Expand to view concept information</summary>

### Concept and Twist

📦 Concepts: Dijkstra on Trie + Weighted Graph + Greedy<br>
🌀 Twist: Trie + Dijkstra together — graph structure is implicit.<br>

</details>

---

Q8. “Earthquake Clusters”

A network of seismic sensors are connected in a tree.<br>
Each query gives two sensors. You must report their lowest common ancestor.<br>

But here's the catch: earthquakes can disconnect sensors (edge deletions), and then LCA queries may return “-1” if sensors are no longer connected.<br>

🧪 Input: Tree with n nodes + q queries + d disconnect operations<br>
🎯 Output: LCA node or -1 per query<br>

<details>

<summary>Expand to view concept information</summary>

### Concept and Twist

📦 Concepts: Offline Tarjan's LCA + Union-Find + DFS<br>
🌀 Twist: Dynamic edge deletions affect connectivity → classic LCA breaks without handling disconnection.<br>

</details>

---

Q9. “Delivery Drones”

You’re given an array deliveries[i] indicating how much time each delivery takes.<br>

Rule:<br>

After each delivery, the drone must rest for k minutes before taking another delivery.<br>

Maximize the number of deliveries within total time T.<br>


🧪 Input: List of delivery times, rest k, and max time T<br>
🎯 Output: Max number of deliveries<br>

<details>

<summary>Expand to view concept information</summary>

### Concept and Twist

📦 Concepts: Knapsack DP with Cooldown<br>
🌀 Twist: DP state depends not just on index and time, but also rest windows.<br>

</details>

---

Q10. “Version Revert Chain”

You’re given a list of code commits and their dependencies (u → v means v depends on u).<br>

Now, a developer wants to revert a commit and all downstream commits affected by it.<br>

Process a list of revert(commit_id) queries — for each, return the list of commits that must be reverted.<br>

🧪 Input: DAG of dependencies + list of revert queries<br>
🎯 Output: List of nodes to revert for each query<br>

<details>

<summary>Expand to view concept information</summary>

### Concept and Twist

📦 Concepts: Topological Sort + Reverse DFS + Memoization<br>
🌀 Twist: Lazy propagation & caching — same revert may be queried repeatedly.<br>

</details>

---
