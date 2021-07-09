#include <bits/stdc++.h>
using namespace std;

#define Fast ios::sync_with_stdio(0); cin.tie(0);


typedef long long ll;
typedef long int li;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef vector<string> vs;

void insertionSort(vs arr, int n)
{
    int aws = 0;
     while (!is_sorted(arr.begin(), arr.end())){
         for (size_t i = 0; i < n-1; i++)
         {
            if(arr[i] > arr[i+1]) {
            swap(arr[i], arr[i+1]);
            }
         }
    }
   for (size_t i = 0; i < n; i++)
   {   
       arr[i][0]=toupper(arr[i][0]);
       cout<<arr[i]<<endl;
   }cout<<endl;
   
}

int main(){
    Fast
    while (true)
    {
        
       int n; cin>>n;
       vs arr(n);
       if(!n){
           break;
       }
       for (size_t i = 0; i < n; i++)
       {
          cin>>arr[i];
          transform(arr[i].begin(), arr[i].end(), arr[i].begin(), [](unsigned char c){ return tolower(c); });
       }
       insertionSort(arr, n);
       
    }
    
} 