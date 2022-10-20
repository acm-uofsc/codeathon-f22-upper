
import java.util.Scanner;
public class bad {


  static long sol(int n, int M, int K) {

    if (n < M) return n;

    long sum = 0;
    for (int i = n-M; i < n; i++) {
      sum += sol(i,M,M);
    }

    return sum;
  }

  public static void main(String[] args) {
    
    Scanner scanner = new Scanner(System.in);
    int L,M,K;

    String[] params = scanner.nextLine().split(" ");
    L = Integer.parseInt(params[0]);
    M = Integer.parseInt(params[1]);
    K = Integer.parseInt(params[2]);




    for (int i = 0; i < L; i++) {
      int n = Integer.parseInt(scanner.nextLine());
      System.out.println(sol(n,M,K));
    }


    scanner.close();
  }
}