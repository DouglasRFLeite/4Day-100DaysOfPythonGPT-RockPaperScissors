# 4Day-100DaysOfPythonGPT-RockPaperScissors
Day 4 of the [100 Days of Code with Python Bootcamp](https://www.udemy.com/course/100-days-of-code/) from Udemy.

## What is 100DaysOfPythonGPT?

100 Days of Python is a Python Bootcamp from Udemy that provides 100 days of Python pratical content with lessons and projects. The GPT part is something I'm adding to the course and infers that I shall use ChatGPT's engine and/or API in some way on each and every one of those 100 projects. Furthermore, I shall also practice using PyTest to test these projects and applications at least in some level.

## RockPaperScissors

Rock Paper Scissors is the fourth project of the fourthday of the bootcamp. Its original purpose is to use Lists and the Random module.

As the name says, it is a game of Rock, Paper and Scissors, where the player/user chooses one of the three and the computer chooses one at random. If-else statements (choosen not for eficiency but for clarity) determine the winner.

ChatGPT's API was used to substitute the if-else decision and also to generate the winning tiying or losing message printed on the console afterwards.

Testing was possible but I genuinely skiped it due to lack of time.

## Project Structure

 - [src/](src/) - The `rock_paper_scissors.py` file holds the basic game as suggested by the bootamp, whilst `rock_paper_scissors_gpt.py` has the code for the game with the AI message-generation function declared in `message_gpt.py`;
 - [include/](include/) - The `gpt.py` file holds the `get_completion` function that accesses the ChatGPT API. 
