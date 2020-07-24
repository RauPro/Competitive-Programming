#include <bits/stdc++.h>
using namespace std;
#define Fast ios::sync_with_stdio(0); cin.tie(0);
typedef long long ll;
typedef long int li;
typedef vector<int> vi;
typedef vector<ll> vl;
//Union-Find Algorithm

int find(int i, vi &vector){
	return (vector[i]==i)? i : vector[i] = find(vector[i], vector);
}

void _union(int p, int q, vi &vector){
	vector[find(p, vector)]= find (q, vector);
}

int main(){
	Fast
	//_unoin(int,int, vector) is for simpe union between 2 numbers
	
	//find(int, vector) is to find the index 
} 
