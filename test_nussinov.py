import nussinov

def test_nussinov():
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

    assert nussinov.nussinov("") == ''
    assert nussinov.nussinov("A") == '.'
    assert nussinov.nussinov("C") == '.'
    assert nussinov.nussinov("G") == '.'
    assert nussinov.nussinov("U") == '.'

    #code doesn't work when the RNA sequence has no base pairs