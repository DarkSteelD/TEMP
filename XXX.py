import pydicom
import os

# Путь к вашей директории с DICOM файлами
dicom_dir = "C:\\CTAG-2"

# Проходим по всем файлам в директории
for root, dirs, files in os.walk(dicom_dir):
    for file_name in files:
        file_path = os.path.join(root, file_name)
        try:
            # Загружаем DICOM файл
            ds = pydicom.dcmread(file_path)
            # Проверяем, содержит ли файл пиксельные данные
            if 'PixelData' in ds:
                print(f"Файл содержит изображение: {file_path}")
            else:
                print(f"В файле отсутствуют пиксельные данные: {file_path}")
        except Exception as e:
            print(f"Ошибка при чтении файла {file_path}: {e}")
