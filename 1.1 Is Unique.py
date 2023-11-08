import time
# Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?

#time variables
m1time = 0
m2time = 0

# brute force first attempt O(n^2)
def isUnique(string):
    global m1time
    begin = time.time()
    for currLetter in range(0, len(string)):
        for letter in range(len(string) - 1, 0, -1):
            if string[letter].lower() == string[currLetter].lower() and letter != currLetter:
                time.sleep(.001)
                end = time.time()
                print(end - begin-.001)
                m1time += end - begin - .001
                return False
    time.sleep(.001)
    end = time.time()
    print(end-begin-.001)
    m1time += end-begin-.001
    return True

print("Method one tests")
assert isUnique("hello") == False
assert isUnique("world") == True
assert isUnique("racecar") == False
assert isUnique("bannana") == False
assert isUnique("Uncopyrightable") == True
assert isUnique("Uncopyrightablu") == False

#attempt with a set O(N)
def isUnique(string):
    global m2time
    begin = time.time()
    unique = set(s.lower() for s in string)
    if len(unique) == len(string):
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
print("Method two tests")
assert isUnique("hello") == False
assert isUnique("world") == True
assert isUnique("racecar") == False
assert isUnique("bannana") == False
assert isUnique("Uncopyrightable") == True
assert isUnique("Uncopyrightablu") == False

print("Every thing passed")
print("Method 1 took: " + str(round(m1time, 4)) + " seconds to complete the tests")
print("Method 2 total took: " + str(round(m2time, 4)) + " seconds to complete the tests")
print("Difference in time to complete the tests between method 1 and method 2: " + str(abs(round(m1time-m2time, 6))) + " seconds")
if m1time < m2time:
    print("Method 1 is " + str(round(((m2time-m1time)/m2time)*100, 2)) + "% faster than method 2")
else:
    print("Method 2 is " + str(round(((m1time-m2time) / m1time)*100, 2)) + "% faster than method 1")
