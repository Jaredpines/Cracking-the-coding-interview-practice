import time
#Check Permutation: Given two strings, write a method to decide if one is a permutation of the other.


m1time = 0
m2time = 0
m3time = 0

#First attempt lazy way O((N*log(N))+(M*log(M)))
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

print("Method 1 Times")
assert checkPermutation("bob", "joe") == False
assert checkPermutation("cat", "tac") == True
assert checkPermutation("stone", "notes") == True
assert checkPermutation("avacado", "apple") == False
assert checkPermutation("abc", "cab") == True
assert checkPermutation("bacon", "conda") == False

#Second Attempt Sets O(N+M) Doesn't work for duplicates see line 74
def checkPermutation(string1, string2):
    global m2time
    l1 = set()
    l2 = set()
    begin = time.time()
    if len(string1) != len(string2):
        time.sleep(.001)
        end = time.time()
        print(end - begin - .001)
        m2time += end - begin - .001
        return False
    for s in string1:
      l1.add(s)
    for s in string2:
      l2.add(s)
    if l1 == l2:
        time.sleep(.001)
        end = time.time()
        print(end - begin - .001)
        m2time += end - begin - .001
        return True
    time.sleep(.001)
    end = time.time()
    print(end - begin - .001)
    m2time += end - begin - .001
    return False

print()
print("Method 2 Times")
assert checkPermutation("bob", "joe") == False
assert checkPermutation("cat", "tac") == True
assert checkPermutation("stone", "notes") == True
#assert checkPermutation("avacado", "avocado") == False
assert checkPermutation("abc", "cab") == True
assert checkPermutation("bacon", "conda") == False

#Third Attempt Nested For Loops O(N*M) Doesn't work for duplicates see line 114
def checkPermutation(string1, string2):
    global m3time
    flag = False
    begin = time.time()
    if len(string1) != len(string2):
        time.sleep(.001)
        end = time.time()
        print(end - begin - .001)
        m3time += end - begin - .001
        return False
    for s1 in string1:
        for s2 in string2:
            if s1 == s2:
                flag = True
        if flag == False:
            break
        flag = False
    else:
        time.sleep(.001)
        end = time.time()
        print(end - begin - .001)
        m3time += end - begin - .001
        return True
    time.sleep(.001)
    end = time.time()
    print(end - begin - .001)
    m3time += end - begin - .001
    return False


print()
print("Method 3 Times")
assert checkPermutation("bob", "joe") == False
assert checkPermutation("cat", "tac") == True
assert checkPermutation("stone", "notes") == True
#assert checkPermutation("avacado", "avocado") == False
assert checkPermutation("abc", "cab") == True
assert checkPermutation("bacon", "conda") == False

print()
print("Every thing passed")
print("Results")
print("Method 1 total took: " + str(round(m1time, 4)) + " seconds to complete the tests")
print("Method 2 total took: " + str(round(m2time, 4)) + " seconds to complete the tests")
print("Method 3 total took: " + str(round(m3time, 4)) + " seconds to complete the tests")
print("Difference in time to complete the tests between method 1 and method 2: " + str(abs(round(m1time-m2time, 6))) + " seconds")
print("Difference in time to complete the tests between method 1 and method 3: " + str(abs(round(m1time-m3time, 6))) + " seconds")
print("Difference in time to complete the tests between method 2 and method 3: " + str(abs(round(m2time-m3time, 6))) + " seconds")
if m1time < m2time and m1time < m3time:
    print("Method 1 is " + str(round(((m2time-m1time)/m2time)*100, 2)) + "% faster than method 2")
    print("Method 1 is " + str(round(((m3time-m1time) / m3time) * 100, 2)) + "% faster than method 3")
elif m3time < m2time and m3time < m1time:
    print("Method 3 is " + str(round(((m1time-m3time) / m1time)*100, 2)) + "% faster than method 1")
    print("Method 3 is " + str(round(((m2time-m3time) / m2time) * 100, 2)) + "% faster than method 2")
else:
    print("Method 2 is " + str(round(((m1time-m2time) / m1time)*100, 2)) + "% faster than method 1")
    print("Method 2 is " + str(round(((m3time - m2time) / m3time) * 100, 2)) + "% faster than method 3")