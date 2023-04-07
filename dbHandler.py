import pymysql


def insertData(data):
    rowId = 0

    db = pymysql.connect(host="localhost", user="root",
                         password="root", database="criminaldb")
    cursor = db.cursor()
    print("database connected")

    query = "INSERT INTO criminaldata VALUES(0, '%s', '%s', '%s', '%s', '%s');" % \
            (data["Name"], data["Father's Name"], data["Gender"],
             data["DOB(yyyy-mm-dd)"],
             data["Crimes Done"])

    try:
        cursor.execute(query)
        db.commit()
        rowId = cursor.lastrowid
        print("data stored on row %d" % rowId)
    except:
        db.rollback()
        print("Data insertion failed")

    db.close()
    print("connection closed")
    return rowId


def retrieveData(name):
    id = None
    crim_data = None

    db = pymysql.connect(host="localhost", user="root", password="root",
                         database="testdb", charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cursor = db.cursor()
    print("database connected")

    query = "SELECT * FROM criminaldata WHERE name='%s'" % name

    try:
        cursor.execute(query)
        result = cursor.fetchone()

        id = result[0]
        crim_data = {
            "Name": result[1],
            "Father's Name": result[2],
            "Gender": result[3],
            "DOB(yyyy-mm-dd)": result[4],
            "Crimes Done": result[5]
        }

        print("data retrieved")
    except:
        print("Error: Unable to fetch data")

    db.close()
    print("connection closed")

    return (id, crim_data)
