from Crypto.Cipher import AES
from Crypto import Random
from hashlib import sha256


def pad_bytes(b, block_size=16):
    diff_to_full_block = block_size - len(b) % block_size
    return b + bytes([diff_to_full_block] * diff_to_full_block)


def unpad_bytes(b):
    diff_to_full_block = b[-1]
    return b[:-diff_to_full_block]


def aes(key, data, encrypt=True, extend_key=True):
    if extend_key:
        key = sha256(key).digest()

    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CFB, iv)

    if encrypt:
        return iv + cipher.encrypt(pad_bytes(data))
    return unpad_bytes(cipher.decrypt(data)[AES.block_size:])
