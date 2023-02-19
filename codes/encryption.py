from Crypto.Cipher import DES

def des_encryption(plaintext, key):
    # Convert the binary plaintext and key into bytes
    plaintext = bytes.fromhex(plaintext)
    key = bytes.fromhex(key)

    # Create a DES object with the key
    des = DES.new(key, DES.MODE_ECB)

    # Encrypt the plaintext
    ciphertext = plaintext
    for i in range(16):
        # Divide the plaintext into two halves
        left = ciphertext[:4]
        right = ciphertext[4:]

        # Perform the DES round operation
        new_right = bytes([left[j] ^ des.encrypt(right)[j] for j in range(4)])
        new_left = right

        # Combine the two halves back into the ciphertext
        ciphertext = new_left + new_right

        # Print the ciphertext at each round
        print(f"Round {i+1}: {ciphertext.hex().upper()}")

    # Return the final ciphertext
    return ciphertext.hex().upper()

def main():
    plaintext = '000001111'
    key = '0000'
    ciphertext = des_encryption(plaintext, key)
    print("Final Ciphertext: ", ciphertext)
