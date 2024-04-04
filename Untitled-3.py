def count_bits(x):
    count = 0
    while x:
        count += 1
        x &= x - 1  
    return count

def main():
    N, M = map(int, input().split())  
    adjacency_bitmasks = [[0] * ((N + 63) // 64) for _ in range(N + 1)] 
    for _ in range(M):
        a, b = map(int, input().split())
        adjacency_bitmasks[a][b // 64] |= 1 << (b % 64)
        adjacency_bitmasks[b][a // 64] |= 1 << (a % 64)
    common_neighbors = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(i + 1, N + 1): 
            total_common = 0
            for k in range((N + 63) // 64): 
                total_common += count_bits(adjacency_bitmasks[i][k] & adjacency_bitmasks[j][k])
            common_neighbors[i][j] = common_neighbors[j][i] = total_common

    count = 0
    for i in range(1, N + 1):
        for j in range(i + 1, N + 1):
            if common_neighbors[i][j] > 1:  
                count += common_neighbors[i][j] * (common_neighbors[i][j] - 1) // 2

    unique_routes = count // 2
    print(unique_routes)

if __name__ == "__main__":
    main()
