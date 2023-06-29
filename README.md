# WordleSolver

Wordle is a game that gives a player 6 chances to guess a 5 letter word. Every time you guess a word, the game gives you feedback based on each letter. If the letter turns **green**, that means that the letter is in the correct position. If the letter is **yellow**, this letter exists in the word, but not at that index. If the letter is **grey**, that letter does not belong in the correct answer.

Many players seem to struggle 2-3 guesses into the game as they can't find _"a word that starts with D, ends in an R, and has an N somewhere".___

This is where WorldSolver aims to help individuals. Users can input a word they guessed and the script with return possible 5-letter words given the conditions. It also stores all previous information regarding the guesses, to keep track of grey letters(across all guesses entered, it will not return any words that contain all the grey letters provided), yellow letters and their previous positions, and all the green letters.


