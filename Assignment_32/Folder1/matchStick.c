#include <stdio.h>
int main()
{
  int sticks = 20, pick;
  int player1 = 1;
  int player2 = 2;
  int turn = player1;

  printf("Welcome to the Matchstick Game :\n");
  printf("Notes :\n");
  printf("1. There are 20 matchsticks in total.\n");
  printf("2. Each player must pick between 1 and 4 sticks on their turn.\n");
  printf("3. The player forced to pick the LAST stick will LOSE.\n");
  printf("4. Player 1 starts first.\n\n");

  while (sticks > 1)
  {
    printf("\nSticks: ");
    for (int i = 0; i < sticks; i++)
    {
      printf("| ");
    }
    printf("  (%d remaining)\n", sticks);

    if (turn == player1)
    {
      printf("Player 1, enter number of sticks (1-4): ");
    }
    else
    {
      printf("Player 2, enter number of sticks (1-4): ");
    }

    scanf("%d", &pick);

    if (pick < 1 || pick > 4)
    {
      printf("Invalid input! You must pick between 1 and 4 sticks.\n");
      continue;
    }
    if (pick > sticks)
    {
      printf("Invalid input! You cannot pick more than remaining sticks.\n");
      continue;
    }

    sticks = sticks - pick;

    if (turn == player1)
    {
      turn = player2;
    }
    else
    {
      turn = player1;
    }
  }

  printf("\nSticks: |  (1 remaining)\n");

  if (turn == player1)
  {
    printf("Player 1 is forced to pick the last stick.\n");
    printf("Player 2 Wins!\n");
  }
  else
  {
    printf("Player 2 is forced to pick the last stick.\n");
    printf("Player 1 Wins!\n");
  }

  return 0;
}