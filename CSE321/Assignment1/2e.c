#include <stdio.h>
#include <string.h>

int isPalindrome(char *str) {
    char *start = str;
    char *end = str + strlen(str) - 1;
    
    while (end > start) {
        if (*start != *end)
            return 0;
        start++;
        end--;
    }
    
    return 1;
}

int main() {
    char str[100];
    printf("Enter a string: ");
    scanf("%s", str);
    
    if (isPalindrome(str))
        printf("%s is a palindrome", str);
    else
        printf("%s is not a palindrome", str);
    
    return 0;
}
