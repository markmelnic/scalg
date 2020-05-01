
import os
import csv


if __name__ == '__main__':
    fileName = "input.csv"
    
    # read file contents
    with open(fileName, mode="r", newline='') as csvFile:
        csvReader = csv.reader(csvFile)
        data = list(csvReader)
        data.pop(0)
        csvFile.close()

    # getting data
    allReg = []
    allPrices = []
    allMiles = []
    for dat in data:
        allReg.append(int(dat[0]))
        allPrices.append(int(dat[1]))
        allMiles.append(int(dat[2]))

    # calculating price score
    minPrice = min(allPrices)
    maxPrice = max(allPrices)

    multiplier = 3.333
    
    priceScore = []
    for price in allPrices:
        try:
            priceScore.append((1 - ((price - minPrice) / (maxPrice - minPrice))) * multiplier)
        except:
            priceScore.append(1)

    # reg score
    minReg = min(allReg)
    maxReg = max(allReg)
    
    regScore = []
    for reg in allReg:
        try:
            regScore.append(((reg - minReg) / (maxReg - minReg)) * multiplier)
        except Exception as e:
            regScore.append(0)

    # mileage score
    minMiles = min(allMiles)
    maxMiles = max(allMiles)

    milScore = []
    milTempScore = []
    for mil in allMiles:
        try:
            milScore.append((1 - (mil - minMiles) / (maxMiles - minMiles)) * multiplier)
        except:
            milScore.append(1)


    # final score
    fScore = []
    for pricesc, mileagesc, regsc in zip(priceScore, milScore, regScore):
        fScore.append(pricesc + mileagesc + regsc)

    
    with open(fileName, 'w', encoding="utf-8", newline='') as csvFile:
        csvWriter = csv.writer(csvFile)
        for dat, score in zip(data, fScore):
            csvWriter.writerow([dat[0], dat[1], dat[2], score])
        csvFile.close()