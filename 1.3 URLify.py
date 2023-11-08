import time
"""
URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string
has sufficient space at the end to hold the additional characters, and that you are given the "true"
length of the string. (Note: If implementing in Java, please use a character array so that you can
perform this operation in place.)
EXAMPLE
Input: "Mr 3ohn Smith"
Output: "Mr%203ohn%20Smith"
"""
m1time = 0
m2time = 0
m3time = 0

#First Attempt replace O(1)? possibly O(n) depending on how replace fully works
#After looking it up seems to be O(N+M) with N being length of the string and M being number of occurrences
def URLify(string):
    global m1time
    begin = time.time()
    string = string.replace(" ", "%20")
    time.sleep(.001)
    end = time.time()
    print(end - begin - .001)
    m1time += end - begin - .001
    return string

print("Method 1 Times")
assert URLify("Mr 3ohn Smith") == "Mr%203ohn%20Smith"
assert URLify("The cat is out of the bag") == "The%20cat%20is%20out%20of%20the%20bag"
assert URLify("Space") == "Space"
assert URLify("avacado is spelled avocado") == "avacado%20is%20spelled%20avocado"
assert URLify("Sam and Tim") == "Sam%20and%20Tim"
assert URLify("%20 %20 %20") == "%20%20%20%20%20"

#Second Attempt Split and Combine O(N+M)
def URLify(string):
    global m2time
    begin = time.time()
    string = string.split(" ")
    result = ""
    for s in range(len(string)):
        result += string[s]
        if s != len(string)-1:
            result += "%20"
    time.sleep(.001)
    end = time.time()
    print(end - begin - .001)
    m2time += end - begin - .001
    return result

print()
print("Method 2 Times")
assert URLify("Mr 3ohn Smith") == "Mr%203ohn%20Smith"
assert URLify("The cat is out of the bag") == "The%20cat%20is%20out%20of%20the%20bag"
assert URLify("Space") == "Space"
assert URLify("avacado is spelled avocado") == "avacado%20is%20spelled%20avocado"
assert URLify("Sam and Tim") == "Sam%20and%20Tim"
assert URLify("%20 %20 %20") == "%20%20%20%20%20"


#Third Attempt List and Combine O(N+N) or O(N)?
def URLify(string):
    global m3time
    begin = time.time()
    string = list(string)
    result = ""
    for s in string:
        if s != " ":
            result += s
        else:
            result += "%20"
    time.sleep(.001)
    end = time.time()
    print(end - begin - .001)
    m3time += end - begin - .001
    return result

print()
print("Method 3 Times")
assert URLify("Mr 3ohn Smith") == "Mr%203ohn%20Smith"
assert URLify("The cat is out of the bag") == "The%20cat%20is%20out%20of%20the%20bag"
assert URLify("Space") == "Space"
assert URLify("avacado is spelled avocado") == "avacado%20is%20spelled%20avocado"
assert URLify("Sam and Tim") == "Sam%20and%20Tim"
assert URLify("%20 %20 %20") == "%20%20%20%20%20"

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