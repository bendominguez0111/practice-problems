# Learn Python with Fantasy Football Practice Problems

These are practice problems for the first five sections of *Learn Python with Fantasy Football*.

Read over the practice problems and try to complete them within your Google Colab environment. Solutions are found within the `solutions` folder.

## Module 1: Our First Project and an Intro to Python.

#### Problem 1 (Easy)

Tyler Lockett had the following stat line for 2019.

82 receptions, 69 targets, 1057 receiving yards, 8 receiving touchdowns

Using simple, Python `print` Lockett's catch rate and fantasy points scored for 2019.

#### Problem 2 (Medium)

[Visit this URL and find Michael Thomas's receiving yards for 2019.](https://www.pro-football-reference.com/players/T/ThomMi05/gamelog/2019/) Input each weeks receiving yards in to a ordered list, and find the average of the list using Python's built in functions `len` and `sum`. Both of these functions can be found in the Python docs.

Print out MT's average receiving yards for 2019 using the `print` function.

#### Problem 3 (Very Hard)

Using the list above, find the standard deviation of Michael Thomas's receiving yards. This is how you calculate the standard deviation: For each element in the list, subtract away the mean of the list, and square the difference for each of these intermediary calculations. Set these numbers to the side. Once you are finish iterating this operation, sum up all of the results, and divide by the length of the list (the number of observations). [Find out more information about standard deviation here.](https://en.wikipedia.org/wiki/Standard_deviation)

Finally, take the square root of that number (that number is actually the variance). This is your standard deviation.

#### Problem 4 (Medium)

Using `if` statements, find whether or not Rashaad Penny is in the interquartile range for rushing yards (between 25th and 75th percentile), in the bottom 25th percentile, or in the top 75th percentile.

* Rashaad Penny Rushing Yards: 370 yards
* 25th percentile (2019) for all RBs for Rushing Yards: 20 yards
* 75th percentile (2019) for all RBs for Rushing Yards: 465 yards

#### Problem 5 (Easy)

Write a program that calculates yards per carry for 3 three top running backs. Store the player data in a list of dictionaries, where each dictionary corresponds to a separate player. Iterate over each dictionary using a `for` loop.

#### Problem 6 (Very Hard)

For each player in the program you created above, write a program that finds the player with the max rushing yards. You should still store player data in a list of dictionaries.

You should leverage `for` and `if` here. I'll offer an alternative solution in the `problem_6.py` file as there are multiple ways to go about this problem.

#### Problem 7 (Medium)

    rushing_tds = [10, 12, 12, 6, 7, 8, 12, 15, 17]

Sort this list in descending order using the `sorted` built-in function. <a href="https://www.programiz.com/python-programming/methods/built-in/sorted">You can find more information about `sorted` here.</a>

Grab the last element of the list, and the first element of the list using list indexing.

#### Problem 8 (Hard)

Calculate the passer rating for a given player using the following formula:

<img src="https://emergentmath.files.wordpress.com/2011/02/eq15.png" style="margin: 2rem;">


#### Problem 9 (Easy)

<a href="https://docs.python.org/3/library/functions.html">Explore Python's built in functions.</a> Find the `max` and `min` of this list of numbers using Python's built-in functions. Also find the difference between the `min` and `max`, known as the range. As an added bonus, try to find the min and max without using any built-in functions.

    list_obj = [1, 2, 3, 56, 12, 23, 34, 12, 89, 90, 345, 67, 56, 34]

#### Problem 10 

## Module 2: Functions

#### Problem 1 (Hard)

Write a function that calculates standard deviation for any list of numbers.

Test it using any player's rushing yards for the 2019 season.

In the solution, I provide a way you can check your answer to make sure it is correct using one of Python's data science libraries - `numpy`

#### Problem 2 (Medium)

Write a function that calculates fantasy points given a dictionary as an argument with the following format:

    {
      'passing_yds': 3400,
      'passing_tds': 24,
      'passing_int': 6,
      'interceptions': -2,
      'rushing_yds': 324,
      'rushing_tds': 3,
      'fumbles': 2,
      'receiving_yds': 12,
      'receptions': 1,
      'receiving_td': 0
    }

There are multiple ways to go about this problem. I'll cover two possible solutions in the `solutions` file.

#### Problem 3 (Easy)

Write a function that calculates a player's passer rating based off their completions, attempts, yards, interceptions, and touchdowns. These should all be arguments to your function. The formula for passer rating is above in module 1, problem 8 problem description.


## Module 3: Object Oriented Programming

#### Problem 1 (Medium)

Write a class `Player2019` with the following arguments to `__init__`:

* `passing_int`, `rushing_yds`, `rushing_tds`, `receiving_yds`, `receiving_td`, `passing_yds`, `passing_tds`, `fumbles`, `receptions`

Save these arguments to a dictionary called `self.fantasy_stats`

And also create a method called `fantasy_points` that calculates Fantasy Points scored based off the attributes.

As an added bonus, utilize the `@property` decorator for accessing `fantasy_points` as a class attribute rather than a method call.

This part is optional, but find out more about `@property` here.

#### Problem 2 (Easy)

Using the class above, instantiate new Player objects by iterating over a list of dictionaries with 3 NFL players stat lines for 2019.

Save all of the instances to a list.

## Module 4: Python Crash Course Recap

#### Problem 1 (Very Hard)

The average of a set of data points, or mean, is a summary statistic used to measure the central tendency of a data set. Summary statistics are useful for reducing a set of data points down to a single, descriptive number.

Another commonly used summary statistic is standard deviation, which is a measure of spread out a data set is.

When it comes to Fantasy Football, less standard deviation is usually better. We want to pick up those players who consistently get us big outings, with little variation between outings. This makes these players easier to predict.

For this problem, I want you to grab two player's stat lines and compare their mean fantasy output and also the standard deviation of their fantasy output.

For the solution, I'll be comparing [Jameis Winston](https://www.pro-football-reference.com/players/W/WinsJa00/gamelog/2019/) and [Tom Brady](https://www.pro-football-reference.com/players/B/BradTo00/gamelog/2019/).

The definition of the standard deviation:

<img style="margin: 2rem;" src="https://www.gstatic.com/education/formulas/images_long_sheet/en/population_standard_deviation.svg">


For each data point (fantasy football point scored), subtract out the mean fantasy points scored, square that difference and set that number to the side. Add up the results for each data point, sum them, and then divide by the number of observations. From there, take the square root. This is your standard deviation. The larger the standard deviation, the more spread out the data set is.

This problem is admittedly hard for a beginner, and will take some time to set up. The solution I propose in the `solutions` is only one of many ways you could have solved this problem.

#### Problem 2 (Very Hard)

Find the correlation between two lists of numbers utilizing list comprehensions.

<img src="https://media.geeksforgeeks.org/wp-content/uploads/Corre.png">

x prime and y prime here are the mean of the two sample sets, or lists.

The S symbol is Sigma, which means the sum from the bottom number up to n. So for the sigma in the numerator, it is basically saying sum each of the results starting at 1 up to the length of the list (another way of saying sum each result).

#### Problem 3 (Very Hard)

Utilizing the function you wrote above, get two player's fantasy stats for the 2019 season and find the correlation between their fantasy performances. For the solution, I'll be using two fictitious players - a QB and WR and seeing how their performance correlated.

You should format each player object like the following:

    wr = {
      'passing_tds': [0 for _ in range(1, 17)],
      'passing_yds': [0 for _ in range(1, 17)],
      'passing_int': [0 for _ in range(1, 17)],
      'rushing_yds': [0 for _ in range(1, 17)],
      'rushing_tds': [0 for _ in range(1, 17)],
      'fumbles': [0 for _ in range(1, 17)],
      'receiving_yds': [123, 78, 99, 34, 145, 67, 56, 98, 105, 34, 12, 205, 90, 87, 78, 190],
      'receptions': [10, 4, 6, 2, 12, 7, 4, 3, 5, 10, 3, 1, 12, 5, 7, 15],
      'receiving_tds': [2, 0, 0, 0, 3, 1, 1, 0, 2, 0, 0, 3, 0, 0, 0, 2]
    }

As you can see, this is a dictionary with keys as relevant fantasy categories and values as lists - each item in the list contains a separate stat line for that week. Your job is to collapse, or reduce, these lists in to one list that contains only their fantasy football points scored, and then run both those lists through the correlation function and find the correlation of the two players performances.

#### Problem 4 (Hard)

Given this list of rushing attempts for the 2019 season, find the top 25th percentile, and the bottom 75th percentile using only vanilla Python code. 
      
    [287.0, 176.0,303.0,236.0,301.0,250.0,1.0,1.0,298.0,132.0,202.0,52.0,0.0,75.0,1.0,5.0,82.0,278.0,2.0,0.0,217.0,0.0,278.0,223.0,0.0,2.0,2.0,0.0,265.0,59.0,0.0,1.0,0.0,]
