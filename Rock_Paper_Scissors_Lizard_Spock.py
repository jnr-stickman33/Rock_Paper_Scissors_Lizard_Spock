# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 11:08:13 2019

@author: derick
"""

import random
import time


moves = ["rock", "paper", "scissors", "lizard", "spock"]

def print_pause(text):
    print(text)
    time.sleep(1)


class Player:
    def move(self):
        return "rock"

    moving_larry = None
    robot_move = None

    def learn(self, moving_larry, robot_move):
        self.moving_larry = robot_move
        self.robot_move = moving_larry


def beats(one, two):
    return ((one == "rock" and two == "scissors") or
            (one == "scissors" and two == "paper") or
            (one == "paper" and two == "rock") or
            (one == "lizard" and two == "spock") or
            (one == "spock" and two == "rock") or
            (one == "scissors" and two == "lizard") or
            (one == "lizard" and two == "paper"))



class mr_robot(Player):
    def move(self):
        return random.choice(moves)


class sir_larry(Player):
    def move(self):
        player_input = input("Choose your weapon..!! \n"
                             "Rock, Paper, Scissors, Lizard or Spock.\n")
        if player_input.lower() in moves:
            return player_input.lower()
        else:
            return self.move()


class mimic_player(Player):
    def move(self):
        if self.robot_move is None:
            return random.choice(moves)
        else:
            return self.robot_move


class cycle(Player):
    def move(self):
        moves_index = [["rock", "paper"],
                       ["paper", "scissors"],
                       ["scissors", "rock"]
                       ["lizard","spock"]]
        if self.moving_larry is None:
            return random.choice(moves)
        elif self.moving_larry == moves_index[0][0]:
            return moves_index[0][1]
        elif self.moving_larry == moves_index[1][0]:
            return moves_index[1][1]
        else:
            return moves_index[2][1]


class Game:

    total1 = 0
    total2 = 0

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print_pause(f"You: {move1}  Mr Robot: {move2}")
        if beats(move1, move2) is True:
            print_pause("You Won!!")
            Game.total1 += 1
            print_pause(f"Score: {Game.total1} - {Game.total2}")
        elif move1 == move2:
            print_pause("Tie..!!!")
            print_pause(f"Score: {Game.total1} - {Game.total2}")
        else:
            print_pause("Mr_Robot Won..!!")
            Game.total2 += 1
            print_pause(f"Score: {Game.total1} - {Game.total2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print_pause("Get Ready!")
        for round in range(1,50):
            if Game.total1 == 3 or Game.total2 == 3:
                break
            else:
                print(f"Round {round}:")
                self.play_round()
        if Game.total1 > Game.total2:
            print_pause("You Have Won this Game\n"
                       f"Final Score: {Game.total1} - {Game.total2}")
        else:
            print_pause("Mr Robot Beat You **\n"
                       f"Final Score: {Game.total1} - {Game.total2}")
        print_pause("End of the Game!")


if __name__ == '__main__':
    game = Game(sir_larry(), mimic_player())
    game.play_game()
