#!/usr/bin/python3
"""12-pascal_triangle.py
Defines a Pascal's Triangle function.
"""


def pascal_triangle(n):
    """Represent Pascal's Triangle of size n.
    - Returns: a list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    trian = [[1]]
    while len(trian) != n:
        tri = trian[-1]
        temp = [1]
        for i in range(len(tri) - 1):
            temp.append(tri[i] + tri[i + 1])
        temp.append(1)
        trian.append(temp)
    return trian
