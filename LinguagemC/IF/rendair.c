#include<stdio.h>
#include<stdlib.h>
 
int main(){
char CPF[11];
float renda;
 
printf("Digita o CPF do cidadão: \n");
scanf("%s",&CPF);
 
printf("Digita a renda do cidadão: \n");
scanf("%f",&renda);
 
if (renda >= 4664.68){
    printf("\n O cidadão com renda %.2f possui alíquota 27,5%%", renda);
 
}else if (renda>= 3751.06 && renda<4664.68){
    printf("\n O cidadão com renda %.2f possui alíquota 22,5%%", renda);
 
}else if (renda>= 2826.66 && renda<3751.06){
    printf("\n O cidadão com renda %.2f possui alíquota 15%%", renda);
 
}else if (renda>= 2259.21 && renda<2826.66){
    printf("\n O cidadão com renda %.2f possui alíquota 7,5%% \n", renda);

}else{
    printf("\n O cidadão com renda %.2f é isento do IR \n",renda);
 
}
return 0;
 }
