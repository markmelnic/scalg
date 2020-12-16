def score(source_data: list, weights: list, get_scores=False, get_score_lists=False) -> list:
    """Analyse data file using a range based percentual proximity
    algorithm and calculate the linear maximum likelihood estimation.

    Args:
        source_data (list): Data set to process.
        weights (list): Weights corresponding to each column from the data set.
            0 if lower values have higher weight in the data set,
            1 if higher values have higher weight in the data set

    Optional args:
        get_scores (bool): Returns only the final scores.
        get_score_lists (bool): Returns a list with lists of each column scores.

    Raises:
        ValueError: Weights can only be either 0 or 1

    Returns:
        list: Source data with the score of the set appended at as the last element.
    """

    # getting data
    data_lists = [[] for i in source_data]
    for item in source_data:
        for i, val in enumerate(item):
            data_lists[i].append(float(val))

    # calculating price score
    score_lists = []
    for dlist, weight in zip(data_lists, weights):
        mind = min(dlist)
        maxd = max(dlist)

        score = []
        if weight == 0:
            for item in dlist:
                if not maxd - mind == 0:
                    score.append(1 - ((item - mind) / (maxd - mind)))
                else:
                    score.append(1)

        elif weight == 1:
            for item in dlist:
                if not maxd - mind == 0:
                    score.append((item - mind) / (maxd - mind))
                else:
                    score.append(0)

        else:
            raise ValueError("Invalid weight of %f provided" % (weight))

        score_lists.append(score)

    # initialize final scores
    final_scores = [0 for i in range(len(score_lists[0]))]

    # generate final scores
    for i, slist in enumerate(score_lists):
        for j, ele in enumerate(slist):
            final_scores[j] = final_scores[j] + ele

    # append scores to source data
    for i, ele in enumerate(final_scores):
        source_data[i].append(ele)

    # return score lists
    if get_score_lists:
        return score_lists
    # return only scores
    if get_scores:
        return final_scores
    # return source data with appended scores
    return source_data


def score_columns(source_data: list, columns: list, weights: list) -> list:
    """Analyse data file using a range based percentual proximity
    algorithm and calculate the linear maximum likelihood estimation.

    Args:
        source_data (list): Data set to process.
        columns (list): Indexes of the source_data columns to be scored.
        weights (list): Weights corresponding to each column from the data set.
            0 if lower values have higher weight in the data set,
            1 if higher values have higher weight in the data set

    Raises:
        ValueError: Weights can only be either 0 or 1 (int)

    Returns:
        list: Source data with the score of the set appended at as the last element.
    """

    temp_data = [[item[c] for c in columns] for item in source_data]

    if len(weights) > len(columns):
        weights = [weights[item] for item in columns]

    for i, sc in enumerate(score(temp_data, weights, get_scores=True)):
        source_data[i].append(sc)

    return source_data
