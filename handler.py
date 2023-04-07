import csv

# filename = "Criminal_count.csv"
# num=0
# with open(filename, 'w') as csvfile:
#     csvwriter = csv.writer(csvfile)
#     csvwriter.writerow([5])
def insertData(data):
    # field=['Name', "Father's Name", "Gender", "DOB","Crimes"]
    x=[data['Name'], data["Father's Name"], data['Gender'], data['DOB(yyyy-mm-dd)'], data['Crimes Done']]
    filen = "Criminal.csv"
    with open(filen, 'a') as csvfile:
        csvwriter = csv.writer(csvfile)
        # csvwriter.writerow(field)
        csvwriter.writerow(x)
# def insertData(data): 
#     print(data['Name'])
#     rowId=0
#     db=sqlite3.connect('profile.db')
#     cursor=db.cursor()
#     print("Opened Database")

#     query = "INSERT INTO criminaldata VALUES(NAME,FATHER NAME, GENDER, DOB, CRIMES);" % \
#             (data['Name'], data["Father's Name"], data['Gender'],
#              data['DOB(yyyy-mm-dd)'], data['Crimes Done'])

#     cursor.execute(query)
#     db.commit()
#     rowId=cursor.lastrowid
#     print("RowId %d" % rowId)

#     print("Record Created")
#     db.close()
#     return rowId



# def insertData(data):
#     # print(data)
# 	rowId = 0
# 	db = sqlite3.connect('test.db')
#     cursor = db.cursor()
#     # cursor=db.cursor()
# 	print("Opened database Succesfully")

# 	query = "INSERT INTO criminaldata VALUES(0, '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');" % \
#             (data["Name"], data["Father's Name"], data["Mother's Name"], data["Gender"],
#              data["DOB(yyyy-mm-dd)"], data["Blood Group"], data["Identification Mark"],
#              data["Nationality"], data["Religion"], data["Crimes Done"])

#     cursor.execute(query)
#     db.commit()
#     rowId = cursor.lastrowid
#     print("data stored on row %d" % rowId)

#     db.commit()
# 	print ("Records created successfully");
# 	db.close()
# 	return rowId

def retrieveData(name):
    with open("Criminal.csv", 'r') as file:
        reader = csv.reader(file)
        headers = next(reader) # skip the header row
        print("Looking for ",name)
        for i, row in enumerate(reader, 2): # start from row 2
            if len(row) == 0: # handle empty row
                continue
            if row[0] == name.lower():
                print("I:",type(i),{**dict(zip(headers, row))})
                return (1, {**dict(zip(headers, row))})
    return None 