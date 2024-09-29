def getTripletCount1(a, d):
    """
    Complexity: O(n^3).
    Better solution with one or two iterations using dict.
    """
    cpt = 0
    for i in range(len(a) - 2):
        for j in range(i+1, len(a) - 1):
            for k in range(j+1, len(a)):
                if ((a[i] + a[j] + a[k]) % d == 0):
                    cpt += 1
    return cpt

print(getTripletCount(a=[3, 3,4, 7, 8], d = 5))