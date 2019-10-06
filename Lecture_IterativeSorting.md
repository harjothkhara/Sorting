What is an algorithm? a list of steps or procedures or rules to perform something, to perform a task e.g algorithm for baking cookies also known as a recipe

Big O Notation is a measurement of the efficiency of your algorithm
| |
Time Complexity and Space Complexity

What do we mean by complexity and Big O: How does the performance of your code scale based on the size of your inputs eg app runs fine with 5 users, but what happens when you have 5000 users <<---this is what we care about with complexity performance

Big O Notation - these are the shapes of the curve. as your inputs get bigger, does your performance get worse or stay constant \*\*Remember the shapes of these curves (see attached Big-0 Complexity chart)
0(1) -- performance constant
0(n) -- performance is slightly bad
0(n log n) -- performance is getting bad over time
0(n^2) -- performance is a lot worse straight away after only a small increase in the input size

Cost and benefits for each data structure we use

0(1) - constant time complexity. doesn't matter how big out inputs are, or how big our lists is, performance is constant.

Time and Space Complexity both apply to the different common data structures operations. There's different trade offs/cost and benefits for each data structure we use, so its good to learn different ones. Looking at sorts day 1 + day 2

What is the order of complexity? O(1) >> best case, O(n) >>> worst case

0(n / 2) = 0(0.5 \* n) = O(n) drop the coefficient and just call this O(n)

when we look at efficiency we look at big O

Difference between O(n) and O(n^2) is the differences in performance getting really,really big, really fast e.g you notice the difference between 1 millisecond(O(n)) and 1000(O(n^2)) seconds

for loop == O(n) operation because your doing something linearly to each item in your loop.

O(n^2) the number of operations grows really, really fast e.g for loop within another for loop, name pairing animals in a list

O(n^3) the number of operations grows really, really fast e.g for loop within another for loop within another for loop, name pairing animals in a list

O(n!) - o to the n factorials are less common O(n^1,2,3,10,100,1000)

how do we count n items in constant time? e.g big O of len(l), append() is O(1)

Binary Search - split in half and keep the side that contains the value you're searching for. repeat until value is found. values must be sorted already. Time complexity ---> O(log n). This is why sorting is important b/c it allows us to do binary search
