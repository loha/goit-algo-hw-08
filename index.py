import heapq

def min_cost_to_connect_cables(lengths):
    # Створюємо мін-купу з довжин кабелів
    heapq.heapify(lengths)
    
    total_cost = 0
    
    # Поки в купі більше одного елемента
    while len(lengths) > 1:
        # Витягуємо два найменші елементи з купи
        first_min = heapq.heappop(lengths)
        second_min = heapq.heappop(lengths)
        
        # Обчислюємо витрати на з'єднання двох кабелів
        cost = first_min + second_min
        total_cost += cost
        
        # Додаємо новий кабель назад до купи
        heapq.heappush(lengths, cost)
    
    return total_cost

cable_lengths = [8, 4, 6, 12]
min_cost = min_cost_to_connect_cables(cable_lengths)
print("Мінімальні витрати на з'єднання кабелів:", min_cost)
