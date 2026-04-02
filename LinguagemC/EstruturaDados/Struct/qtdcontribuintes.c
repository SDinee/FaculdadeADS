#include <stdio.h> 

    typedef struct {
        char nome[50];
        int idade;
        float renda;
    } contribuinte;
        int n;
        int main(){
            printf("Digite a quantidade de contribuintes:\n");
            scanf("%d", &n);

            contribuinte pessoas[n];
            int menor = 0;
            int isentas = 0;

            for(int i = 0; i < n; i++){
                printf("*********Contribuinte %d*********\n", i + 1);
                printf("Nome:\n");
                scanf("%39s", pessoas[i].nome);

                printf("Idade:\n");
                scanf("%d", &pessoas[i].idade);

                printf("Renda Anual:\n");
                scanf("%f", &pessoas[i].renda);

                if(pessoas[i].idade < 18)
                    menor++;
                
                if(pessoas[i].renda <= 28559.70)
                    isentas++;
                
            }
            printf("**********Resultados*********\n");
            printf("Temos %d menores de idade.\n", menor);
            printf("Temos %d contribuintes isentos de imposto.\n", isentas);
            
            printf("\n");

            printf("Dados dos contribuintes:\n");
            for(int i = 0; i < n; i++){
                printf("\n------Pessoa %d------\n", i + 1);
                printf("\nNome: %s\n", pessoas[i].nome);
                printf("Idade: %d\n", pessoas[i].idade);
                printf("Renda Anual: %.2f\n", pessoas[i].renda);
            }

        return 0;
        }