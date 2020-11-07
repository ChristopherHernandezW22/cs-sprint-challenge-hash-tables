def has_negatives(arr, a):
    """
    YOUR CODE HERE
    """
    # Your code here
    values = []

    # for each item in array
    for i in range(a):

        # finding the negative value of array[i] from i + 1 to
        for j in range(i + 1, a):

            # if the absolute value matches, append
            if(abs(arr[i])) == abs(arr[j]):
                values.append(abs(arr[i]))

    # print "0" if size of vector is 0
    if (len(values) == 0):
        return;

    values.sort()

    # printing negative and positive pairings
    for i in range(len(values)):
        # print(-values[i], "", values[i], end = " ") # print pairs
        print(values[i], end = " ") # print positives that contains negatives

    # return result

if __name__ == "__main__":
    # print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
    arr = [-1, -2, 1, 2, 3, 4, -4]
    a = len(arr)
    has_negatives(arr, a)
