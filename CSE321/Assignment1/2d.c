
#include <stdio.h>
#include <string.h>

int isEmailUpdated(const char* email) {
    const char* updatedDomain = "@sheba.xyz";
    const size_t updatedDomainLen = strlen(updatedDomain);
    const size_t emailLen = strlen(email);
    
    // Check if the email address is long enough to contain the updated domain
    if (emailLen < updatedDomainLen) {
        return 0;
    }
    
    // Check if the email address ends with the updated domain
    const char* domainStart = email + emailLen - updatedDomainLen;
    if (strcmp(domainStart, updatedDomain) != 0) {
        return 0;
    }
    
    return 1;
}

int main() {
    char str[100];
    
    printf("Enter Email: ");
    fgets(str, sizeof(str), stdin); 
    
    if (isEmailUpdated(str)) {
        printf("%s Email is updated\n", str);
    } else {
        printf("%s Email is not updated\n", str);
    }
    
    
    return 0;
}
