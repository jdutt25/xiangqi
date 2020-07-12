# xiangqi
Abstract game of Xiangqi in Python 

Follows the rules from the Xiangqi Wikipedia Page (https://en.wikipedia.org/wiki/Xiangqi), with the exception of chasing and perpetual check. Red's turn is first. 

 Here's an example of how to make a move:
 game = XiangqiGame()
 game.make_move("a4", "a5") #move from, move to
 
 To check whose turn it is:
 game.get_turn()
 
 To check the game state (which is RED_WON, BLACK_WON, or UNFINISHED):
 game.get_game_state()
