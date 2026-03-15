#include<stdio.h>

int main() {
float peso, altura, imc;


printf("----------------IMC----------------\n");
printf("Digite o peso (kg): ");
scanf("%f", &peso);

printf("Digite a altura (m): ");
scanf("%f", &altura);
 
imc = peso / (altura * altura);
printf("Seu IMC é: %.2f\n", imc);

printf("-----------------------------------\n");

if (imc < 18.5){ 
printf("Classificação: Abaixo do peso\n");

}else if (imc >= 18.5 && imc < 24.9){
printf("Classificação: Peso normal\n");

}else if (imc >= 25 && imc < 29.9){
printf("Classificação: Sobrepeso\n");

}else if (imc >= 30 && imc < 34.9){
printf("Classificação: Obesidade grau 1\n");

}else if (imc >= 35 && imc < 39.9){
printf("Classificação: Obesidade grau 2\n");

}else{
 printf("Classificação: Obesidade grau 3 (mórbida)\n");
}
 
return 0;
}
