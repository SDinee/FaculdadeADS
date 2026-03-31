#include <stdio.h>

int main(void){
    int vet[10];

    for(int i = 0; i < 10; i++){
        printf("Digite o %dº elemento\n", i + 1);
        scanf("%d", &vet[i]);
    }
    
    for(int i = 0; i < 10; i++){
        printf("%d\t ", vet[i]);
    }

    return 0;
}