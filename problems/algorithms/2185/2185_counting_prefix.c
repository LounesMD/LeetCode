int prefixCount(char** words, int wordsSize, char* pref) {
    int cpt = 0;
    for(int i=0;i<wordsSize; i++){
        if (strncmp(pref, words[i], strlen(pref)) == 0){
            cpt ++;
        }
    }
    return cpt;
}