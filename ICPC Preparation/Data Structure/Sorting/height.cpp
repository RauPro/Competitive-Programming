#include <bits/stdc++.h>
using namespace std;

#define Fast ios::sync_with_stdio(0); cin.tie(0);


typedef long long ll;
typedef long int li;
typedef vector<int> vi;
typedef vector<ll> vl;
void insertionSort(vi arr, int n, int test)
{
    int aws = 0;
     while (!is_sorted(arr.begin(), arr.end())){
         for (size_t i = 0; i < n-1; i++)
         {
            if(arr[i] > arr[i+1]) {
            swap(arr[i], arr[i+1]);
            aws++;
            }
         }
    }
    cout<<test<<" "<<aws<<endl;;
}
int main(){
    Fast
    int t;cin>>t;
    int test = 0;
    while (t--)
    {
        test++;
        vi arr(20);
        int n; cin>>n;
        for (size_t i = 0; i < 20; i++)
        {
            cin>>arr[i];
        }
        insertionSort(arr, 20, test);
        
    }
    
}   
