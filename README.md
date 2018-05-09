# [Circle-Splitter-DailyProgrammer-Hard321](https://www.reddit.com/r/dailyprogrammer/comments/6ksmh5/20170630_challenge_321_hard_circle_splitter/)
Daily Programmer Challenge - Find the smallest circle in a limited size square, that contains half of the given points.

The smallest circle for any given points has two of the points at the edges of the circle. This tests every combonation of two points as the outside points, and logs every circle that has half of the points inside of it. Then it checks to make sure the circle is within the square, and reduces down to the smallest radius circle
## Input

Input is the number of points, and then the x y coordinates of the given points.

Example Input

    4
    0.5 0
    0.5 1
    0 0
    1 1
    
## Output 

Example Output

    The Smallest Radius Circle is:0.5
    At [X,Y]:[0.5, 0.5]
