#include<iostream>
#include<malloc.h>
using namespace std;
class Test
{
    public:
    int SIZE,MyQueue[3],front=-1,rear=-1,element;
    Test()
    {
        SIZE=3;
    }
    void enQueue()
    {
        if((front==0 && rear==SIZE-1) || (front==rear+1))
        cout<<"Pizza booking is full !!"<<endl;
        else
        {
            cout<<"Entern the pizza quantity :"<<endl;
            cin>>element;
            if(rear==SIZE-1 && front!=0)
            rear=-1;
            MyQueue[++rear]=element;
            if(front==-1)
            front=0;
        }
    }
    void deQueue()
    {
        if(front==-1 && rear==-1)
        cout<<"Pizza can't be searved due to unavailablility !!!"<<endl;
        else
        {
            cout<<"Pizza searvd :"<<MyQueue[front++];
            if(front==SIZE)
            front=0;
            if(front-1==rear)
            front=rear=-1;
        }
    }
    void display()
    {
        if(front==-1)
        cout<<"Out of Pizza !!!"<<endl;
        else
        {
            int i=front;
            cout<<"Pizza orderd are :"<<endl;
            if(front<=rear)
            {
                while(i<=rear)
                cout<<"\t"<<MyQueue[i++];
            }
            else
            {
                while(i<=rear)
                cout<<"\t"<<MyQueue[i++];
            }
        }
    }
};

int main()
{
    int choise;
    Test obj;
    while(1)
    {
        cout<<"********************* Welcome to Pizza Hunt ************************************"<<endl;
        cout<<"1.Place Your Order \n2. Searved order \n3. Display reamaining order \n4. Exit"<<endl;
        cout<<"Enter Your Choise: ";
        cin>>choise;
        switch(choise)
        {
            case1:
            obj.enQueue();
            break;
            case2:
            obj.deQueue();
            break;
            case3:
            obj.display();
            case4:
            exit(0);
            default:cout<<"Invalid Choise !!"<<endl;
        }
    }
}