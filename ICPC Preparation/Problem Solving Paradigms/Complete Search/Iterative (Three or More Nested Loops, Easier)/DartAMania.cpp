// https://onlinejudge.org/external/7/735.pdf
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


int main(){
	Fast
	FastScanner fs;
	set<vector<int>> bst;
    vi results;
    results.push_back(0);
    results.push_back(50);
    for (int i = 1; i <= 20; ++i) {
        for (int j = 1; j <= 3; ++j) {
            results.push_back(i*j);
        }
    }
    sort(results.begin(), results.end()); // O(log n)
    unordered_map<int, int> mapperP;
    unordered_map<int, int> mapperC;

    //n = n;
    for (int i = 0; i < results.size(); ++i) { // O(n^3)
        for (int j = 0; j < results.size(); ++j) {
            for (int k = 0; k < results.size(); ++k) {
                //cout<<(results[i]+results[j]+results[k])<<endl;
                vi node = {results[i], results[j], results[k]};
                int dataSet = results[i]+results[j]+results[k];
                if (bst.count(node)==0) {
                    sort(node.begin(), node.end());
                    do{
                        mapperP[dataSet]++;
                        bst.insert(node);

                    } while (next_permutation(node.begin(), node.end()));
                    mapperC[dataSet]++;
                };
            }
        }
    }
    while (true){
        int n = fs.nextInt();
        if (n<=0)break;

        if (!mapperC[n] && !mapperP[n])cout<<"THE SCORE OF "<<n<<" CANNOT BE MADE WITH THREE DARTS."<<"\n";
        else {
            cout<<"NUMBER OF COMBINATIONS THAT SCORES "<<n<<" IS "<<mapperC[n]<<"."<<"\n";
            cout<<"NUMBER OF PERMUTATIONS THAT SCORES "<<n<<" IS "<<mapperP[n]<<"."<<"\n";
        }
        cout<<"**********************************************************************"<<"\n";
    }
    cout<<"END OF OUTPUT"<<endl;
	return 0;
}