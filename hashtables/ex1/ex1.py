def get_indices_of_item_weights(weights, length, limit):
    hashMap = {}

    for i in range(len(weights)):
        curr = weights[i]

        if (limit - curr) in hashMap:
            return (i, hashMap[limit - curr])
        else:
            hashMap[curr] = i

    return None


# test data below
weights = [4, 6, 10, 15, 16]
length = 5
limit = 21

print(get_indices_of_item_weights(weights, length, limit))  # -> (3, 1)
