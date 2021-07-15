#include <bits/stdc++.h>
using namespace std;

#define Fast ios::sync_with_stdio(0); cin.tie(0);


typedef long long ll;
typedef long int li;
typedef vector<int> vi;
typedef vector<ll> vl;
int main(){
	Fast
	int p;cin>>p;
	int g;cin>>g;
	unordered_map<string, double> mapper;
    for (int i = 0; i < p; ++i) {

        string party;cin>>party;
        double average;cin>>average;
        cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');

        mapper[party] = average*10;
    }
    for (int i = 1; i <= g; ++i) {
        double aws = 0;
        string action;
        while (true){
            cin>>action;
            if(action=="+"){
                cin>>action;
                aws += mapper[action];
            }
            else if(action==">" || action==">=" || action=="<" || action=="<=" || action=="="){
                double doubleComparate;cin>>doubleComparate;
                if(action==">" && aws>doubleComparate*10){
                    cout<<"Guess #" <<i<<" was correct."<<endl;
                }else if(action==">=" && aws>=doubleComparate*10){
                    cout<<"Guess #" <<i<<" was correct."<<endl;
                }else if(action=="<" && aws<doubleComparate*10){
                    cout<<"Guess #" <<i<<" was correct."<<endl;
                }else if(action=="<=" && aws<=doubleComparate*10){
                    cout<<"Guess #" <<i<<" was correct."<<endl;
                }else if(action=="=" && (aws) == (doubleComparate*10)){
                    cout<<"Guess #" <<i<<" was correct."<<endl;
                }else{
                    cout<<"Guess #" <<i<<" was incorrect."<<endl;
                }
                break;
            }
            else{
                aws = mapper[action];
            }
        }
    }
    return 0;
}