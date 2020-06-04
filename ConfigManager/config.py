import csv,json

## Read the csv file and add it to a dictionary

class Config:
    def getConfigFromCsv(self,csvFilePath):
        data={}
        with open(csvFilePath) as csvFile:
            csvReader=csv.DictReader(csvFile)
            for row in csvReader:
                ID=row["Test Case Number"]
                data[ID]=row

        root={}
        root["Query"]=data
        jsonFilePath = csvFilePath+".json"
        ## write data to json file

        with open(jsonFilePath,"w") as jsonFile:
            jsonFile.write(json.dumps(root,indent=4))

        return jsonFilePath
