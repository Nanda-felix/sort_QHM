import random
import time
import heapq
from memory_profiler import memory_usage

# Função para gerar conjuntos de números aleatórios
def generate_random_numbers(size, seed):
    random.seed(seed)
    return [random.randint(0, 1000000) for _ in range(size)]

# Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Heap Sort
def heap_sort(arr):
    heapq.heapify(arr)
    return [heapq.heappop(arr) for _ in range(len(arr))]

# Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Função para medir o tempo de execução e o uso de memória
def measure_performance(sort_function, arr):
    # Medir o tempo de execução
    start_time = time.time()
    sort_function(arr.copy())  # Executa a ordenação
    end_time = time.time()
    time_taken = (end_time - start_time) * 1000  # Convertendo para milissegundos

    # Medir o uso de memória
    mem_usage = memory_usage((sort_function, (arr.copy(),)), max_usage=True)

    return time_taken, mem_usage  # Retorna tempo e pico de memória (já é um float)

# Tamanhos de entrada
sizes = [10000, 50000, 100000]
seed = 42

# Gerar conjuntos de números aleatórios
random_sets = {size: generate_random_numbers(size, seed) for size in sizes}

# Algoritmos de ordenação
algorithms = {
    "Quick Sort": quick_sort,
    "Heap Sort": heap_sort,
    "Merge Sort": merge_sort
}

# Medir o tempo de execução e o uso de memória
if __name__ == '__main__':
    for size in sizes:
        print(f"Tamanho da entrada: {size}")
        for algo_name, algo_func in algorithms.items():
            time_taken, mem_used = measure_performance(algo_func, random_sets[size])
            print(f"{algo_name}:")
            print(f"  Tempo de execução: {time_taken:.2f} ms")
            print(f"  Uso de memória: {mem_used:.2f} MiB")
        print()