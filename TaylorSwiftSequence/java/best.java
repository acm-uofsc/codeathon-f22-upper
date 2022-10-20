
import java.util.Scanner;
public class best {


  static long sol(int n, int M, int K, long[] arr) {

    if (n < M) return n;
    if (arr[n-M] != -1) return arr[n-M];


    long sum = 0;
    for (int i = n-M; i < n; i++) {
      sum += sol(i,M,M,arr);
    }

    arr[n-M] = sum;
    return sum;
  }

  public static void main(String[] args) {
    
    Scanner scanner = new Scanner(System.in);
    int L,M,K;

    String[] params = scanner.nextLine().split(" ");
    L = Integer.parseInt(params[0]);
    M = Integer.parseInt(params[1]);
    K = Integer.parseInt(params[2]);


    //* Create the cache
    long[] cache = new long[K+1];
    //*  Store -1 values as the default
    for (int i = 0; i <= K; i++)  cache[i] = -1;
    

    for (int i = 0; i < L; i++) {
      int n = Integer.parseInt(scanner.nextLine());
      System.out.println(sol(n,M,K,cache));
    }


    scanner.close();
  }
}