# **Hangman Game**
Hangman Game is a Python terminal game which runs in the Code Institute mock terminal on Heroku.

To win the Hangman Game. The user has to guess the correct letters to complete the word. If the user don't complete the word within 7 guesses, then the hangmang guy dies and the game is over. 

[Here is a live version of my project.](https://python-hangman-game.herokuapp.com/)

![hangman-amiresponsive](https://user-images.githubusercontent.com/87748379/138290920-f6823d61-ddc9-43f6-b724-00774194295d.JPG)

## **How To Play**
Before the game starts. The player is given a choice between starting the game or exit the game by typing "yes" or "no". If the player types in "yes" the game starts. If the player types in "no" the game ends.

If the player choose to start the game. The player then gets assigned a hidden word from the computer. The user gets information that he or she has 7 lives left to complete the word.

To win the game you have to guess all the correct letters to complete the word. The player lose one life for each wrong guess that has been made. The game ends if the player lose all the 7 lives before completing the word.

![hangman-start](https://user-images.githubusercontent.com/87748379/138297804-0bb5aae9-2ee0-4765-9cb0-dccdad385ccc.JPG)

## **Features**

### **Existing Features**
 * A random word from a list of 440 words are being generated into the game.
 * The player gets a hint of how long the word is by counting the lines were the correct letters later will be placed.
 * Each correct letter is being placed in the correct order of the word.

![hangman-first-letter](https://user-images.githubusercontent.com/87748379/138300193-e75f3d49-5590-4622-b190-677f0f5c899f.JPG)

* Accept user input.
* Maintains how many lives the player has left.
* Maintains which letters the player have guessed.
* Responds "Wrong!" if the player guesses the wrong letter.
* A hanging man viusalize how many guesses left before the game ends.

![hangman-second-part](https://user-images.githubusercontent.com/87748379/138318672-51217fd6-d971-4f32-9443-1ba13e3e24c9.JPG)

* Input validation and error-checking.
  * You can only enter letters. Not other characters.
  * You cannot enter the same guess twice.

![hangman-input-validation](https://user-images.githubusercontent.com/87748379/138312495-aec4da98-6a4a-471a-9223-d495d21feed6.JPG)

### **Future Features**
* Allow players to also guess the word directly instead of each letter.
* Add a scoreboard of the best players.

## **Testing**

 I have manually tested this project by doing the following:

 * Passed the code through pep8online without any bugs.
 * Given invalid inputs when playing the game. For examples numbers and other characters. 
 * Tested in my local terminal and the Code Institute Heroku Terminal.

 ![pep8-test](https://user-images.githubusercontent.com/87748379/138331958-e30b49a4-074b-4a4c-a2bc-4b249caf9650.JPG)

### **Bugs**

**Solved Bugs**
* When I tested the game I found out that it did not have a return value at the end of the game. So everytime the game ended "None" got printed on the screen. 
* I fixed this bug by calling the start_game() function again.

![hangman-fixed-bug](https://user-images.githubusercontent.com/87748379/138333901-1f7c70ca-fe19-4d0c-be51-8a57dca65ec2.JPG)

### **Remaining  Bugs**

* No bugs remaining.

### **Validator Testing**

* No errors were returned when testing all three files.

![pep8-test](https://user-images.githubusercontent.com/87748379/138331958-e30b49a4-074b-4a4c-a2bc-4b249caf9650.JPG)
![pep8-test2](https://user-images.githubusercontent.com/87748379/138335206-1685c2e5-d478-4b67-b723-c60fe5926698.JPG)
![pep8-test3](https://user-images.githubusercontent.com/87748379/138335287-03284427-21fe-4b7a-a290-171cdc3b9da3.JPG)

## **Deployment**
This project was deployed using Code Institute's mock terminal for Heroku.

* Steps for deployment:
  * Clone this repository.
  * Create an account and a new app on Heroku.
  * Configure vars with "KEY" in port and "8000" as value.
  * Set the buildpacks to python and nodeJS in that order.
  * Connect Heroku to Github.
  * Connect and deploy the repository.

## **Credits**

* Tom on stackoverlow.com.
* Tutor support on Code Institute.
* FreeCodeCamp.org with this video: https://www.youtube.com/watch?v=8ext9G7xspg
* Kite with this video: https://www.youtube.com/watch?v=m4nEnsavl6w

