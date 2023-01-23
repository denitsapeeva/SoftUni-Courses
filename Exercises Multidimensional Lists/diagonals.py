rows = int(input())

primary_diagonal = []
secondary_diagonal = []
matrix = [[int(x) for x in input().split(", ")] for _ in range(rows)]
for r in range(rows):
    primary_diagonal.append(matrix[r][r])
for r in range(rows-1,-1,-1):
    secondary_diagonal.append(matrix[r][rows-r-1])

print(f"Primary diagonal: {', '.join(str(x) for x in primary_diagonal)}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join(str(x) for x in secondary_diagonal[::-1])}. Sum: {sum(secondary_diagonal)}")

