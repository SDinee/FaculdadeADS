#include <stdio.h>

int main() {
float a, b, c;
 
printf("Digite o valor do lado A: \n");
scanf("%f", &a);
 
printf("Digite o valor do lado B: \n");
scanf("%f", &b);
 
printf("Digite o valor do lado C: \n");
scanf("%f", &c);
 
 // Verifica o tipo de triângulo
if (a == b && b == c){
    printf("Triângulo Equilátero\n");
}else if (a != b && a != c && b != c){
    printf("Triângulo Escaleno\n");
}else{
    printf("Triângulo Isósceles\n");
}

return 0;
}
