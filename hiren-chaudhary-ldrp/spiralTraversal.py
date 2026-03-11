def spiralTraversal(mat):
    result = []
    
    if not mat or not mat[0]:
        return result
    
    top, bottom = 0, len(mat) - 1
    left, right = 0, len(mat[0]) - 1
    
    while top <= bottom and left <= right:
        
        # move right
        for i in range(left, right + 1):
            result.append(mat[top][i])
        top += 1
        
        # move down
        for i in range(top, bottom + 1):
            result.append(mat[i][right])
        right -= 1
        
        if top <= bottom:
            # move left
            for i in range(right, left - 1, -1):
                result.append(mat[bottom][i])
            bottom -= 1
        
        if left <= right:
            # move up
            for i in range(bottom, top - 1, -1):
                result.append(mat[i][left])
            left += 1
    
    return result

mat = [[1,2,3],[4,5,6],[7,8,9]]
print(spiralTraversal(mat))