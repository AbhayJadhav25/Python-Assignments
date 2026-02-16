public class Pattern4 {
  public static void main(String[] args) {
    int row = 5;
    for (int i = 5; i >= 1; i--) {
      for (int j = 1; j < i; j++) {
        System.out.print(" ");
      }
      for (int j = 5; j >= i; j--) {
        System.out.print(j);
      }
      System.out.println();
    }
  }
}
/*
 * 
 *  5
   54
  543
 5432
54321
 */