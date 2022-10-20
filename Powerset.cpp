#include<bits/stdc++.h>
using namespace std;
void ps(string str,int index=0,string curr = " "){
    int n=str.length();
    if(index==n){
        cout<<curr<<endl;
        return;
    }
    ps(str,index+1,curr+str[index]);
    ps(str,index+1,curr);

}
//link gfg /recursive program to generate power set
int main(){
    cout<<"enter th string ";
    string str;
    cin>>str;
    
    ps(str);
    return 0;
}

