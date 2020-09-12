def intersection(arrays):
    arr_of_dicts = []
    result = []

    for arr in arrays:
        # create a hashTable for each array to log each elem in the array
        numsMap = {}

        for num in arr:
            if num not in numsMap:
                numsMap[num] = 0

            numsMap[num] += True
        # append each hashTable to the array of dictionaries
        arr_of_dicts.append(numsMap)
    # we only need to loop thru the first dictionary and check which values from it are in all of the other dicts
    for key in arr_of_dicts[0]:
        i = 1
        # here we check if curr key is featured in all the other arrays
        while i < (len(arr_of_dicts)):
            if key in arr_of_dicts[i]:
                i += 1
            else:
                break
        # if true, this means that the key was featured in all of the arrays and can be added to the result array
        if i == len(arr_of_dicts):
            result.append(key)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
