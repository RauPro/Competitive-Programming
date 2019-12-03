#include <iostream>
using namespace std;
void comparar(int *vida,string palabra);
int main(){
	string palabras[3]={"hola","magdalena","otorrinolaringologo"};
	int vida=6;
	cout<<"Ingrese la dificultad: "<<endl;
	cout<<"1.Easy\n2.Normal\n3.Demente: ";
	int opcion;
	cin>>opcion;
	cout<<endl;
	switch(opcion){
		case 1:
			comparar(&vida,palabras[0]);
			break;
		case 2:
			comparar(&vida,palabras[1]);
			break;
		case 3:
			comparar(&vida,palabras[2]);
			break;
	}
	return 0;
}
void comparar(int *vida,string palabra){
	cout<<"Encuentre: "<<endl;
	string auxPalabra="";
	for (int i=0;i<palabra.size();i++){
		auxPalabra+="_";
	}
	verificarLetra:
	cout<<auxPalabra<<endl;
	int acum=0;
	cout<<"Tienes: "<<*vida<<" vidas"<<endl;
	cout<<"Ingrese una letra: ";
	char letra;
	cin>>letra;
	cout<<endl;
	for (int i=0;i<palabra.size();i++){
		if (letra==palabra[i]){
			auxPalabra[i]=letra;
			acum+=1;
		}
	}
	if (acum==0){
			*vida-=1;
		}
	if(*vida==0){
		cout<<"Tu vida llego a 0 :c, perdiste"<<endl;
		return;
	}
	if (auxPalabra==palabra){
		cout<<"LO LOGRASTE, la palabra es: "<<palabra<<endl;
		return;
	}
	else{
		goto verificarLetra;
	}
}
