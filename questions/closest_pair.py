# Find the closest pair from two sorted arrays

ar1 = [1, 4, 5, 7]
ar2 = [10, 20, 30, 40]
# x = 32 
x = 41
pair = []
i=len(ar2)-1
j=len(ar1)-1
while x!= 0 :
    if len(str(x))>1:
        if ar2[i]<=x:
            x = x-ar2[i]
            pair.append(ar2[i])
        else:
            i-=1
    else:
        if ar1[j]<=x:
            x = x-ar1[j]
            pair.append(ar1[j])
        else:
            j-=1

print(pair[:2])