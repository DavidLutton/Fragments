import hashlib


def generate_hash(filename=None):
    """Generate a hash for a file."""
    hasher_256 = hashlib.sha256()
    with open(filename, 'rb') as obj:
        hasher_256.update(obj.read())
    return hasher_256.hexdigest()


# print(generate_hash("hash.py"))
