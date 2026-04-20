import uuid

from werkzeug.security import generate_password_hash, check_password_hash
from cryptography.fernet import Fernet


def hash_password(password, salt):
    return generate_password_hash(password + salt, method="pbkdf2:sha256")


def check_password(password_hash, password, salt):
    return check_password_hash(password_hash, password + salt)


def generate_salt():
    return uuid.uuid4().hex


def generate_key():
    return Fernet.generate_key().decode()


def encrypt_data(data, key):
    cipher = Fernet(key.encode())
    return cipher.encrypt(data.encode()).decode()


def decrypt_data(data, key):
    cipher = Fernet(key.encode())
    return cipher.decrypt(data.encode()).decode()
