# Objectives

* Adversarial search
* Decision Theory
* Minimax
* Homework 3 Announcement

# Metrics/Desired Outcomes

* Apply Minimax to solve simple game

## Adversarial Search

In this chapter, we will cover competitive environments, in which the agents'
goals are in conflict, giving rise to adversarialsearch problems -- often known as games.

Mathematical game theory, a branch of economics, views any multiagent environment
as a game, provided that the impact of each agent on the other is "significant",
regardless of whether the agents are cooperative or competitive. In AI, the most
common games are of a rather specialized kind -- what game theorists call deterministic, 
turn-taking, two-players, zero-sum games of perfect information (such as chess).

Games have engaged the intellectual faculties of humans -- sometimes to an 
alarming degree -- for as long as civilization has existed. For AI researchers,
the abstract nature of games makes them an appealing subject for study. The state
of a game is easy to represent, and agents are usually restricted to a small number 
of actions whose outcomes are defined by precise rules. Physical games, such as
conquest and ice hockey, have much more complicated descriptions, a much larger
range of possible actions, and rather imprecise rules defining the legality of 
actions,. With exception of robot soccer, these physical games have not abstracted
too much interest in the AI community.

We begin with a definition of the optimal move and an algorithm for finding it.
We then look at techniques for choosing a good move when time is limitted. 
Pruning allows us to ignore portions of the search tree that make no difference 
to the final choice, and heuristic evluattion functions allow us to approximate
the true utility of a state without doing a complete search.

A game can be formally defined as kind of search problem with the following elements:

* S0: The initial state, which specifies how the game is set up at the start
* Player(s): defines which player has the move in a state
* Actions(s): Returns the state of legal moves in a state
* Result(s, a): The transition model, which defines the result of a move
* Terminal-test(s): A terminal test, which is true when the game is over and false otherwise
* Utility(s, p): a utlity function (also called an objective function or payoff function), 
define the final numeric value for a game that ends in terminal state s for a player p. 
In chess, the outcome is a win, loss, or draw, with values of 1, 0, or 1/2. Some games 
have a wider variety of possible outcomes.

A zero-sum game is (confingly) defined as one where the total payoff to all players 
is the same for every instance of the game. Chess is zero-sum because every game
has payoff of either 0 + 1, 1 + 0 or 1/2 + 1/2. "Constant-sum" would have been a
better term, but zero-sum is traditional and makes sense if you imagine each 
player is charged an entry fee of 1/2.

## Minmax

* Used in decision theory/game theory
* Under the assumption of both players (you and your opponent(s)) play their best moves
    * Minimize the loss at worst case
    * Opponent **minimize** the score
    * You **maximize** the score
* Originally covers only turn-based 2 players game
* This has been adapted to general games now
* Again relies on a **evaluate** function
* Eventually *tree traversal*

## Picture worthes a thousand words

![Minimax graph](imgs/minimax-example.png)

## Examples

1. Tic-tac-toe
2. Zero sum number game

## Pseudocode

