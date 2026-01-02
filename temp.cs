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