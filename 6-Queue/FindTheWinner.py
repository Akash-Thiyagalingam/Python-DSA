#Find the Winner of the Circular Game
'''The rules of the game are as follows:
    Start at the 1st friend.
    Count the next k friends in the clockwise direction including the friend you started at. The counting wraps around the circle and may count some friends more than once.
    The last friend you counted leaves the circle and loses the game.
    If there is still more than one friend in the circle, go back to step 2 starting from the friend immediately clockwise of the friend who just lost and repeat.
    Else, the last friend in the circle wins the game.
    Given the number of friends, n, and an integer k, return the winner of the game.'''
#Time Complexity : O(N^2)
#Space Complexity : O(N)
def findTheWinner( n, k):
        queue = deque([friend+1 for friend in range(n)])
        while len(queue) > 1:
            round = k-1
            while round:
                queue.append(queue.popleft())
                round -= 1
            queue.popleft()
        return queue[0]

print(findTheWinner([1,2,3,4,5,6],2))
