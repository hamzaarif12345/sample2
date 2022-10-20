#include<bits/stdc++.h>
using namespace std;
int main(){
    cout<<"Enter the size of the array: ";
    int a,arr[100],b;
    cin>>a;
    for(int i=0;i<a;i++){
        cout<<"enter the element: ";
        cin>>arr[i];
    }

    cout<<"Enter the target: ";
    cin>>b;
    for(int i=0;i<a;i++){
        for(int j=0;j<a;j++){
            if(b-arr[i]==arr[j]){
                cout<<'\nThe number are :"<<arr[i]<<" & "<<arr[j];
            }
        }
    }
    return 0;
}