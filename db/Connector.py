import pymysql

def getConnection(ipaddr, username, password, database):

    try:
        # Open database connection
        db = pymysql.connect(ipaddr, username, password, database)
        print('Successfully Connected!')

        return db

    except Exception as e:
        print(e)
        print("\nOops Could'nt Connect :(")


class Connection:
    '''
    A Wrapper for the aleph project
    Server is an EC2 instance running CentOS 7
    '''
    def __init__(self, ipaddr, username, password, database):
        self.ipaddr = ipaddr
        self.username = username
        self.password = password
        self.database = database


    def insert(self, table, values):
        '''
        :param table:
        :param values:
        :return: nothing, but inserts values into specified table
        '''

        db = getConnection(self.ipaddr, self.username, self.password, self.database)
        cursor = db.cursor()

        sql = "INSERT INTO " + table + " Values ("
        for ind in range(0, len(values)):
            sql+= values[ind]
            if ind != len(values) -1:
                sql+=", "
            else:
                sql+= ")"

        print(sql)

        try:
            cursor.execute(sql)
            db.commit()
        except Exception as e:
            print(e)
            db.rollback()
        finally:
            db.close()


    def query(self, table, columns, conditions=[]):
        '''
        :param table: table name
        :param columns: columns to query
        :param conditions: WHERE clause
        :return: python nested tuple with each tuple being one row
        '''
        db = getConnection(self.ipaddr, self.username, self.password, self.database)
        cursor = db.cursor()

        sql = "SELECT "
        for ind in range(0,len(columns)):
            sql += columns[ind]
            if ind != len(columns) - 1:
                sql += ", "

        sql += " FROM " + table

        if len(conditions)>0:
            sql += " WHERE "
            for ind in range(0,len(conditions)):
                sql += conditions[ind]
                if ind != len(conditions) - 1:
                    sql += "and "

        print("\n"+sql)

        result=""
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
        except Exception as e:
            print(e)
        finally:
            db.close()

        return result

    def delete(self, table, conditions=[]):
        '''
        :param table: table name
        :param conditions: WHERE clause
        '''
        db = getConnection(self.ipaddr, self.username, self.password, self.database)
        cursor = db.cursor()

        sql = "DELETE "
        sql += "FROM " + table

        if len(conditions) > 0:
            sql += " WHERE "
            for ind in range(0, len(conditions)):
                sql += conditions[ind]
                if ind != len(conditions) - 1:
                    sql += "and "

        print("\n"+sql)

        try:
            cursor.execute(sql)
            db.commit()
        except Exception as e:
            print(e)
            db.rollback()
        finally:
            db.close()
