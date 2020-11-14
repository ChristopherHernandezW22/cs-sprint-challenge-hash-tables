def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here

    # Creating hash table
    # key: number, value: boolean (list containing negation)
    ht = {}

    # assign result variable to empty array
    result = []

    # Loop through numbers:
    for num in a:
        # If number is greater than 0, it's a positive number
        if num > 0:
            # If a positive number is not in hash table
            if num not in ht:
                # Make it False
                ht[num] = False
            # If the negative version of that number is in ht
            if -num in ht:
                # Make it True
                ht[-num] = True
                ht[num] = True
        # Else it's a negative number
        else:
            # If a negative number is not in hash table
            if num not in ht:
                # Make it False
                ht[num] = False
            # If the absolute number version of that negative number is in ht
            if abs(num) in ht:
                # Make it True
                ht[abs(num)] = True
                ht[num] = True

    # Iterate through the entries
    for num, boolean in ht.items():
        if boolean is True and num > 0:
            result.append(num)

    return result

if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
    