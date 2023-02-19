from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

def des_encryption(plaintext, key):
    cipher = DES.new(key, DES.MODE_ECB)
    num_rounds = 16
    
    # Convert the plaintext and key from binary strings to bytes
    plaintext_bytes = bytes.fromhex(hex(int(plaintext, 2))[2:])
    key_bytes = bytes.fromhex(hex(int(key, 2))[2:])
    
    # Pad the plaintext to a multiple of 8 bytes
    padded_plaintext_bytes = pad(plaintext_bytes, 8)
    
    # Perform the initial permutation
    permuted_plaintext_bytes = perform_initial_permutation(padded_plaintext_bytes)
    
    # Split the permuted plaintext into two 32-bit halves
    L = permuted_plaintext_bytes[:4]
    R = permuted_plaintext_bytes[4:]
    
    # Convert the key bytes into a list of 16 subkeys, one for each round
    subkeys = generate_subkeys(key_bytes)
    
    # Perform the 16 rounds of encryption
    for i in range(num_rounds):
        # Compute the new L and R values for this round
        new_L, new_R = compute_round(L, R, subkeys[i])
        
        # Output the result for this round
        print("Round {}: {}".format(i+1, new_R.hex().upper()))
        
        # Update L and R for the next round
        L = new_L
        R = new_R
    
    # Concatenate the final L and R values and perform the final permutation
    final_block = R + L
    final_permutation_block = perform_final_permutation(final_block)
    
    # Convert the encrypted bytes to a binary string
    encrypted_hex = final_permutation_block.hex().upper()
    encrypted_binary = bin(int(encrypted_hex, 16))[2:].zfill(64)
    
    return encrypted_binary

def perform_initial_permutation(block):
    permutation_table = [
        58, 50, 42, 34, 26, 18, 10, 2,
        60, 52, 44, 36, 28, 20, 12, 4,
        62, 54, 46, 38, 30, 22, 14, 6,
        64, 56, 48, 40, 32, 24, 16, 8,
        57, 49, 41, 33, 25, 17, 9, 1,
        59, 51, 43, 35, 27, 19, 11, 3,
        61, 53, 45, 37, 29, 21, 13, 5,
        63, 55, 47, 39, 31, 23, 15, 7
    ]
    permuted_block = b''
    for i in permutation_table:
        permuted_block += block[i-1:i]
    return permuted_block

def perform_final_permutation(block):
    permutation_table = [
        40, 8, 48, 16, 56, 24, 64, 32,
        39, 7, 47, 15, 55, 23, 63, 31,
        38, 6, 46, 14, 54, 22, 62, 30,
        37, 5, 45, 13, 53, 21, 61, 29,
        36, 4, 44, 12, 52, 20, 60, 28,
        35, 3, 43, 11, 51, 19, 59, 27,
        34, 2, 42, 10, 50, 18, 58, 26,
        33, 1, 41, 9, 49, 17, 57, 25
    ]
    permuted_block = b''
    for i in permutation_table:
        permuted_block += block[i-1:i]
    return permuted_block

def generate_subkeys(key_bytes):
    subkeys = []
    pc1_table = [
        57, 49, 41, 33, 25, 17, 9,
        1, 58, 50, 42, 34, 26, 18,
        10, 2, 59, 51, 43, 35, 27,
        19, 11, 3, 60, 52, 44, 36,
        63, 55, 47, 39, 31, 23, 15,
        7, 62, 54, 46, 38, 30, 22,
        14, 6, 61, 53, 45, 37, 29,
        21, 13, 5, 28, 20, 12, 4
    ]
    pc2_table = [
        14, 17, 11, 24, 1, 5, 3, 28,
        15, 6, 21, 10, 23, 19, 12, 4,
        26, 8, 16, 7, 27, 20, 13, 2,
        41, 52, 31, 37, 47, 55, 30, 40,
        51, 45, 33, 48, 44, 49, 39, 56,
        34, 53, 46, 42, 50, 36, 29, 32
    ]
    # Apply the first permutation to the key
    permuted_key = perform_key_permutation(key_bytes, pc1_table)
    
    # Split the permuted key into two 28-bit halves
    C = permuted_key[:28]
    D = permuted_key[28:]
    
    # Generate 16 subkeys, one for each round
    for i in range(16):
        # Compute the new C and D values for this round
        C, D = compute_subkey(C, D, i+1)
        
        # Combine C and D and apply the second permutation
        CD = C + D
        subkey = perform_key_permutation(CD, pc2_table)
        subkeys.append(subkey)
    
    return subkeys

def main():
    # Example plaintext and key
    plaintext = b'1010101111001101100110101011001010110011101010110010110110101110'
    key = b'1010000011001010100011101110111010001110110000111001111000110001'

    # Generate the subkeys
    subkeys = generate_subkeys(key)

    # Perform the initial permutation on the plaintext
    permuted_block = perform_initial_permutation(plaintext)

    # Split the permuted block into two 32-bit halves
    L = permuted_block[:32]
    R = permuted_block[32:]

    # Perform 16 rounds of encryption
    for i in range(16):
        L, R = perform_round(L, R, subkeys[i])
        print(f"Round {i+1}: L = {L.hex()}, R = {R.hex()}")

    # Combine L and R and perform the final permutation
    LR = L + R
    ciphertext = perform_final_permutation(LR)
    print(f"Ciphertext: {ciphertext.hex()}")

if __name__ == '__main__':
    main()

