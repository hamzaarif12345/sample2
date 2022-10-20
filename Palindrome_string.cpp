#include<bits/stdc++.h>
using namespace std;

int main(){
    cout<<"Enter the string ";
    string a;
    cin>>a;
    string b=a;
    reverse(a.begin(),a.end());
    if(a==b){
        cout<<"string is palindrome";
    }
    else{
        cout<<"not palindrome";
    }
    return 0;

}
