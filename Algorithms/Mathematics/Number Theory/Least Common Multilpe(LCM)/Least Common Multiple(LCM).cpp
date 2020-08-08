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
	
} 
