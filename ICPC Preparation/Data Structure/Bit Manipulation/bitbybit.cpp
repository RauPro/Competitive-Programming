#include <bits/stdc++.h>
using namespace std;

#define Fast ios::sync_with_stdio(0); cin.tie(0);


typedef long long ll;
typedef long int li;
typedef vector<int> vi;
typedef vector<ll> vl;

#define isOn(S, j) (S & (1<<j))
#define setBit(S, j) (S |= (1<<j))
#define clearBit(S, j) (S &= ~(1<<j))
#define toggleBit(S, j) (S ^= (1<<j))
#define lowBit(S) (S & (-S))
#define setAll(S, n) (S = (1<<n)-1)

#define modulo(S, N) ((S) & (N-1))   // returns S % N, where N is a power of 2
#define isPowerOfTwo(S) (!(S & (S-1)))
#define nearestPowerOfTwo(S) (1<<lround(log2(S)))
#define turnOffLastBit(S) ((S) & (S-1))
#define turnOnLastZero(S) ((S) | (S+1))
#define turnOffLastConsecutiveBits(S) ((S) & (S+1))
#define turnOnLastConsecutiveZeroes(S) ((S) | (S-1))

void printSet(vi vS, set<int> positios) {                         // in binary representation
    for(int i = vS.size()-1; i>=0;i--){
        if(vS[i]!=-1){
            cout<<vS[i];
        }else{
            cout<<"?";
        }
    }
    cout<<endl;
}

int main() {
    Fast
        while (true) {
            int n;cin>>n;
            if(n==0)break;
            vi arr(32,-1);
            set<int> positios;
            for (size_t i = 0; i < n; i++){
                string action;cin>>action;
                int data=0, dataAc = 0;
                if(action == "SET"){
                    cin>>data;
                    arr[data]=1;
                    positios.insert(data);
                }
                if(action=="CLEAR"){
                    cin>>data;
                    arr[data]=0;
                    positios.insert(data);

                }
                if(action=="OR"){
                    cin>>data;
                    cin>>dataAc;
                    if(arr[data]==1 || arr[dataAc]==1){
                        arr[data]=1;
                    }
                    else  if(arr[data]==0 && arr[dataAc]==0){
                        arr[data]=0;
                    }else{
                        arr[data]=-1;
                    }
                }
                if(action=="AND"){
                    cin>>data;
                    cin>>dataAc;
                    if(arr[data]==1 && arr[dataAc]==1){
                        arr[data]=1;
                    }
                    else  if(arr[data]==0 && arr[dataAc]==0){
                        arr[data]=0;
                    }else{
                        arr[data]=-1;
                    }
                }
            }
            printSet(arr, positios);
        }

}