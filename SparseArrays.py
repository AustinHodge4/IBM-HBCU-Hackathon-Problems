def matchingStrings(strings, queries):
    # Set empty list
    result = [0] * len(queries)
    # Loop through queries and strings and find if they match
    for index, query in zip(range(len(queries)), queries):
        for string in strings:
            if string == query:
                # Add one to the current query matches 
                result[index] += 1
    return result

strings = ['ab', 'ab', 'abc']
queries = ['ab', 'abc', 'bc']

print("Strings: {}".format(strings))
print("Queries: {}".format(queries))
print("Matches: {}".format(matchingStrings(strings, queries)))