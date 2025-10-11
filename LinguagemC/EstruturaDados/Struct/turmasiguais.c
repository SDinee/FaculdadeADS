#include<stdio.h>
 #include<stdlib.h>
 #include<string.h>
 
 typedef struct{
 int mat;
 char nome[40];
 float nota;
 }aluno; 
 
int main(void){
 aluno ed[4];
 aluno java[3];
 
 printf("\nTurma de Estrutura de Dados\n");
 
 for(int i=0; i<4; i++){
 printf("\n Digite a matricula do %dº aluno: ", i+1);
 scanf("%d",&ed[i].mat);
 
 printf("\n Digite a nota do %dº aluno: ", i+1);
 scanf("%f", &ed[i].nota);
 
 getchar();
 printf("\n Digite a nome do %dº aluno: ", i+1);
 fgets(ed[i].nome, sizeof(ed[i].nome), stdin);
 ed[i].nome[strcspn(ed[i].nome, "\n")] = '\0';
 }
 
printf("\nTurma de Java\n");

 for(int i=0; i<3; i++){
 printf("\n Digite a matricula do %dº aluno: ", i+1);
 scanf("%d",&java[i].mat);
 
 printf("\n Digite a nota do %dº aluno: ", i+1);
 scanf("%f", &java[i].nota);
 
 getchar();
 printf("\n Digite a nome do %dº aluno: ", i+1);
 fgets(java[i].nome, sizeof(java[i].nome), stdin);
 java[i].nome[strcspn(java[i].nome, "\n")] = '\0';
 }
 
for(int i=0; i<4; i++){
 for(int j=0; j<3; j++){
 if(ed[i].mat == java[j].mat){
 printf("\n==================================");
 printf("\n📚 Aluno matriculado nas duas turmas");
 puts(ed[i].nome);
 }
 }
 }
 
 return 0;
}