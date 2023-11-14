"""
Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome.
A palindrome is a word or phrase that is the same forwards and backwards. A permutation
is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
EXAMPLE
Input: Tact Coa
Output: True (permutations : "taco cat" , "atco cta" , etc. )
"""
m1time = 0
def __int__(self):
    pass
#First Attempt
def Palindrome_Permutation(string):
    letter = []
    count = []
    if len(string) == 0 or len(string) == 1:
        return True
    for s in string.lower():
        if not s.isalpha():
            continue
        if letter.__contains__(s):
            count[letter.index(s)] += 1
        else:
            letter.append(s)
            count.append(1)
    only1 = False
    for c in count:
        if (only1 == True and c%2 == 1):
            return False
        if only1 == False and c%2 == 1:
            only1 = True
    return True

