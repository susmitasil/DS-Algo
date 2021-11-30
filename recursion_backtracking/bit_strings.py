def appendAtFront(x, L):
    # print('L ',[element for element in L])
    # print('x + L  ',x,'  ',[x + element for element in L])
    return [x + element for element in L]

def bitStrings(n):
    if n==0:
        return []
    if n==1:
        return ["0","1"]
    else:
        return (appendAtFront("0", bitStrings(n-1)) + appendAtFront("1", bitStrings(n-1)))

print(bitStrings(4))