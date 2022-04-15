# How do you check if two strings are anagrams of each other?

# Approach 1:
# sort both the strings and compare them. Time Complexity: O(nlogn)

# Approach 2:
# use two hashMap, traverse both the string and maintain character count. Compare both the hashMap

# Approach 3:
# use single hashMap, traverse one string and store character count in hashMap. Traverse second string and subtract count for each character.
# if all the characters have count = 0 then strings are anagram else not.


