def rotLeft(a, d):
    # Take the last part after the number of rotations and place it at
    # the beginning then take the first part before the number of rotations
    # and place it at the end.
    rotated_list = a[d:] + a[:d]
    return rotated_list

a = [1,2,3,4,5]
d = 3
print(a)
print("Left Rotated: {}".format(rotLeft(a, d)))