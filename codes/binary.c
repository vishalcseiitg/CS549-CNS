#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Function to convert binary to hexadecimal
char* binaryToHex(char* binary) {
    int decimal = strtol(binary, NULL, 2);
    char* hex = malloc(sizeof(char) * 3);
    sprintf(hex, "%X", decimal);
    return hex;
}

int main() {
    char binary[4][8];
    char* hex[4];

    // Input binary values
    for (int i = 0; i < 4; i++) {
        printf("Enter Roll number %d: ", i+1);
        scanf("%s", binary[i]);
    }

    // Convert binary to hexadecimal
    for (int i = 0; i < 4; i++) {
        hex[i] = binaryToHex(binary[i]);
    }

    // Output hexadecimal values
    for (int i = 0; i < 4; i++) {
        printf("Binary value %d: %s\n", i+1, binary[i]);
        printf("Hexadecimal value %d: %s\n", i+1, hex[i]);
    }

    return 0;
}

