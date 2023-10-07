from cryptography.fernet import Fernet

# Generate key for AES encryption
key = Fernet.generate_key()
cipher_suite = Fernet(key)

def encrypt_data(data):
    encrypted_data = []

    for entry in data:
        encrypted_entry = {k: cipher_suite.encrypt(str(v).encode()) for k, v in entry.items()}
        encrypted_data.append(encrypted_entry)

    return encrypted_data
