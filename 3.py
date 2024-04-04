def read_and_structure_input(W, H, D):
    V = [[[int(x) for x in input().split()] for _ in range(H)] for _ in range(W)]

    # Инициализация сумм
    sums_w = [[0 for _ in range(D)] for _ in range(H)]  # Суммы по ширине для каждой глубины и высоты
    sums_h = [[0 for _ in range(D)] for _ in range(W)]  # Суммы по высоте для каждой глубины и ширины
    sums_d = [[0 for _ in range(H)] for _ in range(W)]  # Суммы по глубине для каждой ширины и высоты

    # Считывание данных и накопление сумм
    for w in range(W):
        for h in range(H):
            for d in range(D):
                V[w][h][d] = int(input())
                sums_w[h][d] += V[w][h][d]
                sums_h[w][d] += V[w][h][d]
                sums_d[w][h] += V[w][h][d]
    
    return V, W, H, D, sums_w, sums_h, sums_d

def calculate_losses(W, H, D, sums_w, sums_h, sums_d):
    min_loss = float('inf')
    coords_with_min_loss = []

    for w in range(W):
        for h in range(H):
            for d in range(D):
                loss_wh = sums_w[h][d] + sums_h[w][d] - V[w][h][d]
                loss_wd = sums_w[h][d] + sums_d[w][h] - V[w][h][d]
                loss_hd = sums_h[w][d] + sums_d[w][h] - V[w][h][d]
                current_loss = min(loss_wh, loss_wd, loss_hd)

                if current_loss < min_loss:
                    min_loss = current_loss
                    coords_with_min_loss = [(w, h, d)]
                elif current_loss == min_loss:
                    coords_with_min_loss.append((w, h, d))

    return min_loss, sorted(set(coords_with_min_loss))

# Главная программа
W, H, D = map(int, input().split())
V, sums_w, sums_h, sums_d = read_and_structure_input(W, H, D)
min_loss, sorted_unique_coords = calculate_losses(W, H, D, sums_w, sums_h, sums_d)

print(min_loss)
for coord in sorted_unique_coords:
    print(' '.join(map(str, coord)))
