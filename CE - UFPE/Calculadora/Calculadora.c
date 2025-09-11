#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(){
int menu, entradamenu, encprog;
float s1, s2, s3, s4, r1, r2;

menu = 1; //Ativa Menu
while(menu == 1){
  entradamenu = NULL;
  printf("\n------------------------------------------------\n");
  printf("<<< Calculadora V1.0 >>>");
  printf("\n------------------------------------------------\n");
  printf("Para utilizar a calculadora, digite uma das opções abaixo.\n");
  printf("1 - Soma\n");
  printf("2 - Subtração\n");
  printf("3 - Multiplicação\n");
  printf("4 - Divisão\n");
  printf("5 - Raiz EQ. 2o Grau\n");
  printf("6 - Derivada\n");
  printf("0 - Sair\n");
  scanf("%d", &entradamenu);
  printf("------------------------------------------------\n");
  
  switch (entradamenu){
      case 1: //Soma
        
        printf("Selecionado SOMA!\n");
        printf("Entre com o Primeiro Numero:");
        scanf("%f", &s1);
        printf("Entre com o Segundo Numero:");
        scanf("%f", &s2);
        
        printf("%.2f + %.2f = %.3f", s1, s2, s1+s2); //Soma e apresenta o resultado!
  
      break;
  
      case 2: //Subtração
        printf("Selecionado SUBTRACAO!\n");
        printf("Entre com o Primeiro Numero:");
        scanf("%f", &s1);
        printf("Entre com o Segundo Numero:");
        scanf("%f", &s2);
  
        printf("%.2f - %.2f = %.3f", s1, s2, s1-s2); //Subrai e apresenta o resultado!
      break;
    
      case 3: //Multi
        printf("Selecionado MULTIPLICACAO!\n");
        printf("Entre com o Primeiro Numero:");
        scanf("%f", &s1);
        printf("Entre com o Segundo Numero:");
        scanf("%f", &s2);
  
        printf("%.2f * %.2f = %.3f", s1, s2, s1*s2); //Multiplica e apresenta o resultado!
      break;
    
      case 4: //Div
        printf("Selecionado DIVISAO!\n");
        printf("Entre com o Primeiro Numero:");
        scanf("%f", &s1);
        printf("Entre com o Segundo Numero:");
        scanf("%f", &s2);
  
        printf("%.2f / %.2f = %.3f", s1, s2, s1/s2); //Divide e apresenta o resultado!
      break;
    
      case 5: //Raiz 2ºGrau
        printf("Selecionado RAIZES DE UMA FUNCAO!\n");
        printf("Entre com o A:");
        scanf("%f", &s1);
        printf("Entre com o B:");
        scanf("%f", &s2);
        printf("Entre com o C:");
        scanf("%f", &s3);
  
        const float delta = (pow(s2,2)-4*s1*s3);
        printf("Delta: %.2f\n", delta);
        r1 = ((-s2+sqrt(delta))/(2*s1));
        r2 = ((-s2-sqrt(delta))/(2*s1));
        printf("\nAs raizes da funcao sao: x1 = &.2f e x2 = %.2f", r1,r2); //Raizes e apresenta o resultado!
      
      break;
    
      case 6: //Deriv.
        printf("Selecionado DERIVADA!\n");
        printf("Entre com o A:");
        scanf("%f", &s1);
        printf("Entre com o B:");
        scanf("%f", &s2);
        printf("Entre com o C:");
        scanf("%f", &s3);
        printf("Entre com o Ponto:");
        scanf( "%f", &s4);
    
  
        r1 = (s1*2*s4)+s2;
    
        printf("A derivada da funcao no ponto %.2f eh %.3f", s4, r1);
      break;
  
  
  
      case 0:
        encprog = NULL;
        while (encprog != 1){
          printf("Encerrar Programa?\n");
          printf("1 - Sim\n2 - Nao\n");
          scanf("%d", &encprog);
          switch (encprog){
          case 1:
            // Encerra
            encprog = 1;
            menu = 0; //desativa menu
          break;
      
          case 2:
            //Volta Menu
            printf("Voltando ao Menu!\n");
            encprog = 1;
            menu = 1; //ativa menu
          break;
      
          default:
            //Repete o Bloco
            printf("OPCAO INVALIDA!\n");
            encprog = 0; //repete a condição
          break;
          }
        }
      break;
  
      default:
      printf("Entrada Invalida.\n");
      menu = 1;
      break;
  };
}
    printf("\nPROGRAMA ENCERRADO!");
    return 0;
};
