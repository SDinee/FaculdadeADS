#include<stdio.h>

 int main(){
 int idade;
 
 printf("Digite a idade do usuário: ");
 scanf("%d",&idade);
 
 //não é obrigatório usar chaves {} quando o bloco tem apenas uma única instrução.
 //mas é mais seguro para ter a certeza onde inicia e termina o bloco, evitando possiveis erros.
 
 if (idade < 12)
 printf("\nUsuário classificado como Criança");
 
 else if (idade<18)
 printf("\nUsuário classificado como Adolescente");
 
 else if (idade<40)
 printf("\n Usuário classificado como Jovem");
 
 else if (idade<60)
 printf("\nUsuário classificado como Adulto");
 
 else
 printf("\nUsuário classificado como Idoso");
 
 return 0;
 
 }