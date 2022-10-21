import java.util.Scanner;

public class naive {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        String[] elections = in.nextLine().split(" ");
        int n = Integer.parseInt(elections[elections.length - 1]);
        in.nextLine();

        for (int i = 0; i < n; i++) {
            String votes = in.nextLine();
            String[] votesArr = votes.split(" ");
            System.out.println(findMajorityElementNaive(votesArr, votesArr.length));
        }
        

        in.close();
    }

    public static int findMajorityElementNaive(String arr[], int n)
    {
        int[] candidates = new int[n];

        for (int i = 0; i < n; i++) {
            candidates[Integer.parseInt(arr[i])]++;
        }
     
        int max = 0;
        for (int i = 1; i < n; i++) {
            if (candidates[max] < candidates[i]) {
                max = i;
            }
        }

        return max;
    }
}