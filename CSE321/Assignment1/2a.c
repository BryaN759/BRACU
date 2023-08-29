#include <stdio.h>

void subtraction(int n1, int n2) {
    int res = n1 - n2;
    printf("%d - %d = %d\n", n1, n2, res);
}

void addition(int n1, int n2) {
    int res = n1 + n2;
    printf("%d + %d = %d\n", n1, n2, res);
}

void multiplication(int n1, int n2) {
    int res = n1 * n2;
    printf("%d * %d = %d\n", n1, n2, res);
}

int main() {
    int n1, n2;
    char op;
    printf("Enter two numbers: ");
    scanf("%d %d", &n1, &n2);
    printf("Enter an operator : ");
    scanf(" %c", &op);

    if (n1 > n2) {
        if (op == '-') {
        subtraction(n1, n2);
        } else {
        printf("Only substraction possible when number 1 > number 2\n");
        }
    } else if (n1 < n2) {
        if (op == '+') {
        addition(n1, n2);
        } else {
        printf("Only addition possible when number 1 < number 2\n");
        }
    } else if (n1 == n2) {
        if (op == '*') {
        multiplication(n1, n2);
        } else {
        printf("Only multiplication possible when number 1 = number 2\n");
        }
    }

    return 0;
}
