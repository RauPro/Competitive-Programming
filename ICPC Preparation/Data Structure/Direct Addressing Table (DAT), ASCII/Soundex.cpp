#include <bits/stdc++.h>
using namespace std;

#define Fast ios::sync_with_stdio(0); cin.tie(0);


typedef long long ll;
typedef long int li;
typedef vector<int> vi;
typedef vector<ll> vl;

int main(){
	Fast
	string line;
    unordered_map<char,int> mapper;
    mapper['B'] = 1;
    mapper['F'] = 1;
    mapper['P'] = 1;
    mapper['V'] = 1;

    mapper['C'] = 2;
    mapper['G'] = 2;
    mapper['J'] = 2;
    mapper['K'] = 2;
    mapper['Q'] = 2;
    mapper['S'] = 2;
    mapper['X'] = 2;
    mapper['Z'] = 2;

    mapper['D'] = 3;
    mapper['T'] = 3;

    mapper['L'] = 4;

    mapper['N'] = 5;
    mapper['M'] = 5;

    mapper['R'] = 6;
    while (getline(cin,line,'\n')){

        for (int i = 0; i < line.length(); ++i) {
            if(line[i]!=line[i+1] && mapper[line[i]] && mapper[line[i]] != mapper[line[i+1]] && (line[i]!='E' && line[i]!='I' && line[i]!='O' && line[i]!='U' && line[i]!='H' && line[i]!='W' && line[i]!='Y')){
                cout<<mapper[line[i]];
            }
        }cout<<endl;
    }
    return 0;
}