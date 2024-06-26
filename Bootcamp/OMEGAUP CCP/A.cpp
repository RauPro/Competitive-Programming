#include <bits/stdc++.h>
#include <bits/extc++.h> // pbds

using namespace std;
using namespace __gnu_pbds;

#define LSOne(S) ((S) & -(S)) // Useful bitmask operation
#define Fast ios::sync_with_stdio(0); cin.tie(0);
#define endl endl;

typedef tree<int, null_type, less<int>, rb_tree_tag, tree_order_statistics_node_update> ost;
typedef long long ll;
typedef long int li;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef vector<ll> vll;
typedef pair<int, int> pi;

const double EPS = 1e-9;
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

int solve(const string& events) {
    int people_in_club = 0;
    int min_people = 0;

    for (char event : events) {
        if (event == '+') {
            people_in_club += 1;
            min_people = std::max(min_people, people_in_club);
        } else if (event == '-' && people_in_club == 0) {
            min_people += 1;
        } else {
            people_in_club -= 1;
        }
    }

    return min_people;
}


int main(){
    Fast
    FastScanner fs;
    string input;
    while (cin >> input){
        cout << solve(input) << endl;
    }
    return 0;
}
