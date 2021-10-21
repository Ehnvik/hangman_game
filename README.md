# **Hangman Game**
Hangman game is a Python terminal game which runs in the Code Institute mock terminal on Heroku.

To win game in Hangmang. The user has to guess to correct letters to complete the word. If the user don't complete the word within 7 guesses, then the hangmang guy dies and the game is over. 

[Here is a live version of my project.](https://python-hangman-game.herokuapp.com/)

![hangman-amiresponsive](https://user-images.githubusercontent.com/87748379/138290920-f6823d61-ddc9-43f6-b724-00774194295d.JPG)

## **How to play**
Before the game starts. The player is given a choice between starting the game or exit the game, by typing "yes" or "no". If the player types in "yes", the game starts. If the player types in "no", then the game ends.

If the player choose to start the game. The player then gets assigned a hidden word from the computer. The user also get information that he or she has has 7 lives left to complete the word.

To win the game you have to guess all the correct letters to complete the word. The player loses one life for each wrong guess that has been made. The game ends if the player lose all the 7 lives before completing the word.

![hangman-start](https://user-images.githubusercontent.com/87748379/138297804-0bb5aae9-2ee0-4765-9cb0-dccdad385ccc.JPG)

## **Features**

### **Existing Features**
 * A random word from a list of 440 words are being generated in to the game.
 * The player gets a hint of how long the word is by counting the stripes, where the correct letters later will be placed.
 * Each correct letter is being placed in the correct order of the word.

![hangman-first-letter](https://user-images.githubusercontent.com/87748379/138300193-e75f3d49-5590-4622-b190-677f0f5c899f.JPG)

