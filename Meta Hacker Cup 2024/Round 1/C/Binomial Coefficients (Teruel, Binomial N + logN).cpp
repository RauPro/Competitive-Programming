/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <iostream>

long long mod = 1000000007LL;
long long binpow(long long a, long long b, long long m) {
    a %= m;
    long long res = 1;
    while (b > 0) {
        if (b & 1)
            res = res * a % m;
        a = a * a % m;
        b >>= 1;
    }
    return res;
}

long long inv(int a){
    return binpow(a, mod - 2, mod);
}

long long f[1000000];

int main()
{
    f[0] = 1;
    for (int i = 1; i <= 1000000; i++){
        f[i] = (f[i - 1] * i) % mod; }  
    int t;std::cin>>t;
    while (t--){
          

//    std::cout<<inv(f[3]);
    long long n; std::cin >> n;
    long long k; std::cin >> k;
    std::cout<<(((f[n] % mod) * (inv(f[k]) % mod) % mod) * (inv(f[n-k]) % mod) % mod) << std::endl;
    }
    return 0;
}