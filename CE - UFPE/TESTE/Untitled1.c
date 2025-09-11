#include<stdio.h>
#include<string.h>

typedef struct sistema{
        char nome[50];
        float consumo;
        int ligado; //0 ou 1
}sistema;

void ler_dados(sistema *sistemas, int *n){
    FILE *arq;
    arq = fopen("dados.txt","r");
    if(arq){
        while(fscanf(arq,"%s %f %i",sistemas[*n].nome,&sistemas[*n].consumo,&sistemas[*n].ligado)==3){
            (*n)++;
        }
    }
    else
        printf("Erro ao abrir arquivo!");
    if(*n == 0)
        printf("Nada no arquivo!\n");
    fclose(arq);
}

void listar_sistemas(sistema *sistemas, int n){
    for(int i =0;i<n;i++){
        if(sistemas[i].ligado!=-1){
        printf("Dados sistema %d:\n",i);
        printf("Nome: %s\n",sistemas[i].nome);
        printf("Consumo: %f\n",sistemas[i].consumo);
        if(sistemas[i].ligado)
            printf("LIGADO.\n");
        else
            printf("DESLIGADO.\n");
        }
    }
}

void adicionar_sistema(sistema *sistemas, int *n){

        FILE *arq;
        arq = fopen("dados.txt","w");

        printf("Inserindo sistema %d:\n",*n);
        printf("Insira Nome: ");
        fflush(stdin);
        scanf("%49[^\n]",sistemas[*n].nome);
        printf("Insira Consumo: ");
        scanf("%f",&sistemas[*n].consumo);
        printf("Ligado (1), Desligado(0)?: ");
        scanf("%d",&sistemas[*n].ligado);
        *n = *n+1;



        for(int i =0;i<*n;i++){
           if(sistemas[i].ligado!=-1){
            fprintf(arq,"%s %f %d\n",sistemas[i].nome, sistemas[i].consumo, sistemas[i].ligado);
           }
        };
        fclose(arq);
}

void remover_sistema(sistema *sistemas, int *n){
    FILE *arq;
    arq = fopen("dados.txt","w");
    char remover[50];
    printf("Insira sistema a ser excluido: ");
    fflush(stdin);
    scanf("%49[^\n]",remover);
    for(int i =0;i<*n;i++){
        if(strcmp(remover,sistemas[i].nome)==0){
                printf("Removendo sistema %d\n",i);
                sistemas[i].ligado = -1;
                //*n=*n-1;
                break;
        }

    }
    if(arq==NULL){
        printf("Erro!");
    }
    else{
        for(int i =0;i<*n;i++){
           if(sistemas[i].ligado!=-1){
            fprintf(arq,"%s %f %d\n",sistemas[i].nome, sistemas[i].consumo, sistemas[i].ligado);
           }
        }
    }

    fclose(arq);
}

int main(){
    sistema sistemas[100];
    int n = 0,opcao;
    //declaracoes
    ler_dados(sistemas,&n);
    //menu
    do{
        printf("----Menu\n");
        printf("1-Adicionar\n2-Remover\n3-Relatorio\n4-Sair: ");
        scanf("%d",&opcao);
        switch(opcao){
            case 1:
                adicionar_sistema(sistemas, &n);
                break;
            case 2:
                remover_sistema(sistemas, &n);
                break;
            case 3:
                listar_sistemas(sistemas, n);
                break;
            case 4:
                printf("Saindo!\n");
                break;
            default:
                printf("Opcao invalida!\n");
        }

    }while(opcao!=4);


return 0;
}
