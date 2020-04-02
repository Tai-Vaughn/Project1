import psycopg2

def getData():
    try:
        connection = psycopg2.connect(user="ddbdugprosrwsp",
                                    password="424e2260898e422727e1b3b3c61281f057b01bbf9e5f1fd61a1adf4fa3d236d0",
                                    host="ec2-50-17-178-87.compute-1.amazonaws.com",
                                    port="5432"
                                    database="dau4fpsqfstnqg")
        cursor = connection.cursor()
        postgreSQL_select_Query = "select * from user_profile"
        cursor.execute(postgreSQL_select_Query)
        return cursor.fetchall()
        

    except (Exception, psycopg2.Error) as error :
        print ("Error while fetching data from PostgreSQL", error)

    finally:
        #closing database connection.
        if(connection):
            cursor.close()
            connection.close()

def getUser(idNumber):
    try:
        connection = psycopg2.connect(user="lab5",
                                    password="jojo",
                                    host="localhost",
                                    database="users")
        cursor = connection.cursor()
        postgreSQL_select_Query = "select * from user_profile where id="+idNumber
        cursor.execute(postgreSQL_select_Query)
        return cursor.fetchall()[0]

    except (Exception, psycopg2.Error) as error :
        print ("Error while fetching data from PostgreSQL", error)

    finally:
        #closing database connection.
        if(connection):
            cursor.close()
            connection.close()