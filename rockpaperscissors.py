"""
file: rockpaperscissors.py
author: Konce Quispe
language: python3
description: interactive rock, paper, scissors game
"""
import random

def play(user_choice):
    """
    A game of rock, paper, scissors. A string representation of the three choices is
    given, and the computer chooses a random choice as well. The two choices are
    compared and either a tie or a winner is declared and printed to the user. Rock
    beats scissors, paper beats rock, and scissors beats paper.
    :paramater user_choice: a string representing either rock, paper, or scissors
    :return: None
    """
    #chooses a random number between 1 and 3
    comp_num = random.randint(0,3)
    #converts number to rock, paper, or scissors choice
    if comp_num == 1:
        comp_choice = "rock"
    elif comp_num == 2:
        comp_choice = "paper"
    else:
        comp_choice = "scissors"
    #prints the computers choice
    print("The computer chose:",comp_choice)

    #if the user and computer both chose the same thing, it's a tie
    if user_choice == comp_choice:
        print("It's a tie!")
    #otherwise, decides who won and prints a message to the user
    elif user_choice == "rock" and comp_choice == "scissors":
        print("Rock beats scissors! You win!")
    elif user_choice == "rock" and comp_choice == "paper":
        print("Paper covers rock! Sorry, the computer wins!")
    elif user_choice == "paper" and comp_choice == "rock":
        print("Paper covers rock! You win!")
    elif user_choice == "paper" and comp_choice == "scissors":
        print("Scissors cut paper! Sorry, the computer wins!")
    elif user_choice == "scissors" and comp_choice == "paper":
        print("Scissors cut paper! You win!")
    elif user_choice == "scissors" and comp_choice == "rock":
        print("Rock beats scissors! Sorry, the computer wins!")

def main():
    """
    Enters a loop and asks the user to enter either rock, paper, or scissors. If the
    user hits enter, the loop exits and the program stops. If the input is invalid,
    an error message is printed and the user can try again. Else, the play() function
    runs and the loop continues.
    """
    end = False
    while end is False:
        user_choice = input("Choose! Type rock, paper, or scissors (hit enter to quit): ")
        if user_choice == "":
            end = True
        elif user_choice != "rock" and user_choice != "paper" and user_choice != "scissors":
            print("Invalid input. Must choose either rock, paper, or scissors.")
            print()
        else:
            play(user_choice)
            print()
    
main()
