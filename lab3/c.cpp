#include <iostream>

using namespace std;

int main(){
    int n;
    cin >> n;
    int a[n];
    for(int i = 1; i <= n; ++i){
        cin >> a[i];
    }
    int num;
    int max = -1000000;
    for(int i = 1; i <= n; ++i){
        if(a[i] > max){
            max = a[i];
            num = i;
        }
    }
    cout << num << " ";
    return 0;
}