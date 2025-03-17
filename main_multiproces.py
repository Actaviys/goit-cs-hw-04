import multiprocessing
import time
from searching_keyword_in_text_files import func_search_coincid_words_with_count


# \\...\\HomeWork\\cs-hw-04\\Files1

# Параметри для двох процесів
folder_1 = "\\...\\HomeWork\\cs-hw-04\\Files1" # Шлях до папки з файлами .txt
folder_2 = "\\...\\HomeWork\\cs-hw-04\\Files2" # Шлях до папки з файлами .txt

keywords_1 = ["windows", "python"]  # Ключові слова для першого процесу
keywords_2 = ["програми", "цифра"]  # Ключові слова для другого процесу



# Функція для запуску пошуку
def run_search(folder, keywords, result_queue, process_name, execution_times):
    start_time = time.time()
    print(f"{process_name} -> Читає папку: '{folder}'...")

    # Виконання пошуку
    result = func_search_coincid_words_with_count(folder, keywords)

    end_time = time.time()
    execution_times[process_name] = end_time - start_time

    print(f"{process_name} -> завершив за {execution_times[process_name]:.2f} сек.")

    # Додаємо результат у чергу
    result_queue.put((process_name, result))




def main():
    result_queue = multiprocessing.Queue()  # Черга для отримання результатів
    execution_times = multiprocessing.Manager().dict()  # Час виконання кожного процесу
    processes = []

    start_time = time.time()  # Загальний старт

    # Створюємо процеси для пошуку в різних папках
    process1 = multiprocessing.Process(target=run_search, args=(folder_1, keywords_1, result_queue, "Process-1", execution_times))
    process2 = multiprocessing.Process(target=run_search, args=(folder_2, keywords_2, result_queue, "Process-2", execution_times))

    processes.extend([process1, process2])

    # Запускаємо процеси
    for process in processes:
        process.start()

    # Очікуємо завершення процесів
    for process in processes:
        process.join()

    end_time = time.time()  # Загальний час виконання

    # Отримуємо результати з черги
    results = {}
    while not result_queue.empty():
        process_name, result = result_queue.get()
        results[process_name] = result

    # Вивід результатів пошуку
    for process_name, result in results.items():
        print(f"\nРезультат потоку: {process_name}: \n{result}")

    # Вивід часу виконання кожного процесу
    print("\nЧас виконання:")
    for process_name, exec_time in execution_times.items():
        print(f"{process_name}: {exec_time:.2f} сек.")

    print(f"\nЗагальний час виконання: {end_time - start_time:.2f} сек.")

if __name__ == "__main__":
    main()