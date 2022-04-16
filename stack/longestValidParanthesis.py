# start with -1 in the stack
# The aim is to find valid parenthesis sub string.
# For each '(' we push index i in stack
# For each ')' ->
# push index i in stack if stack top is -1
# pop element if top index has element ( and calculate max
# if stack top has index has element ( then push index of i in stack


def longestValidParentheses(s):
    stack = [-1]
    maxValid = 0
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
        else:
            if stack[-1] == -1:
                stack.append(i)
                continue
            if s[stack[-1]] == '(':
                stack.pop()
                maxValid = max(maxValid, i - stack[-1])
                continue
            if s[stack[-1]] == ')':
                stack.append(i)

    return maxValid

print(longestValidParentheses("()(()"))
