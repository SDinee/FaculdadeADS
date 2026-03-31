#include <stdio.h>

float calcularIMC(float peso, float altura) {
    return peso / (altura * altura);
}

float calcularPorcentagem(int valor, int total){
    return (valor * 100.0) / total;
}

int main(){
    int qtd;
    float peso,altura, imc;

    int abaixo = 0, normal = 0, sobrepeso = 0, obesidade1 = 0, obesidade2 = 0, obesidade3 = 0;

    printf("Digite a quantidade de pessoas: ");
    scanf("%d", &qtd);
        for(int i = 1; i <= qtd; i++){
            printf("\nPaciente %d:\n", i);
            printf("Digite o peso (kg): ");
            scanf("%f", &peso);
            printf("Digite a altura (m): ");
            scanf("%f", &altura);

            imc = calcularIMC(peso, altura);

            if(imc < 18.5){
                abaixo++;
            } else if(imc < 25){
                normal++;
            } else if(imc < 30){
                sobrepeso++;
            } else if(imc < 35){
                obesidade1++;
            } else if(imc < 40){
                obesidade2++;
            } else {
                obesidade3++;
            }
        }
    printf("\nResultados:\n");
    
    printf("Abaixo do peso: %d (%.2f%%)\n", abaixo, calcularPorcentagem(abaixo, qtd));
    printf("Peso normal: %d (%.2f%%)\n", normal, calcularPorcentagem(normal, qtd));
    printf("Sobrepeso: %d (%.2f%%)\n", sobrepeso, calcularPorcentagem(sobrepeso, qtd));
    printf("Obesidade Grau 1: %d (%.2f%%)\n", obesidade1, calcularPorcentagem(obesidade1, qtd));
    printf("Obesidade Grau 2: %d (%.2f%%)\n", obesidade2, calcularPorcentagem(obesidade2, qtd));
    printf("Obesidade Grau 3: %d (%.2f%%)\n", obesidade3, calcularPorcentagem(obesidade3, qtd));
    
    return 0;
}