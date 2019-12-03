//Raul Guillen 00012119
#include <iostream>
#include <vector>
using namespace std;

struct orden{
    int r;
    int fq;
    int q;
    bool arroz;
};
typedef struct orden Orden;

Orden solicitarOrden(){
    Orden p;
    int n;
    cout << "Revueltas: "; cin >> p.r;
    cout << "Frijol con Queso: ";   cin >> p.fq;
    cout << "Queso: "; cin >> p.q;
    cout << "Que sean de arroz, 1.si:   "; cin >> n;
    if(n == 1){
        p.arroz = true;
    }else if(n != 1){
        p.arroz = false;
    }
    return p;
}

void leyendoOrden(Orden p){
    cout << "**Pupusas:" << endl;
    cout << "Revueltas: " << p.r << endl;
    cout << "Frijol con Queso: " << p.fq << endl;
    cout << "Queso: " << p.q << endl;
    cout << "Son de arroz? ";
    if(p.arroz){
        cout << "Si" << endl;
    }else{
        cout << "No" << endl;
    }
    cout << endl;
}

vector<Orden> lista;

void agregarOrden(){
    Orden p = solicitarOrden();
    bool continuar = true;
    do{
        int opcion = 0;
        cout << "\t1) Al principio\n\t2) Al final"
        << "\n\tOpcion elegida: ";
        cin >> opcion;
        switch(opcion){
            case 1: lista.insert(lista.begin(), p);
                continuar = false;
                break;
            case 2: lista.push_back(p);
                continuar = false;
                break;
            default: cout << "Opcion erronea!" << endl;
                break;
        }
    }while(continuar);
}

void mostrarLista() {
    for (int i = 0; i < lista.size(); i++)
        leyendoOrden(lista[i]);
}

int main(){
    cout << "Inicializando..." << endl;
    
    bool continuar = true;
    do{
        int opcion = 0;
        cout << "Menu: \n\t1) Agregar Pedido\n\t2) Ver pedidos"
        << "\n\t3) Salir\n\tOpcion elegida: ";
        cin >> opcion;
        switch(opcion){
            case 1: cout << "Agregando..." << endl;
                agregarOrden();
                break;
            case 2: cout << "Listando..." << endl;
                mostrarLista();
                break;
            case 3: continuar = false;
                break;
            default: cout << "Opcion erronea!" << endl;
                break;
        }
    }while(continuar);
    
    return 0;
}
