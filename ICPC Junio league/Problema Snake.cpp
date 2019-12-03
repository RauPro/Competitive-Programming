#include <iostream>
#include<stdlib.h>
#include<time.h>
using namespace std;
void generarMatriz(char *matriz[20][20]){
	for (int i=0;i<20;i++){
		for(int j=0;j<20;j++){
			*matriz[i][j]=' ';	
		}
		cout<<endl;
	}	
	for (int i=0;i<20;i++){
		*matriz[0][i]='0';
		*matriz[19][i]='0';
		*matriz[i][0]='0';
		*matriz[i][19]='0';	
		cout<<endl;
	} 
}

int main(){
	char matriz[20][20];
	int num,num2;
    srand(time(NULL));
    num=rand()%19;
	num2=rand()%19;  
	generarMatriz(&&matriz);
	matriz[num][num2]='x';
	for (int i=0;i<20;i++){
		for(int j=0;j<20;j++){
			cout<<matriz[i][j];	
		}
		cout<<endl;
	}  
	return 0;
}
