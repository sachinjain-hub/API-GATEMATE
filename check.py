import bcrypt
print(bcrypt.hashpw("12345".encode(), bcrypt.gensalt()).decode())