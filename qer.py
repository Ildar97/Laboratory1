def MaxAndMinElement (a = []):
    if len(a) != 0:
        max = a[0]
        min = a[0]
    for i in range(len(a)):
        if a[i] > max:
            max = a[i]
        if a[i] < min:
            min = a[i]
    return max,min
