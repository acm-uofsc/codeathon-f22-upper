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
            int curVisitor = input.nextInt();
            int greaterThan = 0;
            int greaterThanEqual = 0;
            for (int j = 0; j < historyCount; j++) {
                if (curVisitor > history[j])
                    greaterThan += 1;
                if (curVisitor >= history[j])
                    greaterThanEqual += 1;
                else
                    break;
            }
                
            System.out.println(greaterThan + " " + greaterThanEqual);
        }
    }
}