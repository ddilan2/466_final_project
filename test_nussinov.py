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

    sequence3 = "AGUG"
    result3 = nussinov.nussinov(sequence3)
    assert result3 == "(.)."
    
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

    
    #code doesn't work when the RNA sequence has no base pairs