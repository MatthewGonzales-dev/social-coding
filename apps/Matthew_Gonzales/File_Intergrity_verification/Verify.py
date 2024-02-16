

import hashlib

def sha256sum(filename):
    with open(filename, 'rb', buffering=0) as f:
        return hashlib.file_digest(f, 'sha256').hexdigest()

sha256sum("UTA.png")
print(sha256sum)
