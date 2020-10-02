def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here`
    cache = {}
    output = []
    count = 1
    # loop over arrays
    for array in arrays:
        # loop over items in array
        for item in array:
            # if item is in cache, add +1 to count
            if item in cache:
                cache[item] = count + 1
            # if not, add it and set the count at 1
            else:
                cache[item] = count
            
    # loop over cache
    for item in cache:
        if cache[item] > 1:
            output.append(item)
   
    return output


    # return output


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1, 5)) + [1, 2, 3])
    arrays.append(list(range(5, 10)) + [1, 2, 3])
    arrays.append(list(range(10, 15)) + [1, 2, 3])

    print(intersection(arrays))
