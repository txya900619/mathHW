
def print_matrix(matrix):
    for row in matrix:
        print(row)
    print('\n')
    pass


def find_eigenvalues(matrix):
    equation = [1, -1*matrix[0][0]-1*matrix[1][1],
                matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]]  # descending power
    if equation[1]**2-4*equation[0]*equation[2] > 0:
        ans1 = (-equation[1]+(equation[1]**2-4*equation[0]*equation[2])**0.5)/2
        ans2 = (-equation[1]-(equation[1]**2-4*equation[0]*equation[2])**0.5)/2
        return [ans1, ans2]
    elif equation[1]**2-4*equation[0]*equation[2] == 0:
        return [(-equation[1]+(equation[1]**2-4*equation[0]*equation[2])**0.5)/2]
    else:
        return []


def row_reduce(matrix):
    ans = matrix
    row = 0
    col = 0
    while row < 2 and col < 2:
        if ans[row][col] == 0:
            noZeroRow = -1
            for i in range(2-row):
                if ans[i+row][col] != 0:
                    noZeroRow = i
                    break
            if noZeroRow == -1:
                col += 1
                continue
            ans[row], ans[noZeroRow] = ans[noZeroRow], ans[row]

        ans[row][0], ans[row][1] = ans[row][0] / \
            ans[row][col], ans[row][1]/ans[row][col]
        if row == 0:
            tmp = ans[1][0]
            ans[1][0] -= ans[0][0]*tmp
            ans[1][1] -= ans[0][1]*tmp
        row += 1
        col += 1
    if ans[1][1] != 0 and ans[0][1] != 0:
        ans[0][1] -= ans[1][1]
    return ans


def find_eigenvectors(eigenvalues, matrix):
    ans = [[], []]
    for eigenvalue in eigenvalues:
        tempMatrix = []

        for row in matrix:
            tempRow = []
            for col in row:
                tempRow.append(col)
            tempMatrix.append(tempRow)

        tempMatrix[0][0] -= eigenvalue
        tempMatrix[1][1] -= eigenvalue
        tempMatrix = row_reduce(tempMatrix)
        if tempMatrix[0][0] == 0:
            ans[0].append(1)
            ans[1].append(0)
        if tempMatrix[0][0] != 0:
            ans[0].append(-tempMatrix[0][1])
            ans[1].append(1)

    return ans


def main():
    S = [[2, 0], [0, -5]]
    T = [[2, -12], [1, -5]]
    U = [[5, 2], [2, 3]]
    V = [[1, 1], [1, 1]]
    W = [[2, 1], [0, 2]]
    X = [[3, 1], [-1, 1]]
    Y = [[0, 1], [-1, 0]]
    Z = [[3, -5], [1, 1]]
    S_eigenvalues = find_eigenvalues(S)
    print('S eigenvalues: {}'.format(S_eigenvalues))
    print("S eigenvectors: ")
    print_matrix(find_eigenvectors(S_eigenvalues, S))
    T_eigenvalues = find_eigenvalues(T)
    print("T eigenvalues: {}".format(T_eigenvalues))
    print("T eigenvectors: ")
    print_matrix(find_eigenvectors(T_eigenvalues, T))
    U_eigenvalues = find_eigenvalues(U)
    print("U eigenvalues: {}".format(U_eigenvalues))
    print("U eigenvectors: ")
    print_matrix(find_eigenvectors(U_eigenvalues, U))
    V_eigenvalues = find_eigenvalues(V)
    print("V eigenvalues: {}".format(V_eigenvalues))
    print("V eigenvectors: ")
    print_matrix(find_eigenvectors(V_eigenvalues, V))
    W_eigenvalues = find_eigenvalues(W)
    print("W eigenvalues: {}".format(W_eigenvalues))
    print("W eigenvectors: ")
    print_matrix(find_eigenvectors(W_eigenvalues, W))
    X_eigenvalues = find_eigenvalues(X)
    print("X eigenvalues: {}".format(X_eigenvalues))
    print("X eigenvectors: ")
    print_matrix(find_eigenvectors(X_eigenvalues, X))
    Y_eigenvalues = find_eigenvalues(Y)
    print("Y eigenvalues: {}".format(Y_eigenvalues))
    print("Y eigenvectors: ")
    Y_eigenvectors = find_eigenvectors(Y_eigenvalues, Y)
    if len(Y_eigenvectors[0]) == 0:
        print('no eigenvectors')
    else:
        print_matrix(Y_eigenvectors)
    Z_eigenvalues = find_eigenvalues(Z)
    print("Z eigenvalues: {}".format(Z_eigenvalues))
    print("Z eigenvectors: ")
    Z_eigenvectors = find_eigenvectors(Z_eigenvalues, Z)
    if len(Z_eigenvectors[0]) == 0:
        print('no eigenvectors')
    else:
        print_matrix(Z_eigenvectors)


if __name__ == "__main__":
    main()
