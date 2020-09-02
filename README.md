# Learn Python with Fantasy Football Practice Problems

These are practice problems for the first five sections of *Learn Python with Fantasy Football*.

Read over the practice problems and try to complete them within your Google Colab environment. Solutions are found within the `solutions` folder.

## Module 1 (Section 2 of the Course): Our First Project and an Intro to Python.

#### Problem 1 (Easy)

Tyler Lockett had the following stat line for 2019.

82 receptions, 69 targets, 1057 receiving yards, 8 receiving touchdowns

Using Python, `print` Lockett's catch rate and fantasy points scored for 2019.

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

#### Problem 10  (Hard)

Using a dictionary of `fantasy_weights`, find the fantasy points scored for Lamar Jackson with the following stats saved to the following dictionary:

    lamar_jackson_stats = {
      'passing_yds': 3127,
      'passing_tds': 36,
      'passing_int': 6,
      'rushing_yds': 1206,
      'rushing_tds': 7,
      'fumbles': 8,
      'receiving_yds': 0,
      'receptions': 0,
      'receiving_td': 0
    }

Your `fantasy_weights` dictionary should look like the following:

    fantasy_weights = {
    'passing_yds': 0.04,
    'passing_tds': 4,
    'passing_int': -2,
    'rushing_yds': 0.10,
    'rushing_tds': 6,
    'fumbles': -2,
    'receiving_yds': 0.10,
    'receptions': 1, # adjust for half PPR and standard
    'receiving_td': 6
    }


## Module 2: Functions, Loops, Conditionals (Section 3 of the Coruse)

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

#### Problem 4 (Easy)

Write a function that takes in a player's rushing stats on the season and returns a formatted dictionary with `yards_per_carry` and `touchdowns_per_carry` 

The input argument should be formatted like this:

        {
            'rushing_yards': 1000,
            'rushing_touchdowns': 12,
            'rushing_attempts': 240
        }

And the `return` value of the function should look like this:

        {
            'yards_per_carry': 5.0, # made up number for example purposes
            'touchdowns_per_carry': 0.25
        }

#### Problem 5 (Medium)

Using this list of dictionaries with information about the last 10 picks in a draft, find the last QB, RB, WR, TE chosen in the draft. Store the information about the last picked players in the draft in a dictionary with key:value pairs of position:pick

        players = [
            {
                'pos': 'RB',
                'pick': 90
            },
            {
                'pos': 'RB',
                'pick': 91
            },
            {
                'pos': 'WR',
                'pick': 92
            },
            {
                'pos': 'TE',
                'pick': 93
            },
            {
                'pos': 'RB',
                'pick': 94
            },
            {
                'pos': 'RB',
                'pick': 95
            },
            {
                'pos': 'WR',
                'pick': 96
            },
            {
                'pos': 'RB',
                'pick': 97
            },
            {
                'pos': 'TE',
                'pick': 98
            },
            {
                'pos': 'RB',
                'pick': 99
            },
            {
                'pos': 'QB',
                'pick': 100
            },
        ]

## Module 3: Object Oriented Programming (Section 4 of the Course)

#### Problem 1 (Medium)

Write a class `Player2019` with the following arguments to `__init__`:

* `passing_int`, `rushing_yds`, `rushing_tds`, `receiving_yds`, `receiving_td`, `passing_yds`, `passing_tds`, `fumbles`, `receptions`

Save these arguments to a dictionary called `self.fantasy_stats`

And also create a method called `fantasy_points` that calculates Fantasy Points scored based off the attributes.

As an added bonus, utilize the `@property` decorator for accessing `fantasy_points` as a class attribute rather than a method call.

This part is optional, but find out more about `@property` <a href="https://www.programiz.com/python-programming/property">here</a>.

## Module 4: Python Crash Course Recap (Section 5 of the Course)

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

#### Problem 4 (Medium)

Calculate and write a function to find the euclidean distance between two points.

    (1.0, 450)
    (5.0, 340)

The euclidean distance is the straight-line distance between two points.

It's defined by this equation:

<img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/795b967db2917cdde7c2da2d1ee327eb673276c0">

Euclidean distance is an important concept to know as we'll be covering it again in the clustering algorithms section.

#### Problem 5 (Hard)

Using the positional value for each position, calculate each player's value score. Each player's value score is their projected points over the value for their respective position.

Your player data should be saved as the following:

        {
            'name': 'AJ Brown',
            'position': 'WR',
            'projected': 145
        }

Store 3 of these dictionaries for any players you like (as long as you use more than one position) in a list called `players`.

Use the following positional values (a lower number means higher positional value - these are actually called replacement values which we'll cover in section six):

        {
            'WR': 50,
            'RB': 32,
            'TE': 45,
            'QB': 110
        }

Use this dictionary to calculate a `value_score` for each player, and append the `value_score` to their dictionary.

For example, AJ Brown's dictionary should look like the following:

        {
            'name': 'AJ Brown',
            'position': 'WR',
            'projected': 145,
            'value_score': 95
        }

When grabbing elements from the dictionary, use the `get` method for dictionaries, rather than the traditional `dict[key]` method.

Finally, sort the dictionaries on the value score (using `sorted`) and find the player with the highest value score.

In the problem solution, I utilize the Python built-in function `enumerate`.
