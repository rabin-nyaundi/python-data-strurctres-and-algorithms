"""
Binary Search algorithm  finds a given item from the given sorted list of items
The worst case is O(log n)
"""
array = [10, 20, 30, 40, 50, 60, 100, 120, 700, 800]  # length = 10
# Example 1
def binary_search(nums: list, first_index, last_index, search_for):

    if last_index >= first_index:
        mid_index = (first_index + last_index) // 2
        mid_element = nums[mid_index]

        if mid_element == search_for:
            return mid_index
        elif mid_element > search_for:
            last_index = mid_index - 1
            return binary_search(nums, first_index, last_index, search_for)
        elif mid_element < search_for:
            first_index = mid_index + 1
            return binary_search(nums, first_index, last_index, search_for)
    else:
        return "Element search for not found"



first = 0
last = len(array) - 1
result = binary_search(array, first, last, 800)

print(result)
# Runtime complexity = O(log n)


# Example 2
def binary_search_example(nums, target):
    i = 0
    j = len(nums) - 1
    while i <= j:
        if nums[i] == target:
            return i
        if nums[j] == target:
            return j

        i += 1
        j -= 1


res = binary_search_example(array, 800)
print(f"\n{res}")

# Example 3
def binary_search_example_4(nums, target):
    first = 0
    last = len(nums) - 1

    while first <= last:
        mid_index = int(first + last) // 2
        mid_element = nums[mid_index]

        if mid_element == target:
            return mid_index
        elif mid_element > target:
            last = mid_index - 1
        else:
            first = mid_index + 1

    return -1


answer = binary_search_example_4(array, 700)
array2 = [-1, 0, 5]
answer2 = binary_search_example_4(array2, -1)
print(answer, answer2)
