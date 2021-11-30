
def find_minimum_movements(lot):
    i = 0
    # global result 
    # result = [0]

    def dfs(lot, i, j, count, steps):
        # if count == 1:
        #     return 0
        
        if (i<0 or i>=len(lot) or j<0 or j>=len(lot[i]) or lot[i][j] == 0):
            # print(False)
            return False
        print(lot[i][j])
        if lot[i][j] == 9:
            count+=1
            return 1

        
        temp = lot[i][j]
        lot[i][j] = 0

        found = (dfs(lot,i+1,j, count, steps+1 ) or dfs(lot, i-1,j, count, steps+1 ) or dfs(lot, i, j+1, count,steps+1) or dfs(lot, i, j-1, count,steps+1 ))
        lot[i][j] = temp
        # if found and steps<result[0]:
        #     print(steps)
        #     result = steps
        return found+1 if found else found

    for j in range(len(lot[i])):
        if lot[i][j] == 1:
            result = dfs(lot, i,j, 0, 0)
            if result:
                return result-1
    return -1

    



if __name__ == '__main__':
    lot = [
        [1,0,9],
        [1,1,1],
        [1,0,0]
    ]
    # lot = [
    #     [1,0,0],
    #     [1,0,0],
    #     [1,9,0]
    # ]
    print(find_minimum_movements(lot))