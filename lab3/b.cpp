// #include <iostream>

// using namespace std;

// int main() {
//     int n;
//     cin >> n;
//     int a[n];
//     for(int i = 0; i < n; ++i){
//         cin >> a[i];
//     }
//     int max = -1000000;
//     for(int i = 0; i < n; ++i){
//         if(a[i] > max){
//             max = a[i];
//         }
//     }
//     cout << max << endl;
//     return 0;
// }

#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> v;
    for(int i = 0; i < n; ++i){
        int x;
        cin >> x;
        v.push_back(x);
    }
    int max = -1000000;
    for(int i = 0; i < n; ++i){
        if(v[i] > max) max = v[i]; 
    }
    cout << max << endl;
    return 0;
}