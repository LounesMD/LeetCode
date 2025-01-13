int minimumLength(char* s) {
    int arr[26] = {0};

    while(*s != '\0'){
        arr[*s - 'a'] ++;
        s++;
    }

    int res =0;
    for(int i=0; i<26; i++){
        if (arr[i] == 0){
            continue;
        }
        else if (arr[i] % 2 == 0){
            res += 2;
        }
        else{
            res += 1;
        }        
    }
    return res;
}