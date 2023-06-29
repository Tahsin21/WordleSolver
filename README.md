# WordleSolver

Wordle is a game that gives a player 6 chances to guess a 5 letter word. Every time you guess a word, the game gives you feedback based on each letter. If the letter turns **green**, that means that the letter is in the correct position. If the letter is **yellow**, this letter exists in the word, but not at that index. If the letter is **grey**, that letter does not belong in the correct answer.

Many players seem to struggle 2-3 guesses into the game as they can't find _"a word that starts with D, ends in an R, and has an N somewhere"_.

This is where WorldSolver aims to help individuals. Users can input a word they guessed and the script with return possible 5-letter words given the conditions. It also stores all previous information regarding the guesses, to keep track of grey letters(across all guesses entered, it will not return any words that contain all the grey letters provided), yellow letters and their previous positions, and all the green letters.

<img width="100" alt="image" src="https://github.com/Tahsin21/WordleSolver/assets/22527648/8ceebbc1-59c9-484d-bd31-17a22a039c5a">

_In this scenario, the word "races" was guessed initially, which provided the feedback of **yellow,grey,grey,green,grey**. We can then take this information and input it into the script._

<img width="100" alt="image" src="https://github.com/Tahsin21/WordleSolver/assets/22527648/f87885f6-77fb-4c6b-a3e0-356b35686d0d">

_Based on the feedback of a word that has an _E_ index 4 and contains an _R_ , these are the possible solutions based on a filter created by going through every 5-letter word in the English Dictionary._

The next step would be to take a word from this list and continue the process

<img width="100" alt="image" src="https://github.com/Tahsin21/WordleSolver/assets/22527648/954d6008-49d3-425c-ab1e-a8f1d2e1df91">

_With a guess in 'Defer', the game gave us feedback with **green,grey,grey,green,green**._

Inserting that into the script, we are given a more refined set of possible words.

<img width="100" alt="image" src="https://github.com/Tahsin21/WordleSolver/assets/22527648/5f2b70c5-693d-4f76-adf7-a40e90c56753">

<img width="100" alt="image" src="https://github.com/Tahsin21/WordleSolver/assets/22527648/4a71b694-da4f-4aef-8982-20790ac5ca0f">

_The process continues until the correct word is found_








