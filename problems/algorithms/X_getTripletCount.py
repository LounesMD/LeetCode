def getTripletIndices(a, d):
    """
    d = a_i + a_j + a_k
    """
    n = len(a)
    result = []  # Stores index triplets
    for i in range(n):
        new_target = d - a[i]
        res = {}  # Dictionary to store {value: index}
        for j in range(i + 1, n):  # Ensure distinct indices
            if a[j] in res:  # Found a valid triplet
                result.append((i, res[a[j]], j))  # Store indices
            
            res[new_target - a[j]] = j  # Store {needed complement: index} for future lookups
    
    return result


print(getTripletIndices(a=[3, 3,4, 2, 1, 2, 7, 8], d = 5))