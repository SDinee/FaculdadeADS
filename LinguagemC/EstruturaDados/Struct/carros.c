#include <stdio.h>

typedef struct {
    int id;
    char marca[30];
    char modelo[30];
    int ano;
    float tanque;
    float consumo;
} carro;

carro cadastrar(void){

    carro c;

    printf("ID: ");
    scanf("%d", &c.id);

    printf("Marca: ");
    scanf("%29s", &c.marca);

    printf("Modelo: ");
    scanf("%29s", &c.modelo);

    printf("Ano: ");
    scanf("%d", &c.ano);

    printf("Capacidade do tanque (litros): ");
    scanf("%f", &c.tanque);

    printf("Consumo (km/l): ");
    scanf("%f", &c.consumo);

    return c;
}

void imprimir(carro c){
    printf("\n-----Dados do Carro-----\n");
    printf("ID: %d\n", c.id);
    printf("Marca: %s\n", c.marca);
    printf("Modelo: %s\n", c.modelo);
    printf("Ano: %d\n", c.ano);
    printf("Capacidade do tanque: %.2f litros\n", c.tanque);
    printf("Consumo: %.2f km/l\n", c.consumo);
}

int main(void){
    int n;
    printf("Quantos carros deseja cadastrar?\n");
    scanf("%d", &n);

    carro veiculos[n];

    for(int i = 0; i < n; i++){
        printf("\nCadastro do carro %d:\n", i + 1);
        veiculos[i] = cadastrar();
    }
    printf("\n****Lista de Carros****\n");
    for(int i = 0; i < n; i++){
        imprimir(veiculos[i]);
    }
    return 0;
}