#include <stdio.h>

int main() {
    int decimal[4];
    int i, j;

    // Get decimal numbers from user input
    printf("Enter 4 Roll numbers:\n");
    for (i = 0; i < 4; i++) {
        scanf("%d", &decimal[i]);
    }

    // Output binary and hexadecimal for each decimal number
    for (i = 0; i < 4; i++) {
        printf("\nRoll Number %d:\n", decimal[i]);

        // Output binary number
        printf("Binary: ");
        for (j = 31; j >= 0; j--) {
            printf("%d", (decimal[i] >> j) & 1);
        }
        printf("\n");

        // Output hexadecimal number
        printf("Hexadecimal: 0x%X\n", decimal[i]);
    }

    return 0;
}

