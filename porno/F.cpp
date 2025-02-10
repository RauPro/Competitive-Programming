//
// Created by paypa on 2/9/2025.
//
#include<bits/stdc++.h>

#include <utility>

#define int long long

using namespace std;

const int N = 2025;

struct Polynomial{
    int n;
    vector<int> c;
    explicit Polynomial(vector<int> coefficients){
        c = std::move(coefficients);
        n = c.size();
    }
};

int binpow(int a, int b){
    int res = 1;
    for(; b; b >>= 1, a *= a) if(b & 1) res *= a;
    return res;
}

int eval(Polynomial p1, int x){
    int ans = 0;
    for(int i = 0; i < p1.n; i++){
        ans += binpow(x, i);
    }
    return ans;
}

Polynomial multiply(Polynomial p1, Polynomial p2){
    int n = p1.n + p2.n - 1;
    vector<int> coef(n, 0);
    for(int i = 0; i < p1.n; i++){
        for(int j = 0; j < p2.n; j++){
            coef[i+j] += p1.c[i]*p2.c[j];
        }
    }
    return Polynomial(coef);
}

signed main(){
    string s;
    cin >> s;
    vector<int> roots;
    vector<int> sign;
    for(int i = 1; i <= s.size() - 1; i++){
        if(s[i-1] != s[i]){
            roots.push_back(2*i+1);
            sign.push_back(1);
        }
    }
    if(!roots.size()){
        if(s[0] == 'H')
            cout << 0 << '\n' << 1 << '\n';
        else
            cout << 0 << '\n' << -1 << '\n';
        return 0;
    }
    if(s.front() == 'A' && s.back() == 'A'){
        sign[0] = -1;
    }
    else if(s.front() == 'H' && s.back() == 'A'){
        sign[0] = -1;
    }
    Polynomial p({-roots[0]*sign[0], sign[0]});
    for(int i = 1; i < roots.size(); i++){
        Polynomial pi({-roots[i]*sign[i], sign[i]});
        p = multiply(p, pi);
    }
    cout << p.n - 1  << '\n';
    for(int i = p.n-1; i >= 0; i--)
        cout << p.c[i] << ' ';
    cout << '\n';
    return 0;
}