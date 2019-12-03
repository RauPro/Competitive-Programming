#include <iostream>
using namespace std;
struct libro{
	string titulo;
	int numPaginas;
	libro *sig;
};
int verificador=0;
void menu(){
	cout<<"Ingrese la opcion a Elegir: "<<endl;
	cout<<"1.Ingrese el nombre de libro \n";
	cout<<"2.Buscar libro o Ingresa 0 para Salir: \n";
}
void buscarlibro(libro *libroT, string name){
	if (verificador==0){
		cout<<"El libro no existe.\n";
	}

	if(libroT->titulo==name){
		cout<<"El numero de paginas es: "<<(libroT->numPaginas)<<endl;
	}
	else{
		buscarlibro(libroT->sig,name);
	}
	
}

int main(){
	libro *libroT;
	libro *inicio;
	while (1){
		menu();
		int opcion;cin>>opcion;
		if (opcion==0){
			break;
		}
		switch (opcion){
		case 1:
			verificador+=1;
			libroT = new libro;
			cout<<"Ingrese el nombre de el libro: "<<endl;
			cin>>libroT->titulo;
			cout<<"Ingrese el Numero de paginas: "<<endl;
			cin>>libroT->numPaginas;
			libroT->sig=inicio;
			inicio=libroT;
			break;
		case 2:
			string lib;
			cout<<"Ingrese el Libro que desea saber el N de paginas: "<<endl;
			cin>>lib;
			buscarlibro(inicio, lib);
			break;
	}
	}
	
}

