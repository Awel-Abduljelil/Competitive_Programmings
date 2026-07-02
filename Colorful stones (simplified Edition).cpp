#include <iostream>
#include <string> 
using namespace std; 
int main() {
  string s, t;
  cin >> s >> t; 
  int current_stone = 0; 
  for (int i = 0; i < t.length(); ++i) {
    if (s[current_stone] == t[i]) { 
      current_stone++; }
  }  
  cout << current_stone + 1 << endl;
  return 0;
}
