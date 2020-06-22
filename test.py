
import csv
import scalg

def read_csv(filename):
    if not ".csv" in filename:
        filename = str(filename) + ".csv"

    # read file contents
    with open(filename, mode="r", newline='') as csvFile:
        csvReader = csv.reader(csvFile)
        return list(csvReader)
    
def write_data(filename, source_data, final_scores):
    if not ".csv" in filename:
        filename = str(filename) + ".csv"
        
    with open(filename, 'w', encoding="utf-8", newline='') as csvFile:
        csvWriter = csv.writer(csvFile)
        
        for i in range(len(source_data)):
            csvWriter.writerow(source_data[i])

        csvFile.close()
       

if __name__=='__main__':
    dt = read_csv("input.csv")
    sc = scalg.score(dt, [1, 0, 0, 1])
    write_data("input.csv", dt, sc)