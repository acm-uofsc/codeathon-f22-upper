import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner input = new Scanner(System.in);
        int historyCount = input.nextInt();
        int visitorCount = input.nextInt();
    
        int[] history = new int[historyCount];
        // int[] visitors = new int[visitorCount];
        for (int i = 0; i < historyCount; i++) {
            history[i] = input.nextInt();
        }
        for (int i = 0; i < visitorCount; i++) {
            // visitor[i] = input.nextInt();
            int toFind = input.nextInt();
            int greaterThan = binarySearchGreaterThan(history, toFind);
            int greaterThanEqual = binarySearchGreaterThanEqual(history, toFind);
            System.out.println(greaterThan + " " + greaterThanEqual);
        }
    }

    public static int binarySearchGreaterThan(int[] hist, int toSearchFor) {
        //hi should be exclusive upper bound
        int lo = 0;
        int hi = hist.length;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (hist[mid] >= toSearchFor) {
                hi = mid;
            } else if(hist[mid] < toSearchFor) {
                lo = mid + 1;
            }
        }
        return hi;
    }

     public static int binarySearchGreaterThanEqual(int[] hist, int toSearchFor) {
        //hi should be exclusive upper bound
        int lo = 0;
        int hi = hist.length;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (hist[mid] > toSearchFor) {
                hi = mid;
            } else if(hist[mid] <= toSearchFor) {
                lo = mid + 1;
            }
        }
        return hi;
    }
}