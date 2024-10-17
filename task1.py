import hashlib
import time
import random
import string

# Hashes the input string, returns only numBits bits of the hashed value
def sha256_hash(inputStr, numBits):
    # str to bytes
    encoded_string = inputStr.encode('utf-8')

    sha256 = hashlib.sha256(encoded_string)

    # string -> int
    hashed = sha256.hexdigest()
    hashed = int(hashed, 16)

    # get only the last numBits bits
    mask = pow(2, numBits) - 1
    hashed &= mask

    # int -> hex
    hashed = hex(hashed)

    return hashed

# Finds two different strings that collide when hashed, given numBits bits of the hashed values
def findCollision(numBits):
    # map hashes to their strings
    hashes = {}
    numStringsTried = 0
    startTime = time.time()
    while True:
        # generate random string
        strLen = 10
        randomString = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(strLen))
        hashed_value = sha256_hash(randomString, numBits)
        numStringsTried += 1
        if hashed_value in hashes:
            if randomString != hashes[hashed_value]:
                endTime = time.time()
                totalTime = endTime - startTime
                totalTime = round(totalTime, 6)
                print(f"Solution for {numBits} bits:")
                print(f"Word 1: {randomString}")
                print(f"Word 2: {hashes[hashed_value]}")
                print(f"Collision: {hashed_value}")
                print(f"{numStringsTried} strings tried in {totalTime} seconds")
                print()
                return [randomString, hashes[hashed_value], numStringsTried, totalTime]
        else:
            hashes[hashed_value] = randomString

if __name__ == '__main__':
    findCollision(8)
    findCollision(10)
    findCollision(12)

