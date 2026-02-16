class Pattern2 {
  public static void main(String[] args) {
    int row = 5;
    for (int i = 1; i <= 5; i++) {
      for (int j = 1; j <= row - i; j++) {
        System.out.print(" ");
      }

      for (int j = 1; j <= i; j++) {
        System.out.print(j + "");
      }
      System.out.println();
    }
  }
}

/*
 * 12
 * 123
 * 1234
 * 12345
 */