# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    result = []
    for file in files:
        elements = file.split("/")
        if elements[-1] not in cache:
            cache[elements[-1]] = [file]
        else:
            cache[elements[-1]].append(file)

    for query in queries:
        if query in cache:
            result.extend(cache[query])

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
