# Linear Search
def linear_search(nums:list, target:int):
    if target in nums:
        return nums.index(target)

#Correct Binary Search using recursion
def binary_search(nums:list, target:int, low:int = 0, high:int = None) -> int:
    if high is None:
        high = len(nums) - 1
    if low > high:
        return -1
    mid = (low+high)//2
    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        return binary_search(nums, target, mid+1, high)
    else:
        return binary_search(nums, target, low, mid-1)

#Binary search using loops instead of recursion
def Binary(nums:list, target:int) ->int:
    lower_bound = 0
    upper_bound = len(nums) - 1
    while lower_bound <= upper_bound:
        mid = (lower_bound + upper_bound)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            upper_bound = mid - 1
        else:
            lower_bound = mid + 1
    return -1