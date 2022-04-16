# create increasing from left sequence list
# create increasing from right sequence list
# find min of left right sequence and subtract with the height
# store all the water in total water


def trap(height):
    increasingFromLeft = [-1] * len(height)
    increasingFromRight = [-1] * len(height)

    maxItem = 0
    for i in range(len(height)):
        maxItem = max(maxItem, height[i])
        increasingFromLeft[i] = maxItem

    maxItem = 0
    for i in range(len(height) - 1, -1, -1):
        maxItem = max(maxItem, height[i])
        increasingFromRight[i] = maxItem

    print(increasingFromLeft)
    print(increasingFromRight)

    total_water = 0
    for i in range(len(height)):
        water = min(increasingFromRight[i], increasingFromLeft[i]) - height[i]
        total_water = total_water + water

    return total_water


print(trap([4, 2, 0, 3, 2, 5]))
