

'''
https://www.geeksforgeeks.org/snake-ladder-problem-2/
Given a snake and ladder board, find the minimum number of dice throws required to reach the destination or last cell from source or 1st cell.


The idea is to consider the given snake and ladder board as a directed graph with number of vertices equal to the number of cells in the board. The problem reduces to finding the shortest path in a graph. Every vertex of the graph has an edge to next six vertices if next 6 vertices do not have a snake or ladder. If any of the next six vertices has a snake or ladder, then the edge from current vertex goes to the top of the ladder or tail of the snake. Since all edges are of equal weight, we can efficiently find shortest path using Breadth First Search of the graph.

An entry in queue used in BFS
class QueueEntry(object):
    def __init__(self, v = 0, dist = 0):
        self.v = v
        self.dist = dist

This function returns minimum number of
dice throws required to. Reach last cell
from 0'th cell in a snake and ladder game.
move[] is an array of size N where N is
no. of cells on board. If there is no
snake or ladder from cell i, then move[i]
is -1. Otherwise move[i] contains cell to
which snake or ladder at i takes to.

def getMinDiceThrows(move, N):

    # The graph has N vertices. Mark all
    # the vertices as not visited
    visited = [False] * N

    # Create a queue for BFS
    queue = []

    # Mark the node 0 as visited and enqueue it
    visited[0] = True

    # Distance of 0't vertex is also 0
    # Enqueue 0'th vertex
    queue.append(QueueEntry(0, 0))

    # Do a BFS starting from vertex at index 0
    qe = QueueEntry() # A queue entry (qe)
    while queue:
        qe = queue.pop(0)
        v = qe.v # Vertex no. of queue entry

        # If front vertex is the destination
        # vertex, we are done
        if v == N - 1:
            break

        # Otherwise dequeue the front vertex
        # and enqueue its adjacent vertices
        # (or cell numbers reachable through
        # a dice throw)
        j = v + 1
        while j <= v + 6 and j < N:

            # If this cell is already visited,
            # then ignore
            if visited[j] is False:

                # Otherwise calculate its
                # distance and mark it
                # as visited
                a = QueueEntry()
                a.dist = qe.dist + 1
                visited[j] = True

                # Check if there a snake or ladder
                # at 'j' then tail of snake or top
                # of ladder become the adjacent of 'i'
                a.v = move[j] if move[j] != -1 else j

                queue.append(a)

            j += 1

    # We reach here when 'qe' has last vertex
    # return the distance of vertex in 'qe
    return qe.dist

# driver code
N = 30
moves = [-1] * N

# Ladders
moves[2] = 21
moves[4] = 7
moves[10] = 25
moves[19] = 28

# Snakes
moves[26] = 0
moves[20] = 8
moves[16] = 3
moves[18] = 6

print("Min Dice throws required is {0}".
       format(getMinDiceThrows(moves, N)))

'''



'''
Algorithm for snakes and Ladders game in python
	1)There are two players and they are given a dice
	2)Typically the game board has 100 cells starting from 1 to 100
	3)There are snakes and ladders in different cells. And each has either a ladder or a snake or nothing but not both snake and ladder in the same cell.
	4)I use two python dictionaries namely 'snakes' and 'ladders' to declare the positions of snakes and ladders.
	5)I make starting cell number of snake or ladder as 'key' and ending cell number as 'value' of the dictionary.
	6)Define a function to roll the dice i.e., accepting the input from Player1 and Player2 with a checking condition of dice number to be between 1 & 6.
	7)Define a function to check if Player1 or Player2 found ladder or a snake mouth.
	8)Check for the 'key's in both dictionaries & proceed accordingly.
	9)The rolling of dice continues until any of the player reaches above 99, if any of the players reach 100 they will be declared as winner of the game.
'''

from random import randint

class Player:
    def __init__(self, name):
        self._name = name
        self._position = 1

    @property
    def name(self):
        return self._name

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, position):
        self._position = position


class Game:
    BOARD_SIZE = 101
    def __init__(self, players):
        self.players = players
        self.turn = 0
        self.board = [0]*Game.BOARD_SIZE
        self.winner = None

    @property
    def player_count(self):
        return len(self.players)

    def add_ladder(self, on, to):
        if to < 0:
            raise TypeError('to must be greater than 0')
        self.board[on] = to

    def add_snake(self, on, to):
        if to > 0:
            raise TypeError('to must be less than 0')
        self.board[on] = to

    def roll_dice(self, player=None):
        if self.winner:
            print 'game finished player %s won' % player.name
            return

        dice = randint(1, 6)
        print 'dice rolled', dice

        player = player or self.get_player_turn()
        player.position += dice

        if player.position >= Game.BOARD_SIZE:
            self.winner = player
            print(player.name, ' wins')
            return
        player.position +=  self.board[player.position]
        if dice == 6:
            print(player.name, 'turn again')
            self.roll_dice(player)
        self.print_positions_of_players()

    def print_positions_of_players(self):
        for player in self.players:
            print '%s position: %s' % (player.name, player.position)

    def get_player_turn(self):
        player = self.players[self.turn]
        self.turn += 1
        if self.turn >= self.player_count:
            self.turn = 0
        return player


