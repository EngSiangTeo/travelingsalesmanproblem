# travelingsalesmanproblem
My attempt at solving the traveling salesman problem

## The Context
A game is to be played in a huge open flat field where several flags are
planted. Each flag is labelled with a positive number that indicates the
number of points the flag is worth. Players touching a flag the first time will
receive these points (no points for a subsequent touch). All players start
from the same starting point (SP) (x=0.0, y=0.0). When the whistle blows,
players are free to move from flag to flag to collect as many points as
possible by touching them. <br>

For simplicity, you can assume that all players run at the same speed (which implies that the total
distance travelled determines the time taken by each player). You can also assume that players
move from between flags directly in straight lines. This means that the distance between two flags
can be easily calculated as the Euclidian distance between these two points. In order to facilitate
planning, players are given the coordinates of every single flag, as well as the points of each flag
before the game starts.

### Question
You are a player in this game. The objective is to collect at least p points. (Since players run at the
same speed, this means that you want to minimize the distance taken in your route.) It does not
matter how many points you manage to accumulate; as long as you get at least p points. Plan the
route that you will take in your attempt to win the game. There are two variations of this game:<br>
(i) In the first variation, players stop at the last flag in their route to end the game; there
is no need to move back to the SP.<br>
(ii) in the second variation, all players must get back to the SP to end the game.
In both variations, the objective is still the same: minimize the distance the player has to travel to
collect at least p points.


#### Requirement
You are required to fill up the body of this function in p2q1.py:<br>
get_route(p, v, flags)<br>
where:<br>
• p is the target number of points that a player must collect before ending the game. Players
who fail to accumulate at least p points lose the game immediately. You can assume that
p is >0 and that there are enough flag points in the field to meet p’s requirement.<br>
• v is the game variation. If v is 1, players do not need to move back to the SP. If v is 2, players
must get back to the SP. <br>
• flags is a 2D list that contains the unique ID, points, and x and y coordinates of each flag.<br>

The following shows two flags:
`[[F001, 3, -39.088893, 14.9550392], [F002, 1, -10.341334, -14.654583]]`
Flag F001 is worth 3 points, and is positioned at (x=-39.088893, y=14.9550392). Flag F002
is worth 1 point, and is positioned at (x=-10.341334, y=-14.654583).
This function should return a list of flag IDs that represent the route that you will take. For example,
your function may return this:
`[F002, F005, F003, F009]`
<br>
This is to be interpreted as:
1) Player starts from (0, 0) and goes to F002 and touches F002.
2) Player then goes from F002 to F005 to touch F005.
3) Player then goes from F005 to F003 to touch F003.
4) Player then goes from F003 to F009 to touch F009.
5) Player then goes from F009 back to (0, 0) in order to end the game.

The total distance travelled by the player would be the sum of Euclidian distances between each
of these locations that constitute the route. Let d(A to B) represent the Euclidian distance between
A and B, then:
If v = 1, total distance =
d(SP to F002) + d(F002 to F005) + d(F005 to F003) + d(F003 to F009)
If v = 2, total distance =
d(SP to F002) + d(F002 to F005) + d(F005 to F003) + d(F003 to F009) + d(F009 to SP)

## My Solution

Refer to `p2q1.py`

### Explanation 
My algorithm works by adding 1 most optimal flag from the pool of remaining flags at a time until P score is reach. <br>
How I calculate the most optimal flag?<br>
**When v=1:**<br>
I used the Euclidian distance between the next flag
 and player’s current position to determine the next
best options. <br>
**Reason**: Aim to get the shortest route with no regards
to points of the flag, as we might need to detour if we
try to optimise with points as well. (Image 1 and Image 2) <br>
![image](https://user-images.githubusercontent.com/56392203/111672688-2dfbb380-8855-11eb-8865-daafc0e8bc96.png)![image](https://user-images.githubusercontent.com/56392203/111672700-30f6a400-8855-11eb-908f-4c32a93375fa.png)

**Image 1 (Optimisation using Distance only)** p = 30
Starting from SP(0,0), it returns [F007,F019,F005,F020,F022].
Which seems to be the most optimal route. <br>
**Image 2 (Optimisation using Distance and Points)** p=30
For this instead of going to F019 after F007, it will go to F005,
as F005 gives more points per distance travelled (Points/Distance).
It returns [F007,F005,F020,F022,F026]. Which seems further than
the Image 1’s route. <br>
**Therefore**, I optimised with distance (Image 1) only for v==1

**When v==2**<br>
I used the optimisation using points per distance travelled (Image2), however with extra checks. The reason for this optimisation is I wanted to get more value for each distance moved and to leave some nearby flags for the next step.<br>
**Extra check**<br>
if current score is less than 75% of the P score
1) it will using Image 2’s optimisation, It will take 
when the current score is above 75%
2) it will also take into consideration of the next flag’s
distance to SP(0,0). So, the value will now be **point of next flag / (distance of current to next flag + distance of next flag to SP)** 

**This optimisation will be visualised in below image**. P=50
It will follow Image 2’s route until it hits F022, when P=39, which is more than 75% of 50. Then instead of going over to F026, it will go to F025, because its close to SP(0,0), giving it a higher value. Then over to F027, which will give a total score of 57. Then back to SP(0,0). It’s an attempt to create a “loop” tour while choosing the next optimal flag.<br> ![image](https://user-images.githubusercontent.com/56392203/111673189-b11d0980-8855-11eb-964a-71e57e646a44.png)




