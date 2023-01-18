# Example 2

array = [10, 20, 30, 40, 50, 60, 100, 120, 700, 800]  # length = 10


def bisect(nums, target):
    size = len(nums)
    for i in range(size):
        if nums[i] == target:
            return i
    return -1


res = bisect(array, 800)
print(f"\n{res}")

# Runtime complexity O(n)
