#include<iostream>
#include<time.h>
#include<string>
using namespace std;

struct personas{
	string nombre;
	string apellido;
	int edad;
	long numtelefono;
	string correo;
	personas *sig;
};
void eliminar(personas* p,string name);
void menu();
int main(){
	int opcion;
	
	personas *inicio=NULL;
	personas *nodo=NULL;
	while (1){
		menu();
		cin>>opcion;
	if (opcion==0){
		break;
	}
	switch(opcion){
		case 1: 
			nodo=new personas;
			cout<<"ingrese nombres";
			cin.ignore();
			getline(cin,nodo->nombre);
			cout<<endl;
			cout<<"un apellido";
			cout<<endl;
			cin>>nodo->apellido;
			cout<<endl;
			cout<<"edad";
			cin>>nodo->edad;
			cout<<"numero telefono";
			cin>>nodo->numtelefono;
			cout<<"correo";
			cin>>nodo->correo;
			nodo->sig=inicio;
			inicio=nodo;
			break;
			case 2:
			cout<<"ingresar el nombre de la persona que quiere eliminar";
			string name;
			cin>>name;
			eliminar(inicio,name);
			break;
			}
		}
			
			
			
			
			 
			
	
	return 0;
}
void eliminar(personas* p,string name){
	if(name==p->nombre){
		delete (p);
		cout<<"se a eliminado el dato";
	}
	
	
	
}

void menu(){
	cout<<"1.llenar lista"<<endl;
	cout<<"2.eliminar persona"<<endl;
	cout<<"3.actualizar datos"<<endl;
	cout<<"4.mostrar todas las personas"<<endl;
	cout<<"0.salir";	
}
