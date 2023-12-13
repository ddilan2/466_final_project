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
                diag = dp[i + 1][j - 1] + int((seq[i], seq[j]) in pairs)
                rc = max([dp[i][t] + dp[t + 1][j] for t in range(i, j)], default=0)
            
                dp[i, j] = max(down, left, diag, rc)
        
    print(dp)
    return dp

# TODO: Not implemented




def find_secondary_structure(seq):
    dp = find_max_base_pairs(seq)
    #Find backtrace of dp matrix
    optimal_base_pairings = []
    def backtrace(dp, seq, i, j):
        if j - i >= 0:
            if dp[i][j] == dp[i + 1][j]:
                backtrace(dp, seq, i + 1, j)
            elif dp[i][j] == dp[i][j - 1]:
                backtrace(dp, seq, i, j - 1)
            elif dp[i][j] == dp[i + 1][j - 1] + int((seq[i], seq[j]) in pairs):
                optimal_base_pairings.append((i, j))
                backtrace(dp, seq, i + 1, j - 1)
            else:
                for k in range(i + 1, j - 1):
                    if dp[i][j] == dp[i][k] + dp[k + 1][j]:
                        backtrace(dp, seq, i, k)
                        backtrace(dp, seq, k + 1, j) 
                        break
    L = len(seq)
    backtrace(dp, seq, 0, L - 1) 
    output_list = ['.' for _ in range(L)]
    for pair in optimal_base_pairings:
        (i, j) = pair
        output_list[i] = '('
        output_list[j] = ')'
    output_str = ''.join(output_list)
    print('Optimal Base Pair: ' + output_str)
    return output_str
    
#TODO: Hairpin loops with minimum length l

#TODO: Make test file
seq = "GGGAAAUCC"
find_secondary_structure(seq)