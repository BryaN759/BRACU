#include <stdio.h>
#include <ctype.h>

int main()
{
    char password[50];

    printf("Enter a password: ");
    fgets(password, 50, stdin);

    int has_lower = 0, has_upper = 0, has_digit = 0, has_special = 0;

    for(int i = 0; password[i] != '\0'; i++)
    {
        if(islower(password[i]))
        {
            has_lower = 1;
        }
        else if(isupper(password[i]))
        {
            has_upper = 1;
        }
        else if(isdigit(password[i]))
        {
            has_digit = 1;
        }
        else if(password[i]=='_' || password[i]=='$' || password[i]=='#' || password[i]=='@' )
        {
            has_special = 1;
        }
        
    }

    if(has_lower && has_upper && has_digit && has_special)
    {
        printf("OK.\n");
    }
    else
    {
        if (has_lower == 0)
        printf("Lowercase Character missing\n");
        
        if (has_upper == 0)
        printf("Uppercase Character missing\n");
        
        if (has_digit == 0)
        printf("Digit missing\n");
        
        if (has_special == 0)
        printf("Special Character missing\n");
    }

    return 0;
}
