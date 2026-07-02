#include <iostream>
#include <vector> 
using namespace std;
int main() { int n;
cin >> n;  
vector<int> 
birds(n);
for (int i = 0; i < n; ++i) { 
  cin >> birds[i]; }  
  int m; cin >> m;  
for (int i = 0; i < m; ++i) { 
int x, y; cin >> x >> y; x--;
  int l = y - 1;
int r = birds[x] - y;  
  birds[x] = 0;  if (x > 0) {
    birds[x - 1] += l; }
  if (x < n - 1) {
    birds[x + 1] += r;
  }
}
 for (int i = 0; i < n; ++i) {
  cout << birds[i] << endl; }
return 0;
}
