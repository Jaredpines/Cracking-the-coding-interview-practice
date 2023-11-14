from importlib.machinery import SourceFileLoader
palindrome_permutation_module = SourceFileLoader("palindrome_permutation_module", "1.4 Palindrome Permutation.py").load_module()

def testPalindrome():
    p = palindrome_permutation_module.Palindrome_Permutation
    assert p("taco cat") == True
    assert p("hello") == False

    # Edge cases
    assert p("") == True  # Empty string is a palindrome
    assert p("a") == True  # Single character is a palindrome
    assert p("abc") == False  # No permutation of abc is a palindrome

    # Palindromes with odd length
    assert p("civic") == True
    assert p("deified") == True
    assert p("radar") == True

    # Palindromes with even length
    assert p("noon") == True
    assert p("level") == True
    assert p("refer") == True

    # Permutations that are not palindromes
    assert p("aab") == True  # "aab" is a permutation of a palindrome
    assert p("xyz") == False  # "xyz" is not a permutation of a palindrome

    # Case-insensitive tests
    assert p("Taco Cat") == True
    assert p("Able was I ere I saw elba") == True

    # Non-alphabetic characters
    assert p("A man, a plan, a canal, Panama!") == True
    assert p("12321") == True