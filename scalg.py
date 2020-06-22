
import csv

def score(source_data, height):
    '''
    height
    description - list where each value corresponds to each data column
    possible values - 0 / 1
    0 if lower values have higher priority
    1 if higher values have higher priority
    '''
    
    # getting data
    data_lists = []
    for item in source_data:
        for i in range(len(item)):
            try:
                data_lists[i].append(float(item[i]))
            except:
                data_lists.append([])
                data_lists[i].append(float(item[i]))
            
    score_lists = []
    # calculating price score
    for i in range(len(data_lists)):
        mind = min(data_lists[i])
        maxd = max(data_lists[i])
        
        score = []
        if height[i] == 0:
            for item in data_lists[i]:
                try:
                    score.append(1 - ((item - mind) / (maxd - mind)))
                except:
                    score.append(1)
   
        elif height[i] == 1:
            for item in data_lists[i]:
                try:
                    score.append((item - mind) / (maxd - mind))
                except Exception as e:
                    score.append(0)
    
        else:
            raise Exception("Invalid height provided")
        
        score_lists.append(score)

    #final score
    final_scores = []
    for s in score_lists[0]:
        final_scores.append(0)
    for s_list in score_lists:
        for i in range(len(s_list)):
            final_scores[i] = final_scores[i] + s_list[i]
            
    for i in range(len(source_data)):
        source_data[i].append(final_scores[i])

    return source_data