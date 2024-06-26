from random import randint

# Encrypt:
def encrypt(input: str):
    try:
        key = ''.join(chr(randint(33, 126)) for _ in range(len(input)))
        matrix = [[int(bit) for bit in f"{bin(ord(chr))[2:]:0>8}"] for chr in [*input]]
        key_matrix = [[int(bit) for bit in f"{bin(ord(chr))[2:]:0>8}"] for chr in [*key]]
        output = ''.join([chr(int(''.join(map(str, row)), 2)) for row in [[matrix[i][j] ^ key_matrix[i][j] for j in range(len(matrix[0]))] for i in range(len(matrix))]])
        return output, key
    except Exception as e:
        return False

# Decrypt:
def decrypt(input: str, key: str):
    try:
        matrix = [[int(bit) for bit in f"{bin(ord(chr))[2:]:0>8}"] for chr in [*input]]
        key_matrix = [[int(bit) for bit in f"{bin(ord(chr))[2:]:0>8}"] for chr in [*key]]
        output = ''.join([chr(int(''.join(map(str, row)), 2)) for row in [[matrix[i][j] ^ key_matrix[i][j] for j in range(len(matrix[0]))] for i in range(len(matrix))]])
        return output
    except Exception as e:
        return False