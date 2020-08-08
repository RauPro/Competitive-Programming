#include <bits/stdc++.h>
using namespace std;

#define Fast ios::sync_with_stdio(0); cin.tie(0);

typedef long long ll;
typedef long int li;
typedef vector<int> vi;
typedef vector<ll> vl;
int gcd(int a, int b){
	while(b){
		int r= a%b;
		a = b;
		b = r;
	}
	return a;
}
//Least common multiple
int lcm(int a, int b){  
    return (a*b)/gcd(a, b);  
}   
int main(){
	Fast
	int t;cin>>t;
	while(t--){
		int l, r;cin>>l>>r;
		if(lcm(l,l*2)<=r and l*2<=r){
			cout<<l<<" "<<l*2<<endl;
		}
		else{
			cout<<-1<<" "<<-1<<endl;
		}
		
	}
} 
