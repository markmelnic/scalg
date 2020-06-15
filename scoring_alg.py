
import csv

class scalg():
    
    def read_csv(filename):
        if not ".csv" in filename:
            filename = str(filename) + ".csv"

        # read file contents
        with open(filename, mode="r", newline='') as csvFile:
            csvReader = csv.reader(csvFile)
            return list(csvReader)

    def score(source_data):
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
            
            if height == 0:
                score = []
                for item in lit:
                    try:
                        score.append(1 - ((item - mind) / (maxd - mind)))
                    except:
                        score.append(1)
            else:
                for item in lit:
                    try:
                        score.append((item - mind) / (maxd - mind))
                    except Exception as e:
                        score.append(0)
                        
            score_lists.append(score)

        #final score
        final_scores = []
        for s in score_lists[0]:
            final_scores.append(0)
        for s_list in score_lists:
            for i in range(len(s_list)):
                final_scores[i] = final_scores[i] + s_list[i]
                
        return final_scores
    
    def write_data(filename, source_data, final_scores):
        if not ".csv" in filename:
            filename = str(filename) + ".csv"
            
        with open(filename, 'w', encoding="utf-8", newline='') as csvFile:
            csvWriter = csv.writer(csvFile)
            
            for i in range(len(source_data)):
                source_data[i].append(final_scores[i])
                csvWriter.writerow(source_data[i])

            csvFile.close()