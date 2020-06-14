
import csv

if __name__ == '__main__':
    fileName = "input.csv"
    
    # read file contents
    with open(fileName, mode="r", newline='') as csvFile:
        csvReader = csv.reader(csvFile)
        source_data = list(csvReader)

    # getting data
    data_lists = []
    for item in source_data:
        for i in range(len(item)):
            try:
                data_lists[i].append(float(item[i]))
            except:
                data_lists.append([])
                data_lists[i].append(float(item[i]))
            
    height = 0
    score_lists = []
    # calculating price score
    for lit in data_lists:
        mind = min(lit)
        maxd = max(lit)

        multiplier = 1
        
        if height == 0:
            score = []
            for item in lit:
                try:
                    score.append((1 - ((item - mind) / (maxd - mind))) * multiplier)
                except:
                    score.append(1)
        else:
            for item in lit:
                try:
                    score.append(((item - mind) / (maxd - mind)) * multiplier)
                except Exception as e:
                    score.append(0)
                    
        score_lists.append(score)

    #final score
    final_score = []
    for s in score_lists[0]:
        final_score.append(0)
    for s_list in score_lists:
        for i in range(len(s_list)):
            final_score[i] = final_score[i] + s_list[i]
    
    with open(fileName, 'w', encoding="utf-8", newline='') as csvFile:
        csvWriter = csv.writer(csvFile)
        
        for i in range(len(source_data)):
            source_data[i].append(final_score[i])
            csvWriter.writerow(source_data[i])
            
        csvFile.close()