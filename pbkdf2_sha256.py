import hashlib
import os
import base64
from django.utils.crypto import pbkdf2

# Example parameters
password = '1234'
iterations = 720000
salt = base64.b64encode(os.urandom(12)).decode('ascii')

# PBKDF2 hashing
hash_bytes = pbkdf2(password, salt, iterations, dklen=32, digest=hashlib.sha256)
hash_str = base64.b64encode(hash_bytes).decode('ascii')

# Format the final password hash string
final_hash = f'pbkdf2_sha256${iterations}${salt}${hash_str}'
print(final_hash)
