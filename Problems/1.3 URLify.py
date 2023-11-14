"""
URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string
has sufficient space at the end to hold the additional characters, and that you are given the "true"
length of the string. (Note: If implementing in Java, please use a character array so that you can
perform this operation in place.)
EXAMPLE
Input: "Mr 3ohn Smith"
Output: "Mr%203ohn%20Smith"
"""

#First Attempt replace O(1)? possibly O(n) depending on how replace fully works
#After looking it up seems to be O(N+M) with N being length of the string and M being number of occurrences
def URLifyV1(string):
    string = string.replace(" ", "%20")
    return string

#Second Attempt Split and Combine O(N+M)
def URLifyV2(string):
    string = string.split(" ")
    result = ""
    for s in range(len(string)):
        result += string[s]
        if s != len(string)-1:
            result += "%20"
    return result



#Third Attempt List and Combine O(N+N) or O(N)?
def URLifyV3(string):
    string = list(string)
    result = ""
    for s in string:
        if s != " ":
            result += s
        else:
            result += "%20"
    return result
