#include <iostream>
#include <algorithm>
 
using namespace std;
 
int main() {
 int Y, W;
 cin >> Y >> W;
 int winning = max(Y, W);
int outcomes = 6 - winning + 1;
int gcd = __gcd(outcomes, 6);
 
 outcomes /= gcd;
 int denominator = 6 / gcd;
 cout << outcomes << "/" << denominator << endl;
 
 return 0;
}