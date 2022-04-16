# Find nsl index and nsr index
# maxArea fro each histogram can be decided using (nsr[i]-nsl[i]-1)*histogram[i]
# return the maxArea


def largestRectangleArea(histogram):
    nslIndex = [-1] * len(histogram)
    nsrIndex = [len(histogram)] * len(histogram)
    stack = []

    for i in range(len(histogram)):
        while len(stack) > 0:
            if stack[-1][0] >= histogram[i]:
                stack.pop()
            else:
                nslIndex[i] = stack[-1][1]
                break
        stack.append((histogram[i], i))

    stack = []
    for i in range(len(histogram) - 1, -1, -1):
        while len(stack) > 0:
            if stack[-1][0] >= histogram[i]:
                stack.pop()
            else:
                nsrIndex[i] = stack[-1][1]
                break
        stack.append((histogram[i], i))
    # print(nsrIndex)

    maxArea = 0
    for i in range(len(histogram)):
        area = (nsrIndex[i] - nslIndex[i] - 1) * histogram[i]
        maxArea = max(maxArea, area)

    print(maxArea)


largestRectangleArea([6, 2, 5, 4, 4, 1, 6])
