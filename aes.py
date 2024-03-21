import base64

encrypted_text_base64 = "6Gk9of3j0CyeRet8g7zUWV9RVaFOeW0KT0tF0Xs0rQc="  # Пример зашифрованного текста в формате base64
encrypted_bytes = base64.b64decode(encrypted_text_base64)
encrypted_length = len(encrypted_bytes)
print("Длина зашифрованного текста в байтах:", encrypted_length)
