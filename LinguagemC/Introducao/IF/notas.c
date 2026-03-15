#include<stdio.h>

 int main(){
 float av1, av2, media;
 
 printf("Digite a nota da AV1 do aluno: ");
 scanf("%f",&av1);
 
 printf("\nDigite a nota da AV2 do aluno: ");
 scanf("%f",&av2);
 
 media=(av1+av2)/2;
 
  //controle do valor da média (adicional), feito por min.
 if (media < 0 || media > 10){
     printf("Nota inválida.");
 }else{
    if (media>=6){
        printf("\nO aluno esta aprovado com a media %.2f", media);
    }else if (media>=4){
        printf("\nO aluno está em recuperação com média %.2f", media);
    }else{
        printf("\nO aluno esta reprovado com a media %.2f",media);
    }
}
 return 0;
 
}
 