#include <iostream>
 
using namespace std;
 
int main() {
  long long n, k;
  cin >> n >> k;
 
  long long num_odds = (n + 1) / 2;
 
  if (k <= num_odds) {
    cout << 2 * k - 1 << endl; // k-th odd number
  } else {
    cout << 2 * (k - num_odds) << endl; // k-th even number
  }
 
  return 0;
}