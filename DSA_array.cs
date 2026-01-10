public first_array()
{
    int [] arr = {1, 2, 3, 4, 5};
    foreach (var item in arr){
        console .WriteLine(item);
        
    }
}
public second_array()
{
    int [] arr2 = new int [5] {1,2,3,4,5};
    for (int i = 0; i < arr2.Length; i++){
        console .WriteLine(arr2[i]);
    }}

public Multidimensional_array()
{ //Multidimensional Arrays are also called rectangular arrays.
    int [,] multiArr = new int [2,3] { {1,2,3}, {4,5,6} };
    for (int i = 0; i < 2; i++){   
        for (int j = 0; j < 3; j++){
            console .WriteLine(multiArr[i,j]);
        }
    }
}

public jagged_array()
{
        // Declaring Jagged Array
		int[][] arr = { new int[] { 1, 3, 5, 7, 9 },
						new int[] { 2, 4, 6, 8 } };
        
		Console.WriteLine("Arrays :");
      
      	// Display the array elements:
		for (int i = 0; i < arr.Length; i++)
		{
			System.Console.Write("Elements[" + i + "] Array: ");
			
          	// Printing the elements of array
          	for (int j = 0; j < arr[i].Length; j++) {
				Console.Write(arr[i][j] + " ");
            }
          
            Console.WriteLine();
		}
}

public another_jagged_array(){
    int[][] jaggedArr = new int[3][];

    // Initialize each row with different lengths
    jaggedArr[0] = new int[] { 1, 2, 3 };
    jaggedArr[1] = new int[] { 4, 5 };
    jaggedArr[2] = new int[] { 6, 7, 8, 9 };
}


public static void Main (string[] args)
{
    first_array();
    second_array();
    Multidimensional_array();
    jagged_array();
}using System;

public list_in_Chsarp(){
    List<int> l =new list<int>();
    l.add(1);
    l.add(2);
    l.add(3);
    foreach(var item in l){
        console.writeline(item);
    }

    //there are three ways to declare a list in csharp
    List<int> list1 = new List<int>(); // Method 1: Using the List<T> constructor
    List<int> list2 = new List<int> { 1, 2, 3 }; // Method 2: Using collection initializer
    List<int> list3 = new List<int>(new int[] { 4, 5, 6 }); // Method 3: Initializing from an array

    int [] arr ={1,2,3,4,5};
    List<int> list4 = new List<int>(arr); // Method 4: Initializing from an existing array
    //size of list4 
    console.writeline("size of list4: " + list4.count);
    List<int> list5 = new List<int>(10);
    list5 = {1,2,3,4,5}; // Method 5: Specifying initial capacity
    list5.foreach(a =>console.writeline(a));
    list5.remove(3);
    console.writeline("after removing 3");
    list5.foreach(a =>console.writeline(a));
    // give me all functions of list in csharp
    list5.add(6);
    list5.add(7);
    list5.add(8);
    list5.add(9);
    list5.add(10);
    list5.add(11);
    list5.add(12);
    list5.add(13);
    list5.add(14);
    list5.add(15);
    list5.add(16);
    list5.add(17);
    console.writeline("after adding more elements");
    list5.foreach(a =>console.writeline(a));
    
    bool exists = list.Contains(3);

    list5.clear();
    console.writeline("after clearing the list");
    list5.foreach(a =>console.writeline(a));

    //sort list using this
    list5.sort();
    console.writeline("after sorting the list");
    list5.foreach(a =>console.writeline(a));


    //3. Remove Elements from the List

    // Remove(T): This method is used to remove the first occurrence of a specific object from the List.
    // RemoveAll(Predicate<T>): This method is used to remove all the elements that match the conditions defined by the specified predicate.
    // RemoveAt(Int32): This method is used to remove the element at the specified index of the List.
    // RemoveRange(Int32, Int32): This method is used to remove a range of elements from the List<T>.
    // Clear(): This method is used to remove all elements from the List<T>.


    
}

public stack (){
    {
        // Creating a Stack of strings
        Stack<string> myStack1 = new Stack<string>();
        // Inserting the elements into the Stack
        myStack1.Push("GeeksforGeeks");
        myStack1.Push("is");
        myStack1.Push("the");
        myStack1.Push("best");
        myStack1.Push("website");

        // Displaying the count of elements
        // contained in the myStack1
        Console.Write("Total number of elements in the Stack 1 are : ");

        Console.WriteLine(myStack1.Count);

        // Displaying the elements in Stack myStack1
        foreach(string str in myStack1)
        {
            Console.WriteLine(str);
        }

        // Creating a Stack from a collection
        Stack<string> myStack2 = new Stack<string>(myStack1.ToArray());

        // Displaying the count of elements
        // contained in the myStack2
        Console.Write("Total number of elements in the Stack 2 are : ");

        Console.WriteLine(myStack2.Count);

        // Displaying the elements in Stack myStack2
        foreach(string str in myStack2)
        {
            Console.WriteLine(str);
        }
    }
}