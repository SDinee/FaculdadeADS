#include <stdio.h>

int main(){
    int l, c;

    printf("Digite o número de linhas:\n");
    scanf("%d", &l);

    printf("Digite o número de colunas:\n");
    scanf("%d", &c);

    int matriz[l][c];
    int soma = 0;

    printf("Digite os elementos da matriz:\n");
    for(int i = 0; i < l; i++){
        for(int j = 0; j < c; j++){
            printf("Elemento [%d][%d]: ", i + 1, j + 1);
            scanf("%d", &matriz[i][j]);
            soma += matriz[i][j];
        }
    }
    printf("Matriz:\n");
    for(int i = 0; i < l; i++){
        for(int j = 0; j < c; j++){
            printf("\t%d ", matriz[i][j]);
        }
        printf("\n");
    }
    printf("Soma dos elementos: %d\n", soma);

    int qtdpar, qtdimpar;
    qtdpar = qtdimpar = 0;
    for(int i = 0; i < l; i++){
        for(int j = 0; j < c; j++){
            if(matriz[i][j] % 2 == 0){
                qtdpar++;
            } else {
                qtdimpar++;
            }
        }
    }
    printf("Quantidade de elementos pares: %d\n", qtdpar);
    printf("Quantidade de elementos ímpares: %d\n", qtdimpar);

    return 0;
}