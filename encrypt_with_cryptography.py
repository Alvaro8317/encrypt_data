import base64
from cryptography.fernet import Fernet

# Cadena Base64 que deseas decodificar
encoded_str = 'SG9sYSwgZXN0ZSBlcyB1biBlamVtcGxvIGRlIGNvZGlmaWNhY2nDs24geSBlbmNyaXB0YWNpw7Nu'

# Decodifica la cadena Base64 en datos binarios
decoded_data = base64.b64decode(encoded_str)
print(f'Esta es la información decofidicada: {decoded_data}')
# Clave de cifrado generada aleatoriamente
encryption_key = Fernet.generate_key()
print(f'Esta es la llave: {encryption_key}')
# Inicializa un objeto Fernet con la clave
fernet = Fernet(encryption_key)
print(f'Esta es la instancia: {fernet}')
# Cifra los datos binarios
encrypted_data = fernet.encrypt(decoded_data)
print(f'Esta es la información encriptada: {encrypted_data} \n y esta es la descifrada: {decoded_data}')

# Puedes almacenar la clave de cifrado de manera segura para futuras operaciones de descifrado
print("Clave de cifrado:", encryption_key)

# Para descifrar los datos en el futuro, utilizarás la misma clave
# Decodificar los datos
decrypted_data = fernet.decrypt(encrypted_data)
print("Datos decodificados:", encryption_key)
# Convierte los datos descifrados en una cadena de texto
decrypted_str = decrypted_data.decode('utf-8')

print("Datos descifrados:", decrypted_str)
