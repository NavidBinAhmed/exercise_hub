class Program
{
    static void Main()
    {
        list<int> given_list = new List<int> {1, 9, 2, 3, 7, 4, 5, 6};
        int largestElement = FindLargest(given_list);
        Console.WriteLine("The largest element is: ", + largestElement);
    }

    static int FindLargest (List<int> given_list)
    {
        int largest = given_list[0];

        for (int i = 1; i<given_list.Count; i++)
        {
            if (given_list[i] > largest)
            {
                largest = given_list[i]
            }
        }
        return largest
    }
}

