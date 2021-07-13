#include <bits/stdc++.h>
using namespace std;

#define Fast ios::sync_with_stdio(0); cin.tie(0);
int minT = 0;
int hashTable[3000+1];

typedef long long ll;
typedef long int li;
typedef vector<int> vi;
typedef vector<ll> vl;

void solve(vector<pair<int,int>>& pq, int count){
    bool flag = false;
    int acum = 0;
    for(int j=0;j<count;j++){
        for (int i = 0;i<pq.size();i++){
            if(acum==count)break;
            if(pq[i].second==minT){
                cout<<pq[i].first<<endl;
                pq[i].second += hashTable[pq[i].first];
                flag = true;
                acum++;
            }else
            flag = false;
        }
        if(!flag){
            j--;
            minT++;
        }

    }
}

int main(){
	Fast
	vector<pair<int,int>> pq;
    while (true){
        string action;cin>>action;
        if (action=="#"){
            sort(pq.begin(),pq.end());
            int count;cin>>count;
            minT = min(minT,count);
            solve(pq, count);
            break;
        }
        else if(action == "Register"){
            int id;cin>>id;
            int count;cin>>count;
            hashTable[id] = count;
            pq.push_back({id,count});
        }
    }
    return 0;
}