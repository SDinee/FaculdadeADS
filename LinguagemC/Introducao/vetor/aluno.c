#include <stdio.h>
#include <string.h>
#define TAM 50

int main(){
    int n, i;
    printf("Informe a quantidade de alunos da turma:\n");
    scanf("%d", &n);
    getchar();

    char nomes[n][TAM];
    float notaAV[n];
    float sim1[n];
    float sim2[n];
    float media[n];

    for (i = 0; i < n; i++){
        printf("\n-----Aluno %d-----\n", i + 1);
        printf("Nome: ");
        fgets(nomes[i], TAM, stdin);
        printf("Nota da AV (0 a 8): ");
        scanf("%f", &notaAV[i]);
        printf("Nota da Simulado 1 (0 a 1): ");
        scanf("%f", &sim1[i]);
        printf("Nota da Simulado 2 (0 a 1): ");
        scanf("%f", &sim2[i]);
        getchar();   
    }
    printf("\n-----Resultados-----\n");
        for(i = 0; i < n; i++){
            media[i] = notaAV[i] + sim1[i] + sim2[i];
            printf("\nAluno: %s", nomes[i]);
            printf("Média: %.2f\n", media[i]);

            if(media[i] >= 6.0){
                printf("Situação: Aprovado\n");
            
            } else if(media[i] >= 4.0){
                printf("Situação: Recuperação\n");

            } else {
                printf("Situação: Reprovado\n");
            }
        }
    return 0;
}