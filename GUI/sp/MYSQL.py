import pymysql as mysql

connection = mysql.connect(host="localhost", user="root", password="root", database="student")
current_position_of_curser = connection.cursor()

# required empty list
list_for_insert_some_data = list()
list_for_updating_some_data = list()


def insert():
    print("WANT TO INSERT DATA, ENTER 'y' FOR YES & 'n' FOR NO")
    # setting while loop for  to take number of inputs from user and then  barking it's  need complete!
    while True:
        user_inserting = input("ENTER YOUR RESPONSE : ")
        if user_inserting == 'y' or user_inserting == 'n':
            if user_inserting == "n":
                print("DATA IS INSERTED SUCCESSFULLY (if you provided!).")
                break

            elif user_inserting == "y":

                identification_number = int(input("ENTER THE ID : "))
                name = input("ENTER THE NAME : ")
                surname = input("ENTER THE SURNAME : ")
                data = (identification_number, name, surname)
                list_for_insert_some_data.append(data)

        else:
            print("please , enter valid entry!")

    mysql_query = "insert into info values(%s, %s, %s)"
    mysql_multi_argument = tuple(list_for_insert_some_data)

    current_position_of_curser.executemany(mysql_query, mysql_multi_argument)

    connection.commit()
    connection.close()


def update_some_data():
    print("WANT TO UPDATE DATA, ENTER 'y' FOR YES & 'n' FOR NO")

    while True:
        user_updating_some_data = input("enter your response in 'y' or 'n' terms : ")
        if user_updating_some_data == 'y' or user_updating_some_data == 'n':
            if user_updating_some_data == "n":
                print(f"DATA IS UPDATED SUCCESSFULLY (if provided!)")
                break

            elif user_updating_some_data == "y":

                identification_number = int(input("ENTER THE ID WHERE YOU WANT TO UPDATE THE DATA : "))
                name = input("ENTER THE FIRST NAME : ")
                surname = input("ENTER THE LAST NAME : ")
                data = (name, surname, identification_number)
                list_for_updating_some_data.append(data)

        else:
            print("please , enter valid entry!")

    mysql_query = "UPDATE info SET name=%s, surname=%s WHERE id = %s"
    mysql_multi_argument = tuple(list_for_updating_some_data)

    current_position_of_curser.executemany(mysql_query, mysql_multi_argument)

    connection.commit()
    connection.close()


def update_all_data():
    # taking input;
    name = input("enter the name for update : ")
    surname = input("enter the surname for update : ")
    data = (name, surname)

    # SETTING QUERY FOR UPDATE ALL DATA;
    mysql_query = "UPDATE info SET name = %s, surname = %s "
    array = tuple(data)
    # after query let's execute it;
    current_position_of_curser.execute(mysql_query, array)

    # now, commit our connection;
    connection.commit()

    # at the end let's  close the connection;
    connection.close()

    # UPDATED SUCCESSFULLY
    print("DATA IS UPDATED SUCCESSFULLY (if provided!)")


def delete_some_data():
    # taking id number to delete some data;
    id = int(input("enter the id number to delete data : "))

    # the sql query;
    mysql_query = "DELETE FROM info WHERE id = %s"

    #  executing the query;
    current_position_of_curser.execute(mysql_query, id)

    # committing the connection;
    connection.commit()

    # closing the connection;
    connection.close()

    print("PER YOUR REQUEST DATA DELETED SUCCESSFULLY")


def delete_all_data():
    # the sql query;
    mysql_query = "DELETE FROM info "

    #  executing the query;
    current_position_of_curser.execute(mysql_query)

    # committing the connection;
    connection.commit()

    print("ALL DATA IS DELETED SUCCESSFULLY")


user = input('''TO INSERT THE DATA, ENTER : 'i'
TO UPDATE SOME DATA, ENTER : 'us'
TO UPDATE ALL THE DATA, ENTER : 'ua'
TO DELETE SOME DATA, ENTER : 'ds'
TO DELETE ALL THE DATA, ENTER : 'da'
TO SEE THE DATA, ENTER : 'select'

ENTER YOUR RESPONSE : ''')
if user == "i":
    insert()
elif user == "us":
    update_some_data()
elif user == "ua":
    update_all_data()
elif user == "ds":
    delete_some_data()
elif user == "da":
    delete_all_data()