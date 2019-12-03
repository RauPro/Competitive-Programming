//Raul Guillen 00012119 Universidad centroamericana jose simeon cañas.
#include <iostream>
#include <string>
#define max 5 //Definimos el maximo de elementos de la cola.
using namespace std;
typedef struct {//creamos la estructura con el inicio,fina y la cola con el maximo de elementos a contener
  int final;
  int inicio;
  string vector[max];
} queue;//le damos nombre a nuestra estrcutura.
void Crear(queue &Cola) {//Para inicializar la cola
  Cola.final = -1;
  Cola.inicio = -1;
}
bool IsEmpty(queue Cola) {//Verificar si esta vacia
  if(Cola.final == -1) {
    return true;
  } //  cuando encuentran un return AUTOMÁTICAMENTE dejan de ejcutar lo que esté después
  return false;
}

/*
  Me devuelve los elementos de una cola circular
*/
int getElements(queue Cola) {
  if(IsEmpty(Cola)) {
    return 0;
  }
  if(Cola.inicio < Cola.final) {
    return Cola.final - Cola.inicio + 1;
  }
  return max - Cola.inicio + Cola.final + 1;
}

bool IsFull(queue Cola) {
  if(getElements(Cola) == max) {
    return true;
  }
  return false;
}

void Add(queue &Cola, string elemento) {
  if(!IsFull(Cola)) {//if(1)

    if(IsEmpty(Cola)) { //Si es la primera vez que se mete algo, pues incrementamos inicio y YA NO MAS
      Cola.inicio++;
    }
    if(Cola.final == max - 1) {
      Cola.final = 0;
    } else { //Ya sea que esté en el punto "normal" o "circular", siempre se aumenta final
      Cola.final++;
    }

    Cola.vector[Cola.final] = elemento;
    cout << "Add: <" << elemento << ">" << endl;
    cout << "inicio: " << Cola.inicio << endl;
    cout <<"final: " << Cola.final << "\n" << endl;
  } else {
    cout << "Esta llena, no pudo entrar <" << elemento << ">" << endl;
  }
}
void Del(queue &Cola) {
  if(!IsEmpty(Cola)) {

    cout << "Se ha borrado " << Cola.vector[Cola.inicio] << endl;
    if(getElements(Cola) == 1) {
      Crear(Cola);
    } else {
      Cola.inicio++;
    }
  } else {
    cout << "Vacia no se puede borrar nada" << endl;
  }
}
void Recorrer(queue Cola) {
  if(!IsEmpty(Cola)) {
    int x;
    if(Cola.inicio <= Cola.final) {
      for(x = 0; x <= Cola.final; x++) {
        cout << "Cola.vector["<< x << "]: " << Cola.vector[x] << endl;
      }
    } else {
      //kha?
      for(x = Cola.inicio; x < max; x++) {
        cout << "Cola.vector["<< x << "]: " << Cola.vector[x] << endl;
      }
      for(x = 0; x <= Cola.final; x++) {
        cout << "Cola.vector["<< x << "]: " << Cola.vector[x] << endl;
      }
    }
  } else {
    cout << "nada que ver" << endl;
  }
}

int main() {
  queue Cola;
  Crear(Cola);
  Add(Cola,"Raul");
  Add(Cola,"Emely");
  Add(Cola,"maria");
  Add(Cola,"Sam");
  Add(Cola,"Rango");
  Add(Cola,"Dani");
  Del(Cola);
  Add(Cola,"Dani");
  Del(Cola);
  Add(Cola,"Alex");
  Recorrer(Cola);
  return 1;
}
