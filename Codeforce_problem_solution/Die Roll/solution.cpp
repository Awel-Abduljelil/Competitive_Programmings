#include <iostream>
#include <algorithm> 
using namespace std; 
int main() {
  int Y, W; 
  cin>>Y>>W; 
  int win = max(Y, W);
  int outcome = 6 - win + 1;
  int gcd = __gcd(outcome, 6);  
  outcome /= gcd; 
  int rest = 6 / gcd; 
  cout << outcome << "/" << denominator<< endl;
  return 0;}
