# Follow this solution: https://www.geeksforgeeks.org/write-a-c-program-to-print-all-permutations-of-a-given-string/
# 


def allPermutation(string, s, n):
    tempString = []
    for i in string:
        tempString.append(i)
    if s == n:
        return print(string)
    for i in range(s, n):
        tempString[0+i], tempString[0] = tempString[0], tempString[0+i]
        allPermutation(tempString, s + 1, n)


allPermutation(['A', 'B', 'C'], 0, 3)
