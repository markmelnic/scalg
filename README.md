# Scoring-Algorithm

This is an algorithm which works based on a range based procentual proximity principle. Initially it was developed for a personal project, however later I found out it is a form of Newton's method used in statistics to solve maximum likelihood equations numerically.

Right now the main method is score(source_data, weights, *args), where source_data is what you pass into the algorithm to compare. It will compare each data list within itself, doing that for each list, then add up the scores of each element from each list with the same index.

The weights parameter is an int list with possible values of 0 or 1, where 0 means lower values have higher weight in the data set and 1 means higher values have higher weight in the data set.

Other optional arguments are (passed in as a string):

    str - "score_lists"
    get a list with all the scores for each piece of data
    
    str - "scores"
    get only the final scores for each data set