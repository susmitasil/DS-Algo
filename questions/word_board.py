# Find the given word in a matrix of letters.
# -------------------------------------------

board = [
    ['A','B','C','E'],
    ['S','F','C','S'],
    ['A','D','E','E'],
]
# word = 'ABCCED'
# word = 'SEE'
word = 'ABCB'
def dfs(board, i, j, count, word):
    # print(board[i][j])
    if count == len(word):
        return True

    if (i<0 or i>=len(board) or j<0 or j>=len(board[i]) or board[i][j] != word[count]):
        # print(False)
        return False

    temp = board[i][j]
    print(temp)
    board[i][j] = ''

    found = dfs(board, i+1,j, count+1, word ) or dfs(board, i-1,j, count+1, word ) or dfs(board, i, j+1, count+1, word ) or dfs(board, i, j-1, count+1, word )
    # print('find ',  found)
    board[i][j] = temp
    return found

def find_word():
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == word[0] and dfs(board, i, j , 0, word):
                return True
            # return False
    return False

print(find_word())
