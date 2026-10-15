def most_frequent(items):
    # OR if items == []:
    if not items:
        return None

    counts = {}
    for num in items:
        if num not in counts:
            counts[num] = 1
        else:
            counts[num] += 1

    most_frequent_item = None
    highest_count = 0

    for key, count in counts.items():
        if count > highest_count:
            highest_count = count
            most_frequent_item = key

    return most_frequent_item


print(most_frequent([]))
