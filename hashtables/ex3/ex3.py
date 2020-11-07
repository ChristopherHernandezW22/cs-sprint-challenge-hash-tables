def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    hash_table = {}
    result = []

    for arr in arrays:
        for num in arr:
            if num not in hash_table:
                hash_table[num] = 1
            else:
                hash_table[num] += 1
                if hash_table[num] == len(arrays):
                    result.append(num)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3, 4, 5])
    arrays.append(list(range(2000000, 3000000)) + [12, 7, 2, 9, 1])
    arrays.append(list(range(3000000, 4000000)) + [99, 2, 7, 1])

    print(intersection(arrays))
