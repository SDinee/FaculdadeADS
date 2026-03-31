#include <stdio.h>
#include <string.h>

int main(){
    char nome[5][30];
    int idade[5];
    for(int i = 0; i < 5; i++){
        printf("Digite o nome da %d pessoa:\n", i + 1);
        fgets(nome[i], 30, stdin);

        printf("Digite a idade da %d pessoa:\n", i + 1);
        scanf("%d", &idade[i]);
        getchar(); // Limpa o buffer do teclado para evitar problemas com fgets na próxima iteração

    }
    for(int i = 0; i < 5; i++){
        printf("Nome: %sIdade: %d\n", nome[i], idade[i]);
    }
    return 0;
}