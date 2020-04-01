import psycopg2

def getData():
    try:
        connection = psycopg2.connect(user="lab5",
                                    password="jojo",
                                    host="localhost",
                                    database="users")
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