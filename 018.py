def max_path_sum(triangle):

    for row in range(len(triangle) - 2, -1, -1):
        for col in range(len(triangle[row])):
            triangle[row][col] += max(triangle[row + 1][col],
                                      triangle[row + 1][col + 1])

    return triangle[0][0]

triangle = [
    [3],
    [7, 4],
    [2, 4, 6],
    [8, 5, 9, 3]
]

result = max_path_sum(triangle)
print(result)