p1 = Player('ekluv')
p2 = Player('singh')

game = Game([p1, p2])
game.roll_dice()
game.roll_dice()
game.roll_dice()
game.roll_dice()


'''
https://codereview.stackexchange.com/questions/176586/snakes-and-ladders-game

def setup_game():
    players=6
    while True:
        try:
            print("How many players are in the game?")
            players = int(input())
            if players > 4 or players < 2:
                print("Must be less than 5 and greater than 1")
            else:
                break
        except ValueError:
            print("Must be a number")

    names = {}
    for i in range(1,players+1):
        while True:
            name = input("What is the name of Player {}? ".format(i))
            if not name in names:
                names[name] = 0
                break
            else:
                print('Cannot have duplicate names')
    return names

def move_player(player, current_pos):
    snake_squares = {16: 4, 33: 20, 48: 24, 62: 56, 78: 69, 94: 16}
    ladder_squares = {3: 12, 7: 23, 20: 56, 47: 53, 60: 72, 80: 94}

    throw = roll_dice()
    next_pos = current_pos + throw
    print("{0} rolled a {1} and is now on {2}".format(player, throw, next_pos))

    if next_pos in snake_squares:
        print("Player got bitten by a snake and is now on square {}".format(snake_squares[next_pos]))
        next_pos = snake_squares[next_pos]
    elif next_pos in ladder_squares:
        print("Player climbed a ladder and is now on square {}".format(ladder_squares[next_pos]))
        next_pos = ladder_squares[next_pos]
    return next_pos

def game(players):
    print("{}, Welcome To Snakes And Ladders".format(" ".join(players)))
    input("Press Enter")
    while True:

        # Foreach player
        for player, current_pos in players.items():

            # Move player
            players[player] = move_player(player, current_pos)

            # Check win
            if players[player] > 100:
                return player

            # Next player
            input("Press Enter")


if __name__ == "__main__":
    players = setup_game()
    winner = game(players)
    print("Player {} won the game".format(winner))

'''


