#include <stdio.h>

void mostrartab(int num){
    for( int i = 1; i <= 10; i++){
        printf("%d x %d = %d\n", num, i, num * i);
    }
}

int main(){
    int num;
    printf("digite um número: ");
    scanf("%d", &num);

    mostrartab(num);
    return 0;
}