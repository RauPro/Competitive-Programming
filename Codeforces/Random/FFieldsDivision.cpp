// B
#include <bits/stdc++.h>
const int base = 32768;
double begintime, endtime;

using namespace std;
inline void CALC_TIME()
{
    endtime = clock();
    cout<<"\nexecution time : "<<(endtime-begintime+1)/1000<<" s";
}
int n, x, a[base+8];
vector<int>l[base+8];
queue<int>s;
int main()
{
    begintime = clock();
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    memset(a, -1, sizeof(a));
    for(int i = 0; i < base; i++)
    {
        l[(i+1)%base].push_back(i);
        l[(i*2)%base].push_back(i);
    }
    a[0] = 0;
    s.push(0);
    while(!s.empty())
    {
        x = s.front();
        s.pop();
        for(int tmp : l[x])
            if(a[tmp] == -1)
            {
                a[tmp] = a[x]+1;
                s.push(tmp);
            }
    }
    cin>>n;
    while(n--)
    {
        cin>>x;
        cout<<a[x]<<' ';
    }
    return 0;
}