'''
https://www.careercup.com/question?id=9605945


An Linear Array can be used to represent the Snake and Ladder Game. Each index will tell us the position we have rolled dice for. say board.

and board[i]=i

Representing Snake & Ladder.
Say there is snake from which takes us from 10 to 3 then

board[10]=3
similarly for Ladders.

Throw of Dice

The throw of dice can be implemented by a function returning a random number between 1 and 6.

Game of Play.
we get evaluate the player position by checking the position the player has rolled for in the board i.e. say i am at 10 and by throw of dice returns 3 so I will check board[13] and the value will be final position.




Algorithm for snakes and Ladders game in python
	1)There are two players and they are given a dice
	2)Typically the game board has 100 cells starting from 1 to 100
	3)There are snakes and ladders in different cells. And each has either a ladder or a snake or nothing but not both snake and ladder in the same cell.
	4)I use two python dictionaries namely 'snakes' and 'ladders' to declare the positions of snakes and ladders.
	5)I make starting cell number of snake or ladder as 'key' and ending cell number as 'value' of the dictionary.
	6)Define a function to roll the dice i.e., accepting the input from Player1 and Player2 with a checking condition of dice number to be between 1 & 6.
	7)Define a function to check if Player1 or Player2 found ladder or a snake mouth.
	8)Check for the 'key's in both dictionaries & proceed accordingly.
	9)The rolling of dice continues until any of the player reaches above 99, if any of the players reach 100 they will be declared as winner of the game.

import java.util.HashMap;
import java.util.Map;
import java.util.Random;
import java.util.Scanner;

public class GameBoard {

	private static Scanner scanner = new Scanner(System.in);
	private static Random random = new Random();
	private static int noOfPlayers;
	private static Map<Integer, Integer> ladderPositionMap = new HashMap<>();
	private static Map<Integer, Integer> snakePositionMap = new HashMap<>();
	private static Map<Integer, Player> playerMap = new HashMap<>();

	public static void main(String[] args) {

		constructSnakePostion();
		constructLadderPostion();
		noOfPlayers = setUpNoOfPlayers();
		playGame();

	}

	private static void constructLadderPostion() {

		ladderPositionMap.put(3, 16);
		ladderPositionMap.put(5, 7);
		ladderPositionMap.put(15, 25);
		ladderPositionMap.put(18, 20);
		ladderPositionMap.put(21, 32);

	}

	private static void constructSnakePostion() {

		snakePositionMap.put(12, 2);
		snakePositionMap.put(14, 11);
		snakePositionMap.put(17, 4);
		snakePositionMap.put(31, 19);
		snakePositionMap.put(35, 22);

	}

	private static int setUpNoOfPlayers() {

		System.out.println("Input the no of player...");
		int noOfUsers = 0;

		try {

			noOfUsers = scanner.nextInt();

			for (int i = 1; i <= noOfUsers; i++) {
				Player player = new Player();
				player.playerName = "Player: " + i;
				playerMap.put(i, player);
			}

		} catch (Exception e) {
			e.printStackTrace();
		}

		return noOfUsers;
	}

	private static void playGame() {

		int currentPlayer = 1;

		for (;;) {

			try {
				Thread.sleep(1000);
			} catch (InterruptedException e) {
				e.printStackTrace();
			}

			scanner.nextLine();

			System.out.println("Its Player: " + currentPlayer
					+ " chance to play, Role the dice by pressing enter...");

			Player player = playerMap.get(currentPlayer);
			player.oldPosition = player.currentPosition;

			scanner.nextLine();

			int currentPosition = random.nextInt(6) + 1;

			System.out.println(player.playerName + " has rolled no "
					+ currentPosition + " in the dice");

			player.currentPosition = player.oldPosition + currentPosition;

			Integer newLadderPosition = checkIfLadderExists(player,
					player.currentPosition);
			Integer newSnakePosition = checkIfSnakeExists(player,
					player.currentPosition);

			if (newLadderPosition == null && newSnakePosition == null) {
				System.out.println(player.playerName
						+ " has moved from the position: " + player.oldPosition
						+ " to position: " + player.currentPosition);
			}

			if (player.currentPosition >= 36) {
				System.out.println(player.playerName
						+ " has finished the game...");
				break;
			}

			if (noOfPlayers == currentPlayer) {
				currentPlayer = 1;
				continue;
			}

			currentPlayer++;

		}

	}

	private static Integer checkIfLadderExists(Player player,
			int currentPosition) {

		Integer newLadderPosition = ladderPositionMap.get(currentPosition);

		if (newLadderPosition != null) {

			player.currentPosition = newLadderPosition;
			System.out.println(player.playerName + " has found a ladder: "
					+ "at position: " + currentPosition
					+ " hence moving up to a new position: "
					+ player.currentPosition + " from position: "
					+ currentPosition);

		}

		return newLadderPosition;
	}

	private static Integer checkIfSnakeExists(Player player, int currentPosition) {

		Integer newSnakePosition = snakePositionMap.get(currentPosition);

		if (newSnakePosition != null) {

			player.currentPosition = newSnakePosition;
			System.out.println(player.playerName + " has found a snake: "
					+ "at position: " + currentPosition
					+ " hence moving down to a new position: "
					+ newSnakePosition + " from position: " + currentPosition);

		}

		return newSnakePosition;
	}

}



By graph theory
http://theoryofprogramming.com/2014/12/25/snakes-and-ladders-game-code/

If you roll 5 from block 1 you will jump directly to block 27. So is for block 2 when you roll out 4, or, block 3 when you roll out 3 and so on. Now, “logically” speaking, the block 6 does not exists in our graph…! Think about the statement for a while. Whenever you reach block, you are directly jumping to block 27, you don’t stay there. Now, if you were constructing an Adjacency List for this graph…. In the list of adjacent vertices for Vertex 1, would you have Vertex 6 in the list, or Vertex 27…? Vertex 27 of course…! Being at Vertex 6 means being at Vertex 27…!

That is why, our edge arrow did not end at Vertex 6… See it…? One more thing, in your Adjacency List, in the list of adjacent vertices for Vertex 6, what would you have…? Nothing…! Because you cannot come to a situation where you would have to stay on Vertex 6 and roll the dice. So the adjacent nodes list corresponding to Vertex 6 should be empty. These two things are very important, when you implement the Adjacency List for the Snake and Ladder board.

ou see the hardest part here in solving the Snakes and Ladder by graphs is correctly determining what your Vertices and Edges are. Once you get that, all you have to do is the Breadth First Search in the resultant graph. Then you can get the shortest path from Vertex 1 to Vertex 100.






Algorithm for snakes and Ladders game in python
	1)There are two players and they are given a dice
	2)Typically the game board has 100 cells starting from 1 to 100
	3)There are snakes and ladders in different cells. And each has either a ladder or a snake or nothing but not both snake and ladder in the same cell.
	4)I use two python dictionaries namely 'snakes' and 'ladders' to declare the positions of snakes and ladders.
	5)I make starting cell number of snake or ladder as 'key' and ending cell number as 'value' of the dictionary.
	6)Define a function to roll the dice i.e., accepting the input from Player1 and Player2 with a checking condition of dice number to be between 1 & 6.
	7)Define a function to check if Player1 or Player2 found ladder or a snake mouth.
	8)Check for the 'key's in both dictionaries & proceed accordingly.
	9)The rolling of dice continues until any of the player reaches above 99, if any of the players reach 100 they will be declared as winner of the game.

'''