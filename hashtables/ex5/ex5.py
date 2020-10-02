# Your code here

def finder(files, queries):
    """
    YOUR CODE HERE
    """
    cache = {}
    result = []
  

    for query in queries:
    # put them in the cache
        cache[query] = []
   
    for item in files:
        split = item.split('/')
        if split[-1] in cache:
            cache[split[-1]].append(item)

    for item in cache.items():
        result += item[1]


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

    # files = []

    # for i in range(500000):
    #     files.append(f"/dir{i}/file{i}")

    # for i in range(500000):
    #     files.append(f"/dir{i}/dirb{i}/file{i}")

    # queries = []

    # for i in range(1000000):
    #        queries.append(f"nofile{i}")

    # queries += [
    #     "file3490",
    #     "file256",
    #     "file999999",
    #     "file8192"
    # ]
    print(finder(files, queries))
