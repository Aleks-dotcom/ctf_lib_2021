#include <stdio.h>
#include <stdlib.h>


int main(){
	char c = 'F';
		char guess[256];
			guess[0] = c;
			int guessLen = read(0, guess+1, 255)+1; //add to already entered char
			guess[guessLen-1] = 0; //remove newline
			char flag[32];
			FILE *f = fopen("flag.txt", "rb");
			int r = fread(flag, 1, 32, f);
			flag[r] = 0; //null terminate
			if (strncmp(guess, flag, strlen(flag))) {
				char wrong[strlen(guess)+35];
				wrong[0] = 0; //string is empty intially
				strncat(wrong, guess, guessLen);
				strncat(wrong, " was wrong. Better luck next time!\n", 35);
				write(1, wrong, guessLen+35);
				exit(0);
			}
		 else{
			char wrong[64] = "_ was wrong. What you wanted was _!\n";
			wrong[0] = c; //user inputted char
			wrong[strlen(wrong)-3] = "TEST"; //correct char
			write(1, wrong, strlen(wrong));
			getchar(); //so there's no leftover newline
			exit(0);
		}

	return 0;
}



