def mat_mul(mat1, mat2):
    row1 = len(mat1)
    col1 = len(mat1[0])
    row2 = len(mat2)
    col2 = len(mat2[0])
    res_mat =[[0]*col2]*row1
    if col1 == row2:
        for row in range(row1):
            for col in range(col2):
                each_sum = 0
                for ele in range(col1):
                    each_sum += (mat1[row][ele] * mat2[ele][col])
                res_mat[row][col] = each_sum
    return res_mat

