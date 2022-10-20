#include<iostream>
#include<bits/stdc++.h>
//Question link https://practice.geeksforgeeks.org/problems/convert-array-into-zig-zag-fashion1638/1?page=1&company[]=Amazon&company[]=Microsoft&curated[]=1&sortBy=submissions
using namespace std;
int main(){
    cout<<"Enter the size of the array: ";
    int a,arr[100];
    cin>>a;
    for(int i=0;i<a;i++){
        cout<<"enter the element: ";
        cin>>arr[i];
    }
    sort(arr,arr+a);
    for (int i = 1; i < a - 1; i += 2) {
        // swap the current element with the next element
        swap(arr[i], arr[i + 1]);
    }
    cout<<"array is :";
    for(int i=0;i<a;i++){
        cout<<arr[i];
        
    }
    return 0;

}