//
// Created by Daniel Tim Lee on 2016. 4. 11..
//

#include "1.h"

int c_baseball(){
    int com[3];
    int usr[3];
    int count=10;
    int strike=0, ball=0;

    srand(time(NULL));

    //com random init
    do{
        for (int i = 0; i < 3; i++) {
            com[i]=(rand()%10 + 1);
            printf("%d is : %d\n",i ,com[i]);
        }
    }while(com[0]==com[1] ||com[1]==com[2] ||com[0]==com[2]);


    for (int l = 0; l < 10; ++l) {
        printf("\t%dnd trial \n",l);
        do{
            printf("input your number\n");
            scanf("%d",&usr[0]);
            scanf("%d",&usr[1]);
            scanf("%d",&usr[2]);
        }while(usr[0]==usr[1] ||usr[1]==usr[2] ||usr[0]==usr[2]);

        strike =0, ball=0;
        for (int j = 0; j < 3; j++) {
            for (int k = 0; k < 3; k++) {
                if(com[j]==usr[k] && j==k)  strike++;
                if(com[j]==usr[k] && j!=k)  ball++;
            }
        }
        printf("Strike : %d, Ball : %d",strike,ball);

        if(strike==3){
            printf("Good!!");
            return 0;
        }
        if(l==10){
            printf("Lose!!");
            return 0;
        }
    }
}
