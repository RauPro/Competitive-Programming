#include <bits/stdc++.h>
using namespace std;


int main(){
    int n;
    cin >> n;
    while (n--){
        int k, x;
        cin >> k >> x;
        cout << x + 9 * --k << endl;
    }
}