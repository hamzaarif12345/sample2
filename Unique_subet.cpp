#include<bits/stdc++.h>
using namespace std;
void display(char a[],int n){
    for(int i=0;i<n;i++){
        cout<<a[i]<<" ";
    }
    cout<<endl;
}
void fp(char a[],int n){
    sort(a,a+n);
    cout<<"the possible combinations are\n";
    do{
        display(a,n);
    }while(next_permutation(a,a+n));
}
int main(){
    cout<<"enter the no of elements ";
    int q;
    cin>>q;

    char a[q];
    for(int i=0;i<q;i++){
        cout<<"enter the element ";
        cin>>a[i];
    }
    int n=sizeof(a)/sizeof(a[0]);
    fp(a,n);
    return 0;

}