import random
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
password = ""
for i in range(10):
    password = password + random.choice(characters)
print("Generated Password:", password)