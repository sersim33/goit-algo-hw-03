import os
import sys
import shutil

def copy_and_sort(source_dir, dest_dir):
    # Перевірка існування вихідної директорії
    if not os.path.exists(source_dir):
        print(f"Директорія '{source_dir}' не існує.")
        return

    # Перевірка існування директорії призначення, або створення нової
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # Отримання списку файлів та піддиректорій в вихідній директорії
    contents = os.listdir(source_dir)

    for item in contents:
        item_path = os.path.join(source_dir, item)
        # Якщо це файл, копіюємо його
        if os.path.isfile(item_path):
            # Отримуємо розширення файлу
            extension = os.path.splitext(item)[1].strip('.')
            # Створюємо директорію з назвою розширення, якщо вона ще не існує
            extension_dir = os.path.join(dest_dir, extension)
            if not os.path.exists(extension_dir):
                os.makedirs(extension_dir)
            # Копіюємо файл у відповідну директорію
            shutil.copy(item_path, extension_dir)
            print(f"Скопійовано файл '{item}' до '{extension_dir}'.")
        # Якщо це директорія, викликаємо функцію рекурсивно
        elif os.path.isdir(item_path):
            # Функція викликає саму себе для обробки піддиректорії
            copy_and_sort(item_path, dest_dir)

if __name__ == "__main__":
    # Отримання аргументів командного рядка
    if len(sys.argv) < 3:
        print("Потрібно вказати шлях до вихідної директорії та (за необхідності) шлях до директорії призначення.")
        sys.exit(1)

    source_directory = sys.argv[1]
    destination_directory = sys.argv[2] if len(sys.argv) > 2 else "dist"

    copy_and_sort(source_directory, destination_directory)