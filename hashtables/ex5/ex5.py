def finder(files, queries):
    result = []
    queryMap = {}
    # log each query in a hashTable
    for q in queries:
        queryMap[q] = True

    for f in files:
        i = len(f) - 1
        # loop backwards from each file till a "/" occurs
        while f[i] != "/":
            i -= 1
        # now check if that file path is in the query hashTable
        if f[i+1:] in queryMap:
            # if so, append it to the result array
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
