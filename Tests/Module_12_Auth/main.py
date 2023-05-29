from jose import jwt, JWTError

# дані для заповнення токена
payload = {"sub": "andriy.martynyuk.if@gmail.com", "name": "Andriy", "role": "administrator"}

# створення токена з симетричним ключем
encoded = jwt.encode(payload, "secret_key", algorithm='HS256')
print(encoded)

# перевірка токена
try:
    decoded = jwt.decode(encoded, "secret_key", algorithms=['HS256'])
    print(decoded)
except JWTError as e:
    print(e)