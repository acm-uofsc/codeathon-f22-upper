import java.util.Scanner;

public class naive {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        in.nextLine();
        in.nextLine();

        String votes = in.nextLine();
        String[] votesArr = votes.split(" ");

        System.out.println(findMajorityElementNaive(votesArr, votesArr.length));

        in.close();
    }

    public static String findMajorityElementNaive(String arr[], int n)
    {
        // check whether `nums[i]` is a majority element or not
        for (int i = 0; i <= n/2; i++)
        {
            int count = 1;
            for (int j = i + 1; j < n; j++)
            {
                if (arr[j].equals(arr[i])) {
                    count++;
                }
            }
     
            if (count > n/2) {
                return arr[i];
            }
        }
     
        return "None";
    }
}