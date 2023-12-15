
import numpy as np
import sys
pairs = [('A', 'U'), ('U', 'A'), ('C', 'G'), ('G', 'C')]

def find_max_base_pairs(seq):
    n = len(seq)
    #Initialize the dp matrix to store max num of base pairs for each subsequence
    dp = np.zeros((n, n))
    #Fill in the dp matrix
    
    for diagonal_num in range(1, n):
        for i in range(n - diagonal_num):
            j = i + diagonal_num
            #(i, j) is correct for iterating through diagonals
            if j - i >= 0:
                dp[i, j] = max(dp[i + 1][j], dp[i][j - 1], 
                               dp[i + 1][j - 1] + int((seq[i], seq[j]) in pairs), 
                               max([dp[i][k] + dp[k + 1][j] for k in range(i, j)], default=0))
    print("Scoring matrix for " + seq + ":") 
    print(dp)
    return dp

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
    if dp[0][L - 1] == 0:
        return "." * L
    backtrace(dp, seq, 0, L - 1) 
    output_list = ['.' for _ in range(L)]
    for pair in optimal_base_pairings:
        (i, j) = pair
        output_list[i] = '('
        output_list[j] = ')'
    output_str = ''.join(output_list)
    return output_str
    
def nussinov(seq):
    output_str = find_secondary_structure(seq)
    print('Optimal Base Pair: ' + output_str)
    return output_str

if (len(sys.argv) == 2):
    user_input = sys.argv[1] # Gets the user input from command line
    nussinov(user_input)
elif (len(sys.argv) > 2):  # More than 1 RNA sequence input
    print("Please only input one RNA sequence")
else:
    print("Please add RNA sequence to command line argument.") # No RNA sequence input
