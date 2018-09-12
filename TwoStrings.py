def twoStrings(s1, s2):
    # Loop through each character in s2 and see if it is in s1
    # and add that letter to this list
    # If list is empty then if statement will be false
    if [letter for letter in s2 if (letter in s1)]:
        return "YES"
    else:
        return "NO"
s1 = "hello"
s2 = "world"

print("Strings:\n {}\n {}".format(s1, s2))
print(twoStrings(s1,s2))