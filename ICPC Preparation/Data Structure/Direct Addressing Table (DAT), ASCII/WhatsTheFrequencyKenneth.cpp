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
	int current = 0;

    while (getline(cin, line, '\n')){
        unordered_map<char, int> mapper;
        current = 0;
        for (char & i : line) {
            if(i>=65 && i<=122){
                mapper[i] += 1;
                current = max(current, mapper[i]);
            }
        }
        for (int i = 65; i <= 122; ++i) {
            if(mapper[(char)i]==current){
                cout<<(char)i;
            }
        }cout<<" "<<current<<endl;
    }
    return 0;
}