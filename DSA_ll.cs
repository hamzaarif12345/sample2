// this is the code for linked list in csharp

using System;
using System.Collections.Generic;

pulblic linked_list_in_csharp(){
    LinkedList<int> ll = new LinkedList<int>();
    ll.addlast(1);
    ll.addlast(2);
    ll.addlast(3);
    foreach(var item in ll){
        console.writeline(item);
    }


    //there are three ways to declare a linked list in csharp
    LinkedList<int> ll1 = new LinkedList<int>();
    LinkedList<string> ll2 = new LinkedList<string>();
    LinkedList<int> ll3 = new LinkedList<int>(new int[] { 1, 2, 3 }); 
    ll3.Contains(2); // returns true if 2 is present in the linked list
}


/*
LinkedList<T> class provides five different methods to remove elements and the methods are:

    Clear(): Clear() method is used to remove all nodes from the LinkedList.
    Remove(LinkedListNode): Remove(LinkedListNode) method is used to remove the specified node from the LinkedList.
    Remove(T): Remove(T) method is used to remove the first occurrence of the specified value from the LinkedList.
    RemoveFirst(): RemoveFirst() method is used to remove the node at the start of the LinkedList.
    RemoveLast(): RemoveLast() method is used to remove the node at the end of the LinkedList.
    LinkedList class provide Contains(T) method to check if the element is present in the LinkedList or not.
*/

/*
LinkedList class provides four different methods to insert nodes and these methods are listed below:

    AddAfter(): This method is used to add a new node or value after an existing node in the LinkedList.
    AddBefore(): This method is used to add a new node or value before an existing node in the LinkedList.
    AddFirst(): This method is used to add a new node or value at the start of the LinkedList.
    AddLast(): This method is used to add a new node or value at the end of the LinkedList.
*/
    