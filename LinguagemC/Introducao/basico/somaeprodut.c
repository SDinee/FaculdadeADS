 #include<stdio.h>
 
 int main(){
 int num1, num2, soma, prod;
 
 printf("Digite o valor do primeiro número: ");
 scanf("%d",&num1);
 
 printf("Digite o valor do segundo número: ");
 scanf("%d",&num2);
 
 soma=num1+num2;
 prod = num1*num2;
 
 printf("\n********************");
 printf("\nResultados");
 printf("\n********************");
 
 printf("\n%d + %d = %d",num1,num2,soma);
 printf("\n%d x %d = %d", num1, num2, prod);
 
 return 0;
 }