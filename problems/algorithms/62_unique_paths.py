class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Step 1: Recursion approach
        # Step 2: Memoization
    
        def dep_nb_path(m,n,memo):
            if memo[m][n] != 0: # Includes the (0,0) = 1
                return memo[m][n]

            else:
                r1, r2 = 0, 0
                if m > 0:
                    r1 = dep_nb_path(m-1,n,memo)
                if n > 0:
                    r2 = dep_nb_path(m,n-1,memo)
            
            memo[m][n] = r1 + r2
            return r1 + r2

        memo = [[0] * n for _ in range(m)]
        memo[0][0] = 1

        return dep_nb_path(m-1,n-1,memo)