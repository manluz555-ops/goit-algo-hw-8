import heapq

def min_cost_to_connect_cables(cables):
    heapq.heapify(cables)  # перетворюємо список у мін-heap
    total_cost = 0

    while len(cables) > 1:
        # беремо два найкоротші кабелі
        a = heapq.heappop(cables)
        b = heapq.heappop(cables)

        cost = a + b
        total_cost += cost

        # повертаємо об’єднаний кабель назад
        heapq.heappush(cables, cost)

    return total_cost



cables = [4, 3, 2, 6]
print("Мінімальні витрати:", min_cost_to_connect_cables(cables))
