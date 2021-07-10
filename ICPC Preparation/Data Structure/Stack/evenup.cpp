#include <bits/stdc++.h>
using namespace std;

#define Fast ios::sync_with_stdio(0); cin.tie(0);


typedef long long ll;
typedef long int li;
typedef vector<int> vi;
typedef vector<ll> vl;

int main(){
    Fast
    int n;cin>>n;
    int num;
    stack<int> s;
    cin >> num;
    s.push(num);
    for(int i=1;i<n;i++) {
        cin >> num;
        if(!s.empty() && (num + s.top())%2 == 0) {
            s.pop();
        }
        else {
            s.push(num);
        }
    }
    cout << s.size() << endl;
    
    return 0;
} 