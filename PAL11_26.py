nums = [1,2,3,4,5]
length = len(nums)-1
reversedList = []
def reverse(i, List, reversed):
    reversed.append(List[i])
    if i > 0:
        reverse(i-1, List, reversed)
    return(reversed)

print(reverse(length, nums, reversedList))
