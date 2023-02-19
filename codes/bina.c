#include <stdio.h>
#include <stdlib.h>

// Function to convert decimal to binary
void decToBinary(int n, int binary[]) {
    int i = 0;
    while (n > 0) {
        binary[i] = n % 2;
        n = n / 2;
        i++;
    }
}

int main() {
    // Array to store 4 decimal numbers
    int decimal[4] = {226101004, 226101005, 226101001, 226101006};

    // Loop through each decimal number
    for (int i = 0; i < 4; i++) {
        int binary[8] = {0}; // Array to store binary values
        int hex[2] = {0}; // Array to store hex values

        // Convert decimal to binary
        decToBinary(decimal[i], binary);

        // Convert decimal to hex
        int quotient = decimal[i];
        for (int j = 0; quotient > 0 && j < 2; j++) {
            hex[j] = quotient % 16;
            quotient = quotient / 16;
        }

        // Output binary and hex values
        printf("Roll Number: %d, Binary: ", decimal[i]);
        for (int j = 7; j >= 0; j--) {
            printf("%d", binary[j]);
        }
        printf(", Hex: ");
        for (int j = 1; j >= 0; j--) {
            if (hex[j] >= 0 && hex[j] <= 9) {
                printf("%d", hex[j]);
            } else if (hex[j] >= 10 && hex[j] <= 15) {
                printf("%c", hex[j] + 55);
            }
        }
        printf("\n");

        // Perform binary calculations by each bit
        if (sizeof(decimal[i]) == 1) { // Only perform for 8-bit values
            int bit32[32] = {0}; // Array to store 32-bit binary value
            int binary8[8] = {0}; // Array to store 8-bit binary value

            // Convert decimal to binary8
            decToBinary(decimal[i], binary8);

            // Extend binary8 to binary32
            for (int j = 0; j < 32; j++) {
                if (j < 8) {
                    bit32[j] = binary8[j];
                } else {
                    bit32[j] = bit32[j-8];
                }
            }

            // Output binary32 value
            printf("Roll Number: %d, Binary32: ", decimal[i]);
            for (int j = 31; j >= 0; j--) {
                printf("%d", bit32[j]);
            }
            printf("\n");
        }
    }

    return 0;
}

