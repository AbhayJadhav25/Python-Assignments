#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <ctype.h>
#include <windows.h>

#define MAX_WORDS 20
#define MAX_LEN 100

typedef struct {
    char word[MAX_LEN];
    char hint[MAX_LEN];
} WordHint;

// Function to trim newline characters
void trimNewline(char *str) {
    str[strcspn(str, "\r\n")] = '\0';
}

// Function to load words and hints from file
int loadWords(const char *filename, WordHint words[], int maxWords) {
    FILE *file = fopen(filename, "r");
    if (!file) {
        printf("Failed to open %s\n", filename);
        return 0;
    }

    int count = 0;
    char line[MAX_LEN * 2];
    while (fgets(line, sizeof(line), file) && count < maxWords) {
        trimNewline(line);
        char *token = strtok(line, ":");
        if (token) {
            strcpy(words[count].word, token);
            token = strtok(NULL, ":");
            if (token) {
                strcpy(words[count].hint, token);
                count++;
            }
        }
    }

    fclose(file);
    return count;
}

// Function to play the hangman game
void hangmanGame() {
    WordHint words[MAX_WORDS];
    int wordCount = loadWords("words.txt", words, MAX_WORDS);

    if (wordCount == 0) {
        printf("No words found. Please check your words.txt file.\n");
        return;
    }

    srand(time(NULL));
    int index = rand() % wordCount;

    char *word = words[index].word;
    char *hint = words[index].hint;
    int len = strlen(word);
    int attempts = 5;
    int correctGuesses = 0;

    int guessed[26] = {0}; // To track guessed letters
    char displayWord[MAX_LEN];

    for (int i = 0; i < len; i++) {
        displayWord[i] = '_';
    }
    displayWord[len] = '\0';

    printf("\n========= HANGMAN GAME =========\n");
    printf("Hint: %s\n", hint);

    while (attempts > 0 && correctGuesses < len) {
        printf("\nWord: ");
        for (int i = 0; i < len; i++) {
            printf("%c ", displayWord[i]);
        }

        printf("\nAttempts left: %d", attempts);
        printf("\nGuessed letters: ");
        for (int i = 0; i < 26; i++) {
            if (guessed[i]) {
                printf("%c ", 'a' + i);
            }
        }

        printf("\nEnter a letter: ");
        char guess;
        scanf(" %c", &guess);
        guess = tolower(guess);

        if (!isalpha(guess)) {
            printf("Please enter a valid letter.\n");
            continue;
        }

        if (guessed[guess - 'a']) {
            printf("You already guessed '%c'. Try another letter.\n", guess);
            continue;
        }

        guessed[guess - 'a'] = 1;

        int found = 0;
        for (int i = 0; i < len; i++) {
            if (tolower(word[i]) == guess && displayWord[i] == '_') {
                displayWord[i] = word[i];
                correctGuesses++;
                found = 1;
            }
        }

        if (found) {
            printf("Good guess!\n");
        } else {
            printf("Wrong guess!\n");
            attempts--;
        }

        Sleep(500); // 0.5-second pause for better experience
    }

    if (correctGuesses == len) {
        printf("\n🎉 Congratulations! You guessed the word: %s\n", word);
    } else {
        printf("\n💀 Game Over! The correct word was: %s\n", word);
    }
}

int main() {
    int playAgain;
    do {
        hangmanGame();
        printf("\nDo you want to play again? (1 = Yes, 0 = No): ");
        scanf("%d", &playAgain);
    } while (playAgain == 1);

    printf("Thanks for playing!\n");
    return 0;
}
