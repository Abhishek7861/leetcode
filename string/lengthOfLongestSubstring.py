# while char found in hashSet remove the char and move left+1
# if. char not found in hashSet push char in hashset, calculate maxSubSubtring length - right+1
# return the maxSubString




def lengthOfLongestSubstring(s):
    hashSet = {}
    left = 0
    right = 0
    maxSubString = 0

    while right < len(s):
        if s[right] in hashSet.keys():
            while s[right] in hashSet.keys():
                hashSet.pop(s[left])
                left = left + 1
        else:
            hashSet[s[right]] = right
            maxSubString = max(maxSubString, right - left + 1)
            right = right + 1

    return maxSubString


lengthOfLongestSubstring("pwwkew")
