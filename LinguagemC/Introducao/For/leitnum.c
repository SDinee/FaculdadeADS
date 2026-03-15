#include<stdio.h>

 int main() {
     
 int qtd, i, num;
 int somatorio = 0;
 long produtorio = 1;
 
//long é usado quando você espera que o valor possa ficar muito grande, como no caso de multiplicar vários números (produtório).
//parecido com int, mas com maior capacidade de armazenamento.
//Por que começa com 1? Porque o produto de qualquer número com 1 é ele mesmo. 
//Se começasse com 0, o resultado final seria sempre 0.

 printf("Digite a quantidade de números: ");
 scanf("%d", &qtd);
 
 printf("===============================\n");
 printf("   Leitura de %d números\n", qtd);
 printf("===============================\n");
 
 for (i = 1; i <= qtd; i++) {
 printf("Digite o %d º número: ", i );
 scanf("%d", &num);
 somatorio += num;
 produtorio *= num;
 }
 
 printf("===============================\n");
 printf("Somatório: %d\n", somatorio);
 printf("Produtório: %ld\n", produtorio);
 printf("===============================\n");
 
 return 0;
 }