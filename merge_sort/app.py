def merge_sort(arr):
    if len(arr) == 1:
        return arr

    midpint = len(arr) // 2

    sublist_a = arr[:midpint]
    sublist_b = arr[midpint:]

    first_half = merge_sort(sublist_a)
    second_half = merge_sort(sublist_b)

    return merge(first_half, second_half)


def merge(first_sublist, second_sublist):
    i = j = 0

    merged_list = []

    while i < len(first_sublist) and j < len(second_sublist):

        if first_sublist[i] < second_sublist[j]:
            merged_list.append(first_sublist[i])
            i += 1

        else:
            merged_list.append(second_sublist[j])
            j += 1

    while i < len(first_sublist):
        merged_list.append(first_sublist[i])
        i += 1

    while j < len(second_sublist):
        merged_list.append(second_sublist[j])
        j += 1

    return merged_list


marks = [78, 90, 89, 67, 91, 90, 67, 56, 45, 13, 4, 11]
print(merge_sort(marks))