** [From Wikipedia](https://en.wikipedia.org/wiki/Minimax)**
```js
function minimax(node, depth, maximizingPlayer)
    if depth = 0 or node is a terminal node
        return the heuristic value of node
    if maximizingPlayer
        bestValue := -∞
        for each child of node
            val := minimax(child, depth - 1, FALSE)
            bestValue := max(bestValue, val)
        return bestValue
    else
        bestValue := +∞
        for each child of node
            val := minimax(child, depth - 1, TRUE)
            bestValue := min(bestValue, val)
        return bestValue

(* Initial call for maximizing player *)
minimax(origin, depth, TRUE)
```

**Our modification to use Graph interface**
```js
function minimax(graph, sourceNode, depth, maximizingPlayer) {
    // usually being optimized in a way to compute even before
    // the end of game by **evaluate** function
    if (depth = 0 || sourceNode is a leaf) {
        return evaluate(soureNode.gameState); // return a number
    }
    
    if (maximizingPlayer) {
        bestValue = Number.MAX_VALUE; // positive infinite
        for (node in graph.neighbors(sourceNode)) {
            value = minimax(node, graph, depth - 1, false);
            bestValue = Math.max(bestValue, value);
        }
        return bestValue;
    } else {
        bestValue = Number.MIN_VALUE; // negative infinite
        for (node in graph.neighbors(sourceNode)) {
            value = minimax(node, graph, depth - 1, true);
            bestValue = Math.min(bestValue, value);
        }
        return bestValue;
    }
}

// initial call of the above function to traverse 3 level for example
minimax(graph, startingNode, 3, TRUE); 
```

# Alpha-Beta Pruning

## Objectives

* Comprehend Alpha-Beta Pruning 

## Metrics/Desired Outcomes

* Implement alpha-beta pruning example

### References

http://inst.eecs.berkeley.edu/~cs61b/fa14/ta-materials/apps/ab_tree_practice/

### Adversarial Search

We now consider something called `Adversarial Search`.  If `Min` and `Max` are adversaries so they will compete with each other at each move by selecting the best `option` while considering the opponent's next move.

![Minimax Example](imgs/min-max-tree.png)

Max would like to select *a1* is the optimal choice because highest value when it is MIN's turn to go.

### Pruning Concept

We want to ignore tree path that does not contribute to the final result one way or another.

## Alpha-Beta

The MINIMAX algorithm properly evaluates a player’s best move when considering the opponent’s countermoves.  This information is not while leveraged when generating tree.

Downside: even if a potentially bad move is ahead, minmax does not eliminate the sub-tree from consideration.  It does so with a consistent strategy to eliminate unproductive sub-tree from future search.

![Alpha Beta Tree](imgs/alpha-beta-tree.png)

(a) The first leaf below B has the value 3. Hence, B, which is a MIN node, has a value of at most 3. 

(b) The second leaf below B has a value of 12; MIN would avoid this move, so the value of B is still at most 3. 

(c) The third leaf below B has a value of 8; we have seen all B’s successor states, so the value of B is exactly 3. Now, we can infer that the value of the root is at least 3, because MAX has a choice worth 3 at the root. 

(d) The first leaf below C has the value 2. Hence, C,which is a MIN node,has a value of at most2. But we know that B is worth 3, so MAX would never choose C. Therefore, there is no point in looking at the other successor states of C. This is an example of alpha–beta pruning. 

(e) The first leaf below D has the value 14, so D is worth at most 14. This is still higher than MAX’s best alternative (i.e., 3), so we need to keep exploring D’s successor states. Notice also that we now have bounds on all of the successors of the root, so the root’s value is also at most 14. 

(f) The second successor of D is worth 5, so again we need to keep exploring. The third successor is worth 2, so now D is worth exactly 2. MAX’s decision at the root is to move to B, giving a value of 3.

![Alpha Beta General](imgs/alpha-beta-general.png)

Generally speaking: if *m* is better than *n* for, then we will never see *n* so path leading up to *n* can be eliminated.

Back to adversarial search:

* Alpha is the value of the best (i.e., highest-value) choice we have found so far at any choice point along the path for MAX.

* Beta is the value of the best (i.e., lowest-value) choice we have found so far at any choice point along the path for MIN.

### Algorithm Summary

Strategy: Alpha-beta recursively search the game tree and tracks two values: alpha and beta.  A couple of observations (rules):

![Alpha Beta Summary](imgs/alpha-beta-summary.png)

* As long as alpha < beta, the branch is consider an opportunity.
* Alpha is the lowerbound game states.
* If alpha is -INF if no information is available.  
* The higher alpha, the better the move.
* If alpha is +INF then a winning move is found.

## Algorithm

```java
public class AlphaBetaEvaluation implements IEvaluation {
  IGameState state;    /** State to be modified during search. */
  int ply;             /** Ply depth. How far to continue search. */

  public AlphaBetaEvaluation (int ply) { 
    this.ply = ply;
  }

  public IGameMove bestMove(IGameState s, IPlayer player, IPlayer opponent) {
    this.state = s.copy();
    MoveEvaluation move = alphabeta(ply, player, opponent, 
      MoveEvaluation.minimum(), MoveEvaluation.maximum()); 
    return move.move;
  }

  private MoveEvaluation alphabeta(int ply, IPlayer player, IPlayer opponent,
    int alpha, int beta) {
   // If no moves, return evaluation of board from player's perspective. 
   Iterator<IGameMove> it = player.validMoves(state).iterator();
   if (ply == 0 || !it.hasNext()) {
     return new MoveEvaluation(player.eval(state));
   }

   // Select "maximum of negative value of children" that improves alpha 
   MoveEvaluation best = new MoveEvaluation (alpha);
   while (it.hasNext()) {
     IGameMove move = it.next();
     // Recursively evaluate position.
     move.execute(state);
     MoveEvaluation me = alphabeta (ply-1, opponent, player, -beta, -alpha);
     move.undo(state);
     // If improved upon alpha, keep track of this move.
     if (-me.score > alpha) {
       alpha = -me.score;
       best = new MoveEvaluation (move, alpha);
     }
     if (alpha >= beta) { 
       return best;
     } // search no longer productive.
   }
   return best;
 }
}

```

### Min-Max and Alpha-Beta Comparison

Let us take a closer look at the two adversarial search algorithm side-by-side to see what part of the algorithm drives the improvements.

![Min-Max Algorithm](imgs/minimax-algorithm.png)

* S0: The initial state, which specifies how the game is set up at the start.
* PLAYER(s): Defines which player has the move in a state.
* ACTIONS(s): Returns the set of legal moves in a state.
* RESULT(s,a): The transition model, which defines the result of a move.
* TERMINAL-TEST(s): A terminal test, which is true when the game is over and false otherwise. States where the game has ended are called terminal states.
* UTILITY(s, p): A utility function (also called an objective function or payoff function), defines the final numeric value for a game that ends in terminal state s for a player p. 

![Alpha-Beta Algorithm](imgs/alpha-beta-algorithm.png)

## Analysis

Time complexity is *O(b^m)*

### References

Materials taken 
* Russell, Stuart.  Artificial Intelligence: A Modern Approach, 3rd Edition
* Heineman, G et al. [Algorithms in a Nutshell, 1st ed.](http://shop.oreilly.com/product/9780596516246.do) 
