#include <stdio.h>

int main() {

    char input[1000], output[1000];
    FILE *input_file, *output_file;

    input_file = fopen("input.txt", "r"); 
    output_file = fopen("output.txt", "w"); 

    while (fgets(input, 100, (FILE*)input_file) != NULL) { 
        int i, j;
        for (i = 0, j = 0; input[i] != '\0'; i++) {
            if (input[i] != ' ' || (i > 0 && input[i - 1] != ' ')) {
                output[j] = input[i];
                j++;
            }
        }
        output[j] = '\0';
        fprintf(output_file, "%s\n", output); 
    }

    printf("Now check the output.txt file.\n");

    fclose(input_file); 
    fclose(output_file); 

    return 0;

}
