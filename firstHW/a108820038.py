def is_matrix(array):
    length = len(array[0])
    for row in array:
        if len(row) != length:
            return False
    return True


def is_multiable(first, second):
    if len(first[0]) == len(second):
        return True
    return False


def is_square(array):
    if len(array) == len(array[0]):
        return True
    return False


def calc_det(matrix):
    tmp = 0
    tmp += (matrix[0][0]*matrix[1][1])
    tmp -= (matrix[0][1]*matrix[1][0])
    return tmp


def comparelength(first, second):
    if len(first[0]) != len(second[0]):
        return False
    return True


def compareheight(first, second):
    if len(first) != len(second):
        return False
    return True


def transfer_matrix(matrix):
    assert is_matrix(matrix)
    new_matrix = []
    for i in range(len(matrix[0])):
        new_matrix.append([])
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            new_matrix[i].append(matrix[j][i])
    return new_matrix


def plus_and_sub_matrix(first, second, method):
    assert is_matrix(first)
    assert is_matrix(second)
    assert comparelength(first, second)
    assert compareheight(first, second)
    new_matrix = []
    if method == "+":
        for i, row in enumerate(second):
            new_matrix.append([])
            for j, col in enumerate(row):
                if type(col) == str or type(first[i][j]) == str:
                    new_matrix[i].append(str(first[i][j])+method+str(col))
                else:
                    new_matrix[i].append(first[i][j] + col)
        return new_matrix
    if method == "-":
        for i, row in enumerate(second):
            new_matrix.append([])
            for j, col in enumerate(row):
                if type(col) == str or type(first[i][j]) == str:
                    new_matrix[i].append(str(first[i][j])+method+str(col))
                else:
                    new_matrix[i].append(first[i][j] - col)
        return new_matrix


def multiply_matrix(first, second):
    if type(second) == int or type(second) == float:
        first, second = second, first
    if type(first) == int or type(first) == float:
        assert is_matrix(second)
        new_matrix = []
        for i in range(len(second)):
            new_matrix.append([])
            for j in range(len(second[i])):
                new_matrix[i].append(first*second[i][j])
        return new_matrix
    else:
        assert is_matrix(first)
        assert is_matrix(second)
        assert is_multiable(first, second)
        new_matrix = []

        for i in range(len(first)):
            new_matrix.append([])
            for j in range(len(second[0])):
                tmp = 0
                for z in range(len(second)):
                    tmp += first[i][z]*second[z][j]
                new_matrix[i].append(tmp)
        return new_matrix


def inverse_matrix(matrix):
    assert is_square(matrix)
    det = calc_det(matrix)
    assert det != 0
    return multiply_matrix(1/det, [[matrix[1][1], -matrix[0][1]], [-matrix[1][0], matrix[0][0]]])


def main():
    a = [[-1, 2, 0], [2, 0, 3]]
    b = [[2, 0, -1], [1, -2, 0]]
    c = [[0, 2], [1, 0], [-1, 1]]
    e = [[2, -1], ["pi", "log2"], [-2, 6]]
    i = [[1, 0], [0, 1]]
    f = multiply_matrix(a, c)
    print(plus_and_sub_matrix(a, multiply_matrix(2, b), "+"))
    print(plus_and_sub_matrix(c, e, "-"))
    print(transfer_matrix(a))
    print(transfer_matrix(e))
    print(f)
    print(multiply_matrix(c, a))
    print(inverse_matrix(f))
    print(multiply_matrix(inverse_matrix(f), f))
    print(i == multiply_matrix(inverse_matrix(f), f))


if __name__ == "__main__":
    main()
