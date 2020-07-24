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
	int accept=0, wrong=0;
	int t;cin>>t;
	while(t--){
		accept = 0;
		wrong =0;
		int n;cin>>n;
		vi vector(n);
		for (int i=0;i<n;i++){
			vector[i]=i;
		}
		string m;
		int q=0, p=0;
		char c;
		getline(cin,m);
		while(1){
			getline(cin,m);
			if (m.size()==0){
			break;
			}
			istringstream temp(m);
			temp>>c>>q>>p;
			if (c=='c'){
				_union(p-1,q-1,vector);
			}
			else if(c=='q'){
				if(find(p-1,vector)==find(q-1,vector)){
					accept++;
				}
				else{
					wrong++;
				}
			}
		}
		cout<<accept<<","<<wrong<<endl;
		if (t)cout<<endl;
	}
} 
