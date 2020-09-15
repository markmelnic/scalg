
# Scoring Algorithm (SCALG)

This algorithm works based on a percentual range proximity principle. Initially it was developed for a personal project, however later I found out it is a form of Newton's method used in statistics to solve maximum likelihood equations numerically.

## Usage

    pip install scalg

As of __15 september 2020__ it contains two methods (`score` and `score_columns`) which will be described and demonstrated in the examples below.

    import scalg

## Examples

This will be the sample dataset used as source_data withing the examples with the corresponding indexes and column weights.

    Columns ->  0     1      2      3
    Weights ->  1     0      0      1
            1[[2016 ,21999 ,62000  ,181],
    Sets -> 2 [2013 ,21540 ,89000  ,223],
            3 [2015 ,18900 ,100000 ,223],
            4 [2013 ,24200 ,115527 ,223],
            5 [2016 ,24990 ,47300  ,223]]

### scalg.score(source_data : list, weights : list, *args) -> list

The output if you pass in source_data and weights:

    [[2016, 21999, 62000,  181, 2.2756757812463335],
     [2013, 21540, 89000,  223, 1.9553074815952338],
     [2015, 18900, 100000, 223, 2.894245191297678],
     [2013, 24200, 115527, 223, 1.1297208538587848],
     [2016, 24990, 47300,  223, 3.0]]

The output if you pass in source_data, weights and "scores":

    [2.2756757812463335, 1.9553074815952338, 2. 894245191297678, 1.1297208538587848, 3.0]

The output if you pass in source_data, weights and "score_lists":

    [[1.0, 0.0, 0.6666666666666666, 0.0, 1.0]
     [0.49113300492610834, 0.5665024630541872, 1.0, 0.12972085385878485, 0.0]
     [0.7845427763202251, 0.38880501854104677, 0.22757852463101114, 0.0, 1.0]
     [0.0, 1.0, 1.0, 1.0, 1.0]]

### scalg.score_columns(source_data : list, columns : list, weights : list, *args) -> list

Here you may use the same weights which you would use in `scalg.score`, or you may specify the weights of each column in the corresponding order. In this example using `[1, 0, 0, 1]` or `[0, 1]` would make no difference.

The output if you pass in source_data, columns and weights:

    [[2016, 21999, 62000, 181, 1.4911330049261085],
     [2013, 21540, 89000, 223, 0.5665024630541872],
     [2015, 18900, 100000, 223, 1.6666666666666665],
     [2013, 24200, 115527, 223, 0.12972085385878485],
     [2016, 24990, 47300, 223, 1.0]]

The score was computet only based on columns 0 and 1.