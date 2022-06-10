# This code come from : https://replit.com/@aaron_bernath/PythonTicTacToeApp#main.py
import random
class TicTacToe:
    def __init__(self):
        self.board = ["-","-","-",
                      "-","-","-",
                      "-","-","-"]
        self.game_still_going = True
        self.winner = None
        self.current_player = "X"
        self.humancounter = 0
        self.humanchoices = []
        self.aicounter = 0
        self.aichoices = []

    # Display the game board to the screen
    def display_board(self):
        print("\n")
        print(self.board[0] + " | "+ self.board[1] + " | "+ self.board[2]+ "      1 | 2 | 3")
        print(self.board[3] + " | "+ self.board[4] + " | "+ self.board[5]+ "      4 | 5 | 6")
        print(self.board[6] + " | "+ self.board[7] + " | "+ self.board[8]+ "      7 | 8 | 9")
        print("\n")

    # Handle a turn for an arbitrary player
    def handle_turn(self, player):

        print(player + "'s turn.")
        position = input("Choose a position from 1-9: ")

        # make sure the user input is valid
        valid = False
        while not valid:

            while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                position = input("Choose a position from 1-9: ")

            # Get correct index in our board list
            position = int(position) - 1

            if self.board[position] == "-":
                valid = True
            else:
                print("You can't go there. Go again.")

        # Put the game piece on the board
        self.board[position] = player

        # Show the game board again
        self.display_board()
        self.humancounter += 1
        self.humanchoices.append(str(position + 1))

    def check_rows(self):
        # Check if any of the rows have all the same value (and is not empty)
        row_1 = self.board[0] == self.board[1] == self.board[2] != "-"
        row_2 = self.board[3] == self.board[4] == self.board[5] != "-"
        row_3 = self.board[6] == self.board[7] == self.board[8] != "-"
        if row_1 or row_2 or row_3:
            self.game_still_going = False
        # Return the winner
        if row_1:
            return self.board[0]
        elif row_2:
            return self.board[3]
        elif row_3:
            return self.board[6]
        else:
            return None

    def check_columns(self):
        column_1 = self.board[0] == self.board[3] == self.board[6] != "-"
        column_2 = self.board[1] == self.board[4] == self.board[7] != "-"
        column_3 = self.board[2] == self.board[5] == self.board[8] != "-"
        if column_1 or column_2 or column_3:
            self.game_still_going = False
        if column_1:
            return self.board[0]
        elif column_2:
            return self.board[1]
        elif column_3:
            return self.board[2]
        else:
            return None

    def check_diagonals(self):
        diagonal_1 = self.board[0] == self.board[4] == self.board[8] != "-"
        diagonal_2 = self.board[2] == self.board[4] == self.board[6] != "-"

        if diagonal_1 or diagonal_2:
            self.game_still_going = False
        if diagonal_1:
            return self.board[4]
        elif diagonal_2:
            return self.board[4]
        else:
            return None

    # check if there a tie
    def check_for_tie(self):
        if "-" not in self.board:
            self.game_still_going = False
        else:
            return True

    # Change player from X to O, or O to X
    def flip_player(self):
        if self.current_player == "X":
            self.current_player = "O"
        else:
            self.current_player = "X"

    def check_for_winner(self):
        row_winner = self.check_rows()
        column_winner = self.check_columns()
        diagonal_winner = self.check_diagonals()
        # Get the winner
        if row_winner:
            self.winner = row_winner
        elif column_winner:
            self.winner = column_winner
        elif diagonal_winner:
            self.winner = diagonal_winner
        else:
            self.winner = None

    def check_if_game_over(self):
        self.check_for_winner()
        self.check_for_tie()

    def play_game(self):

        # Show the initial game board
        self.display_board()

        while self.game_still_going:
            self.handle_turn(self.current_player)
            # check if game over
            self.check_if_game_over()

            #Flip to the other player
            self.flip_player()

        # Since the game is over, print the winner or tie
        if self.winner == "X" or self.winner == "O":
            print(self.winner + "won.")
        else:
            print("Tie.")

    def aiPlay2(self):
        """
        ai play last
        """
        player = "O"
        places = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        # make sure the user input is valid
        valid = False
        while not valid:
            if self.aicounter == 0:
                if self.humanchoices[0] != "5":
                    position = "5"
                else:
                    position = random.choice(places)
            else:#if self.aicounter == 1:
                if {"1", "5"}.issubset(self.humanchoices) and self.board[8] == "-":
                    position = "9"
                elif {"2", "5"}.issubset(self.humanchoices) and self.board[7] == "-":
                    position = "8"
                elif {"3", "5"}.issubset(self.humanchoices) and self.board[6] == "-":
                    position = "7"
                elif {"4", "5"}.issubset(self.humanchoices) and self.board[5] == "-":
                    position = "6"
                elif {"6", "5"}.issubset(self.humanchoices) and self.board[3] == "-":
                    position = "4"
                elif {"7", "5"}.issubset(self.humanchoices) and self.board[2] == "-":
                    position = "3"
                elif {"8", "5"}.issubset(self.humanchoices) and self.board[1] == "-":
                    position = "2"
                elif {"9", "5"}.issubset(self.humanchoices) and self.board[0] == "-":
                    position = "1"
                elif {"1", "2"}.issubset(self.humanchoices) and self.board[2] == "-":
                    position = "3"
                elif {"1", "3"}.issubset(self.humanchoices) and self.board[1] == "-":
                    position = "2"
                elif {"1", "4"}.issubset(self.humanchoices) and self.board[6] == "-":
                    position = "7"
                elif {"1", "7"}.issubset(self.humanchoices) and self.board[3] == "-":
                    position = "4"
                elif {"2", "3"}.issubset(self.humanchoices) and self.board[0] == "-":
                    position = "1"
                elif {"2", "8"}.issubset(self.humanchoices) and self.board[4] == "-":
                    position = "5"
                elif {"3", "6"}.issubset(self.humanchoices) and self.board[8] == "-":
                    position = "9"
                elif {"3", "9"}.issubset(self.humanchoices) and self.board[5] == "-":
                    position = "6"
                elif {"3", "7"}.issubset(self.humanchoices) and self.board[4] == "-":
                    position = "5"
                elif {"4", "6"}.issubset(self.humanchoices) and self.board[4] == "-":
                    position = "5"
                elif {"4", "7"}.issubset(self.humanchoices) and self.board[0] == "-":
                    position = "1"
                elif {"6", "9"}.issubset(self.humanchoices) and self.board[2] == "-":
                    position = "3"
                elif {"7", "8"}.issubset(self.humanchoices) and self.board[8] == "-":
                    position = "9"
                elif {"7", "9"}.issubset(self.humanchoices) and self.board[7] == "-":
                    position = "8"
                elif {"8", "9"}.issubset(self.humanchoices) and self.board[6] == "-":
                    position = "7"
                else:
                    position = random.choice(places)

            # Get correct index in our board list
            position = int(position) - 1

            if self.board[position] == "-":
                valid = True
            else:
                pass

        # Put the game piece on the board
        self.board[position] = player

        # Show the game board again
        self.display_board()
        self.aicounter +=  1
        self.aichoices.append(str(position + 1))

    def aiPlay(self):
        """
        ai play first
        """
        player = "X"
        places = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        # make sure the user input is valid
        valid = False
        while not valid:
            if self.aicounter == 0:
                position = "5"
            elif self.aicounter == 1:
                position = random.choice(places)
            else:
                if {"1", "5"}.issubset(self.humanchoices) and self.board[8] == "-":
                    position = "9"
                elif {"2", "5"}.issubset(self.humanchoices) and self.board[7] == "-":
                    position = "8"
                elif {"3", "5"}.issubset(self.humanchoices) and self.board[6] == "-":
                    position = "7"
                elif {"4", "5"}.issubset(self.humanchoices) and self.board[5] == "-":
                    position = "6"
                elif {"6", "5"}.issubset(self.humanchoices) and self.board[3] == "-":
                    position = "4"
                elif {"7", "5"}.issubset(self.humanchoices) and self.board[2] == "-":
                    position = "3"
                elif {"8", "5"}.issubset(self.humanchoices) and self.board[1] == "-":
                    position = "2"
                elif {"9", "5"}.issubset(self.humanchoices) and self.board[0] == "-":
                    position = "1"
                elif {"1", "2"}.issubset(self.humanchoices) and self.board[2] == "-":
                    position = "3"
                elif {"1", "3"}.issubset(self.humanchoices) and self.board[1] == "-":
                    position = "2"
                elif {"1", "4"}.issubset(self.humanchoices) and self.board[6] == "-":
                    position = "7"
                elif {"1", "7"}.issubset(self.humanchoices) and self.board[3] == "-":
                    position = "4"
                elif {"2", "3"}.issubset(self.humanchoices) and self.board[0] == "-":
                    position = "1"
                elif {"2", "8"}.issubset(self.humanchoices) and self.board[4] == "-":
                    position = "5"
                elif {"3", "6"}.issubset(self.humanchoices) and self.board[8] == "-":
                    position = "9"
                elif {"3", "9"}.issubset(self.humanchoices) and self.board[5] == "-":
                    position = "6"
                elif {"3", "7"}.issubset(self.humanchoices) and self.board[4] == "-":
                    position = "5"
                elif {"4", "6"}.issubset(self.humanchoices) and self.board[4] == "-":
                    position = "5"
                elif {"4", "7"}.issubset(self.humanchoices) and self.board[0] == "-":
                    position = "1"
                elif {"6", "9"}.issubset(self.humanchoices) and self.board[2] == "-":
                    position = "3"
                elif {"7", "8"}.issubset(self.humanchoices) and self.board[8] == "-":
                    position = "9"
                elif {"7", "9"}.issubset(self.humanchoices) and self.board[7] == "-":
                    position = "8"
                elif {"8", "9"}.issubset(self.humanchoices) and self.board[6] == "-":
                    position = "7"
                else:
                    position = random.choice(places)

            # Get correct index in our board list
            position = int(position) - 1

            if self.board[position] == "-":
                valid = True
            else:
                pass

        # Put the game piece on the board
        self.board[position] = player

        # Show the game board again
        self.display_board()
        self.aicounter +=  1
        self.aichoices.append(str(position + 1))

    def play_game_ai(self):

        # Show the initial game board
        self.display_board()

        while self.game_still_going:
            #print("human chouce", self.humanchoices)
            if self.current_player == "X":
                self.handle_turn(self.current_player)
            else:
                self.aiPlay2()
            # check if game over
            self.check_if_game_over()

            #Flip to the other player
            self.flip_player()

        # Since the game is over, print the winner or tie
        if self.winner == "X" or self.winner == "O":
            print(self.winner + "won.")
        else:
            print("Tie.")

    def play_game_ai2(self):

        # Show the initial game board
        # self.display_board()

        while self.game_still_going:
            #print("human chouce", self.humanchoices)
            if self.current_player == "X":
                self.aiPlay()
            else:
                self.handle_turn(self.current_player)

            # check if game over
            self.check_if_game_over()

            #Flip to the other player
            self.flip_player()

        # Since the game is over, print the winner or tie
        if self.winner == "X" or self.winner == "O":
            print(self.winner + "won.")
        else:
            print("Tie.")

tic_tac_toe = TicTacToe()
# tic_tac_toe.play_game_ai2()

playgame = True
while playgame != "no":
    tic_tac_toe.__init__()
    print("You go First\n")
    tic_tac_toe.play_game_ai()
    tic_tac_toe.__init__()
    print("You are Backhand")
    tic_tac_toe.play_game_ai2()
    playgame = input("Press 'no' to end the game: ")

