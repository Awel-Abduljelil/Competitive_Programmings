#include <iostream>
#include <vector>
 
using namespace std;
 
int main() {
 int n;
 cin >> n;
 
 vector<int> birds(n);
for (int i = 0; i < n; ++i) {
 cin >> birds[i];
 }
 
 int m;
 cin >> m;
 
 for (int i = 0; i < m; ++i) {
 int x, y;
 cin >> x >> y;
 
x--;
 
 int left_birds = y - 1;
  int right_birds = birds[x] - y;
 
  birds[x] = 0;
 
 if (x > 0) {
birds[x - 1] += left_birds;
 }
 if (x < n - 1) {
birds[x + 1] += right_birds;
 }
}
 for (int i = 0; i < n; ++i) {
cout << birds[i] << endl;
 }
return 0;
}