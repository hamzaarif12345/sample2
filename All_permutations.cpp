#include<bits/stdc++.h>
using namespace std;
void display(int a[],int n){
    for(int i=0;i<n;i++){
        cout<<a[i]<<" ";
    }
    cout<<endl;
}
void fp(int a[],int n){
    sort(a,a+n);
    cout<<"the possible combinations are\n";
    do{
        display(a,n);
    }while(next_permutation(a,a+n));
}
int main(){
    int a[]={12,12,67,76};
    int n=sizeof(a)/sizeof(a[0]);
    fp(a,n);
    return 0;

}