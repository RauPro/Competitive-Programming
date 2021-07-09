#include <bits/stdc++.h>
using namespace std;

#define Fast ios::sync_with_stdio(0); cin.tie(0);


typedef long long ll;
typedef long int li;
typedef vector<int> vi;
typedef vector<ll> vl;

void printVector(vi arr){
    for (size_t i = 0; i < arr.size(); i++)
    {
        cout<<arr[i]<<" ";
    }
    cout<<endl;
    
}
int main(){
    Fast
    vi arr(5);
    for (size_t i = 0; i < 5; i++)
    {
        cin>>arr[i];
    }
    while (!is_sorted(arr.begin(), arr.end())){
        if(arr[0] > arr[1]) {
            swap(arr[0], arr[1]);
            printVector(arr);
        }
        if(arr[1] > arr[2]) {
            swap(arr[1], arr[2]);
             printVector(arr);
        }
        if(arr[2] > arr[3]) {
            swap(arr[2], arr[3]);
            printVector(arr);
        }
        if(arr[3] > arr[4]) {
            swap(arr[3], arr[4]);
             printVector(arr);
        }
    }
} 