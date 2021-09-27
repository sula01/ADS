#include <iostream>
#include <vector>
#include <algorithm>
#include <set>

using namespace std;
int a[10001];
set<int> s;

int main() {
    int n;
    cin >> n;
    for(int i = 0; i < n; i ++){
        cin >> a[i];
        s.insert(a[i]);
    }
    set<int>::iterator it = s.end();
    cout << *(--(--it));

    return 0;
}