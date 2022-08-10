def buildArray(target, n):
    res = []
    for i in range(1, n + 1):
        if i in target:
            res.append("Push")  
        elif i < target[-1]:
            res.extend(["Push", "Pop"])
    return res

print(buildArray([1,3], 3))