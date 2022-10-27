import java.util.HashMap;
import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        int n, m;
        Scanner input = new Scanner(System.in);
        n = input.nextInt();
        m = input.nextInt();
        HashMap<String, Integer> counts = new HashMap<String, Integer>();
        String line;
        input.nextLine();
        for (int i = 0; i < n; i++) {
            line = input.nextLine();
            for (int j = 1; j < line.length() + 1; j++) {
                String sub  = line.substring(0, j);
                counts.putIfAbsent(sub,0);
                counts.put(sub, counts.get(sub) + 1);
            }
        }
        input.nextLine();

        for (int i = 0; i < m; i++) {
            line = input.nextLine();
            int total = 0;
            for (int j = 1; j < line.length() + 1; j++) {
                String sub = line.substring(0, j);
//                System.err.println(sub);
                if(counts.containsKey(sub))
                {
                    total += counts.get(sub);
                }
                else {
                    break;
                }

            }
            System.out.println(total);

        }

    }
}
