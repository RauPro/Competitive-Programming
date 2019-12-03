#include <iostream>
#include <stdlib.h>
using namespace std;
struct nodo{
	int dato;
	nodo* sig;
};
void buscarMenor(nodo *lista);
int main(){
	nodo *proxi=NULL;
	int n, axu1,axu2,axu3;
	cin>>n;
	int datos[n][3];
	int registro[n][3];
	for (int i=0;i<n;i++){
		for (int j=0;j<3;j++){
			cin>>datos[i][j];
		}
	}
	//guardamos todas las diferencias anuales
	for (int i=0;i<n-1;i++){
		nodo *lista= new nodo();
		lista->	dato=abs(datos[i][2]-datos[i+1][2]);
		lista->sig=proxi;
		proxi=lista;
	}
	buscarMenor(proxi);
	return 0;
}
//buscamos la diferencia minima anual
void buscarMenor(nodo *lista){
	int minimo=lista->dato;
	while (lista!=NULL){

		if (lista->dato<=minimo){
			minimo =lista->dato;
		}
		
		lista=lista->sig;
	}
	cout<<minimo;

}
