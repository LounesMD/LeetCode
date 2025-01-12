#include <stdbool.h>

bool canConstruct(char* s, int k) {
    int size = 0;
    int arr[26] = {0};

    while (*s != '\0') {
        arr[*s - 'a'] ++;
        s++;
        size ++;
    }

    if (size < k){
        return false;
    }

    int odd = 0;
    for(int i=0; i<26; i++){
        if (arr[i] % 2 == 1){
            odd ++;
        }
    }
    
    return odd <= k;
}