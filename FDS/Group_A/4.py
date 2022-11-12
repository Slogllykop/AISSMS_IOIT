# Write a python program that determines the location of a saddle point of matrix if one exists. An
# m x n matrix is said to have a saddle point if some entry a[i][j] is the smallest value in row i and
# the largest value in j.


def findSaddlePoint(mat, n):

    # Process all rows one
    # by one
    for i in range(n):

        # Find the minimum element
        # of row i.
        # Also find column index of
        # the minimum element
        min_row = mat[i][0]
        col_ind = 0

        for j in range(1, n):

            if (min_row > mat[i][j]):
                min_row = mat[i][j]
                col_ind = j

        # Check if the minimum element
        # of row is also the maximum
        # element of column or not
        k = 0
        for k in range(n):

            # Note that col_ind is fixed
            if (min_row < mat[k][col_ind]):
                break

            k += 1

        # If saddle point present in this
        # row then print
        if (k == n):
            print("Value of Saddle Point ", min_row)
            return True

    # If Saddle Point found
    return False


# main matrix
mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

n = 3
if (findSaddlePoint(mat, n) == False):
    print("No Saddle Po")
