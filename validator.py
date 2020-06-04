from ConfigManager import Config
from DatabaseManager import GenerateQuery
from DatabaseManager import ConnectDB

class Validator:
    def __init__(self,path):
        self.path=path
        testcase_config = Config()
        jsonpath = testcase_config.getConfigFromCsv(self.path)
        print(jsonpath)
        self.source_database = ConnectDB('hr', 'hr', 'localhost', '1521', 'ORCL')
        self.staging_database = ConnectDB('scott', 'scott', 'localhost', '1521', 'ORCL')
        generate_query = GenerateQuery(self.validateDatabaseQuery)
        generate_query.UpdateQuery(jsonpath)


    def validateDatabaseQuery(self,SourceDataBaseQuery,StagingDataBaseQuery):
        print("Source database query:- ", SourceDataBaseQuery)
        print("Staging database query:- ", StagingDataBaseQuery)
        print("Source records are as follows: \n")
        self.source_database.execute_query(SourceDataBaseQuery)
        print("Staging records are as follows: \n")
        self.staging_database.execute_query(StagingDataBaseQuery)



def __main__():
    print("hello")
    path = "ConfigManager/query.csv"
    validator=Validator(path)
__main__()
