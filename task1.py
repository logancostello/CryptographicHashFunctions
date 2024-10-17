import hashlib

# Task 1a:
def sha256_hash(string, numBits):
    # str to bytes
    encoded_string = string.encode('utf-8')

    sha256 = hashlib.sha256(encoded_string)

    # string -> int
    hashed = sha256.hexdigest()
    print(hashed)
    hashed = int(hashed, 16)

    # get only the last numBits bits
    mask = pow(2, numBits) - 1
    hashed &= mask

    # int -> hex
    hashed = hex(hashed)

    print(hashed)


if __name__ == '__main__':
    a = "aaa"
    b = "aab"
    numBits = 8
    sha256_hash(a, numBits)
    sha256_hash(b, numBits)
