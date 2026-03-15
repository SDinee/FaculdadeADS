#include <stdio.h>
 
 int main() {
 int numero;
 int soma = 0;
 
 printf("Digite números inteiros (0 para sair):\n");
 scanf("%d", &numero);
 

 // continua rodando o código até digitar 0.
 while (numero != 0) {
 soma += numero;
 scanf("%d", &numero);
 }
 
 printf("\nA soma dos números digitados é: %d\n", soma);
 
 return 0;
 }