import time
#Check Permutation: Given two strings, write a method to decide if one is a permutation of the other.


m1time = 0

#First attempt lazy way
def checkPermutation(string1, string2):
    global m1time
    begin = time.time()
    if len(string1) != len(string2):
        time.sleep(.001)
        end = time.time()
        print(end - begin - .001)
        m1time += end - begin - .001
        return False
    string1 = sorted(string1)
    string2 = sorted(string2)
    if string1 == string2:
        time.sleep(.001)
        end = time.time()
        print(end - begin - .001)
        m1time += end - begin - .001
        return True
    time.sleep(.001)
    end = time.time()
    print(end - begin - .001)
    m1time += end - begin - .001
    return False



assert checkPermutation("bob", "joe") == False
assert checkPermutation("cat", "tac") == True
assert checkPermutation("stone", "notes") == True
assert checkPermutation("avacado", "apple") == False
assert checkPermutation("abc", "cab") == True
assert checkPermutation("bacon", "conda") == False



print("Every thing passed")
print("Method 1 total took: " + str(round(m1time, 4)) + " seconds to complete the tests")