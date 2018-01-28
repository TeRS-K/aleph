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


    def insert(self, table, rows, values):
        '''
        :param table:
        :param values:
        :return: nothing, but inserts values into specified table
        '''

        db = getConnection(self.ipaddr, self.username, self.password, self.database)
        cursor = db.cursor()

        sql = "INSERT INTO " + table + " ("
        for ind in range(0, len(rows)):
            sql+= rows[ind]
            if ind != len(rows) -1:
                sql+=", "
            else:
                sql+= ")"

        sql+= " Values ("
        for ind in range(0, len(values)):
            sql+= values[ind]
            if ind != len(values) -1:
                sql+=", "
            else:
                sql+= ")"

        print("\n" + sql)

        try:
            cursor.execute(sql)
            db.commit()
        except Exception as e:
            print(e)
            db.rollback()
        finally:
            db.close()


    def query(self, table, columns=[], conditions=[], order=[]):
        '''
        :param table: table name
        :param columns: columns to query
        :param conditions: WHERE clause
        :return: python nested tuple with each tuple being one row
        '''
        db = getConnection(self.ipaddr, self.username, self.password, self.database)
        cursor = db.cursor()

        sql = "SELECT "
        if( isinstance(columns, list) ):
            for ind in range(0,len(columns)):
                sql += columns[ind]
                if ind != len(columns) - 1:
                    sql += ", "
        else:
            sql+= columns

        sql += " FROM " + table

        if len(conditions)>0:
            sql += " WHERE "
            for ind in range(0,len(conditions)):
                sql += conditions[ind]
                if ind != len(conditions) - 1:
                    sql += " and "

        if len(order)>0:
            sql += " ORDER BY"
            for ind in range(0,len(order)):
                sql += " " + order[ind]
                if ind < len(order) - 2:
                    sql += ","

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

        sql = "DELETE FROM " + table

        if len(conditions) > 0:
            sql += " WHERE "
            for ind in range(0, len(conditions)):
                sql += conditions[ind]
                if ind != len(conditions) - 1:
                    sql += " and "

        print("\n"+sql)

        try:
            cursor.execute(sql)
            db.commit()
        except Exception as e:
            print(e)
            db.rollback()
        finally:
            db.close()


    def update(self, table, mutate=[], conditions=[]):
        '''
        :param table: table to update
        :param mutate: [column1=new1, column2=new2,....]
        :param conditions: [username=..., ...]
        :return: void
        '''

        db = getConnection(self.ipaddr, self.username, self.password, self.database)
        cursor = db.cursor()

        sql = "UPDATE " + table + " "

        if len(mutate) > 0:
            sql += "SET"
            for ind in range(0, len(mutate)):
                sql += " " + mutate[ind]
                if ind != len(mutate) - 1:
                    sql += ","

        if len(conditions) > 0:
            sql += " WHERE "
            for ind in range(0, len(conditions)):
                sql += conditions[ind]
                if ind != len(conditions) - 1:
                    sql += " and "

        print("\n"+sql)

        try:
            cursor.execute(sql)
            db.commit()
        except Exception as e:
            print(e)
            db.rollback()
        finally:
            db.close()

    def debugging(self):
        print(self.query('Login', '*'))
        print(self.query('Friends', '*'))
        print(self.query('Location', '*'))
        print(self.query('Status', '*'))
        print(self.query('AddCode', '*'))
    
    def deleteall(self):
        self.delete("Login")
        self.delete("Friends")
        self.delete("Location")
        self.delete("Status")
        self.delete("Addcode")
