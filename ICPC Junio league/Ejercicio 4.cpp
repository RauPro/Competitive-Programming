#include <iostream>
using namespace std;
struct numeros{
	int num;
	numeros *sig;
};
int verificador=0;
void menu(){
	cout<<"Ingrese la opcion a Elegir: "<<endl;
	cout<<"1.Ingresar numeros \n";
	cout<<"2.Calcular Pares impares o 0 para Salir: \n";
}
void buscarnumeros(numeros *numerosT, int numeroPar, int numeroImpar,int acum){
	if(acum==verificador){
		cout<<"Numeros pares: "<<numeroPar<<endl;
		cout<<"Numeros Impares: "<<numeroImpar<<endl;
		return;
	}
	if((numerosT->num)%2==0){
		numeroPar+=numerosT->num;
		buscarnumeros(numerosT->sig,numeroPar,numeroImpar,acum+=1);
	}
	else {
		numeroImpar+=numerosT->num;
		buscarnumeros(numerosT->sig,numeroPar,numeroImpar,acum+=1);
	}
	
}

int main(){
	numeros *numerosT;
	numeros *inicio;
	while (1){
		menu();
		int opcion;cin>>opcion;
		if (opcion==0){
			break;
		}
		switch (opcion){
		case 1:
			verificador+=1;
			numerosT = new numeros;
			cout<<"Ingrese el numero: "<<endl;
			cin>>numerosT->num;
			numerosT->sig=inicio;
			inicio=numerosT;
			break;
		case 2:
			buscarnumeros(inicio, 0,0,0);
			break;
	}
	}
	
}
