#include<iostream>
using namespace std;
main(){
    int t;
    cin>>t;
    for(int i=1;i<= t;i++){
        int x;
        cin>>x;
        int sum=0;
        for(int j=1;j<10;j++){
            int aa,bb,cc,dd;
            aa=j;
            bb=j+(j*10);
            cc=j+(j*110);
            dd=j+(j*1110);
             if (x==aa){
                sum+=1;
                break;
                }
            else if(x==bb){
                sum+=3;
                break;
                }
            else if(x==cc){
                sum+=6;
                break;
                }
            else if(x==dd){
                sum+=10;
                break;
                }
            else
                    sum+=10;
 
 
        }
        cout<<sum<<endl;
    }
    return 0;
}