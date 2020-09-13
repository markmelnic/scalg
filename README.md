# Scoring-Algorithm

This is an algorithm which works based on a range based procentual proximity principle. Initially it was developed for a personal project, however later I found out it is a form of Newton's method used in statistics to solve maximum likelihood equations numerically.

scalg.score:
    Args:
        source_data (list): Data set to process.
        weights (list): Weights corresponding to each column from the data set.
            0 if lower values have higher weight in the data set,
            1 if higher values have higher weight in the data set

    Optional args:
        "score_lists" (str): Returns a list with lists of each column scores.
        "scores" (str): Returns only the final scores.

    Raises:
        ValueError: Weights can only be either 0 or 1 (int)

    Returns:
        list: Source data with the score of the set appended at as the last element.

scalg.score_columns:
    Args:
        source_data (list): Data set to process.
        weights (list): Weights corresponding to each column from the data set.
            0 if lower values have higher weight in the data set,
            1 if higher values have higher weight in the data set
        columns (list): Indexes of the source_data columns to be scored.

    Optional args:
        "score_lists" (str): Returns a list with lists of each column scores.
        "scores" (str): Returns only the final scores.

    Raises:
        ValueError: Weights can only be either 0 or 1 (int)

    Returns:
        list: Source data with the score of the set appended at as the last element.
