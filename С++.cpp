#include <iostream>
#include <vector>
using namespace std;

int count_bits(unsigned long long x) {
    int count = 0;
    while (x) {
        count += x & 1;
        x >>= 1;
    }
    return count;
}

int main() {
    int N, M;
    cin >> N >> M;

    vector<vector<unsigned long long>> adjacency_bitmasks(N + 1, vector<unsigned long long>((N + 63) / 64, 0));

    for (int i = 0; i < M; ++i) {
        int a, b;
        cin >> a >> b;
        adjacency_bitmasks[a][b / 64] |= 1ULL << (b % 64);
        adjacency_bitmasks[b][a / 64] |= 1ULL << (a % 64);
    }

    vector<vector<int>> common_neighbors(N + 1, vector<int>(N + 1, 0));
    for (int i = 1; i <= N; ++i) {
        for (int j = i + 1; j <= N; ++j) {
            int total_common = 0;
            for (size_t k = 0; k < (N + 63) / 64; ++k) {
                total_common += count_bits(adjacency_bitmasks[i][k] & adjacency_bitmasks[j][k]);
            }
            common_neighbors[i][j] = common_neighbors[j][i] = total_common;
        }
    }

    long long count = 0;
    for (int i = 1; i <= N; ++i) {
        for (int j = i + 1; j <= N; ++j) {
            if (common_neighbors[i][j] > 1) {
                count += common_neighbors[i][j] * (common_neighbors[i][j] - 1) / 2;
            }
        }
    }

    cout << count / 2 << endl;

    return 0;
}
