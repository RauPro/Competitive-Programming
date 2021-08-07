// I GOT FK WA
#include <bits/stdc++.h>
#include <bits/extc++.h> // pbds

using namespace std;
using namespace __gnu_pbds;

#define LSOne(S) ((S) & -(S)) // Useful bitmask operation
#define Fast ios::sync_with_stdio(0); cin.tie(0);

typedef tree<int, null_type, less<int>, rb_tree_tag, tree_order_statistics_node_update> ost;
typedef long long ll;
typedef long int li;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef vector<ll> vll;
typedef pair<int, int> pi;

class FastScanner{
public:
	int nextInt(){int a;cin>>a;return a;}
    char nextChar(){char a;cin>>a;return a;}
    ll nextLong(){ll a;cin>>a;return a;}
    string next(){string a;cin>>a;return a;}
    vi readArray(int n){
		vi a(n);
		for (size_t i = 0; i < n; i++)cin>>a[i];
		return a;}
};

string lastToStartDelete(string a, string b){
    string s = a;
    bool allEqual = true;
    for (int i = 1; i <= min(a.length(), b.length()); ++i) {
        //cout<<"imin"<<a.substr(a.length()-(i+1))<<" "<<b.substr(0, i+1)<<endl;
        if (i==min(a.length(), b.length())){
            if (a.substr(a.length()-i)==b.substr(0, i)){
                //cout<<"imin"<<a.substr(a.length()-(i+1))<<" "<<b.substr(0, i+1)<<endl;
                allEqual = false;
                a.erase(a.begin()+(a.length()-i), a.end());
                a+=b;
                s = a;
                break;
            }
        }else{
            if (a.substr(a.length()-i)==b.substr(0, i) && (a.substr(a.length()-(i+1))!=b.substr(0, i+1)) ){
                //cout<<"imin"<<a.substr(a.length()-(i+1))<<" "<<b.substr(0, i+1)<<endl;
                allEqual = false;
                a.erase(a.begin()+(a.length()-i), a.end());
                a+=b;
                s = a;
                break;
            }
        }
    }
    if (min(a.length(), b.length())==1){
        if (a.substr(a.length()-1)==b.substr(0, 1)){
            //cout<<"WHAT"<<endl;
            allEqual = false;
            a.erase(a.begin()+(a.length()-1), a.end());
            a+=b;
            s = a;
        }
    }
    //cout<<"OUT"<<endl;
    if (allEqual){
        string auxA = a;
        string auxB = b;
        sort(auxA.begin(), auxA.end());
        sort(auxB.begin(), auxB.end());
        if (auxA[0] == auxA[auxA.length()-1] && auxB[0] == auxB[auxB.length()-1] && auxA[0] == auxB[auxB.length()-1] && auxB[0] == auxA[auxA.length()-1]){
            if (a.length()>b.length())s=a;
            else s = b;

        }else{
            a+=b;
            s=a;
        }

    }
    //cout<<s<<endl;
    return s;
}

int main(){
	Fast
	FastScanner fs;
	//cout<<lastToStartDelete("EDCCFBFD", "FD")<<endl;
    int t = fs.nextInt();
    for (int tt = 1; tt <=t; ++tt) {
        int n = fs.nextInt();
        vector<string> vs(n);
        for (int i = 0; i < n; ++i) {
            vs[i]=fs.next();
        }
        sort(vs.begin(), vs.end());
        int aws = 111111111;
        do {
            string s = vs[0];
            for (int i = 1; i < n; ++i) {
                //cout<<"COMPARE "<<s<<" "<<vs[i]<<endl;
                s = lastToStartDelete(s, vs[i]);

            }
            /*for (int i = 0; i < vs.size(); ++i) {
                cout<<vs[i]<<" ";
            }cout<<endl;
            cout<<s<<" "<<s.length()<<endl;*/
            int size = s.length();
            aws = min(aws, size);
        } while (next_permutation(vs.begin(), vs.end()));
        cout<<"Case "<<tt<<": "<<aws<<endl;
    }
	return 0;
}