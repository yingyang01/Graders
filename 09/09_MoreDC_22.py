def read_matrix():
    m = []
    nrows = int(input())
    for k in range(0, nrows, 1):
        m.append([float(e) for e in input().split()])
    return m

def mult_c(c, A):
    for i in range(len(A)):
        for j in range(len(A[i])):
            A[i][j] *= c
    return A

def mult(A, B):
    A_rows = len(A)
    A_cols = len(A[0]); B_cols = len(B[0])
    C = []
    for i in range(0, A_rows, 1):
        temp = []
        for j in range(0, B_cols, 1):
            temp.append(0)
        C.append(temp)
    for i in range(0, A_rows, 1):
        for j in range(0, B_cols, 1):
            sgm = 0
            for k in range(0, A_cols, 1):
                sgm += A[i][k]*B[k][j]
            # print("sgm : {}".format(sgm))
            C[i][j] = sgm
            # print("C[{}][{}] : {}".format(i, j, C[i][j]))
            # print(C)
    return C

exec(input())