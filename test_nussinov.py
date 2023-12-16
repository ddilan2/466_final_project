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
def test_nussinov_loops():
    #loop is a completely unpaired, single-stranded region
    sequence1 = "AAAAAGGG"
    assert nussinov.nussinov(sequence1) == '........'

    sequence2 = "CCUUUCC"
    assert nussinov.nussinov(sequence2) == '.......'

    sequence3 = "AAAACCCCCAAAA"
    assert nussinov.nussinov(sequence3) == '.............'

    sequence4 = "UUUUUUUUUUUUUUCCCCCCCCCCC"
    assert nussinov.nussinov(sequence4) == '.........................'

def test_nussinov_bulges():
    #bulge is a type of non-helical region where there
    #is an unpaired nucleotide or a small number of unpaired
    #nucleotides, and this region interrupts an otherwise 
    #helical structure
    sequence1 = "AGGGCU"
    assert nussinov.nussinov(sequence1) == '(..())'

    sequence2 = "AAAGGGAAAAGAAAGGAAAGGGAAAGAAGAUUUGGGUUGUUGGGGUUGGUUUGGGUUGGUUUGGGUU"
    assert nussinov.nussinov(sequence2) == '(((...((((.(((..(((...(((.((.()))...)).))....))..)))...))..)))...))'

def test_nussinov_helix_loop_combination():
    # This tests a combination of helix (GGCC) followed by a loop (AAAA) and ending with another helix (CCGG)
    sequence = "GGCCAAAACCGG"
    expected_structure = "(())....(())"
    assert nussinov.nussinov(sequence) == expected_structure

def test_nussinov_helix_loop_bulge_combination():
    # This tests a combination of helix (GGCC), loop (AAAA), and a bulge (C) within another helix (CCGG)
    sequence = "GGCCAAAAC.CGG"
    expected_structure = "(())....(.())"
    assert nussinov.nussinov(sequence) == expected_structure

def test_nussinov_complex_combination():
    # This tests a complex structure with multiple helices, loops, and a bulge
    sequence = "GGGAAACCCGGUUUGAAGCC"
    expected_structure = "...(((.(()))))(..())"
    assert nussinov.nussinov(sequence) == expected_structure
