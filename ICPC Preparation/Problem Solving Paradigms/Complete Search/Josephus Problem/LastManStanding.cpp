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
int josephusMethod(int n, int k){
    if (n == 1)
        return 1;
    else
        /*The position returned by josephus(n - 1, k)
       is adjusted because the recursive call
       josephus(n - 1, k) considers the
       original position k % n + 1 as position 1*/
        return (josephusMethod(n - 1, k) + k - 1) % n + 1;
}
int josephusCircle(int n, int k){
    list<int>l; //creates a doubly linked list using stl container//
    for(int i=1;i<=n;i++)
        l.push_back(i); //pushes i to the end of the doubly linked list//

    auto it = l.begin();
    while(l.size()>1){

        for(int i=1;i<k;i++){
            it++;

            if(it==l.end()){
                //if iterator reahes the end,then we change it to begin of the list//
                it = l.begin();
            }
        }

        it = l.erase(it);

        if(it==l.end()){
            //if iterator reahes the end,then we change it to begin of the list//
            it = l.begin();
        }
    }

    return l.front(); //returns front element of the list//

}
int main(){
	Fast
	FastScanner fs;
	int t = fs.nextInt();
    for (int i = 1; i <= t; ++i) {
        int n = fs.nextInt();
        int k = fs.nextInt();
        cout<<"Case "<<i<<": "<<josephusMethod(n,k)<<"\n";
    }
	return 0;
}