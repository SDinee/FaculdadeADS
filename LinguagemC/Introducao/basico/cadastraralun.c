#include<stdio.h>

 int main(){

 printf("Segunda aula de Programação e C");
 printf("\n*****************************");

 printf("\nProf Alessandro Calin");
 printf("\n*****************************");
 printf("\nCadastrando Aluno:");

 //char de vetor
 char nome[40];
 int idade;

//leitura somente até o 1 espaço no texto.
// scanf por padrão interrompe a leitura ao encontrar um espaço.

 printf("\nDigite o nome do Aluno: ");
 scanf("%s",&nome);

 printf("\nDigite a idade do Aluno: ");
 scanf("%d",&idade);

 printf("\n**********************************");
 printf("\nRelatório");
 printf("\n**********************************");

 printf("\nNome: %s",nome);
 printf("\nIdade: %d", idade);

    return 0;
 }