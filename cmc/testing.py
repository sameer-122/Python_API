def dictionary_counting_sort(lst):
    counts = {}

    # Count the occurrences of each element in the list
    for num in lst:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    sorted_list = []

    # Construct the sorted list based on the counts
    for num, count in sorted(counts.items()):
        sorted_list.extend([num] * count)

    return sorted_list
if __name__ == '__main__':
    # Example usage
    numbers = [4, 2, 5, 1, 3, 4, 5, 2, 3, 1, 2, 4]
    sorted_numbers = dictionary_counting_sort(numbers)
    print(sorted_numbers)
