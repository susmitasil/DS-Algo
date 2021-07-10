# arr = [0,8,4,2,6,10,9,13,11,7,15]
arr = [0,1,0,3,2,3] 
result = []

for i in range(len(arr)):
    temp = []
    temp.append(arr[i])
    c = 1
    j=i+c

    while j < len(arr):
        if temp[-1]<arr[j]:
            temp.append(arr[j])
            print('in temp', temp)
            # print(temp[-1], arr[j])
        
        if j+1 >= len(arr):
            # print('hi', temp)
            # print(len(temp), len(result))
            if len(temp)> len(result):
                result = temp.copy()
                # print('inside result ', result)
            temp.clear()
            temp.append(arr[i])
            c+=1
            j=i+c
            continue
        
        j+=1

        if len(temp)> len(result):
            result = temp.copy()

print('result ',result)
        