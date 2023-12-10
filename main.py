# TODO: Not implemented
import numpy as np
pairs = [('A', 'U'), ('U', 'A'), ('C', 'G'), ('G', 'C')]

def find_max_base_pairs(seq):
    n = len(seq)
    #Initialize the dp matrix to store max num of base pairs for each subsequence
    dp = np.zeros((n, n))
    #Fill in the dp matrix
    
    for k in range(1, n):
        for i in range(n - k):
            j = i + k
            #(i, j) is correct for iterating through diagonals
            if j - i >= 0:
                down = dp[i + 1][j]
                left = dp[i][j - 1]
                a = 0
                if (seq[i], seq[j]) in pairs:
                    a = 1
                diag = dp[i + 1][j - 1] + a
                rc = max([dp[i][t] + dp[t + 1][j] for t in range(i, j)], default=0)
            
                dp[i, j] = max(down, left, diag, rc)
        
    print(dp)
    return dp

# TODO: Not implemented
def find_secondary_structure(seq):
    subseq_max_base_pairs = find_max_base_pairs(seq)
    #Find backtrace of dp matrix

    return 0
    
#TODO: Hairpin loops with minimum length l

#TODO: Make test file

find_max_base_pairs("GGGAAAUCC")