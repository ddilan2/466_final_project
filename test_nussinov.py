import nussinov

def test_nussinov_base_cases():
    assert nussinov.nussinov("") == ''
    assert nussinov.nussinov("A") == '.'
    assert nussinov.nussinov("C") == '.'
    assert nussinov.nussinov("G") == '.'
    assert nussinov.nussinov("U") == '.'

    
def test_nussinov_one_base_pair():
    sequence1 = "AGACA"
    result1 = nussinov.nussinov(sequence1)
    assert result1 == ".(.)."

    sequence2 = "GAAAC"
    result2 = nussinov.nussinov(sequence2)
    assert result2 == "(...)"

    sequence3 = "AGUG"
    result3 = nussinov.nussinov(sequence3)
    assert result3 == "(.)."

    sequence3 = "AAGUG"
    result3 = nussinov.nussinov(sequence3)
    assert result3 == ".(.)."

    sequence4 = "GAAGU"
    result4 = nussinov.nussinov(sequence4)
    assert result4 == "..(.)"

def test_nussinov_multiple_base_pairs():
    sequence1 = "AUGCGAU"
    result1 = nussinov.nussinov(sequence1)
    assert result1 == '((.()))'

    sequence2 = "GAUCAC"
    result2 = nussinov.nussinov(sequence2)
    assert result2 == '(())..'

    sequence3 = "GGGCCC"
    result3 = nussinov.nussinov(sequence3)
    assert result3 == '((()))'

    sequence4 = "ACGUAG"
    result4 = nussinov.nussinov(sequence4)
    assert result4 == '.()().'

#Note stem loops are examples of helices and loops
def test_nussinov_helices():
    #helix loops back on itself, symmetric
    sequence1 = "AUGCAU"
    assert nussinov.nussinov(sequence1) == '((()))'

    sequence2 = "AGUCGUCAGCAUGCUGACGACU"
    assert nussinov.nussinov(sequence2) == '((((((((((()))))))))))'

    sequence3 = "ACGUGCAUUACGGCUAAGGAGCUUGGACCCGGGUCCAAGCUCCUUAGCCGUAAUGCACGU"
    assert nussinov.nussinov(sequence3) == '(((((((((((((((((((((((((((((())))))))))))))))))))))))))))))'
    #Add more helix test cases as needed
def test_nussinov_loops():
    #loop is a completely unpaired, single-stranded region
    sequence1 = "AAAAAGGG"
    assert nussinov.nussinov(sequence1) == '........'

    sequence2 = "CCUUUCC"
    assert nussinov.nussinov(sequence2) == '.......'

    #Add more loop test cases as needed

def test_nussinov_bulges():
    #bulge is a type of non-helical region where there
    #is an unpaired nucleotide or a small number of unpaired
    #nucleotides, and this region interrupts an otherwise 
    #helical structure
    sequence1 = "AGGGCU"
    assert nussinov.nussinov(sequence1) == '(..())'

    sequence2 = "AAAGGGAAAAGAAAGGAAAGGGAAAGAAGAUUUGGGUUGUUGGGGUUGGUUUGGGUUGGUUUGGGUU"
    assert nussinov.nussinov(sequence2) == '(((...((((.(((..(((...(((.((.()))...)).))....))..)))...))..)))...))'

    #Add more bulge test cases as needed
#TODO: Write test cases for below
#Junctions are too complicated for Nussinov - would require 
#more optimizations, also pseudoknots are already avoided in Nussinov
"""
def test_nussinov_junctions():
    sequence1 = "AUGCGAU"
    assert nussinov.nussinov(sequence1) == '((.()))'

    sequence2 = "GAUCAC"
    assert nussinov.nussinov(sequence2) == '(())..'

    #Add more junction test cases as needed
def test_nussinov_pseudoknots():
    sequence1 = "AUGCGAU"
    assert nussinov.nussinov(sequence1) == '((.()))'

    sequence2 = "GAUCAC"
    assert nussinov.nussinov(sequence2) == '(())..'

    #Add more pseudoknot test cases as needed
"""    
    