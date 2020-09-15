def finder(files, queries):
    result = []
    queryMap = {}
    # log each query in a hashTable
    for q in queries:
        queryMap[q] = True

    for f in files:
        arr = f.split("/")
        # i will equal the index of the first character of f's file name
        # now we can check if that file name is in the query hashTable
        if arr[len(arr) - 1] in queryMap:
            # if so, append the current file to the result array
            result.append(f)

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
