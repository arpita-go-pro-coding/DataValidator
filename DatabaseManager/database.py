import cx_Oracle

### create connection

class ConnectDB:

    def __init__(self,user,pswd,host,port,sid):
        self.user=user
        self.pswd=pswd
        self.host=host
        self.port=port
        self.sid=sid
        self.connect_oracle()


    def __del__(self):
        self.conn.close()

    def connect_oracle(self):
        conn_str=f"{self.user}/{self.pswd}@//{self.host}:{self.port}/{self.sid}"
        self.conn=cx_Oracle.connect(conn_str)

    def execute_query(self,query):
        print("Query is ", query)
        connection_done = self.conn.cursor()

        connection_done.execute(query)
        for row in connection_done:
            # print( row[0], "-", row[1])
            print(row)
        print("-----------------------------------------------------------")





#cdb.connect_oracle()


