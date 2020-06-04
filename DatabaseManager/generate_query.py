import json
import os.path

class GenerateQuery:
    def __init__(self,update_query):
        self.__update_query__ = update_query

    def IsValid(self, path):
        return os.path.isfile(path)

    def UpdateQuery(self,path):
        if self.IsValid(path) == True:
            tree = self.ParseJson(path)
            self.ParseQuery(tree)
        else:
            print("Path is invalid")

    def ParseJson(self,path):
        """Load data in json file to Python pbject"""
        with open(path,"r") as json_file:
            data = json.load(json_file)
            #print("Type of data",type(data))
            return data

    def ParseQuery(self,tree):
        tcs= self.get_tc_keys(tree)
        for tc in tcs:
            q_src=self.generate_query_src(tree,tc)
            q_stg = self.generate_query_stg(tree, tc)
            self.__update_query__(q_src, q_stg)

    def get_tc_keys(self, tree):

        list_tc = []
        for tc in tree['Query']:
            list_tc.append(tc)
        return list_tc

    def generate_query_src(self,tree,tc):
        """Generate query for source db"""
        query_str=""
        if tree['Query'][tc]["Source Attribute"] != '*':
            source_owner=tree['Query'][tc]["Source Owner"]
            source_tables= tree['Query'][tc]["Source Table"].split(';')
            source_join_type= tree['Query'][tc]["Source Join type"].split(';')
            source_join_condition = tree['Query'][tc]["Source Join Condition"].split(';')
            print(source_tables)
            print(source_join_condition)
            for src_tab in source_tables:
                for src_join_typ in source_join_type:
                    #for src_join_cond in source_join_condition:
                        q= 'select ' + tree['Query'][tc]["Source Attribute"] + ' from ' \
                            +source_owner + '.' + src_tab + ' ' #+ src_join_typ + ' on ' + src_join_cond + ' ' \


        else:
            q= 'select ' + tree['Query'][tc]["Source Attribute"] + ' from ' \
               +tree['Query'][tc]["Source Owner"] + '.' + tree['Query'][tc]["Source Table"] \
               + " where " + tree['Query'][tc]["Source clause"]
        query_str=query_str+q
        return query_str


    def generate_query_stg(self,tree,tc):
        """Generate query for staging db"""
        query_str=""
        if tree['Query'][tc]["Staging Attribute"] != '*':
            staging_owner = tree['Query'][tc]["Staging Owner"]
            staging_tables= tree['Query'][tc]["Staging Table"].split(';')
            staging_join_type= tree['Query'][tc]["Source Join type"].split(';')
            staging_join_condition = tree['Query'][tc]["Source Join Condition"].split(';')
            print(staging_tables)
            print(staging_join_condition)
            for stg_tab in staging_tables:
                for src_join_typ in staging_join_type:
                    #for src_join_cond in source_join_condition:
                        q= 'select ' + tree['Query'][tc]["Staging Attribute"] + ' from ' \
                            +staging_owner + '.' ++ stg_tab + ' ' #+ src_join_typ + ' on ' + src_join_cond + ' ' \


        else:
            q= 'select ' + tree['Query'][tc]["Staging Attribute"] + ' from ' \
               +tree['Query'][tc]["Staging Owner"] + '.' + tree['Query'][tc]["Staging Table"] \
               + " where " + tree['Query'][tc]["Staging clause"]
        query_str=query_str+q
        return query_str


