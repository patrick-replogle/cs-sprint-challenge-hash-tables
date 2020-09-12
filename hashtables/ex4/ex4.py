def has_negatives(a):
    result = []
    hashMap = {}

    for num in a:
        hashMap[num] = True

    for key in hashMap:
        if key > 0:
            if -(key) in hashMap and key not in result:
                result.append(key)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
