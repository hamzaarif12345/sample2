#include <iostream> // important
using namespace std;


int bs(int arr[], int l, int h, int x) {
  
  while (h >= l) {
    int mid = l+(h - l) / 2;
    if (arr[mid] == x) {
      //cout<<"Element found at index " << mid;
      return mid;
    } 
    else if (x > arr[mid]) {
      l = mid + 1;

    } 
    else {
      h = mid - 1;
    }
    
  }
  return -1;
}

int main() {
  int a, count = 0, c;
  cout<<"Enter the size of the array";
  cin>>a;
  int arr[a];
  for (int i = 0; i < a; i++) {
    cout<<"Enter the element " << i + 1 << "\n";
    cin>>arr[i];
  }
  int n = sizeof(arr) / sizeof(arr[0]);
  //std::sort(arr, arr + n); // sort is a inbuilt c++ function gfg
  cout<<"Enter the element to be searched for "<< "\n";
  cin>>c;
  int r = bs(arr, 0, a-1, c);
  if (r == -1) {
    cout<<"Element not found";
  } else {
    cout<<"Element found at index:" << r;
  }
  return 0;
}