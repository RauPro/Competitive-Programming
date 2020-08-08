#include <bits/stdc++.h>
using namespace std;

#define Fast ios::sync_with_stdio(0); cin.tie(0);

typedef long long ll;
typedef long int li;
typedef vector<int> vi;
typedef vector<ll> vl;
//Euclidean Algorthm
//Running time O(log(a+b))
int gcd(int a, int b){
	while(b){
		int r= a%b;
		a = b;
		b = r;
	}
	return a;
}
int main(){
	Fast
	
} 
