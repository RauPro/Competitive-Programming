#include <bits/stdc++.h>
using namespace std;

#define Fast ios::sync_with_stdio(0); cin.tie(0);

typedef long long ll;
typedef long int li;
typedef vector<int> vi;
typedef vector<ll> vl;

const double pi = 2 * acos (0.0);

int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int n;cin>>n;
        ll vectorA[n + 5];
        ll vectorB[n + 5];
        ll min_a = LONG_MAX;
        ll min_b = LONG_MAX;
        for(int i = 0; i < n; i++)
        {
            cin >> vectorA[i];
            min_a = min(min_a, vectorA[i]);
        }
        for(int i = 0; i < n; i++)
        {
            cin >> vectorB[i];
            min_b = min(min_b, vectorB[i]);
        }
        ll c = 0;

        for(int i = 0; i < n; i++)
        {
            if((vectorA[i] > min_a) && (vectorB[i] > min_b))
            {
                ll x = vectorA[i] - min_a;
                ll y = vectorB[i] - min_b;
                ll z = min(x, y);
                vectorA[i] -= z;
                vectorB[i] -= z;
                c += z;
            }
            if(vectorA[i] > min_a)
            {
                ll x = vectorA[i] - min_a;
                vectorA[i] -= x;
                c += x;
            }

            if(vectorB[i] > min_b)
            {
                ll x = vectorB[i] - min_b;
                vectorB[i] -= x;
                c += x;
            }
        }
        cout << c << endl;
    }

    return 0;
}
