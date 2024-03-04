def merge_sort(string):
    if len(string) <= 1:
        return string

    mid = len(string) // 2
    left = string[:mid]
    right = string[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return "".join(result)


def is_anagram(first_string, second_string):
    if not first_string or not second_string:
        return merge_sort(first_string), merge_sort(second_string), False

    sorted_first = merge_sort(first_string.lower())
    sorted_second = merge_sort(second_string.lower())

    return sorted_first, sorted_second, sorted_first == sorted_second


if __name__ == "__main__":
    first_string = "amor"
    second_string = "roma"
    print(is_anagram(first_string, second_string))
