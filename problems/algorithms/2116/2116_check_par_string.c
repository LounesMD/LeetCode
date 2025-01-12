#include <stdbool.h>

bool canBeValid(char* s, char* locked) {
    int left = 0;
    int v = 0;
    int size = 0;

    for (int i = 0; s[i] != '\0'; i++) {
        size ++;
        if (locked[i] == '0') {
            v++;
        } else if (s[i] == '(') {
            left++;
        } else if (s[i] == ')') {
            if (left > 0) {
                left--;
            } else if (v > 0) {
                v--;
            } else {
                return false;
            }
        }
    }

    if (size % 2 == 1) {
        return false;
    }
    
    int res = 0;
    for (int i = size - 1; i >= 0; i--) {
        if (locked[i] == '0') {
            res--;
            v--;
        } else if (s[i] == '(') {
            res++;
            left--;
        } else if (s[i] == ')') {
            res--; 
        }
        if (res > 0) {
            return false;
        }
        if (left <= 0 && res == 0) {
            break;
        }
    }
    return left <= 0;
}