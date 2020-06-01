"""
雅克比迭代法的矩阵表示

"""
import numpy as np
from sympy import Rational as r


def jacobi_iter_matrix(A, b):
    """
    雅克比迭代法的矩阵表示
    :param A: 系数矩阵
    :param b: 值矩阵
    :return: B, f
    """
    n = len(A)  # 方程组未知量个数
    # 初始化D、L、U:
    D = rational_zeros(A.shape)
    L = rational_zeros(A.shape)
    U = rational_zeros(A.shape)
    # 计算D、L、U:
    for i in range(n):
        D[i, i] = A[i, i]
        L[i, : i] = A[i, : i]
        U[i, i + 1:] = A[i, i + 1:]
    # 计算B、f
    D_inv = inv(D)
    B = np.dot(D_inv, L + U)
    f = np.dot(D_inv, b)
    # 打印结果并返回
    print("B:")
    print(B)
    print("f:")
    print(f)
    return B, f


def rational_zeros(shape):
    """
    生成一个shape型的零矩阵，其类型为sympy.Rational
    :param shape: 矩阵形状
    :return: Rational类型的零矩阵
    """
    all_num = 1
    for num in shape:
        all_num *= num
    return np.array([r(0) for i in range(all_num)]).reshape(shape)


def inv(M):
    """
    求一个对角矩阵的逆矩阵
    :param M: 待处理的对角矩阵
    :return: 其逆矩阵
    """
    n = len(M)
    M_inv = rational_zeros(M.shape)
    for i in range(n):
        M_inv[i, i] = 1 / M[i, i]
    return M_inv


if __name__ == '__main__':
    A = np.array([
        [r(8), r(-3), r(2)],
        [r(4), r(11), r(-1)],
        [r(6), r(3), r(12)]
    ])
    b = np.array([r(20), r(33), r(36)]).reshape((-1, 1))
    jacobi_iter_matrix(A, b)


