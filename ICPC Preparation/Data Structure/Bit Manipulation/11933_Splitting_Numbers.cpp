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

void printSet(int vS) {                         // in binary representation
    printf("S = %2d = ", vS);
    stack<int> st;
    while (vS)
        st.push(vS%2), vS /= 2;
    while (!st.empty())                         // to reverse the print order
       printf("%d", st.top()), st.pop();
    printf("\n");
}

int main(){
    Fast
    while (true){
        int n;cin>>n;
        if(n==0){
            break;
        }
        bool addToA = true;
        int toAdd = 1;
        int a = 0, b = 0;
        while (n) {
           if (isOn(n,0)){            
                if (addToA)
                    a += toAdd;
                else
                    b += toAdd;
                    
                addToA = !addToA;
            }
            
            toAdd *= 2;
            n /= 2;
        }
        cout<<a<<" "<<b<<endl;
        
    }
    
} 