import threading
import time
from searching_keyword_in_text_files import func_search_coincid_words_with_count


# Параметри для двох потоків
folder_1 = "\\...\\HomeWork\\cs-hw-04\\Files1" # Шлях до папки з файлами .txt
folder_2 = "\\...\\HomeWork\\cs-hw-04\\Files2" # Шлях до папки з файлами .txt

keywords_1 = ["windows", "python"]  # Ключові слова для першого потоку
keywords_2 = ["програми", "цифра"]  # Ключові слова для другого потоку


# Функція для запуску пошуку в окремому потоці
def run_search(folder, keywords, results, thread_name, execution_times):
    start_time = time.time()
    print(f"{thread_name} -> Читає папку: '{folder}'...")

    # Запускаємо пошук і зберігаємо результат
    results[thread_name] = func_search_coincid_words_with_count(folder, keywords)

    end_time = time.time()
    execution_times[thread_name] = end_time - start_time

    print(f"{thread_name} -> завершив за: {execution_times[thread_name]:.2f} сек.")




def main():
    results = {}  # Для збереження результатів пошуку
    execution_times = {}  # Для збереження часу виконання
    threads = [] # Список для потоків
    start_time = time.time()  # Загальний старт
    
    # # Створюємо потоки для пошуку в різних папках
    thread1 = threading.Thread(target=run_search, args=(folder_1, keywords_1, results, "Thread-1", execution_times))
    thread2 = threading.Thread(target=run_search, args=(folder_2, keywords_2, results, "Thread-2", execution_times))

    threads.extend([thread1, thread2])

    # # Запускаємо потоки
    for thread in threads:
        thread.start()

    # # Очікуємо завершення потоків
    for thread in threads:
        thread.join()

    end_time = time.time()  # Загальний час виконання

    # # Вивід результатів пошуку
    for thread_name, result in results.items():
        print(f"\nРезультат потоку: {thread_name}: \n{result}")

    # Вивід часу виконання кожного потоку
    print("\nЧас виконання:")
    for thread_name, exec_time in execution_times.items():
        print(f"{thread_name}: {exec_time:.2f} сек.")

    print(f"\nЗагальний час виконання: {end_time - start_time:.2f} сек.")



if __name__ == "__main__":
    main()