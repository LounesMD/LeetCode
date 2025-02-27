class Solution:    
    def lenLongestFibSubseq(self, arr):
        res = 0
        n = len(arr)
        all_elements = set(arr) # Makes it faster
        for i in range(n):
            for j in range(i+1, n):
                a, b = arr[i], arr[j]
                curr_longest = 2
                while (a+b) in all_elements:
                    c = a + b
                    a, b = b, c
                    curr_longest += 1
                    res = max(res, curr_longest)

        return res 