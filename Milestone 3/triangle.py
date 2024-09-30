
from typing import List
def get_triangle(rows: int) -> List[List[int]]:
    if rows <= 0:
        return []
    triangle = [[1]]
    for i in range(1, rows):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)
    
    return triangle

print(get_triangle(5))

triangle = get_triangle(5)
for row in triangle:
    print(row)

from typing import List

def get_triangle(rows: int) -> List[List[int]]:
    if rows <= 0:
        return []
    triangle = [[1]]
    for i in range(1, rows):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)
    
    return triangle

def print_triangle(triangle: List[List[int]]) -> None:
    max_width = len(" ".join(map(str, triangle[-1])))
    for row in triangle:
        row_str = " ".join(map(str, row))
        print(row_str.center(max_width))

if __name__ == "__main__":
    rows = 5  
    triangle = get_triangle(rows)
    print_triangle(triangle)
