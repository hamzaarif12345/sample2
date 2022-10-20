#include <iostream>
using namespace std;
class cricket{
    public:
        int sum=0,sum2=0;
        char arr[6][10]={"Varun","Arun","Sohan","Mohan","Raju","Shyam"};
        char arr2[6][10]={"Ram","Rishi","Mali","Jeet","Inder","Kartik"};
        int innings_A()
        {
            cout<<"\nTeam A is batting ";
            cout<<"\nPlayer coming for batting is:";
            int k1;
            k1=rand()%6;
            cout<<arr[k1];
            cout<<"\nPlayer coming for bowling is:";
            int k2;
            k2=rand()%6;
            cout<<arr2[k2];
            int r[30];
            for(int j=0;j<6;j++)
            {
                r[j]=rand()%6+1;
                cout<<"\nBowling ball number:"<<j+1<<"          run scored=> "<<r[j];
                sum=sum+r[j];
            }
            cout<<"\nRun scored in the over =>";
            cout<<sum;
            return sum;
        }
        
        int innings_B()
        {
            cout<<"Team B is batting ";
            cout<<"\nPlayer coming for batting is:";
            int k1;
            k1=rand()%6;
            cout<<arr2[k1];
            cout<<"\nPlayer coming for bowling is:";
            int k2;
            k2=rand()%6;
            cout<<arr[k2];

            int r1[30];
            for(int j=0;j<6;j++)
            {
                r1[j]=rand()%6+1;
                cout<<"\nBowling ball number:"<<j+1<<"          run scored=> "<<r1[j];
                sum2=sum2+r1[j];
            }
            cout<<"\nRun scored in the over =>";
            cout<<sum2;
            return sum2;
        }
        
    
};
int main()
{
    cout<<"                        Welcome to the match                 ";
    cout<<"\n\nThe list of the palyer is:";
    cout<<"\nTeam A: ";
    cout<<"Varun  Arun  Sohan  Mohan  Raju  Shyam";
    cout<<"\nTeam B: ";
    cout<<"Ram  Rishi   Mali  Jeet   Inder   Kartik";
    cricket C1,C2;
    cout<<"\n\n                 Firts Inning                  ";
    C1.innings_A();
    cout<<"\n\n";
    C1.innings_B();
    cout<<"\n\n                 Second Inning                  ";
    C2.innings_A();
    cout<<"\n\n";
    C2.innings_B();
    if(C1.sum+C2.sum==C1.sum2+C2.sum2)
    {
        cout<<"\n\nThe match tied";
    }
    else if(C1.sum+C2.sum>C1.sum2+C2.sum2)
    {
        cout<<"\n\nTeam A won by "<<(C1.sum+C2.sum)-(C1.sum2+C2.sum2)<<" runs";
    }
    else{
        cout<<"\n\nTeam B won by "<<(C1.sum2+C2.sum2)-(C1.sum+C2.sum)<<" runs";
    }
    cout<<"\n\n                   Match ends";
    return 0;
}
