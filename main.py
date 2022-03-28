"""
Модуль для шифровки и расшифровки файла .env
"""

# pip install cryptography
from cryptography.fernet import Fernet


def write_key():
    """
    Создаем ключ и сохраняем его в файл
    :return:
    """
    key = Fernet.generate_key()
    with open('crypto.key', 'wb') as key_file:
        key_file.write(key)


def load_key():
    """
    Загружаем ключ 'crypto.key' из текущего каталога
    :return:
    """
    return open('crypto.key', 'rb').read()


def encrypt(filename, key):
    """
    Функция шифрования файла
    :param filename:
    :param key:
    :return:
    """
    # Зашифруем файл и записываем его
    f = Fernet(key)
    with open(filename, 'rb') as file:
        # прочитать все данные файла
        file_data = file.read()
        # шифруем файл
        encrypted_data = f.encrypt(file_data)
    # записать зашифрованный файл
    with open(filename, 'wb') as file:
        file.write(encrypted_data)


def decrypt(filename, key):
    """
    Функция расшифровки файла
    :param filename:
    :param key:
    :return:
    """
    # Расшифруем файл и записываем его
    f = Fernet(key)
    with open(filename, 'rb') as file:
        # читать зашифрованные данные
        encrypted_data = file.read()
    # расшифровать данные
    decrypted_data = f.decrypt(encrypted_data)
    # записать оригинальный файл
    with open(filename, 'wb') as file:
        file.write(decrypted_data)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # write_key() эта функция нужна для создания ключевого файла, она должна быть закомментирована при расшифровке
    # загрузить ключ
    key = load_key()
    # имя шифруемого файла
    file = '.env'
    # зашифровать файл
    # encrypt(file, key)
    # расшифровать файл
    decrypt(file, key)
