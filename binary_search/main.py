"""
Binary Search algorithm  finds a given item from the given sorted list of items
The worst case is O(log n)
"""
array = [10, 20, 30, 40, 50, 60, 100, 120, 700, 800]  # length = 10
# Example 1
def binary_search_example_1(nums: list, first_index, last_index, search_for):

    if last_index >= first_index:
        mid_index = (first_index + last_index) // 2
        mid_element = nums[mid_index]

        if mid_element == search_for:
            return mid_index
        elif mid_element > search_for:
            last_index = mid_index - 1
            return binary_search_example_1(nums, first_index, last_index, search_for)
        elif mid_element < search_for:
            first_index = mid_index + 1
            return binary_search_example_1(nums, first_index, last_index, search_for)
    else:
        return "Element search for not found"


first = 0
last = len(array) - 1
result = binary_search_example_1(array, first, last, 800)
print("*" * 10)
print(f"Example 1 \n Answer: => Element 800 found at index {result}")
print("*" * 10)
# Runtime complexity = O(log n)


# Example 2
def binary_search_example_2(nums, target):
    i = 0
    j = len(nums) - 1
    while i <= j:
        if nums[i] == target:
            return i
        if nums[j] == target:
            return j

        i += 1
        j -= 1


res = binary_search_example_2(array, 800)
print("*" * 10)
print(f"Example 2 \n Answer: => Element 800 found at index {res}")
print("*" * 10)

# Example 3
def binary_search_example_3(nums, target):
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


answer = binary_search_example_3(array, 700)
array2 = [-1, 0, 5]
answer2 = binary_search_example_3(array2, -1)
print(answer, answer2)

print("*" * 10)
print(f"Example 3 \n Answer: => Element 700 and -1 found at index {answer, answer2} respectively")
print("*" * 10)


def binary_search_example_4(nums, start, end, search_for):

    while end >= start:
        mid = start + (end - start) // 2
        mid_element = nums[mid]

        if mid_element == search_for:
            return f"Element {search_for} found at index {mid}"

        elif mid_element > search_for:
            end = mid - 1

        else:
            start = mid + 1

    return -1


example_4 = binary_search_example_4(array, 0, len(array) - 1, 0)
print("*" * 10)
print(f"Example 4 \n Answer: =>   {example_4}")
print("*" * 10)
